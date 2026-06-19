import csv
import re
import os

INPUT  = '/Users/mothi.venkatesh/Downloads/Ecom live merchants - Data.csv'
OUTPUT = '/Users/mothi.venkatesh/Downloads/Ecom_merchants_relay_enriched.csv'

# ── brand overrides: well-known Indian brands we can identify by domain ──────
BRAND_OVERRIDES = {
    'nykaa':           ('D2C Beauty',   'Nykaa'),
    'nykaafashion':    ('D2C Fashion',  'Nykaa Fashion'),
    'mamaearth':       ('D2C Beauty',   'Mamaearth'),
    'purplle':         ('D2C Beauty',   'Purplle'),
    'myglamm':         ('D2C Beauty',   'MyGlamm'),
    'bellavitaorganic':('D2C Beauty',   'Bella Vita Organic'),
    'bellavitaluxury': ('D2C Beauty',   'Bella Vita Luxury'),
    'clinikally':      ('D2C Beauty',   'Clinikally'),
    'theayurvedaco':   ('D2C Beauty',   'The Ayurveda Co'),
    'pilgrim':         ('D2C Beauty',   'Pilgrim'),
    'boldcare':        ('D2C Beauty',   'Bold Care'),
    'traya':           ('D2C Beauty',   'Traya'),
    'chicnutrix':      ('D2C Beauty',   'Chicnutrix'),
    'discoverpilgrim': ('D2C Beauty',   'Pilgrim'),
    'miduty':          ('D2C Beauty',   'Miduty'),

    'firstcry':        ('D2C Fashion',  'FirstCry'),
    'meesho':          ('D2C Fashion',  'Meesho'),
    'myntra':          ('D2C Fashion',  'Myntra'),
    'snapdeal':        ('D2C Fashion',  'Snapdeal'),
    'ajio':            ('D2C Fashion',  'AJIO'),
    'shoppersstop':    ('D2C Fashion',  "Shoppers Stop"),
    'tatacliq':        ('D2C Fashion',  'TataCliq'),
    'westside':        ('D2C Fashion',  'Westside'),
    'shriramfinance':  ('Fintech',      'Shriram Finance'),
    'forevernew':      ('D2C Fashion',  'Forever New'),
    'tresmode':        ('D2C Fashion',  'Tresmode'),
    'suta':            ('D2C Fashion',  'Suta'),
    'kanakavalli':     ('D2C Fashion',  'Kanakavalli'),
    'thesouledstore':  ('D2C Fashion',  'The Souled Store'),
    'redwolf':         ('D2C Fashion',  'Redwolf'),
    'superkicks':      ('D2C Fashion',  'Superkicks'),
    'vegnonveg':       ('D2C Fashion',  'VegNonVeg'),
    'freakins':        ('D2C Fashion',  'Freakins'),
    'urbanmonkey':     ('D2C Fashion',  'Urban Monkey'),
    'streetstylestore':('D2C Fashion',  'Street Style Store'),
    'bewakoof':        ('D2C Fashion',  'Bewakoof'),
    'arcticfox':       ('Electronics',  'Arctic Fox'),
    'manmatters':      ('D2C Beauty',   'Man Matters'),
    'bebodywise':      ('D2C Beauty',   'Be Bodywise'),
    'myfitness':       ('D2C Beauty',   'MyFitness'),
    'thriveco':        ('D2C Beauty',   'The Thrive Co'),

    'caratlane':       ('Jewellery',    'CaratLane'),
    'giva':            ('Jewellery',    'Giva'),
    'ornaz':           ('Jewellery',    'Ornaz'),
    'kisna':           ('Jewellery',    'Kisna'),
    'navratan':        ('Jewellery',    'Navratan'),
    'navrathan':       ('Jewellery',    'Navrathan'),
    'bhimagold':       ('Jewellery',    'Bhima Gold'),
    'bhima':           ('Jewellery',    'Bhima Jewels'),
    'safegold':        ('Fintech',      'SafeGold'),
    'onemuthoot':      ('Jewellery',    'One Muthoot'),
    'manepally':       ('Jewellery',    'Manepally'),
    'pateljewellers':  ('Jewellery',    'Patel Jewellers'),
    'orra':            ('Jewellery',    'Orra'),
    'auragold':        ('Jewellery',    'Aura Gold'),
    'myviba':          ('Jewellery',    'Viba'),
    'batuk':           ('Fintech',      'Batuk Gold'),
    'tapinvest':       ('Fintech',      'TapInvest'),
    'brightdigigold':  ('Fintech',      'Bright DigiGold'),
    'ebullion':        ('Fintech',      'eBullion'),
    'digigold':        ('Fintech',      'DigiGold'),

    'headphonezone':   ('Electronics',  'Headphone Zone'),
    'crossbeats':      ('Electronics',  'Crossbeats'),
    'scogo':           ('Electronics',  'Scogo'),
    'etherbit':        ('Electronics',  'EtherBit'),

    'swiggy':          ('Food & Beverage','Swiggy'),
    'thirdwavecoffeeroasters':('Food & Beverage','Third Wave Coffee'),
    'cafecoffeeday':   ('Food & Beverage','Café Coffee Day'),
    'burgersinghonline':('Food & Beverage','Burger Singh'),
    'curefit':         ('D2C Sports',   'Cult.fit'),
    'aroleap':         ('D2C Sports',   'AroLeap'),
    'wakefit':         ('Home & Decor', 'Wakefit'),
    'homelane':        ('Home & Decor', 'HomeLane'),
    'livspace':        ('Home & Decor', 'Livspace'),
    'decorpot':        ('Home & Decor', 'Decorpot'),
    'freedomtree':     ('Home & Decor', 'Freedom Tree'),
    'birlaopus':       ('Home & Decor', 'Birla Opus'),
    'nestroots':       ('Home & Decor', 'Nestroots'),

    'magicpin':        ('Digital Goods','MagicPin'),
    'kreditbee':       ('Fintech',      'KreditBee'),
    'kredx':           ('Fintech',      'KredX'),
    'bharatpe':        ('Fintech',      'BharatPe'),
    'pagarbook':       ('Fintech',      'PagarBook'),
    'legalpay':        ('Fintech',      'LegalPay'),
    'finsall':         ('Fintech',      'Finsall'),
    'refrens':         ('Fintech',      'Refrens'),
    'vyaparapp':       ('Fintech',      'Vyapar'),
    'jodo':            ('Fintech',      'Jodo'),
    'grayquest':       ('Fintech',      'GrayQuest'),
    'zetapp':          ('Fintech',      'ZetApp'),
    'shiprocket':      ('Fintech',      'Shiprocket'),
    'indiafilings':    ('Fintech',      'India Filings'),
    'zingoy':          ('Fintech',      'Zingoy'),
    'gyftr':           ('Fintech',      'Gyftr'),
    'busy':            ('Fintech',      'Busy Accounting'),

    'kukufm':          ('Digital Goods','Kuku FM'),
    'gaana':           ('Digital Goods','Gaana'),
    'pocketfm':        ('Digital Goods','Pocket FM'),
    'chingari':        ('Digital Goods','Chingari'),
    'eloelo':          ('Digital Goods','Elo Elo'),
    'frnd':            ('Digital Goods','FRND'),
    'adda':            ('Digital Goods','Adda52'),
    'probo':           ('Digital Goods','Probo'),
    'winzogames':      ('Digital Goods','WinZO'),
    'dream':           ('Digital Goods','Dream.money'),
    'cosmofeed':       ('Digital Goods','CosmFeed'),
    'tagmango':        ('Digital Goods','TagMango'),
    'heycoach':        ('EdTech',       'Hey Coach'),
    'goseeko':         ('EdTech',       'Goseeko'),
    'docthub':         ('EdTech',       'DocThub'),
    'japalouppe':      ('EdTech',       'Japalouppe'),
    'indiaparentingforum':('EdTech',    'India Parenting Forum'),
}

# ── keyword bags for fallback classification ──────────────────────────────────
KW = {
    'Jewellery': ['jewel','gold','silver','diamond','gem','ornament','bullion','thangamaligai',
                  'mangatrai','saravana','sriganesh','nacjewel','outhouse','tyaani'],
    'Electronics': ['electron','headphone','gadget','laptop','mobile','speaker','camera','smart',
                    'device','drone','robotics','robo','cctv','sensor','iot','electra','radiumbox',
                    'tanotis','bajaao'],
    'D2C Beauty': ['beauty','cosmet','skincare','skin','haircare','hair','makeup','glow',
                   'organic','ayurved','herbal','wellness','nutra','vitamin','supplement','serum',
                   'sadhev','sheshaayurved','mahavastu','turmeriq','avimee'],
    'D2C Fashion': ['fashion','cloth','apparel','wear','textile','fabric','saree','ethnic',
                    'dress','kurti','shirt','jeans','shoe','footwear','styl','boutique','outfit',
                    'linen','cotton','silk','flair','suta','sari','canvas','tshirt','hosiery'],
    'D2C Sports': ['sport','fitness','gym','yoga','martial','cricket','football','badminton',
                   'workout','athlete','lavos','shapercult','warrior'],
    'Home & Decor': ['home','decor','furniture','interior','living','kitchen','lamp','sofa',
                     'carpet','mattress','curtain','houseinnovate','nestroots','qube'],
    'Food & Beverage': ['food','restaurant','cafe','beverage','coffee','snack','burger','chai',
                        'drink','dairy','milk','chicken','fmcg','grocery','bakers','sweets',
                        'countrychicken','milkmantra','gayathrimil','crisfood'],
    'EdTech': ['school','college','learn','edu','class','course','coach','tutor','study','books',
               'academic','campus','training','skill','uniform','scribblesuniform'],
    'Fintech': ['pay','fintech','invest','loan','credit','banking','wallet','insurance','nbfc',
                'emi','kyc','ledger','account','finance','fiscal','paymatrix'],
    'Digital Goods': ['app','platform','media','digital','software','saas','tech','stream',
                      'gaming','game','live','audio','podcast','content','creator','social'],
}

USE_CASES_MAP = {
    'Jewellery': {
        'use_cases': (
            'Big-ticket payment alerts (₹50K+ orders on WhatsApp/Slack), '
            'Auto-sync transactions to Google Sheets (replace daily CSV export), '
            'Failed payment digest (hourly/daily by reason code), '
            'Settlement reconciliation against Tally/Zoho Books'
        ),
        'pitch': (
            "Hi {name}, jewellers like {biz} see ₹2–5L/week in missed follow-up on high-value orders "
            "because alerts reach the team too late. With Cashfree Relay, you get a WhatsApp notification "
            "the moment any payment above ₹50K clears — plus auto-sync to Sheets and a daily digest of "
            "failed payments with reason codes. Free during beta. "
            "Would a 20-minute walkthrough work this week?"
        ),
    },
    'Electronics': {
        'use_cases': (
            'Big-ticket payment alerts (₹20K+ orders), '
            'Failed payment digest with ₹ impact and reason breakdown, '
            'Auto-sync to Google Sheets, '
            'Settlement reconciliation'
        ),
        'pitch': (
            "Hi {name}, electronics brands like {biz} lose 8–12% of high-value orders to delayed ops alerts. "
            "Relay notifies your team on WhatsApp the moment a ₹20K+ payment lands and sends a daily digest of "
            "failed payments — auto-grouped by reason (UPI timeout, 3DS fail, insufficient funds). "
            "Free during beta. Worth a 20-min demo this week?"
        ),
    },
    'D2C Beauty': {
        'use_cases': (
            'Abandoned checkout recovery (WhatsApp payment link in 5 min), '
            'COD confirmation + RTO reduction (WhatsApp before shipment), '
            'Failed payment digest with recovery nudges, '
            'Auto-sync to Google Sheets'
        ),
        'pitch': (
            "Hi {name}, D2C beauty brands like {biz} recover 15–25% of dropped checkouts with a timed "
            "WhatsApp follow-up. Relay sends a fresh Cashfree payment link 5 minutes after any checkout "
            "drop — and auto-confirms COD orders before they ship to cut RTO. "
            "Free during beta. 20-min walkthrough this week?"
        ),
    },
    'D2C Fashion': {
        'use_cases': (
            'COD confirmation + RTO reduction (WhatsApp confirmation before shipment), '
            'Abandoned checkout recovery (WhatsApp payment link), '
            'Failed payment digest, '
            'Auto-sync to Google Sheets'
        ),
        'pitch': (
            "Hi {name}, fashion D2C brands like {biz} run 60–70% COD — and RTO eats ₹15–100K/day at scale. "
            "Relay confirms every COD order on WhatsApp before it ships and recovers dropped checkouts "
            "with a fresh payment link. Free during beta. 20-min demo this week?"
        ),
    },
    'D2C Sports': {
        'use_cases': (
            'Abandoned checkout recovery (WhatsApp nudge), '
            'Failed payment digest, '
            'Big-ticket payment alerts, '
            'Auto-sync to Google Sheets'
        ),
        'pitch': (
            "Hi {name}, {biz} likely loses 20–30% of revenue to checkout drops and untracked failed payments. "
            "Relay auto-sends a WhatsApp recovery link 5 minutes after any checkout drop and gives your ops "
            "team a daily digest of failed payments with ₹ impact. Free during beta. Quick walkthrough?"
        ),
    },
    'Home & Decor': {
        'use_cases': (
            'Big-ticket payment alerts (₹30K+ orders on WhatsApp), '
            'Abandoned checkout recovery, '
            'Failed payment digest, '
            'Auto-sync to Google Sheets'
        ),
        'pitch': (
            "Hi {name}, home and decor brands like {biz} have high average order values — yet most founders "
            "only find out about a ₹50K order the next morning. Relay sends a WhatsApp alert the moment any "
            "high-value payment clears, and a daily digest of failed payments. "
            "Free during beta. 20 minutes this week?"
        ),
    },
    'Food & Beverage': {
        'use_cases': (
            'COD/order confirmation on WhatsApp before preparation, '
            'Failed payment digest, '
            'Auto-sync to Google Sheets, '
            'Big-ticket/bulk order alerts'
        ),
        'pitch': (
            "Hi {name}, {biz} loses revenue when COD orders go unconfirmed and start prep before the customer "
            "cancels. Relay auto-confirms every online order on WhatsApp and sends a real-time alert on payment "
            "failures. Free during beta. Quick demo this week?"
        ),
    },
    'EdTech': {
        'use_cases': (
            'Calendar event per payment (auto-schedule class/cohort on successful enrollment), '
            'Failed payment recovery nudges, '
            'Monthly collection cycle for EMI/batch fees, '
            'Auto-sync to Google Sheets'
        ),
        'pitch': (
            "Hi {name}, every enrollment payment at {biz} likely triggers 3 manual tasks — add to roster, "
            "schedule session, send confirmation. Relay does all three automatically: Google Calendar event, "
            "Sheets row, and WhatsApp confirmation — the moment payment clears. "
            "Free during beta. 20-min demo this week?"
        ),
    },
    'Fintech': {
        'use_cases': (
            'Settlement reconciliation against Tally/Zoho Books, '
            'Big-ticket payment alerts, '
            'Monthly collection cycle automation, '
            'Failed payment digest with ₹ impact'
        ),
        'pitch': (
            "Hi {name}, fintech ops teams like {biz} spend 10+ hours/week on manual reconciliation. "
            "Relay auto-syncs Cashfree settlements against your books, flags mismatches by category, and sends "
            "your finance team a weekly digest. Free during beta. Worth exploring in a 20-min call?"
        ),
    },
    'Digital Goods': {
        'use_cases': (
            'Failed payment recovery (WhatsApp/email nudge with retry link), '
            'Big-ticket payment alerts, '
            'Auto-sync to Google Sheets, '
            'Calendar event per payment (for cohort/subscription products)'
        ),
        'pitch': (
            "Hi {name}, digital goods platforms like {biz} lose 15–20% of subscription/purchase revenue to "
            "silent payment failures with no follow-up. Relay auto-sends a WhatsApp recovery link after every "
            "failed payment and alerts your team on high-value purchases. "
            "Free during beta. 20-min demo this week?"
        ),
    },
    'D2C Brand': {
        'use_cases': (
            'Abandoned checkout recovery (WhatsApp payment link in 5 min), '
            'COD confirmation + RTO reduction, '
            'Failed payment digest with ₹ impact, '
            'Auto-sync to Google Sheets'
        ),
        'pitch': (
            "Hi {name}, D2C brands like {biz} still manually follow up on failed payments and abandoned "
            "checkouts. Relay automates both — WhatsApp payment link within 5 mins of a drop, daily failed "
            "payment digest with ₹ impact, and COD confirmation before shipment. "
            "Free during beta. 20 minutes this week?"
        ),
    },
}

# ── helpers ───────────────────────────────────────────────────────────────────

def extract_domain_key(domain):
    """Return lowercase full domain (all parts joined, no TLD) for matching."""
    if not domain or domain.upper() == 'NA':
        return ''
    d = domain.lower().strip()
    d = re.sub(r'https?://', '', d)
    d = re.sub(r'^www\.', '', d)
    d = d.split('/')[0]   # drop path
    d = d.split('?')[0]   # drop query
    # Remove TLD(s): drop last 1-2 dot-segments (.com, .co.in, .in, etc.)
    parts = d.split('.')
    if len(parts) >= 3 and len(parts[-2]) <= 3:   # co.in, net.in style
        core = parts[:-2]
    elif len(parts) >= 2:
        core = parts[:-1]
    else:
        core = parts
    return ''.join(core)  # join all subdomains + domain for broad matching


def classify(row):
    dk = extract_domain_key(row['Domain'])
    type_ = (row['Type'] or '').lower().strip()

    # 1. Check named brand overrides
    for key, (cat, display) in BRAND_OVERRIDES.items():
        if key in dk:
            return cat, display

    # 2. Type-level shortcuts
    if type_ == 'jewellery':
        return 'Jewellery', title_case(dk)
    if type_ == 'electronics & appliances':
        return 'Electronics', title_case(dk)
    if type_ == 'fashion and lifestyle':
        return 'D2C Fashion', title_case(dk)

    # 3. Keyword match in domain
    for cat, kws in KW.items():
        for kw in kws:
            if kw in dk:
                return cat, title_case(dk)

    # 4. Type-based fallback
    if type_ == 'digital goods':
        return 'Digital Goods', title_case(dk)

    return 'D2C Brand', title_case(dk)


def title_case(dk):
    """Convert domain key to a readable display name (first segment only)."""
    if not dk:
        return 'your business'
    # dk is the joined core — split on known sub-domain prefixes
    # Use only first 20 chars to keep names readable
    clean = re.sub(r'[-_]', ' ', dk).strip().title()
    # Truncate at first word boundary after 20 chars if too long
    words = clean.split()
    result = words[0] if words else 'your business'
    return result


_GENERIC_WORDS = {
    'accounts', 'admin', 'info', 'hello', 'help', 'care', 'team', 'payments',
    'finance', 'billing', 'contact', 'support', 'business', 'sales', 'ops',
    'pg', 'tech', 'noreply', 'no', 'hi', 'hey', 'mail', 'email', 'service',
    'one', 'two', 'new', 'web', 'api', 'dev', 'ceo', 'cto', 'cfo', 'hr',
    'it', 'legal', 'digital', 'online', 'official', 'enquiry', 'query',
    'cashfree', 'cashier', 'banking', 'ecom', 'ecommerce', 'revenue',
}

def first_name_from_email(email):
    if not email:
        return 'there'
    local = email.split('@')[0]
    local = re.sub(r'\+.*', '', local)          # strip sub-address
    local = re.sub(r'^\d+', '', local)          # strip leading digits
    parts = re.split(r'[._\-]', local)
    for p in parts:
        p = re.sub(r'\d+', '', p)               # remove trailing digits
        pl = p.lower()
        if len(p) < 3:
            continue
        if pl in _GENERIC_WORDS:
            continue
        # reject if any generic word is a suffix (bcaccounts, cashmgmt, ticketing)
        if any(pl.endswith(w) for w in _GENERIC_WORDS if len(w) >= 4):
            continue
        if any(pl.startswith(w) for w in _GENERIC_WORDS if len(w) >= 4):
            continue
        # looks like a real name segment
        return p.capitalize()
    return 'there'


def enrich(row):
    cat, biz_display = classify(row)
    uc_data = USE_CASES_MAP.get(cat, USE_CASES_MAP['D2C Brand'])

    name = first_name_from_email(row.get('Email', ''))
    pitch = (
        uc_data['pitch']
        .replace('{name}', name)
        .replace('{biz}', biz_display)
    )
    return uc_data['use_cases'], pitch


# ── main ──────────────────────────────────────────────────────────────────────
def main():
    with open(INPUT, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        orig_fields = reader.fieldnames

    new_fields = list(orig_fields) + [
        'Relevant high impact use cases',
        'Pitch line / Email copy with CTA'
    ]

    with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=new_fields)
        writer.writeheader()
        for row in rows:
            uc, pitch = enrich(row)
            row['Relevant high impact use cases'] = uc
            row['Pitch line / Email copy with CTA'] = pitch
            writer.writerow(row)

    print(f'Written {len(rows)} rows → {OUTPUT}')


if __name__ == '__main__':
    main()
