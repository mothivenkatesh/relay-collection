"""
Reddit scraper for Indian D2C / SMB payment pain points.
Targets the right subreddits with the right queries — not global search.
Output: reddit_d2c_india.json + reddit_d2c_india_report.md
"""

import json
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# (subreddit, query) — subreddit-specific because Reddit's global search is broken for niche India topics
SEARCHES = [
    # D2C / Ecommerce ops pain
    ("IndiaStartups", "D2C"),
    ("IndiaStartups", "ecommerce"),
    ("IndiaStartups", "payment gateway"),
    ("IndiaStartups", "RTO"),
    ("IndiaStartups", "COD"),
    ("IndiaStartups", "shopify"),
    ("IndiaStartups", "refund"),
    ("IndiaStartups", "abandoned cart"),

    ("IndiaBusiness", "payment"),
    ("IndiaBusiness", "ecommerce"),
    ("IndiaBusiness", "razorpay"),
    ("IndiaBusiness", "cashfree"),
    ("IndiaBusiness", "shopify"),

    ("indianstartups", "payment"),
    ("indianstartups", "D2C"),

    # Developer pain
    ("developersIndia", "razorpay"),
    ("developersIndia", "cashfree"),
    ("developersIndia", "payment gateway"),
    ("developersIndia", "UPI integration"),
    ("developersIndia", "webhook"),

    # Workflow automation
    ("n8n", "razorpay"),
    ("n8n", "india"),
    ("n8n", "cashfree"),
    ("nocode", "india payment"),
    ("automation", "india"),

    # E-commerce general (often has India threads)
    ("ecommerce", "COD India"),
    ("ecommerce", "RTO"),
    ("shopify", "india COD"),
    ("shopify", "razorpay"),
    ("shopify", "cashfree"),

    # Entrepreneurship
    ("Entrepreneur", "india D2C"),
    ("smallbusiness", "india payment"),

    # India broad
    ("india", "Razorpay"),
    ("india", "Cashfree"),
]

CUTOFF_DAYS = 180  # 6 months — relax from 3 to get more signal
NOW = datetime.now(timezone.utc).timestamp()
CUTOFF_TS = NOW - (CUTOFF_DAYS * 86400)

# Keywords that signal real pain (used for scoring)
PAIN_KEYWORDS = [
    "RTO", "COD", "return to origin", "fraud", "refund", "payment failed",
    "abandoned cart", "razorpay", "cashfree", "payment gateway", "shopify",
    "webhook", "settlement", "reconciliation", "chargeback", "dispute",
    "Interakt", "AiSensy", "Gupshup", "WhatsApp", "n8n", "Zapier",
    "D2C", "ecommerce", "automation", "support", "frustrating",
    "lost money", "lost orders", "broken", "doesn't work", "nightmare",
    "stuck", "help", "advice", "problem", "issue",
]

OUT_DIR = Path("/Users/mothi.venkatesh/Documents")


def fetch_json(url, max_retries=2):
    for attempt in range(max_retries + 1):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 5 * (attempt + 1)
                print(f"    Rate limited, waiting {wait}s...")
                time.sleep(wait)
                continue
            print(f"    HTTP {e.code}: {url[:80]}")
            return None
        except Exception as e:
            print(f"    ERROR: {type(e).__name__}: {str(e)[:80]}")
            return None
    return None


def build_search_url(subreddit, query, sort="top", t="year"):
    params = urllib.parse.urlencode({
        "q": query,
        "sort": sort,
        "t": t,
        "limit": 25,
        "type": "link",
        "restrict_sr": 1,
    })
    return f"https://www.reddit.com/r/{subreddit}/search.json?{params}"


def extract_post(post_data):
    d = post_data.get("data", {})
    created = d.get("created_utc", 0)
    if created < CUTOFF_TS:
        return None
    return {
        "id": d.get("id"),
        "title": d.get("title", ""),
        "selftext": d.get("selftext", "")[:3000],
        "subreddit": d.get("subreddit", ""),
        "author": d.get("author", "[deleted]"),
        "url": d.get("url", ""),
        "permalink": "https://reddit.com" + d.get("permalink", ""),
        "score": d.get("score", 0),
        "upvote_ratio": d.get("upvote_ratio", 0),
        "num_comments": d.get("num_comments", 0),
        "created_utc": created,
        "created_date": datetime.fromtimestamp(created, tz=timezone.utc).strftime("%Y-%m-%d"),
        "flair": d.get("link_flair_text", "") or "",
    }


def score_post(post):
    """Score a post based on pain signal keywords + engagement."""
    text = (post["title"] + " " + post.get("selftext", "")).lower()
    pain_hits = sum(1 for kw in PAIN_KEYWORDS if kw.lower() in text)
    # Engagement weight (comments matter more than upvotes for finding discussion)
    engagement = post["score"] + (post["num_comments"] * 2)
    return pain_hits * 5 + min(engagement, 200)


def fetch_comments(permalink, limit=8):
    """Fetch top comments for a post."""
    base = permalink.replace("https://reddit.com", "https://www.reddit.com").rstrip("/")
    url = f"{base}.json?limit={limit}&sort=top&depth=1"
    data = fetch_json(url)
    if not data or len(data) < 2:
        return []
    comments = []
    for child in data[1].get("data", {}).get("children", []):
        c = child.get("data", {})
        body = c.get("body", "")
        if body and body not in ("[deleted]", "[removed]") and len(body) > 30:
            comments.append({
                "author": c.get("author", "[deleted]"),
                "body": body[:1500],
                "score": c.get("score", 0),
            })
    return comments[:5]


def main():
    print(f"Reddit D2C India Scraper — cutoff: {CUTOFF_DAYS} days")
    print(f"Cutoff timestamp: {datetime.fromtimestamp(CUTOFF_TS, tz=timezone.utc).strftime('%Y-%m-%d')}")
    print(f"Total searches: {len(SEARCHES)}\n")

    all_posts = {}
    search_stats = []

    for i, (sub, query) in enumerate(SEARCHES, 1):
        print(f"[{i}/{len(SEARCHES)}] r/{sub} · '{query}'")
        url = build_search_url(sub, query)
        data = fetch_json(url)

        new_count = 0
        if data and "data" in data:
            for child in data["data"].get("children", []):
                post = extract_post(child)
                if post and post["id"] not in all_posts:
                    all_posts[post["id"]] = post
                    new_count += 1
        search_stats.append({"subreddit": sub, "query": query, "new_posts": new_count})
        print(f"    → {new_count} new posts in window")
        time.sleep(1.2)  # polite delay

    posts_list = list(all_posts.values())
    print(f"\nTotal unique posts in window: {len(posts_list)}")

    # Score and rank
    for p in posts_list:
        p["pain_score"] = score_post(p)
    posts_list.sort(key=lambda x: -x["pain_score"])

    # Filter: must have at least 1 pain keyword OR be in a payment-relevant sub
    relevant_subs = {"IndiaStartups", "IndiaBusiness", "developersIndia", "n8n",
                     "indianstartups", "shopify", "ecommerce", "nocode", "automation"}
    filtered = [p for p in posts_list
                if score_post(p) > 5
                or p["subreddit"] in relevant_subs]
    print(f"After pain-relevance filter: {len(filtered)}")

    # Fetch comments for top 40 by pain score
    top = filtered[:40]
    print(f"\nFetching comments for top {len(top)} posts...")
    for i, post in enumerate(top, 1):
        print(f"  [{i}/{len(top)}] {post['title'][:60]}")
        post["top_comments"] = fetch_comments(post["permalink"])
        time.sleep(1.2)

    # Save
    out = {
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "window_days": CUTOFF_DAYS,
        "total_searches": len(SEARCHES),
        "total_unique_posts": len(filtered),
        "posts_with_comments": len(top),
        "search_stats": search_stats,
        "posts": filtered,
    }
    json_path = OUT_DIR / "reddit_d2c_india.json"
    json_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\n✓ JSON → {json_path}")

    # Build markdown report
    sub_counts = defaultdict(int)
    for p in filtered:
        sub_counts[p["subreddit"]] += 1

    lines = []
    lines.append("# Reddit: Indian D2C Payment Pain — Verbatim Signal")
    lines.append(f"\n**Scraped:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Window:** Last {CUTOFF_DAYS} days")
    lines.append(f"**Total posts (filtered):** {len(filtered)}")
    lines.append(f"**Top posts with comments:** {len(top)}\n")
    lines.append("---\n")

    lines.append("## Subreddit Distribution")
    for sub, cnt in sorted(sub_counts.items(), key=lambda x: -x[1])[:15]:
        lines.append(f"- r/{sub}: **{cnt}** posts")
    lines.append("")

    lines.append("---\n")
    lines.append("## Top 40 Pain-Signal Posts (with comments)\n")
    for i, p in enumerate(top, 1):
        lines.append(f"### {i}. {p['title']}")
        lines.append(f"**r/{p['subreddit']}** · {p['created_date']} · "
                     f"{p['score']}↑ · {p['num_comments']}💬 · pain={p['pain_score']}")
        lines.append(f"[{p['permalink']}]({p['permalink']})\n")
        if p.get("selftext"):
            body = p["selftext"][:1500]
            lines.append("**Post body:**")
            lines.append(f"> {body.replace(chr(10), chr(10) + '> ')}\n")
        if p.get("top_comments"):
            lines.append("**Top comments:**")
            for c in p["top_comments"]:
                body = c["body"][:800].replace("\n", " ")
                lines.append(f"- **{c['author']}** ({c['score']}↑): {body}")
            lines.append("")
        lines.append("---\n")

    report_path = OUT_DIR / "reddit_d2c_india_report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ Report → {report_path}")

    # Summary print
    print(f"\n{'='*60}\nSUMMARY")
    print(f"  Total searches:     {len(SEARCHES)}")
    print(f"  Total unique posts: {len(posts_list)}")
    print(f"  After filter:       {len(filtered)}")
    print(f"  With comments:      {len(top)}")
    print(f"\nTOP 15 PAIN POSTS:")
    for p in filtered[:15]:
        print(f"  [pain={p['pain_score']:>3} {p['score']:>4}↑ {p['num_comments']:>3}💬] "
              f"r/{p['subreddit']:<18} {p['title'][:65]}")


if __name__ == "__main__":
    main()
