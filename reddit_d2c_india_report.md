# Reddit: Indian D2C Payment Pain — Verbatim Signal

**Scraped:** 2026-05-13 21:40
**Window:** Last 180 days
**Total posts (filtered):** 271
**Top posts with comments:** 40

---

## Subreddit Distribution
- r/developersIndia: **65** posts
- r/IndiaStartups: **61** posts
- r/IndiaBusiness: **55** posts
- r/indianstartups: **31** posts
- r/smallbusiness: **14** posts
- r/n8n: **12** posts
- r/shopify: **12** posts
- r/automation: **10** posts
- r/ecommerce: **6** posts
- r/india: **2** posts
- r/nocode: **2** posts
- r/Entrepreneur: **1** posts

---

## Top 40 Pain-Signal Posts (with comments)

### 1. Me and my Team worked with 20+ Indian D2C brands. Here is the brutal reality of COD &amp; RTO that agencies won't tell you.
**r/IndiaStartups** · 2025-12-05 · 188↑ · 51💬 · pain=245
[https://reddit.com/r/IndiaStartups/comments/1pequ0g/me_and_my_team_worked_with_20_indian_d2c_brands/](https://reddit.com/r/IndiaStartups/comments/1pequ0g/me_and_my_team_worked_with_20_indian_d2c_brands/)

**Post body:**
> We have helped many startups solve common COD (Cash on Delivery) issues, and we’ve audited the data of several D2C brands. The Indian market is unique, and standard "Western" e-commerce advice often fails here.
> 
> Here is the catch, the tips, and the reality check based **on actual ground data**.
> 
> If you are doing less than 500 orders a month, logistics companies generally do not care about your grievances regarding RTO or lost shipments.
> 
> * If you are on Shopify/WooCommerce, opt for services like GoKwik, Magic Checkout, or Shiprocket Checkout.
> * They have data on millions of shoppers. If a user has a history of RTO or fraud, these apps can automatically **Hide COD** as an option for that specific user. It costs a bit of money, but I’ve seen large dips in fraud when using them.
> 
> Add a COD charge, **ideally more than Rs. 100, or push for "Partial Pay"** (pay small amount now, rest on delivery).
> 
> * Yes, it adds friction. But it filters out window shoppers who have zero intent to buy.
> * Since you don’t have trust yet, **Partial Pay** is the middle ground. It proves the customer has a payment method and intent.
> 
> **Retention is the Only Metric that Matters** My mantra in D2C is simple: *"If there is no repeating customer, there is no sale."* Many founders burn money acquiring new customers while their existing ones. If a customer bought via COD and kept the product, you have earned their trust. **Retarget them.** Offer loyalty points, memberships, or exclusive perks. Stop being obse

**Top comments:**
- **axxodesi** (3↑): Very well put. Do you foresee any problems in existing tools or tech being used ?  Is this space crowded already?
- **OrdinaryElk117** (2↑): Hey  Would it be possible for you to give me an experience certificate for a particular tenure ?
- **Arigold_Lloyddddd** (2↑): Great post!  I have been in this industry and agree with most of what's said out here.  Working directly with a courier partner unlocks most value in support and eliminates the middle man, I would suggest eKart for COD orders, they have good conversion.
- **NoExercise3077** (2↑): Would love to connect with you , I am looking to get into this space
- **aquarian9** (2↑): This is nothing to do with COD and I am a buyer. I stopped Amazon ordering as 6 out of 10 orders never delivered and courier always marked customer not available. Amazon never supported me. I realized offline shopping is better and cost effective.  You have to move away from couch.

---

### 2. How are you guys dealing with COD fraud? It's killing my margins.
**r/IndiaStartups** · 2025-11-28 · 78↑ · 68💬 · pain=225
[https://reddit.com/r/IndiaStartups/comments/1p8o8h6/how_are_you_guys_dealing_with_cod_fraud_its/](https://reddit.com/r/IndiaStartups/comments/1p8o8h6/how_are_you_guys_dealing_with_cod_fraud_its/)

**Post body:**
> Hey everyone
> 
> A friend of mine is running a small apparel DTC brand and COD fraud is becoming a serious problem these days.
> 
> Last month alone, 23% of COD orders were fake/undelivered, average loss per fake order is around ₹350... because we need to package, bear shipping on both ways and other logistics costs.
> 
> We've tried, OTP verification, restricting certain postal codes where we get more fake orders and even tried charging a bit extra for COD orders. Nothing is really helping :(
> 
> So I wanted to ask what's working for you to reduce COD fraud? Is there a way to build trust so customers choose prepaid more often?
> 
> Any advice would be really helpful.

**Top comments:**
- **Pristine_Egg_7187** (2↑): Dont offer COD till you can financially afford the risks associated. Even if you remove COD, the people who really want to try the product will buy it either way, period. If they dont, the problem is with your marketing/product improvement and you've got to rethink the process. 
- **i_didnt_get_one** (2↑): Either you don't offer it or you only offer it after a user has already made a few orders.
- **Unlikely_Ad_4366** (2↑): You can create a risk profile of all your customers based on their postal codes, devices and other very specific data.  Blacklist pin codes with the highest default rates. Accept only full payment from those pincodes.  Add a gamification feature - if they are recurring customers over a certain LTV, only then they get to place COD.  Also check your logistics partner, often their last mile delivery agent don't deliver and mark the delivery as " out for delivery" or even attempted delivery 🚚   It has happened to me several times.
- **Any-Neighborhood-686** (2↑): I have few ideas on this. 1.add an upfront payment of 10% of the order value as payment for COD orders  2.offer escrow payment option instead of offering COD. Most of the fake orders would stop the moment payment is involved. Money would be returned for genuine cases.  2nd option is a startup idea I have. Let me know how it looks :)
- **speedracer316** (1↑): Please update the post if you find a solution that works

---

### 3. DO NOT USE _ in Your webhook urls, learned it the hard way
**r/developersIndia** · 2026-02-06 · 334↑ · 40💬 · pain=225
[https://reddit.com/r/developersIndia/comments/1qxfsrw/do_not_use_in_your_webhook_urls_learned_it_the/](https://reddit.com/r/developersIndia/comments/1qxfsrw/do_not_use_in_your_webhook_urls_learned_it_the/)

**Post body:**
> In short:- using \_ in webhook or any url will make it not work with meta or other api provider, if you dont seem to get any request on your server this might be the issue. 
> 
> Longer yapping:-
> 
> I'm going to voice type this. so I've been building this project for a property dealer on whatsapp AI agent and everything was working fine on the local system I deployed it on a EC2 instance on AWS and there I had a cloudflared tunnel with a URL that had an \_ in it, and As soon as I deployed this on production I noticed meta was not sending any request to my AWS server now I thought this might be AWS server security issues so I just fixed that, gave all the permission everything I thought cloudflare might have some issues I fixed that you know looked at everything, I also used all the AI tools okay to find out what's going on I spent like hours on this. I did deep research on the specific things I was facing and mind you the URL was always visible in every single text I sent to every single AI and to every single Google search I did and for some reason there was not a single thing I could find about this okay so I am typing this in hopes of helping someone else I just hoped that if this is something that's not allowed I would get a single error or a log or anything from meta or from cloudflare or anyone saying okay this is not allowed and this might cause some issues or anything, I was hoping to get something, at least some logs, some error, so that I would know what's wrong or maybe 

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **No_Life_27** (159↑): Its funny how sometimes we have to waste so much time finding a small issue which isnt even our fault.. thanks for sharing this info OP!
- **CommissionSad6916** (28↑): I will do you one better. Our API key validation was failing. It was our own API key for our product. Spent entire fucking day just to find out that it was better auth's fault.  And whats interesting ? The rolled out the fix just 30 mins ago when I found out the better auth problem.  Wasted entire day just to run: npm update better-auth  Lesson learned for my project atleast: update better auth if any auth issue  And we faced similar issues with better auth twice in the last week
- **Helpful-Diamond-3347** (6↑): there are lot such gotchas we face in our experience   i designed a js sdk to be injected in client's webpages but who could imagine that some static pages were re rendered as iframes to some pages, which means single script is loaded more than once in a page  production is crazy, appreciated your valuable insight too
- **BitterAd6419** (4↑): Reminds me of that me - you fking you fking you lol

---

### 4. I spent 2 months building a WhatsApp AI sales agent for my family's clothing store. 44 nodes, 2 AI agents, 8 conversation stages. Here's what I actually built.
**r/n8n** · 2026-03-25 · 356↑ · 117💬 · pain=225
[https://reddit.com/r/n8n/comments/1s3hejk/i_spent_2_months_building_a_whatsapp_ai_sales/](https://reddit.com/r/n8n/comments/1s3hejk/i_spent_2_months_building_a_whatsapp_ai_sales/)

**Post body:**
> My family runs a clothing store in Jaipur. Like most small retail shops in India, their entire customer interaction happens on WhatsApp.
> 
> Every day, my brother was handling the same messages manually:
> 
> * "Kya available hai?" (What's available?)
> * "Budget 5000 hai, kya dikhao ge?" (Budget 5000, what can you show me?)
> * The same category and budget questions from 20 different people.
> * Customers waiting 30 minutes for a product link, giving up, and going elsewhere.
> 
> 
> 
> He was running Instagram to bring leads in. The leads were coming. But there was nothing on the other end to handle them. Just a phone and one person replying to everything.
> 
> I'd been learning n8n and building small AI workflows for a while. I thought: this is exactly the problem automation is supposed to solve.
> 
> What I didn't expect was how long it would take.
> 
> Version 1 was embarrassing. A basic webhook that sent a canned reply. Fine for testing, useless for real customers.
> 
> The real problem hit around version 3. A customer sends "hi", the agent greets them, they say they want something, the agent jumps straight to asking for their name and budget. Same customer messages the next day. The agent has no idea who they are.
> 
> No memory. No routing. No sense of where a customer is in their journey.
> 
> I started over properly.
> 
> 
> 
> The final system: 44 nodes, 2 AI agents
> 
> Entry layer (before AI even runs):
> 
> Every incoming WhatsApp message passes through a filter first:
> 
> * Is this from the store's own number? Ignore.
> * Is i

**Top comments:**
- **AutoModerator** (1↑): **Attention Posters:**   - Please follow our subreddit's rules:  - You have selected a post flair of Workflow - Code Included - The json or any other relevant code MUST BE SHARED or your post will be removed. - Acceptable ways to share the code are:    - Github Repository    - Github Gist    - n8n.io/workflows/    - Directly here on Reddit in a code block - Sharing the code any other way is not allowed.    - Your post will be removed if not following these guidelines.   *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/n8n) if you have any questions or concerns.*
- **DepartureNo2745** (25↑): If you post a workflow, which you did, you must include a GitHub link to its code   Please add it or this post will be removed 
- **South-Opening-9720** (6↑): This is the part people miss: the model is rarely the hard part, the state machine is. The only thing I’d add early is cleaner human handoff plus shared context across channels, because that’s where these builds usually get messy. I use chat data for similar support flows and the useful bit is less “AI magic” and more routing, memory, and knowing when to stop automating and hand it to a person.
- **gokhan02er** (4↑): This is a really solid build, thanks for sharing! It’s clear it reduced the manual burden for the store, but I’m curious about the customer side too. Have you noticed a real improvement in customer satisfaction or sales, or do customers still get frustrated and drop off?  
- **nova-50** (3↑): Don't mind me but your workflow is dumb. You're calling Google Sheet A lot and that will have a massive cost. You should use some other database.

---

### 5. 10cr revenue business down to 2cr debt, need advice!
**r/IndiaBusiness** · 2026-03-24 · 359↑ · 169💬 · pain=220
[https://reddit.com/r/IndiaBusiness/comments/1s239nz/10cr_revenue_business_down_to_2cr_debt_need_advice/](https://reddit.com/r/IndiaBusiness/comments/1s239nz/10cr_revenue_business_down_to_2cr_debt_need_advice/)

**Post body:**
> TLDR-
> 
> 1. Father had trading business but ran on credit cycles of more than a month.
> 2. To save the business, started own clothing brand and setup a manufacturing facility.
> 3. Started selling on ecommerce platforms thinking the payments would be secured.
> 4. Faced TM registration issue because of objection from a reputed Japanese brand.
> 5. Spent money on ads and product quality but others copied the same.
> 6. Suffered losses due to low cashflow and returns.
> 7. Loans and garment stock piled up.
> 8. Father took loan against property as well.
> 
> Need some advice on how to proceed further and get to stability. Either via job or doing something else in the business.
> 
> Thank you!
> 
> Edit - Thanks a lot for the overwhelming response. I received so many valuable advices in comment section and some helping hands who reached out to me in DMs asking for the product catalog. 
> 
> I hope some of them actually convert to potential buyer, so some cash flows in.

**Top comments:**
- **Accomplished-Tax-521** (43↑): I know how this feels buddy, stay strong 
- **YodaYodha** (24↑): Dude you are one firebrand who did not bother to check the eco system before putting your stakes . What has happened with you is nothing unique ask any one selling on online platform you will hear same story. Ask Trade mark registration office , stupid for small ones to object , you will win but will take your entire time . Time is the most expensive capital you have . You need to talk more to people who have already gone through this , listening others need not make you compliant but know better when to follow and when to go offbeat.  3 things you can do immediately  A Stick to your job , you need more exposure without burning yourself.  B Network , Network Network...make many Gurus .  C dispose off any stock in excess of your 3 months sales or whatever  replenishment stock level . 
- **Final-Batz** (21↑): Here's what I feel based on my understanding of the description:  Your business is in need of new customers, as your existing circle vanished during pandemic.  There are 2 ways such businesses operate today:  1. Roll out specific consumer clothing which is available in your stock or is a regular part of it. Make targeted social media content around the same using Insta and maybe Facebook. Have shipping partners like Delhivery or Rocketreach to enable direct shipping from your own website not dependent on Amazon/ Flipkart.  Expected costs for the above would be about 30k INR and max 2 weeks to setup. What it needs is consistency and dedication to customer review and detailing.   PS: Share different journey topics like your own, of the material you sell and processing over insta/ shorts. The
- **Temporary_Dare_5773** (10↑): I will suggest you to go for the job. Because the economy and market conditions are not good for business in recejt times. There are so many ups and downs , so choose wisely. I am a 28M businessman myself and facing similar problem. But now i have made my younger brother leave the business and settle for job. And im thinking of changing my business style also.
- **adikul** (9↑): One point, 10cr was revenue and 2cr is net loss and as it is debt it will keep increasing.  Also good luck for your future 

---

### 6. [Review] China to India Freight Forwarder Experience (DDP, Audio Gear, 12 Days)
**r/IndiaBusiness** · 2026-05-02 · 119↑ · 57💬 · pain=220
[https://reddit.com/r/IndiaBusiness/comments/1t1bs66/review_china_to_india_freight_forwarder/](https://reddit.com/r/IndiaBusiness/comments/1t1bs66/review_china_to_india_freight_forwarder/)

**Post body:**
> I know many of you here are constantly looking for reliable logistics for importing samples or inventory from China, so I wanted to share a successful run I just had. I recently used a forwarder for a shipment from China to India and the experience was solid.
> The Shipment Details
> 
> 
>   **Cargo**: 25k Rs worth of electronics/audio gear (IEMs, DACs, and eartips). Minimum quantity was 2kg
> 
> 
>   **Route**: China Warehouse to Delhi and Dispatched via Tirupati Courier to my house.
> 
> 
>  **Timeline**: 12 days (landed exactly within the promised window).
> 
> 
> **The Process &amp; Logistics**
>  They asked for specific details including dimensions, HS codes, and a packing list (all of which were easy to grab from the seller).
> 
> 
>  **Communication**: While there was no live tracking link, I received updates at three times arrival at the China warehouse, loading/departure, and arrival in India for final payment.
> 
> 
>  **Payment Terms**: Payment was handled after arrival in India, not upfront. For a first-time use, this definitely reduced the risk factor.
>  
> 
> **Service Style**: It’s a budget-friendly DDP-style setup (Delivered Duty Paid), which helps keep the landed cost predictable.
> Final Take
> If you are an entrepreneur or a small business owner looking for a legit, budget-conscious freight option for smaller tech/electronics hauls, this setup is worth considering. Just be sure to confirm your specific pricing based on weight/volume before you ship.
> 
> 
> **Group Buy &amp; Support**
> The forwarder has a WhatsA

**Top comments:**
- **Sada_dosa_** (20↑): In my experience, the first few runs are always good..as a result you end up gaining confidence and increase your lot to 2-5 lakh rs. Thats when one of the runs gets stuck and all your savings of the previous runs get stuck. Best way is to understand how the logistics work, tie up with similar buyers from India and try to get a direct consignment (of a much bigger size)   Glad for you though
- **bokato2** (3↑): How much did you end up paying?
- **NewmanGoodman** (3↑): Is it the same cost as shipping from sites like alibaba
- **Sensitive_End_2286** (2↑): thanks for sharing man, recently got some materials from a friend. Had it through fed ex - such pain in the ass to pass customs  
- **CalmApartment8637** (2↑): How did it include customs fee because i have heard you have to pay customs after it has arrived in india like they decide on the basis of goods

---

### 7. A boring startup that quietly makes money while everyone else chases startup trends
**r/IndiaBusiness** · 2026-03-06 · 97↑ · 53💬 · pain=220
[https://reddit.com/r/IndiaBusiness/comments/1rmoqaz/a_boring_startup_that_quietly_makes_money_while/](https://reddit.com/r/IndiaBusiness/comments/1rmoqaz/a_boring_startup_that_quietly_makes_money_while/)

**Post body:**
> For a long time I was stuck in the same loop most aspiring founders go through.
> 
> Every day I would see new startup ideas on social media. SaaS tools, AI products, ecommerce brands, dropshipping stores, recruitment agencies, marketing agencies, productivity apps, billing software for local shops, hyperlocal delivery ideas, and the endless “low budget startup ideas” videos.
> 
> At first everything sounds exciting. But after observing closely, most of these ideas are extremely crowded now.
> 
> Restaurants and cafes open everywhere and shut down within a couple of years because margins are thin and competition is brutal.
> 
> Local businesses like small retail, service centers, or agencies are fighting for survival because every street already has multiple competitors doing the same thing.
> 
> Ecommerce and dropshipping look attractive online but in reality customer acquisition costs are rising, returns are high, and platforms control everything.
> 
> SaaS and software products sound scalable, but thousands of founders are building similar tools and most struggle for years just to get a few paying customers.
> 
> Recruitment agencies and service businesses also face intense competition because entry barriers are very low.
> 
> After going through months of confusion and overthinking, I realized something important.
> 
> A lot of startup conversations today are driven by hype rather than real revenue opportunities.
> 
> Everyone wants to build the next AI product or fancy tech platform, but very few people are lo

**Top comments:**
- **No-Job-2302** (10↑): Isn't managing a virtual call center a pain in the ass.. managing one out of an office has its own problems so unless you don't get the most sincere workers u in for some problems 
- **Specialist_Bird9619** (5↑): how did you approach or find clients?
- **CalendarMysterious13** (3↑): Yes well said boring business are real cash flow machines
- **Remarkable-Estate-33** (2↑): But how do you get clients who will be interested in virtual call centre?
- **sumanbcn** (2↑): That’s exactly what squadstck does. AI is replacing call centers. 

---

### 8. The Three-Generation Curse is real: Lessons after working with 250+ Businesses
**r/IndiaBusiness** · 2026-04-20 · 304↑ · 52💬 · pain=215
[https://reddit.com/r/IndiaBusiness/comments/1sqmgqp/the_threegeneration_curse_is_real_lessons_after/](https://reddit.com/r/IndiaBusiness/comments/1sqmgqp/the_threegeneration_curse_is_real_lessons_after/)

**Post body:**
> I run a corporate video agency and spend most of my time with the decision-makers of mid and large-sized manufacturing businesses. When you spend weeks with these companies, you start to see exactly how family dynamics affect the business. After working with **250+ businesses**, here is what I have observed about working with different generations.
> 
> # 1. The 1st Generation
> 
> * These are the people who built the empire from zero. They are usually the most grounded.
> * These are usually my favorite people to work with. They are grounded and have a lot of respect for the "craft."
> * They respect the effort you put in. They ensure you are paid on time because they value their word and understand what it takes to run a small business.
> * They know every single worker's name and can identify a machine fault just by the sound it makes.
> * They are usually humble, straightforward, and value every penny spent.
> 
> # 2. The 2nd Generation
> 
> I usually split this generation into two very different categories.
> 
> 1. **The Value Adders:**
>    * These are the children who took what their parents built and took it forward.
>    * They are very professional and easy to work with because they have a clear vision for the brand. They also ensure you are paid on time.
>    * They are the ones who implement modern systems, ERPs, and tech that actually allow the company to scale.
>    * They respect the hierarchy but favor merit. They hire professionals to run departments instead of just relying on relatives.
> 2. **T

**Top comments:**
- **django-unchained2012** (41↑): There is a saying in Tamilnadu that wealth won't last the third generation and the advice is to sell everything they own and buy new.   What you are saying perfectly aligns with this thought. The third generation becomes very lethargic and usually lives on the hardwork of their ancestors, they don't know how to make or manage money. Everything they want can be bought easily with little to no effort.  If the third generation let go of their ancestral business and start something new, they can learn to sustain that wealth.
- **doozyrae** (37↑): That's absolutely true  I have seen 4 families with the exact similar pattern The first generation extremely humble helpful grateful and respectful The second ones are of similar behaviour but with the modern touch but they have seen and been through the process themselves And the current generation who been just enjoying the privilege and act all bossy and all mighty but are no good for the business
- **Unknown21892** (32↑): I completely agree with you.  I had read a quote by the founder of Saudi Arabia  It said, my grandfather rode a camel, my father rode a Ford &amp; I drive a Rolls Royce. But my son will will ride a Ford &amp; my grandson will ride a camel
- **cranky_finicky** (14↑): This is so true. Very rarely does a business family escape the 3rd generation curse.  If the enterprise is large, the 3rd generation drags it down and 4th gen drowns it completely.
- **shrikant_shet** (14↑): I worked with the third generation in one family owned business - the first generation started with a small part, second generation built a mechanical product and third generation built electrical/electronic product based on the second generation’s product. Also, the third generation brought in tech - IT/ERP, custom apps for small daily tasks, small mechanical+electronics automations, huge efficiency improvements with newer machines and tools (CNCs, VMCs, …). Third generation almost did 50x revenue as well as profits that of second generation in about 12 yrs.  All 3 generations have had their own products, with their own manufacturing and the owners themselves travel globally for sales. The work ethic across generations has been amazing.   This could be an exception or the 250+ companies O

---

### 9. Importing from China is easy… until you try to pay the supplier
**r/IndiaBusiness** · 2026-05-09 · 226↑ · 57💬 · pain=215
[https://reddit.com/r/IndiaBusiness/comments/1t7wp21/importing_from_china_is_easy_until_you_try_to_pay/](https://reddit.com/r/IndiaBusiness/comments/1t7wp21/importing_from_china_is_easy_until_you_try_to_pay/)

**Post body:**
> I’m planning to start importing products from China and right now my biggest issue is payments.
> 
> The supplier I’m talking to only accepts Alipay, bank transfer, and PayPal. If I use PayPal, they charge an extra 4.8%, which is a lot since the products already have low margins and heavy competition.
> 
> I currently have a zero forex markup card with good exchange rates, but under India’s LRS scheme there’s the ₹10 lakh limit, after which 20% TDS applies. That becomes a big problem for larger payments.
> 
> From what I understand:
> 
> * Personal cards, Wise, PayPal, etc. still come under LRS
> * Business/current account wire transfers may not fall under personal LRS
> * But SWIFT/wire transfers also have extra charges like:
>    * bank fees
>    * intermediary bank fees
>    * forex markup
>    * supplier receiving fees sometimes
> 
> The problem is that even small fees become a lot on bigger payments. For example, if I pay ₹10 lakh for goods, even a 2–5% extra cost becomes a huge amount and can completely affect profit margins.
> 
> For people who regularly import from China:
> 
> * What payment methods do you usually use?
> * Which banks give the best forex rates for business payments?
> * Are there any other commonly used payment methods besides PayPal, Alipay, WeChat Pay, and bank transfer?
> 
> Would appreciate advice from people who regularly deal with Chinese suppliers, especially Indian importers.

**Top comments:**
- **ChiragKharote** (65↑): Bank transfer are the cheapest. They have a fixed fee, not a percentage like other methods charge you. The forex markup is minimal.   Transfers fees are max 15-30 USD even for larger amounts.   Now you can directly make a forex transfer from your banking app or website, no paper work required for several banks. 
- **Public_Entry_3759** (47↑): Importing from china 15years+. Just two ways, bank (legal) way. Or cash via agents . Any other way, would increase the price so much that you may end up in loss or zero margin.   Hdfc/icici are the best. For Heavy volumes, they charge xe+5p commision. And 500/- fixed fee.   Alipay, wechat pay are used by cash agents. 
- **Mannloke** (20↑): register a company (subsidiary) in china, problem solved.   you can even expand what you are selling in future.
- **Inside_Programmer348** (6↑): I hate this chindichor govt for introducing LRS. and they have the audacity to call it liberal
- **Scary-Craft-4995** (3↑): I have been importing from China since 2016, and for the past four years, I have had my own company in China. The reason your supplier is asking for payment in a personal account is to save 13% VAT. If you pay officially through a bank transfer, they are required to issue a commercial invoice, which results in additional tax. The best option for you is to transfer the money to their personal RMB account or via Alipay. There are also people who can handle this on your behalf, or if you have an agent managing your shipment they can assist you with the payment 

---

### 10. I mapped 1,000+ Indian D2C brands across 429 micro-niches so I could stop making blind bets on what to build. Here's what surprised me.
**r/indianstartups** · 2026-04-23 · 118↑ · 508💬 · pain=215
[https://reddit.com/r/indianstartups/comments/1sta4hb/i_mapped_1000_indian_d2c_brands_across_429/](https://reddit.com/r/indianstartups/comments/1sta4hb/i_mapped_1000_indian_d2c_brands_across_429/)

**Post body:**
> Six months ago I was trying to decide between two category ideas. Both felt real. Both had Reddit threads full of complaints. But I had no way to compare them systematically — who was already in each space, how crowded it actually was, whether the brands there were growing or coasting, and whether the demand signal was new or old noise.
> 
> So I did something dumb: I spent three weeks building a spreadsheet. Manual Googling. Instagram follower counts copied by hand. YouTube subscriber counts from six different tabs.
> 
> Then I gave up on the spreadsheet and built an actual tool.
> 
> Today impuls8 tracks 1,042 Indian D2C brands across 19 categories, 100 subcategories and 429 micro-niches. We pull Instagram, YouTube, Reddit and Google Trends data every week. The goal is dead simple: before you pick a category, see the actual landscape.
> 
> Things that surprised me while building this:
> 
> 1. Food &amp; Beverage is by far the most crowded category — 130 brands, and growing. Beauty is only 76. The absolute brand count is the opposite of what most people assume.
> 2. Women's health has 5 distinct sub-niches (PCOS, hormonal health, prenatal/postnatal, menopause, bone &amp; joint) but the brand coverage is wildly uneven. PCOS is crowded. Menopause support has almost nobody.
> 3. Pets has 20 brands but pet dental care is essentially empty. Heads Up For Tails and Supertails have built great general pet stores — but nobody has gone deep on a specific sub-segment.
> 4. Sustainable/eco has 21 brands. Shampoo

**Top comments:**
- **Dismal-Rise6734** (6↑): Please give me access ti the tool  
- **SelvaMurali85** (2↑): Hi i would like to explore all, if possible share it please  

---

### 11. Top 30 list of  companies i will focused for SDE 2 roles
**r/developersIndia** · 2026-02-26 · 578↑ · 243💬 · pain=215
[https://reddit.com/r/developersIndia/comments/1rfd76n/top_30_list_of_companies_i_will_focused_for_sde_2/](https://reddit.com/r/developersIndia/comments/1rfd76n/top_30_list_of_companies_i_will_focused_for_sde_2/)

**Post body:**
> Hey folks,
> 
> Wanted some honest advice from people who’ve made the jump.
> 
> A bit about my journey:
> 
> I started my career at 7 L in a support engineer role. After around 2 years, I got frustrated because I didn’t want to stay in a pure support path. I resigned without another offer (probably risky), stayed jobless for \~4 months, prepared seriously, and eventually cracked an SDE role.
> 
> Right now I’m working as a  SDE, currently in the 15–17 L range.
> 
> By the end of this year or latest by Q1 2027 (so roughly 8–12 months from now), I want to move into a proper SDE-2 role. By then I’ll have 3.5+ years of experience.
> 
> I’ve made a list of \~30 product companies (big tech, fintech, SaaS, strong Indian product orgs) that I want to systematically target instead of randomly applying.
> 
> The salary range is just an average I could find, it could be totally different.
> 
> Elite Tier (70L – 1C+ TC)
> 
> Stripe – 80L – 1C+  
> Google (India) – 65L – 95L (not my dream company)  
> Meta (Facebook India) – 70L – 1C  
> Airbnb – 70L – 90L  
> Rubrik – 75L – 90L  
> Coinbase – 70L – 90L  
> [Booking.com](http://Booking.com) – 60L – 85L (my dream company)  
> Databricks – 70L – 95L  
> Snowflake – 70L – 95L  
> Tower Research Capital – 80L – 1C+  
> Quadeye – 80L – 1C+
> 
> Upper Mid Tier (50L – 75L TC)
> 
> Uber – 55L – 80L  
> LinkedIn – 55L – 75L  
> Salesforce – 50L – 75L  
> ServiceNow – 50L – 75L  
> Microsoft (India) – 50L – 75L  
> Intuit – 50L – 70L  
> Walmart Global Tech – 45L – 65L  
> Goldman Sachs – 50L – 75L  
> JPMorgan Chase – 45L – 6

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **needsleep31** (155↑): Razorpay isn't paying that much anymore, at least from what I know. They've also stopped giving ESOPs to new joinees now since they're preparing for IPO.
- **Fuzzy_Group_9073** (83↑): These salary ranges are highly inflated. I am an SDE - 2 who has gone through the processes of these orgs and had few offers. These are not the real ranges. More like half of what's mentioned
- **TalkZealousideal2666** (46↑): stripe pays approx 1cr for sde-2 and sde-3 band is wider, ranging from 1.2 - 1.8cr
- **Outspoken_Infantry04** (33↑): U missed the elite of elite....   BlackRock,Citadel,Vanguard,Mercer.

---

### 12. My cousin got scammed out of ₹26000, posting this here for awareness.
**r/developersIndia** · 2026-02-19 · 440↑ · 56💬 · pain=215
[https://reddit.com/r/developersIndia/comments/1r90ypl/my_cousin_got_scammed_out_of_26000_posting_this/](https://reddit.com/r/developersIndia/comments/1r90ypl/my_cousin_got_scammed_out_of_26000_posting_this/)

**Post body:**
> My cousin recently got scammed out of ₹26000. I am a student not in the same field so do let me know if this is the right sub to post or not.
> 
> He has a 4LPA salary and has been actively searching for data analyst roles in other companies. Last month, he got selected for an interview at EXL services. The interview rounds were highly professional with english fluent interviewers. There was a hands-on experience round in which they were not satisfied with his answers. But he still qualified and finally, an offer letter was sent stating an 8.5LPA salary. But before he could join, he was required to purchase a course from "algogladiators" priced at ₹26000 to get better and be industry ready. He was promised the job and also a refund if he passed the test at the end of the course with 60%+ marks (I'm not sure about the exact details). 
> 
> This was sketchy, but the procedure was super professional, the person from the company in contact with him also had a linkedin profile with the same credentials as mentioned. The offer letter, which he forwarded to me was a proper 20 page document with everything one would expect from an offer letter. We were convinced it was legit. The next suspicious part is, he couldn't directly pay algogladiators with his credit card and had to purchase a voucher from another reputed website to pay for the course. 
> 
> Finally the course was bought. It was a 25 day course with lectures assigned for each day. He kept watching it and learning for 25 days straight. T

**Top comments:**
- **dipshi27** (290↑): Any job which requires money in any form is a scam, however professional/polished it may seem.
- **Suspicious-String-46** (70↑): How did he received the offer letter?, through the original company mail ID?
- **MasalaDosa37** (20↑): File a complaint in the cyber crime cell and get the account of the scammer frozen. Might recover the money.
- **zhingooora** (16↑): Happened with my spouse as well, luckily I paid using a credit card and reached out to the credit card support, they have refunded the amount but the transaction is in dispute, The merchant has 45 days to prove that the transaction is valid.
- **ActBig9637** (12↑): The basic thing to check is the domain of the mail id from which the offer letter was received. It should be @company.com. @exl.com in your case. Generating a 20 page offer letter and creating a LinkedIn profile is just a piece of cake. One more thing is most of the MNCs have either their own recruitment platform or they use portals like workday for hiring. Nowadays no one sends an Offer letter to mail ID except small companies. Also no genuine company asks for money or any course before joining the organisation.

---

### 13. Why are we still paying Vercel in Dollars? I built an Indian PaaS with UPI &amp; ₹199 pricing. Tell me why it’s a bad idea.
**r/developersIndia** · 2025-12-22 · 534↑ · 153💬 · pain=215
[https://reddit.com/r/developersIndia/comments/1pssshl/why_are_we_still_paying_vercel_in_dollars_i_built/](https://reddit.com/r/developersIndia/comments/1pssshl/why_are_we_still_paying_vercel_in_dollars_i_built/)

**Post body:**
> Tech community,
> 
> Let’s be real AWS, Vercel, and Heroku don’t care about the Indian developer. If you are a student or a freelancer here, you’re stuck with:
> 
> * **International transaction failures** on your debit cards.
> * **Paying $20 (₹1,600+)** for basic features because of the USD conversion.
> * **High latency** because the nearest "cheap" server is in Singapore or US-East.
> 
> I got tired of waiting for a "Local Vercel," so I built Riven Deploy
> 
> .
> 
> **The Goal:** Git push to deploy, pay with UPI, and host on Mumbai servers starting at **₹199**.
> 
> **What’s under the hood so far:**
> 
> * **Full Git Integration:** Connect GitHub/GitLab and deploy on every push.
> * **Zero-Config:** Automatic SSL, Custom Domains, and Env Variable management.
> * **Tech Stack:** Native support for Next.js, React, Node, Python, and Go.
> * **The "Desi" Edge:** Native UPI integration and localized support.
> 
> **The "Aggressive" Part:** I know what you're thinking: *"Why should I trust a new platform with my code?"* or *"Is this just another wrapper?"*
> 
> I’m looking for the **harshest feedback possible**. I’m at 0 users and I want to fix that by building something that actually works for us.
> 
> **I want you to roast me on:**
> 
> 1. **The UI/UX:** Is it trash? Does it feel "cheap"?
> 2. **The Architecture:** Ask me the hard questions about security and isolation.
> 3. **The "Trust" Factor:** What is the #1 thing stopping you from moving a side project here?
> 
> I’m a solo founder building this for the Indian dev community. Be a

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **Sridhar02** (142↑): [https://postimg.cc/JG9bbyfH](https://postimg.cc/JG9bbyfH) . I don't want to deploy with out knowing anything about the company, if something goes wrong it si hard, cheaper is not always I preper, I may choose $5 railway &amp; gradually upgrade it when I have users, instead beliving an known person, even vercel has that where if some one DOSS my site it will protect me , is your platform that effecient ?
- **Sridhar02** (71↑): chepest way is to take a heztner &amp; use something like [https://coolify.io/](https://coolify.io/) to use it as it does everything a vercel , you own everything from db, server &amp; anything
- **[deleted]** (40↑): Who's developing this? New firm, no founder name or creds, 0 users so far ... As a potential customer, how do I know this is not vibe coded trash?
- **gepilo8695** (33↑): I paid my AWS bill via UPI - it's supported.  But, I see the 18% added GST as a bigger problem.  I was doing the same PoC w/ 2 accounts, one work email (based in the US, with corporate CC) and the other my personal account based in India. The Bill was similar, but I had to pay an extra 18% GST in India.

---

### 14. Why doesn’t India have its own Vercel? I’m trying to build one. Roast my idea.
**r/developersIndia** · 2026-03-05 · 168↑ · 132💬 · pain=215
[https://reddit.com/r/developersIndia/comments/1rl7ewt/why_doesnt_india_have_its_own_vercel_im_trying_to/](https://reddit.com/r/developersIndia/comments/1rl7ewt/why_doesnt_india_have_its_own_vercel_im_trying_to/)

**Post body:**
> Hello Tech community,
> 
> Let’s be real AWS, Vercel, and Heroku don’t care about the Indian developer. If you are a student or a freelancer here, you’re stuck with:
> 
> * **International transaction failures** on your debit cards.
> * **Paying $20 (₹1,600+)** for basic features because of the USD conversion.
> * **High latency** because the nearest "cheap" server is in Singapore or US-East.
> 
> I got tired of waiting for a "Local Vercel," so I built Riven Deploy.
> 
> **The Goal:** Git push to deploy, pay with UPI, and host on Mumbai servers starting at **₹199**.
> 
> **What’s under the hood so far:**
> 
> * **Full Git Integration:** Connect GitHub/GitLab and deploy on every push.
> * **Zero-Config:** Automatic SSL, Custom Domains, and Env Variable management.
> * **Tech Stack:** Native support for Next.js, React, Node, Python, and Go.
> * **The "Desi" Edge:** Native UPI integration and localized support.
> 
> **The "Aggressive" Part:** I know what you're thinking: *"Why should I trust a new platform with my code?"* or *"Is this just another wrapper?"*
> 
> I’m looking for the **harshest feedback possible**. I’m at 0 users and I want to fix that by building something that actually works for us.
> 
> **I want you to roast me on:**
> 
> 1. **The UI/UX:** Is it trash? Does it feel "cheap"?
> 2. **The Architecture:** Ask me the hard questions about security and isolation.
> 3. **The "Trust" Factor:** What is the #1 thing stopping you from moving a side project here?
> 
> I’m a solo founder building this for the Indian dev community. 

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **holey_shite** (88↑): 0 trust in this as it stands.   The pricing page does not tell anything. What is the difference between 299, 699 and 1499 ? All of them have the exact same placeholders.   The Services and Resources dropdowns on your home page show generic descriptions for the controls.   This is the problem most people have with vibecoded apps. You created a site, but did not even take time to proofread basic stuff and you expect us to QA for you with no way to even see a demo without having to give my email address ? No thanks.   
- **mello_hyu** (40↑): Looks cool tbh and great idea, we definitely need something like this.  The pricing plans list the same things with no differentiation, how am I to know how pro is better than starter ?  The UI can definitely use some work, idk looks a bit bland/static, opposing the overal theme vibes.  That bottom right div showing page views in last 30 days looks annoying, why not add a cross button there to close it ?  P.S. : Is it open source ?I would love to contribute to this great project.
- **Warlock2111** (30↑): As someone that pays for vercel (because commercial product requires a pro plan), quick feedback without testing the platform but for the post.  \- Who's your target audience? If it's students/vibe coders, why won't they stick with vercel's free plan or cloudflare pages/workers? If it's users that have a commercial product, and they are whining about a $20/mo infra cost, they either need to pivot to a different product that makes money or intends to make money or stop being cheap.  \- How long before you realise that 199/mo isn't sustainable and which is why most infra companies don't do it (Cloudflare gives shit out for free because A. Public company, B. Enterprise and nearly 60% of the world runs on it makes them enough money to give shit out for free)  \- The cheap price is a turnoff in
- **miserableLad7** (24↑): why doesnt India has its own "X"

---

### 15. Built a free tool for my wife's home bakery — she was spending 30 mins every day chasing UPI payments on WhatsApp
**r/IndiaBusiness** · 2026-03-24 · 129↑ · 38💬 · pain=210
[https://reddit.com/r/IndiaBusiness/comments/1s2glfy/built_a_free_tool_for_my_wifes_home_bakery_she/](https://reddit.com/r/IndiaBusiness/comments/1s2glfy/built_a_free_tool_for_my_wifes_home_bakery_she/)

**Post body:**
> My wife runs a home bakery. Every evening she'd open WhatsApp, scroll through 40 chats, and try to
> 
> remember who paid and who didn't. She'd screenshot payment confirmations, paste them in a notes app, do mental math. It was chaos.
> 
> I'm a developer so I built her a simple tool — she sends a payment link on WhatsApp, customer scans a
> 
> UPI QR and pays, she sees exactly who paid and who still owes. No more chasing.
> 
> Turns out tutors, freelancers, and Instagram sellers have the exact same problem. So we opened it up.
> 
> It's called YugaPe. Free forever for the basics. Would love feedback from anyone running a small business here — what's the most painful part of collecting payments for you?
> 
> Link in comments 

**Top comments:**
- **OwlIntelligent6836** (16↑): Here's the link: [yugape.in](http://yugape.in)   Happy to answer any questions about how it works.
- **Working-Situation766** (9↑): How about YuPe over YugaPe or something easy? Am I the only one who has problem with the name?
- **reddituseonlyyy** (3↑): What if someone sends scam link on her behalf
- **ash_ai** (3↑): this is a real problem. every small home business owner in india chases payments manually. the wedge is clear, the distribution channel (whatsapp) is already where the users are. good luck with yugape.
- **intimidator** (1↑): We use zoho payments with zoho pos to track this. 

---

### 16. Shopdeck review, my personal experience (good and bad)
**r/IndiaBusiness** · 2026-01-09 · 7↑ · 186💬 · pain=210
[https://reddit.com/r/IndiaBusiness/comments/1q83h1f/shopdeck_review_my_personal_experience_good_and/](https://reddit.com/r/IndiaBusiness/comments/1q83h1f/shopdeck_review_my_personal_experience_good_and/)

**Post body:**
> I have been running a small home decor/lifestyle brand for my dad for about 2 years now. I manage the online part. Earlier we were selling on Meesho. I saw potential so thought of having our own website.
> 
> I did not have any experience for the same, shopify seemed complicated (not a technical person) and, so I tried this after someone from their team called me. I was very skeptical about this but onboarded anyway to try
> 
> I had onboarded with them 4 months ago
> 
> I was informed about every step at first and had a back and forth with team to understand all the work. Website building was quick, within 4-5 days things were done. I paid 5,000 for onboarding then but i think now they adjust that amount in sellers ads account- my friend who onboarded mentioned this.
> 
>   
> They had asked me to spend a minimum of 30,000 for ads (in a month) I was  very doubtful because the team also made no promise at that time they said Facebook takes time to learn data. . But i decided to just trust them because honestly this seemed like the best option at the time. They were taking care of creatives and managing my ads account, so i was okay with it
> 
> After 2-3 weeks i saw some progress and started getting some orders, and the team also communicated everything that can be improved in early days, so i was assured they were monitoring performance properly. Today monthly budget is 50,000 and i am getting decent orders.
> 
> About rto, they have managers who handle this also, that’s okay, but rto does not disapp

**Top comments:**
- **Extreme_Protection81** (3↑): i have been working with them for a while now. i have had ups and down honestly.  what mattered to me was mainly 2 things. first, i could see the team was actually involved. there was a phase where we were having almost daily discussions where they were monitoring my account, pointing out what’s going wrong, suggesting improvements etc. i still had to be involved obviously, but that’s how it should be. what’s the point of your business if you give full control to someone else.  second thing was website. creating a website was a big challenge for me, so the fact that they gave website without extra cost really pushed me to move ahead. only thing is it’s not very straightforward in the beginning, you need time to settle.
- **PuzzleheadedData248** (2↑): i have seen a lot of people comparing this to meesho, but they forget meesho itself has a lot of issues.  the whole point of moving to your own website is having your own brand and more control over customers, which amazon/meesho don’t really allow.
- **Inknight033** (2↑): I have been with them for 2.5 months now. The initial onboarding was a bit frustrating but post that things have been better. They experimented with Google ads for my account and it has now picked up. I am still running at break even but orders have scaled.  My 2 cents are that if you are planning to go with them, things might seem random at the start but ideally it should fall in place within 3-4 months. If it doesn't then I guess their services might not be fitting your business
- **Potential-Leg-6384** (2↑): Thanks for sharing! It’s really hard to find honest reviews about these platforms. Glad it's working out for your dad’s business, I will also try this
- **OneSinger7183** (2↑): Is the website easy to use on a phone? Most of my customers come from Instagram, so mobile speed is everything

---

### 17. How I made 45 lakhs in 2 months as 2 person team and why we got banned for that
**r/indianstartups** · 2026-02-04 · 157↑ · 65💬 · pain=210
[https://reddit.com/r/indianstartups/comments/1qvgbak/how_i_made_45_lakhs_in_2_months_as_2_person_team/](https://reddit.com/r/indianstartups/comments/1qvgbak/how_i_made_45_lakhs_in_2_months_as_2_person_team/)

**Post body:**
> we built pocketsflow, a digital product marketplace and we used stripe in the backend.
> 
> As a 2 person team(cofounders from India and Netherlands),   
> I am 20 year old from India we met on twitter and I offered to help in building the product and distribution. We did everything ourselves and I did the marketing for it through various channels :
> 
> X, instagram and tiktok and sometimes youtube.
> 
> we quickly saw people who needed it and we made $50,000 in 2 months powering &gt;10,000 creators inside selling digital products and software subscriptions.  
> and we had 0.4 dispute rate when stripe put on a pause for the payouts on us.
> 
> since then, they gave various reasons on why they paused.  
> first reason was "it is a routine check that we are doing" while pausing the entire business for us. since, we were using stripe connect at that time.
> 
> we did not get any payment processors for us just because stripe flagged our entire business which has an LLC in Netherlands (I believe that's how the payment processors like stripe works. because, we got the same reply from all major payment processors (adyen, airwallex, mangopay, shift, etc)
> 
> we created a new business entity just for that and only now, we have activated the business again and is back on track using whop's payment infrastructure. given, we shared everything to them and how it happened.
> 
> I believe they knew what they were doing for our business which is really unfair given what they did to lemonsqueezy too.
> 
> For me, I am not going

**Top comments:**
- **Unlikely_Ad_4366** (14↑): What you could have done differently.
- **Curious-Battle-557** (8↑): who use your platform?  how users percieve you differently than others?   what gave you signals to build this company more than just a tool?
- **threepoint142** (4↑): Is this guy just talking to a bunch of bots? 🤖
- **SpecialistMenu7973** (3↑): Btw how long did i take you to make the product and did you handle tech?
- **No-Fox-5628** (3↑): payment gateways are a real pain in the ass currently.

---

### 18. I’m losing my fucking mind watching Indian startups celebrate funding while their data is a ₹250 crore ticking bomb 😡
**r/indianstartups** · 2026-03-29 · 59↑ · 104💬 · pain=210
[https://reddit.com/r/indianstartups/comments/1s70rdd/im_losing_my_fucking_mind_watching_indian/](https://reddit.com/r/indianstartups/comments/1s70rdd/im_losing_my_fucking_mind_watching_indian/)

**Post body:**
> Been grinding on the DPDP Act for months now, I have a legal background with Supreme Court practice + tech experience so I actually read the full gazette notification, all the rules, penalty structure, everything.
> 
> And it pisses me off seeing founders on Twitter popping champagne for Series A while their whole customer data setup is basically a lawsuit waiting to happen.
> 
> Straight up: if your startup collects emails, phones, payments or any personal shit and you’ve done nothing on DPDP compliance, you’re carrying a ₹250 crore bomb.
> 
> The excuses are so stupid:
> 
> “Bhai GDPR bhi aaya tha kuch nahi hua” — bro GDPR fined companies billions, Meta got slapped with €1.2 billion alone. DPDP penalties are even higher.
> 
> “We’re too small” — bullshit. No size exemption at all. Even a chaiwala saving numbers on WhatsApp is a Data Fiduciary.
> 
> “Our privacy policy is enough” — lol a page nobody reads isn’t consent, isn’t breach protocol, isn’t anything the Act actually wants.
> 
> Penalties that should scare you:
> 
> \- ₹250cr for shit security  
> 
> \- ₹200cr for kids data mess  
> 
> \- ₹200cr if you miss 72hr breach report  
> 
> \- ₹150cr+ for everything else
> 
> Board is getting set up right now. Nov 2026 Consent Manager live, May 2027 full compliance mandatory. No grace.
> 
> I talked to 50+ founders, most think its future problem. Its not. VCs already asking for compliance in DD, I saw 3 term sheets get delayed coz of this.
> 
> Tools like Sprinto OneTrust treat it like checkbox #47 and foreign ones can’t even be C

**Top comments:**
- **chungkingexp** (20↑): It's india where people's adhaar info was leaked along with other data and everything is still available online. Kisi ko ghanta fark nai padta gpdppdp se.
- **Wizardofoz756** (8↑): Ur overthinking it. Here they don't care until the last moment n even then they do jugad to pay next to nothing. I know of well established companies in this service who'll do ur audit n issue certificate for 5L or less. No matter if ur complaint or not
- **Loud_Engineering3071** (6↑): I know a startup personally not following this and doing unethical things 
- **ActuaryVegetable5471** (6↑): Nothing's gonna happen. This might be working with some firm that does this compliance. Simple enough.
- **[deleted]** (6↑): Lawyers aren't allowed to advertise. Someone should DM this guy pretending to be a founder, get his details, and then complain to his bar council.   Let's see who gets fined.

---

### 19. One of the most talked-about headlines last year was that India is the world’s fourth-largest economy.
**r/indianstartups** · 2026-01-13 · 934↑ · 85💬 · pain=210
[https://reddit.com/r/indianstartups/comments/1qbmgoz/one_of_the_most_talkedabout_headlines_last_year/](https://reddit.com/r/indianstartups/comments/1qbmgoz/one_of_the_most_talkedabout_headlines_last_year/)

**Post body:**
> But what does that really mean for the market size of B2C startups? 
> 
> Does it mean most Indians are getting richer and ready to spend? 
> 
> Does it mean the Total Addressable Market (TAM) is exploding?
> 
> The data says: not really.
> 
> Nearly 40% of India’s total wealth is held by just the top 1% of the population (World Inequality Report). 
> 
> Meanwhile, the bottom 50% of Indians together own only about 3% of the nation’s wealth.
> 
> 
> 
> This level of concentration makes GDP per capita a misleading indicator for founders. Because averages hide extremes.
> 
> In fact, if you remove just the top 1% of earners, the per capita figure drops sharply. 
> 
> And if you remove the top 5%, who control nearly 62% of national wealth, the average income falls to around $1,100 a year.
> 
> That is less than ₹1 lakh for an entire year. And that is where the majority of Indians actually live.
> 
> 
> 
> **The Startup Reality Check (2025 Trends)**
> 
> This data explains exactly why we are seeing a "K-Shaped" market in 2024-25:
> 
> **1.The Premiumization Boom:** This is why luxury housing sales (₹1 Cr+), SUVs, and premium electronics are hitting record highs. Startups targeting the top 5% (Quick Commerce in metros, D2C premium brands) are seeing massive growth because that is where the disposable income is concentrated.
> 
> **2.The Mass Market Struggle:** Meanwhile, FMCG volumes in the mass market have been sluggish. Entry-level cars and budget smartphone sales have flattened. The "bottom 50%" simply doesn't have the purchasing power y

**Top comments:**
- **wahvinci** (60↑): Great illustration.   Finally something that people can truly understand what 4th place for India means.
- **Alternative-Good-413** (57↑): I don’t understand what’s wrong in being happy for climbing to 4th place. Isn’t it better than 10th place or any other place? Even that would mean that the most of the Indians might be living in a level below than now’s. I am not sure about my view though, if I am wrong please enlighten me.
- **[deleted]** (11↑): the guy who drew this should also include how much support Japan got from USA after getting nuked.  And how India had to solve many basic problems ( open defecation ) from scratch whilst fighting a hostile neighbor and also accommodating millions of poor bangladeshi refugees
- **Firm_Shoe717** (2↑): Amazing handle and detail on basic consumer market . So speaking in numbers what might be the spending power of top 5 percent and 1 percent , I think this does mean that luxury market is exploding and maybe market for very cheap products too 
- **Short_Conflict_6994** (3↑): While it’s definitely an accomplishment, but like that Kobe Bryant quote says, “rest at the end, not in the middle”. Still got a long way to go. Productivity is still way below Japan, Germany and South Korea, to say nothing of China and the USA.   We’ll always be amongst the largest economies due to population size and having a much higher baseline of economic activity associated with that. We’re only returning to our historical norm, as the country slowly gets going again after 270 years.  Only difference this time around is that instead of our neighbour to the north-east being in their historically normal #1 spot, it’s the new guy (USA) sitting there instead.

---

### 20. Why Your Premium" T-shirt turns into a rag after 5 washes (The science of the "Wash-out")
**r/indianstartups** · 2026-01-24 · 233↑ · 224💬 · pain=210
[https://reddit.com/r/indianstartups/comments/1qldmzk/why_your_premium_tshirt_turns_into_a_rag_after_5/](https://reddit.com/r/indianstartups/comments/1qldmzk/why_your_premium_tshirt_turns_into_a_rag_after_5/)

**Post body:**
> I’m the guy who spent the last year obsessing over fabric science and acting like a total nerd about cotton. In my last post, I talked about building the "perfect" tee because I was tired of being let down by the "good" brands.
> 
> I actually bought shirts from everyone—including popular ones like March Tee—to figure out **why** they start out great but lose their "magic" after a few laundry cycles. I took them to the lab, and here is the "T-shirt autopsy" I found.
> 
> # The "First Wash" Deception
> 
> Most high-end brands and D2C brands use decent cotton ( Supima cotton for eg. ), which is a big change for the industry in the recent years. But the problem is - they rely on **topical finishes**.
> 
> * **The Problem:** To make a shirt feel "silky" in the store, they soak it in silicone softeners. It’s like putting makeup on the fabric.
> * **The Result:** After 3–5 washes, that coating disappears. The short-staple fibers underneath start to "fuzz" or pill, and suddenly your expensive shirt feels like a dishcloth.
> 
> # Why "Good" Brands Fail the Longevity Test:
> 
> 1. **Short Fiber Length:** Most brands use "combed cotton" ( Which they advertise also but it does not give the full story ) but the fibers are still only 22–28mm. When these short fibers get agitated in a machine, the ends pop out. That’s why your shirt gets that "hairy" look. ( This is the cause behind the T Shirt Itch )
> 2. **The "Bacon" Neck:** They use cheap ribbing that doesn't have "recovery." Once it stretches in the heat of a dr

**Top comments:**
- **bulkkuonuo** (39↑): Good Job. All the best!   Remember one thing though, your market doesn't care for the technology you are using, it cares for the outcome!  Highlight the pain in your communication and hopefully, there will be good response.
- **zabnotavailable** (15↑): Looks like the website is not fully developed. Images are not loading and I am not able to click anywhere.   Also one feedback, the website is giving a vibe of a Cyber Security or an AI startup company.
- **ReceptionAcademic262** (5↑): So you mean to say your target audience is men whose t-shirts go through intense wash and dry cycles in expensive machines?  Do the same problems happen if the garments are hand-washed by maids??  Genuinely curious??
- **Boring_Top_1328** (5↑): Only one suggestion for tshirt brands, solve length issue. Indians have a very different body then other nations so study this. If a men of 6ft wears medium then the lenght is about 40-50cm, but why the hell company believes that a men who wears xxl is about 8 feet tall. I have seen obese people wearing tshirts which covers half of their thighs. Performax is the only company i believe which makes decent lemght tshirt.
- **siddharthnibjiya** (4↑): I don’t know about your brand (I wish you all the best) but I just want to put it out for anyone reading that RareRabbit is surprisingly extremely bad when it comes to longevity.  They are priced on the higher side of premium pricing — a shirt typically 3k, tshirt 2k+, pants 3-4k (atleast) and look great on first wear.  But 10 washes later, these premium expensive clothing become truly rags.

---

### 21. Need Advice: Hyperface (Bangalore) vs HSBC (Pune) (Packages: 14L, 16L). Which Should I Choose for ?
**r/developersIndia** · 2025-11-23 · 202↑ · 41💬 · pain=210
[https://reddit.com/r/developersIndia/comments/1p4ehkm/need_advice_hyperface_bangalore_vs_hsbc_pune/](https://reddit.com/r/developersIndia/comments/1p4ehkm/need_advice_hyperface_bangalore_vs_hsbc_pune/)

**Post body:**
> I got an internship offer from clg (Hyperface) they told its intern + PBC, so after this i was allowed to sit for FTE only offers.
> 
> Then i get HSBC offer, thing is HSBC told its FTE only but when i got the offer mail from clg they say its intern + FTE now and they gave like 3 hours to reply the confirmation i replied with "I accept only the said FTE offer"
> 
> Both the offers are in-campus placements.
> 
> Pros and Cons of both the places-
> 
> Hyperface (Role SDE) -
> 
> \-  Pros: Bangalore based, startup so might learn more.
> 
> \- Cons - Idk how it will be in a startup + job security + PBC so might not give FTE.
> 
> HSBC (Role TSE) -
> 
> \- Cons - Pune/Hyd (mostly Pune), have to relocate and live by myself so less savings.
> 
> \- Pros - stability + relatively more free time than former. Confirmed FTE.
> 
> Compensation-
> 
> Hyperface - 14 CTC (12 Base + 2PB) + 6L worth ESOPS (30k internship stipend)
> 
> HSBC - 15 CTC (14 Base) + 1.4L variable pay (50k internship stipend)
> 
> I contacted a senior who worked at hyperface and he told me he had a "very bad" experience and pressure is more.
> 
> If anyone has worked in either of the companies please share your experiences.
> 
> My Goal: To Get a better job at a big MNC or more established startups  (Razorpay, Inmobi etc)
> 
> TLDR: Hyperface (Bangalore) or HSBC (Pune) almost same compensation.
> 
> Edit: I am from Bangalore.

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **watchingRummy** (88↑): Startups hire Indians to exploit them. You’ll learn a lot and have to work on things way above your job description. If you’re looking for something like that join it otherwise hsbc.
- **Single_Savings4940** (53↑): Dude HSBC all the way. That senior's feedback about Hyperface having "very bad" experience is a massive red flag. Plus they're already being shady with the intern+PBC bait and switch     Bangalore might seem cool but you'll blow through that extra money on rent anyway. HSBC gives you actual stability and a recognizable name that'll help when you're applying to those MNCs later. Hyperface could fold tomorrow and then you're back to square one     The variable pay at HSBC is way more reliable than hoping for ESOPs that might never materialize
- **kidakaka** (20↑): OP go for HSBC. The learning will be a bit slow but structure would be great. Startups are great if they manage the burn. However startups are not for everyone.   If you like structure with the occasional stretch then HSBC is perfect.
- **TechAny124** (12↑): Hsbc. Confirmed FTE + you will save more in Pune.

---

### 22. I built a Gumroad alternative for India. Here is the stack.
**r/developersIndia** · 2025-12-12 · 118↑ · 64💬 · pain=210
[https://reddit.com/r/developersIndia/comments/1pknb0e/i_built_a_gumroad_alternative_for_india_here_is/](https://reddit.com/r/developersIndia/comments/1pknb0e/i_built_a_gumroad_alternative_for_india_here_is/)

**Post body:**
> International payments are a pain. PayPal fails. Stripe is hard to get. So I built a solution.
> 
> **The Stack:**
> 
> 1. **Frontend:** Next.js (Speed matters).
> 2. **Backend:** Supabase (Postgres is reliable).
> 3. **Auth:** Google + Magic Links (No passwords to forget).
> 4. **Payments:** Razorpay + UPI (Because India runs on UPI).
> 
> **The Problem:** Most US platforms charge $10/month just to exist. I wanted something free to start. Zero fixed fees. You only pay when you sell.
> 
> It is live now. I call it **\[ SAUCE \]**.
> 
> I am looking for developers to break it. Try to upload a file. Try to break the auth. Tell me what I missed.
> 
> (Link is in the first comment).

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **Ok-Preparation866** (23↑): Here: [getsauce.in](https://www.getsauce.in)
- **bnagaonkar** (21↑): Site is clean!! Like it.   You should now think about Marketing. How to get people to your platform.
- **luhar_21** (19↑): Good UI but back-navigation is hard. Router.push keeps all the pages history so that I have to click back button that many times to exit the website
- **DataDrivenJournalist** (13↑): Love it when people love their craft! UI says it all.  Planning to put my $1 app over here. \[Edit: Self-plug for the app, [**Plug That In**](https://www.plugthat.in/)\]

---

### 23. 900+ DSA problems and full stack projects but still no internship interviews – what am I missing?
**r/developersIndia** · 2026-03-04 · 108↑ · 63💬 · pain=210
[https://reddit.com/r/developersIndia/comments/1rknvn5/900_dsa_problems_and_full_stack_projects_but/](https://reddit.com/r/developersIndia/comments/1rknvn5/900_dsa_problems_and_full_stack_projects_but/)

**Post body:**
> Hi everyone, I am a third year engineering student currently trying to land a software engineering internship but I have not been getting many interview opportunities despite preparing for a long time. I have solved more than 900 DSA problems, have around 1750 rating on LeetCode and I am a Pupil on Codeforces. I have also built two full stack projects using the MERN stack and I am comfortable with JavaScript, React, Node.js, Express and MongoDB. I have attached my resume here and would really appreciate honest feedback on what I might be doing wrong or how I can improve my chances. If anyone knows about opportunities or has suggestions on where I should apply, I would be very grateful.

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **According-Willow-98** (37↑): You are from NIT, why even go offcampus?
- **Shot_Process_1498** (27↑): Tier 3 mech, I'm cooked 😭😭 no wonder I'm finding it really hard to switch. 
- **tan_djent** (7↑): Which platforms are you using ?
- **PreparationNo556** (7↑): Something big is gonna happen in your life, and it's really good. Just keep on going.

---

### 24. 6 months building an app to compete with Splitwise in India. What I got wrong.
**r/developersIndia** · 2026-05-05 · 593↑ · 76💬 · pain=210
[https://reddit.com/r/developersIndia/comments/1t4d0pu/6_months_building_an_app_to_compete_with/](https://reddit.com/r/developersIndia/comments/1t4d0pu/6_months_building_an_app_to_compete_with/)

**Post body:**
> Started building Hisaab six months ago thinking "Splitwise has bad UPI integration, this should be easy." Six months later, here's everything I underestimated. Posting in case it helps another indie founder avoid the same mistakes.
> 
> **Mistake 1: Assuming "Indian users want UPI" was enough of a wedge.**
> 
> It isn't. UPI is table stakes. The actual wedge is the social context around money in India — joint families, recurring rent, group trips of 8+ people, the "didi I'll pay later" dynamic that doesn't exist in the West. UPI is a feature. The cultural fit is the moat.
> 
> **Mistake 2: Building features users said they wanted instead of features they actually used.**
> 
> Users in early interviews asked for: receipt scanning, multi-currency, complex splitting rules, recurring expenses. I built all of them. Usage data: &lt;3% of users touched any of them. The features that actually got used: equal split, settle-up button, group balance view. Three features. That's the whole product.
> 
> **Mistake 3: Underestimating Splitwise's brand gravity.**
> 
> I thought "people will switch the moment a better Indian option exists." They don't. Splitwise has 8+ years of brand equity — it's literally a verb in some friend groups. Replacing a verb is hard. You don't beat them on features, you beat them on a specific use case where they're weak (in my case: Indian rent + UPI flatmates).
> 
> **Mistake 4: Spending 6 weeks on UAC ads before realizing it was poisoning my retention numbers.**
> 
> UAC brought cheap install

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **Accurate-Surprise-56** (81↑): I never felt the need of such app, seems like solution looking for problem case atleast in india. All upi apps have this but I think it never scaled.
- **venu_18** (80↑): This is a great breakdown, especially the part about cultural fit being the real moat. A lot of people assume “local feature = advantage,” but behavior matters way more than features.  The overbuilding point is also real. Most products end up shipping tons of stuff that maybe 10–20% of users ever touch.  One thing that helped me think about this better was actually building small experiments fast. I’ll sketch ideas in Notion, sometimes run quick landing pages or decks through Runable, and then talk to users before writing real code.  Your point about doubling down on the flatmate + UPI niche makes a lot of sense. That’s one of the few places where something could actually beat Splitwise.
- **Desperate_Sand_8789** (33↑): Doesnt paytm or supermoney already have this feature
- **hyperactivebeing** (24↑): I hate these AI generated posts. Can't you guys write on your own?   Asking AI models to fix the grammar is a totally different thing than asking it to spit out entire post. 

---

### 25. From ₹3,356 first Airbnb booking to ₹10L+ annually!
**r/IndiaBusiness** · 2026-03-14 · 403↑ · 114💬 · pain=205
[https://reddit.com/r/IndiaBusiness/comments/1rtcmu2/from_3356_first_airbnb_booking_to_10l_annually/](https://reddit.com/r/IndiaBusiness/comments/1rtcmu2/from_3356_first_airbnb_booking_to_10l_annually/)

**Post body:**
> On 14 March 2024, I listed my own room in my home on Airbnb. I was still working a corporate job in Gurgaon (media marketing, ex-TVF), so this started purely as an experiment.
> 
> My first booking came after 18 days. It was a 4-night stay and I still remember the payment notification: ₹3,356
> 
> I literally travelled back to my hometown just to check-in the guests myself.
> 
> At that time I was juggling:
> - Weekday corporate job in Gurgaon
> - WWeekend travel to manage the Airbnb listing
> - Cleaning, guest communication, check-ins, everything myself
> 
> Slowly bookings started coming in beyond weekends and the back and forth became exhausting.
> 
> On 23 August 2024, after 6 years in corporate, I quit my job to pursue this full time.
> 
> By winter 2024, I had expanded to:
> 
> - 1 room in my own house
> - 2 rented properties
> 
> 2024 Financials
> 
> Net profit for the year: ₹2 Lakhs
> 
> Not huge numbers, but enough validation that the model worked.
> 
> 2025: Scaling :)
> 
> Once I went full time, growth accelerated.
> I added another property on lease and expanded operations.
> 
> At peak in 2025 I was managing:
> 
> - 2 Private Rooms (budget single bed setups)
> - 1 BHK
> - 2 BHK
> - 3 BHK
> 
> Different price segments helped capture different types of travellers.
> 
> Operational structure also evolved:
> 
> - 4 staff members (cleaning + operations)
> - Standardized check-in processes
> - Outsourced cleaning cycles
> - Property maintenance system
> 
> 2025 Financials
> 
> Gross annual earnings crossed ₹10 Lakhs+
> 
> After accounting for:
> 
> - Rent/lease payments
> - 

**Top comments:**
- **rustcohle_02** (54↑): I really need to develop a kind of brain required to run such businesses!!
- **adikul** (13↑): Man, you again. Atleast wait for evening so we can digest
- **Historical-Tip888** (6↑): I am also planning for the same.....in panchrukhi (a small town 8kms from palampur HP) ...what's your location?
- **Funny-Raspberry-5865** (2↑): what happens when the visitors vandalise? you'll have to bear the cost?
- **arun911** (2↑): What would you offer for 2.5 bhk space near Gulab bagh?

---

### 26. Last week, I narrowly avoided a scam that could have cost me nearly ten lakh rupees. I am sharing the full story so others in the trade can stay cautious.
**r/IndiaBusiness** · 2025-12-10 · 403↑ · 56💬 · pain=205
[https://reddit.com/r/IndiaBusiness/comments/1pirjv8/last_week_i_narrowly_avoided_a_scam_that_could/](https://reddit.com/r/IndiaBusiness/comments/1pirjv8/last_week_i_narrowly_avoided_a_scam_that_could/)

**Post body:**
> I was looking to procure 200 tons of maize from the Malegaon–Manmad region for the local market in Gujarat. I was contacted by a person who introduced himself as Rajnish. His profile seemed genuine, his pricing was aligned with the market, and he spoke with confidence. Everything appeared legitimate on the surface.
> 
> I insisted on visiting the warehouse before moving forward. Initially, he hesitated, saying many buyers visit and then disappear, but I made it clear that without verification I would not proceed. He then shared a contact named “Sushil,” who he claimed was the loading manager.
> 
> On Sunday, I travelled and was shown a warehouse by Sushil along with another man. Samples were taken for QC on Monday, but the quality did not match. When I informed Rajnish, he immediately redirected me to Manmad, saying Sushil would show me a different stock.
> 
> On Tuesday morning, everything became clear. When I reached Manmad, “Sushil” revealed that his real name was Arshad, not Sushil, and that he did not live in Malegaon as earlier stated. He told me that the person calling himself Rajnish was planning to take payment into a different account and then disappear. After that, once the truck was loaded from someone else’s warehouse, the real warehouse owner would stop the truck, saying no payment had been received. In that scenario, both the money and transporter charges become a total loss, with no legal footing to stand on.
> 
> To make matters worse, both individuals were pushing for urgen

**Top comments:**
- **awakeningdreams** (25↑): Thank you for the post. I am sure it will help a lot of us.
- **Deveraux3** (23↑): These are the kind of posts that really help the community. Thanks.
- **adikul** (14↑): Always meet the person, arrange your man before loading. No compromise with these rules
- **AssociationBrief45** (11↑): Thank you. Our business requires maize. As a guy who newly entered the world of business in India these posts are a massive help!!
- **BeDunedain** (7↑): We don't do distance deals with parties without GST number. On getting the GST number, we check the details on the portal, check the return filing history and also verify the bank account name.

---

### 27. My Residential Society gave me immense support in my new business
**r/IndiaBusiness** · 2026-03-28 · 192↑ · 25💬 · pain=205
[https://reddit.com/r/IndiaBusiness/comments/1s5xeab/my_residential_society_gave_me_immense_support_in/](https://reddit.com/r/IndiaBusiness/comments/1s5xeab/my_residential_society_gave_me_immense_support_in/)

**Post body:**
> 30M who recently started my entrepreneurial journey right from within my own society with a single product, and it’s been an eye-opening experience. The idea was simple—approach people directly, let them see and use the product, and make sure they feel 100% confident that the money they’re spending is actually worth it and not a waste.
> 
> In a society with around 200 flats, I managed to reach about 140 households. Out of those, 67 people agreed to try a demo, which itself felt like a small win. Eventually, 19 people said yes and became paying customers. Most of my buyers were homemakers between the ages of 30–50, which gave me a good understanding of my core audience. One moment that really stood out was when a customer liked the product so much that she sent it along with her daughter to her hostel after the holidays.
> 
> In total, I sold 22 units (16 single units and 3 combos), generating a gross revenue of ₹3,280. It may sound small to some, but for me, it’s a solid and encouraging start. Now, I’m excited to scale this further, reach more people, and grow. Also, the product is now available on major e-commerce platforms for anyone who wants to try and be part of the journey. 

**Top comments:**
- **Western-Let8907** (7↑): is ecozee same as ecozy reusable kitchen tower ?
- **Background-Sector637** (1↑): we get it bro just please stop posting on multiple subs at the same time 
- **hive027** (1↑): Hello, Kindly dm me about your product. I'm interested in exporting the product 

---

### 28. I genuinely hate how badly small business owners are treated by banks
**r/IndiaBusiness** · 2026-02-10 · 171↑ · 58💬 · pain=205
[https://reddit.com/r/IndiaBusiness/comments/1r0zh7l/i_genuinely_hate_how_badly_small_business_owners/](https://reddit.com/r/IndiaBusiness/comments/1r0zh7l/i_genuinely_hate_how_badly_small_business_owners/)

**Post body:**
> I could be making 5L per month but banks still treat me worse than employees making 30k a month. Even getting a simple most basic credit card is a challenge because the banks see me as a liability -- They will ask for 50 pages of documents, a picture of my office building, a picture of my work desk. And just so you know, that's also not enough in case of loans. I am also asked to add my spouse's aadhar card information because the bank sees me as a 'liability'
> 
> I just needed a low FX credit card to make quick business payments online but even that has sucked the sole out of me. I'd love to change my bank, but really, they are all the same.
> 
> There is so much red tape around running a business in India. Its just not for the weak hearted.
> 
> 
> 
> Edit: My credit card got approved! I escalated the issue to the branch manager and told him I will close down my account and FDs -- and it worked!

**Top comments:**
- **kukdukuu** (50↑): Times change..tables turn...you will be on the other side..and they will be the ones waiting to het entry..and approval...and give x,y,z loans and cards.. Stay consistent, pragmatic,optimistic, persistent and stubborn..just dont stop...and that day will arrive when you even won't realise it... :)
- **CapitalistSloth** (25↑): Bullshit.   If you have a registered business, banks themselves will approach you to open an account and push as many of their services as they can possibly stuff down your throat.  
- **Straight_Cherry996** (9↑): Cost to the bank to process a Rs 5 lakh loan and all documentation is not much different comparatively for a Rs 5 to 500 Crore loan  The service fee from 5 Lakh loan and from Rs 5 to 500 Cr loan is substantial earnings for the bank  That is why INDIAN GOVT had PSU banks which POLITICIANS and BUSINESS PEOPLE abused along with promoters and mounted losses - THUS the PSU banks had to be merged with larger banks to save money of those relied on PSU  As of 2025-2026, the issue of large, willful defaulters in India's Public Sector Undertakings (PSU) banks remains a critical concern, with over 1,600 unique borrowers classified as willful defaulters, owing nearly ₹1.63 lakh crore (as of March 31, 2025).   While many names appear across various "top defaulter" lists, the specific group of individua
- **Substantial-Fun5046** (8↑): If you are earning 5L per month and your ITR also says that (i.e an ITR of 60 lacs) then you can get any credit card you want. This is the real gap where ITR does not normally show the actual earning.
- **Training2Life** (3↑): All are same, some small banks supports small businesses but have shtty CC portfolio Eg: Federal, Indusind,etc..  Now most banks are asking for GST login credentials to check business details (yup!) and your account details will be shared via WhatsApp between bank employees if they have a doubt. There's no privacy and they'll treat you like sht until you give them crores of cash to invest in their even shtty products.  Try going for a loan without a agent, you'll lose hope in life even for a secured loan like LAP.

---

### 29. My Shopify made sales on day 1. Im just so happy 🥹💐
**r/IndiaBusiness** · 2026-04-08 · 243↑ · 71💬 · pain=205
[https://reddit.com/r/IndiaBusiness/comments/1sfhhva/my_shopify_made_sales_on_day_1_im_just_so_happy/](https://reddit.com/r/IndiaBusiness/comments/1sfhhva/my_shopify_made_sales_on_day_1_im_just_so_happy/)

**Top comments:**
- **WinterNo7927** (10↑): Hi I’m starting a clothing business too can I just dm you for some insight 
- **piratefather** (5↑): Awesome! Can you share how much it cost you set it all up?
- **electric_chalk** (2↑): Congratulations on the first sale (sales)!!   Did you do anything specific for SEO? How did you manage to get visitors &amp; customers on day 1?
- **No_Appointment_1662** (1↑): Do you accept international customers? 
- **SIDDATIVEZ** (1↑): amazing buddy,  saw your website there is a lot of potential for optimization

---

### 30. I am selling my Clothing Company (Pvt Ltd) along with GST credits, High Quality T-shirts, Hoodies, packaging, shopify website [NOT PROMOTING]
**r/IndiaBusiness** · 2026-02-25 · 62↑ · 162💬 · pain=205
[https://reddit.com/r/IndiaBusiness/comments/1re67eu/i_am_selling_my_clothing_company_pvt_ltd_along/](https://reddit.com/r/IndiaBusiness/comments/1re67eu/i_am_selling_my_clothing_company_pvt_ltd_along/)

**Post body:**
> Hey folks,  
> As mentioned, I am selling my clothing company along with every associated materials, resources, inventory, etc. The reason for the selling is I have started with some other startup and running low on finance to run marketing campaigns. Everything is plug and play, either use it for your own brand or just put in some money in meta/google ads and you can start getting the sales.
> 
> We have more than 1000 stocks in inventory, we own trademark, domain name and have our own design files for the production. Customized packaging, tags, boxes are there. Multiple shipping companies like blue dart, delhivery, shiprocket are already connected with us.  
>   
> Meta account has the campaign data, GST has more than 1.5 lakh input credits, all compliances are clear. Manufacturer is also in Bangalore, will guide on details once we go ahead in process.  
>   
> We own the customized theme of Shopify as well, everything is integrated like data analytics, google ads, google search console, Meta ads, Microsoft Clarity - so you get intelligent analytics of the funnel.
> 
> Company age - 2 years, used to operate it part time along with my full time job. Revenue in last 1.5 years is Rs. 3.5 lakhs+ (stopped operating from last 5 months due to my other startup which is now funded)  
> Based out of Bangalore.
> 
>  
> I am looking to sell it for 7-8 lakhs (negotiable)
> 
> If you are interested or have any referrals as well, please DM.

**Top comments:**
- **Weary_Lavishness9375** (19↑): Why didn't the business work?   You can sell the inventory but to sell a failed business using buzzwords is obnoxious.   Just be upfront and say the business failed doesn't work unless you run ads which eats the profit away.
- **-AsHxD-** (15↑): Where is the 8lakh coming from ? Only registration is valuable, gst is value at 25-50%
- **Potential_Mud_1094** (2↑): My cousin is in similar business and intrested to know more details. please share details in DM.
- **Odd-Guarantee-3** (2↑): Hey, I’m interested. Would love to know more. Please DM me the website link and we can reconnect soon
- **Brief_End512** (2↑): Interested in the offer. DM me more details along with some contact information email or something where I can connect.

---

### 31. I created MoneySplit - Track Expenses, Bills, Subscriptions Offline and private by design.
**r/indianstartups** · 2026-04-26 · 58↑ · 177💬 · pain=205
[https://reddit.com/r/indianstartups/comments/1swa00d/i_created_moneysplit_track_expenses_bills/](https://reddit.com/r/indianstartups/comments/1swa00d/i_created_moneysplit_track_expenses_bills/)

**Post body:**
> Hey folks, I’m built **MoneySplit** (name is confusing, I know 😅) but it’s **not** a group expense app.
> 
> It’s for personal money tracking:
> 
> * Auto-adds spends from bank SMS alerts
> * Lets you import PDF statements
> * Tracks bills, subscriptions, and EMIs in one place
> * Shows upcoming due items so you don’t miss payments
> * Simple budget view to see where money is going
> * No forced signup, data stays on your phone
> * Tonnes of customization options.
> 
> I built this because I wanted something practical for Indian users without the usual clutter.
> 
> Would love honest feedback and if you are interested, I can share the link (alternatively, please search for **MoneySplit** on google play store to download the app)
> 
> * What feels useful?
> * What’s missing for your daily use?
> * What would make you switch to this?
> 
> Yes this is 75% vibecoded, especially the UI part and the algorithms to derive insights out of spending.Being a backend engineer, I wanted to save time and money and hence vibecoding. It took me 5 months for first presentable version.
> 
> 
> 
> &lt;posting keeping mod rules&gt;

**Top comments:**
- **rocketleee** (4↑): Noicee. Is it 100% offline? And do you intend to share git link?
- **CrusherAWSRD** (2↑): I was literally building the exact same thing...
- **oasacorp** (2↑): Does it work for outside india?

---

### 32. I started a new D2C Company, and I am confused about how to increase word-of-mouth publicity?
**r/indianstartups** · 2026-04-05 · 559↑ · 323💬 · pain=205
[https://reddit.com/r/indianstartups/comments/1sdd30b/i_started_a_new_d2c_company_and_i_am_confused/](https://reddit.com/r/indianstartups/comments/1sdd30b/i_started_a_new_d2c_company_and_i_am_confused/)

**Post body:**
> I started a premium mobile accessory business and I am really interested in gaining organic customers, but literally I have no clue. Neither I have a group of friends who can suggest for the same. The first product that I introduced is a professional headphone by the name “Onyxe Opera-1” . www.onyxeindia.com Thankyou in advance. 

**Top comments:**
- **Wonderful_Doubt_279** (113↑): another white lable product?  Edit: It seems I was correct  [https://www.alibaba.com/product-detail/High-Quality-Price-Over-ear-Headset\_1600863202826.html?spm=a2700.7724857.0.0.213362dd9HTCd5](https://www.alibaba.com/product-detail/High-Quality-Price-Over-ear-Headset_1600863202826.html?spm=a2700.7724857.0.0.213362dd9HTCd5)
- **Protagunist** (110↑): Don't sell consumer products in India over 5k unless exceptionally good, or niche.  Pretty generic white labelled headphones and mid website (remove the heading text or change it).  And allowing this post but don't blatantly self promote again.
- **thisisvenky** (23↑): So, dropshipping is your new name for a startup?  Also terrible pricing for a Chinese no name product and a terrible website copywriting.
- **Sexy_Goku** (19↑): Honest feedback: the website is hurting the brand more than helping it. For a D2C electronics brand it looks very raw and unfinished right from the first scroll repeated menu/account sections, weak hierarchy, too many image blocks and no real premium brand feel.   before asking for product feedback the website itself needs work on design, brand communication, and trust-building because right now it undersells whatever the product might actually be. Website is actually the soul of a D2C brand.
- **trojenhorse** (14↑): Why not sony, cmf or any other for 7.5k than your product? If you can answer me as a user you know what mouth marketing will succeed you

---

### 33. How much are you losing to Paypal fees developers?
**r/developersIndia** · 2025-12-21 · 131↑ · 39💬 · pain=205
[https://reddit.com/r/developersIndia/comments/1ps4d0o/how_much_are_you_losing_to_paypal_fees_developers/](https://reddit.com/r/developersIndia/comments/1ps4d0o/how_much_are_you_losing_to_paypal_fees_developers/)

**Post body:**
> PayPal costs 7-8% total (transaction fee + conversion) and sure gives a mini heart attack whenever checking the receipt.
> 
> On ₹3L monthly income, that's ₹21,000-24,000 monthly or ₹2,52,000-2,88,000 annually just in fees.
> 
> I have seen Razorpay International cost 2-3%. Same ₹3L income = ₹6,000-9,000 in fees. Saves ₹15,000 monthly or ₹1,80,000 annually.
> 
> It's easy to switch payment platforms but are clients okay to pay with a payment link that they are not used to?
> 
> Which payment platforms do you use to get payments? Anyone tried Razorpay International?

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **DolGuldurWraith** (25↑): Use skydo, flat fee of $29 and live market rate. Client just have to transfer to bank account, that bank account can be country based on client location e.g. US, UK, EU etc.  This is the best if getting more than $2k per month
- **TraditionalTopic8970** (14↑): How are you finding such clients?
- **urdad_455** (5↑): What are u selling or are u freelancer ? And in which domain

---

### 34. Small Indian team taking on the web scraping giants. Would love your feedback.
**r/developersIndia** · 2026-01-03 · 98↑ · 78💬 · pain=205
[https://reddit.com/r/developersIndia/comments/1q2mi9k/small_indian_team_taking_on_the_web_scraping/](https://reddit.com/r/developersIndia/comments/1q2mi9k/small_indian_team_taking_on_the_web_scraping/)

**Post body:**
> Hey Everyone,
> 
> We're a small dev team with RapierCraft Inc, and we just launched AlterLab ( [alterlab.io](http://alterlab.io) ) - a web scraping API built to power AI workflows, data pipelines, and market intelligence tools.
> 
> The backstory is pretty simple. Like many of you, we were building side projects that needed web data. Every solution we tried was either way too expensive (looking at you, Bright Data), locked us into their infrastructure, built for enterprises with "contact sales" pricing, or just didn't work reliably on protected sites. So we built our own. And now we're putting it out there.
> 
> Why we think we can compete with the big players:
> 
> First, we built this for AI-first workflows. LLM apps, RAG pipelines, training data collection - that's the future, and we've optimized for it. Clean extraction, structured output, markdown conversion. Not just dumping raw HTML.
> 
> Second, simple pricing that doesn't require a CA to understand. Free tier gives you 1,000 scrapes to test with no credit card. After that, it's pure pay-as-you-go. No subscriptions. No "use it or lose it" monthly quotas. Light scrapes are cheap, JS rendering costs more, but you only pay for what you actually need. Compare that to enterprise giants charging $500/month minimums with bandwidth limits and overage fees.
> 
> Third, we let you bring your own proxy. Already paying for proxies from Bright Data, Oxylabs, Smartproxy? Use them through AlterLab. Get our anti-bot bypass engine without double-paying for 

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **Knocking_Doors** (20↑): Welcome to the club!  I run a web scraping startup since 6-7 years. It’s an interesting and challenging field, but can be rewarding.  While I haven’t tested your solution yet, I did go through your pricing/features page. You may want to work on a few things like pricing and concurrent threads offerings.  $1000 per M requests even for the most basic solution is way expensive than zyte, scrapingbee, etc. It still makes little sense if that’s the trade off for having credits/requests with no expiry.  If 1M requests customers are enterprise for you and you have discounted pricing, then you should do away with the cost calculator for 1M requests.  Secondly, you’re just offering 10 threads on a recharge of $500-999. Even if I consider only basic requests (without rendering), you should offer at 
- **Artistic-Loss8063** (5↑): We’re looking for a solution to scrape sports ticket listings from platforms like SeatGeek and StubHub. Please reach out if your solution can reliably handle DataDome protected sites.
- **Ok-Remove8993** (2↑): ITS AWESOME I REALLY LIKE IT WISHING YOU GUYS GOOD LUCK AND A RICH FUTURE
- **SignificantAd1746** (2↑): This looks solid. It’s clear you built this because you actually needed it, not to sell enterprise plans. Best of luck for the future, will be following your product.

---

### 35. Why I walked away from a ₹60 Lakh commission today: A lesson for Founders on who you hire.
**r/IndiaBusiness** · 2026-02-09 · 303↑ · 79💬 · pain=200
[https://reddit.com/r/IndiaBusiness/comments/1r0053l/why_i_walked_away_from_a_60_lakh_commission_today/](https://reddit.com/r/IndiaBusiness/comments/1r0053l/why_i_walked_away_from_a_60_lakh_commission_today/)

**Post body:**
> For context I am a financial consultant and run my own consultancy firm. I just walked away from a deal that would have netted me ₹60L in commission. It’s a hard pill to swallow, but after what happened, there was no way I was moving forward.
> 
>  3 months ago, I got a case for a manufacturing company (₹100Cr+ turnover). They wanted ₹40Cr equity. The catch? Their net profit was a measly 1% and they had a ₹25Cr CC limit that was 100% utilized. No fixed assets.
> 
> Despite the red flags, I used my network and got them 2-3 hybrid equity offers (funding with a fixed interest of 18-22%). But the owner had a massive attitude and rejected them. He then asked me to Balance Transfer (BT) his CC and get a ₹15Cr top-up for a new factory land. Which he already finalized and made some advance payment to the seller for land.
> 
> Most of my coordination was with his Accountant. Throughout the process, I could sense he was greedy. I am in this industry for more than 6 years now and I know how a commission greedy broker behave even though He never said it directly, but his tone always implied he wanted a "cut" or commission, probably fearing I’d tell the owner.
> 
>  I moved the file to Bank of Baroda (BoB). We did the PD, valuation, and legal. Just when the sanction was due, everyone vanished. The accountant stopped picking up calls. The owner was on a foreign visit and wouldn't respond to texts. A month passed, and BoB expired the case due to the delay.
> 
> Here comes the twist- A few days ago, I got a cal

**Top comments:**
- **Nikunj30** (18↑): Are you CA or MBA? Can you please help how can someone become financial consultant?
- **Motor-Office-896** (13↑): Great one...hats off to your conviction for walking away from a potential revenue of 60l straight to uphold your beliefs.
- **GODisAROUND** (12↑): man,   you have 5,000 karma in 1 month of Reddit age !!!   that tells me this story is made up!!!
- **StrawberryMother5002** (7↑): Why did the owner act shocked? You said he wasn't responding to your texts so how'd he believe his accountant when he said that YOU were the one not responding?
- **electric_chalk** (5↑): 60 lakhs commission for what amount?

---

### 36. Not even getting a single interview despite all of it
**r/developersIndia** · 2026-02-23 · 89↑ · 63💬 · pain=200
[https://reddit.com/r/developersIndia/comments/1rcnxkj/not_even_getting_a_single_interview_despite_all/](https://reddit.com/r/developersIndia/comments/1rcnxkj/not_even_getting_a_single_interview_despite_all/)

**Post body:**
> I'm a Fresher , I've applied to more than 200+ places and still didn't get a single interview, currently I'm building a unique microservices project too to replace that url shortner one but I feel kinda hopeless 
> Please any suggestions would be appreciated 

**Top comments:**
- **AutoModerator** (1↑): &gt;Namaste! Thanks for submitting to r/developersIndia. While participating in this thread, please follow the Community [Code of Conduct](https://developersindia.in/code-of-conduct/) and [rules](https://www.reddit.com/r/developersIndia/about/rules).   It's possible your query is not unique, use [`site:reddit.com/r/developersindia KEYWORDS`](https://www.google.com/search?q=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;sca_esv=c839f9702c677c11&amp;sca_upv=1&amp;ei=RhKmZpTSC829seMP85mj4Ac&amp;ved=0ahUKEwiUjd7iuMmHAxXNXmwGHfPMCHwQ4dUDCBA&amp;uact=5&amp;oq=site%3Areddit.com%2Fr%2Fdevelopersindia+%22YOUR+QUERY%22&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiLnNpdGU6cmVkZGl0LmNvbS9yL2RldmVsb3BlcnNpbmRpYSAiWU9VUiBRVUVSWSJI5AFQAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAJgCAKACAJgDAIgGAZIHAKAHAA&amp;sclient=
- **gamma-cygni** (25↑): Use jake's resume template, your current resume looks unprofessional. Also remove that "Summary" section, it only puts dead weight.
- **Responsible-Dig4556** (10↑): We are in 2026 and people still belive that there is a market for juniors...
- **Lucius_Kartos** (7↑): Bro, You made me scared. I'm also following the same tech stack as yours. Even though you have some work experience.  And regarding resume, some of my seniors suggest, add some numbers/percentage to show growth in the experience section. This helps to showcase your work actually create positive impacts in the production.
- **Icy_Track8203** (5↑): Mca karle bhai, bca mca still get opportunities. Bca alone will keep you dry.

---

### 37. Father breaking down, 2.5cr+ loan, Total family assets - 6cr and career dilemma
**r/IndiaBusiness** · 2026-02-08 · 105↑ · 39💬 · pain=198
[https://reddit.com/r/IndiaBusiness/comments/1qzgpsu/father_breaking_down_25cr_loan_total_family/](https://reddit.com/r/IndiaBusiness/comments/1qzgpsu/father_breaking_down_25cr_loan_total_family/)

**Post body:**
> I 25M, saw my father break down today at 2 PM, and he had been ringing relatives to talk sense to me to pay off his loans somehow, which he took to host extravagant weddings of his sisters.
> 
> Father has been manufacturing spare parts of water purifiers (plastic injection moulding) for the last four years.
> 
> My five years have been spent in 2 interviews of Indian Economic Services (IES) and a mains of CSE. Currently, I work as a freelancer (Data Annotation), roughly making 80k/month, but the problem is the uncertain nature of the work and continuous hunting for more gigs.
> 
> Now my family is crying around relatives because what I do has zero financial security, and want me to make over 2.5L+/monthly to cover the interest payments at least, which is genuinely hard to make from freelancing, and also for another useless extravagant wedding.
> 
> They also want me do pick a stable career so it gets easier for them to marry me off as no family would give their daughter to someone who walks with a coffin over his head. (their words)
> 
> I find myself in middle of the storm where I have to make a decision between IES, FREELANCING and starting a BUSINESS-
> 
> 1. Building a water purifier brand for e-com and offline digital stores.
> 2. Adding a vertical by setting up water filter manufacturing plant. inv- 45L+ (loan)
> 
> Suggest me something or give me an advice because i am very confused as how to pick something that would solve my problem. I feel like running away from my family but I cant so I gotta 

**Top comments:**
- **Alarming-Prompt-** (73↑): Given the circumstances you are describing, it's not the right time to jump into entrepreneurship.   Business no matter how solid it sounds on paper involves parameters which are sometimes beyond our control.   Having gone through the CSE experience, I'm sure you understand the gamble with luck. It's the same with business. You'll need time to find a date with your luck. And then make the luck work.   For now, choose the least riskiest path. Do not mitigate risks by adding additional risks.   Whatever you choose to do, factor your peace of mind.
- **indianCorleone** (19↑): \&gt; talk sense to me to pay off his loans somehow     Problem right here. Why would you pay his loans? Ask him to sell of the land and pay his loans himself.
- **Primary-Day-8466** (15↑): Not many would like my comment. Please do not downvote.My opinion comes from my own experience where I noticed people without degrees are earning in lakhs and educated ones are searching ruthlessly for jobs.   I suggest you create YT videos about how you get freelance roles and how data annotation works for time being. Earning 2.5L per month only source is YT which takes time of about 1-1.5 year. Since you are tech-savvy you should prosper.
- **OwnYam932** (12↑): What is your personal net worth. Is the 6cr net worth yours?
- **Ok-Breakfast-4676** (8↑): Why not jump into other products, if i am not wrong you guys might be having inj molding ranging from 400-800 tonnage with a single or double cavity. Why not get into other niche requiring similar tonnage. Since your father has operation expertise, raise the capital look for investors try to become OEM of some company a good one. The problem with this industry is that anyone is trying to get in and since the moulds are explicitly available the people with money they enter this market and just commoditise it. Look for something that requires some kind of heavy investment initially or some kind of moat or expertise  Such as precision molding making molds of some part that requires 0 tolerance or similar.

---

### 38. Big Money Doesn’t Always Mean Big Business. How This Business Failed Even After Investing ₹200 Cr
**r/IndiaBusiness** · 2026-05-07 · 123↑ · 32💬 · pain=192
[https://reddit.com/r/IndiaBusiness/comments/1t5wlmu/big_money_doesnt_always_mean_big_business_how/](https://reddit.com/r/IndiaBusiness/comments/1t5wlmu/big_money_doesnt_always_mean_big_business_how/)

**Post body:**
> A few years ago, I was approached by a US-based jeweler who had set up a massive ₹200 Crore plant in Haridwar to manufacture partition boards made from compressed rice and paddy straw. The concept is huge in Australia and the US, and they wanted to replicate that in India. They hired me to make high-end videos highlighting the product's features: fire resistance, soundproofing, and how "tough" it was.
> 
> As a rule, I never work without an advance. When I asked for the advance, they gave me the classic corporate trap: *"Just come to the plant in Haridwar, we’ll release the payment as soon as the shoot begins."*
> 
> I travelled from Noida and started the shoot. Every day, I’d ask about the advance. Every day, it was: *"It’s in processing, the accounts team is on it."*
> 
> The shoot ended. Still no money. Then they tried to pressure me: *"Just send us the first cut/draft, and we’ll release the funds immediately."*
> 
> At that point, I knew if I shared the edit, I was finished. I clearly told them that editing would not start until the advance was in my account
> 
> Miraculously, the money appeared. But as soon as I delivered the first draft? **Total radio silence.** They vanished. A few weeks later, I saw my unfinished drafts being used all over their social media. At that stage, I didn’t have the resources to take legal action, so I moved on.
> 
> Recently, I got curious and decided to see what happened to these "titans" and their ₹200 Cr plant. I did some digging into their financials available 

**Top comments:**
- **Quick_City_5785** (44↑): You missed the lack of ethics as the reason for failure. That is at the top of the list
- **Longjumping_Fee_1490** (5↑): In my opinion most people who invest in industrial area are smart and business oriented folks.   Agree to your point on indian labour is cheap and b2b dynamic is different. 
- **Illustrious-Milk-896** (3↑): Just curious.   Is this an advertisement for your services?  **They hired me to make high-end videos highlighting the product's features.**  
- **VJ_OA** (3↑): OP you forgot to add important trait for failure - 'Ethics', what you do with one vendor is tend to be repeated with other vendors too. It seeps in your company's DNA.  Though 'Ethics' is a dinosaur-age trait which doesn't have mainstream place in today's business'es; but you can see the real-life success of business'es who follow this.
- **NathuSingh** (2↑): Okay. Im looking for Jobs in Haridwar, so curious.

---

### 39. Indian entrepreneurs should really look at the UAE, it’s way easier than people think!
**r/IndiaBusiness** · 2025-11-29 · 94↑ · 47💬 · pain=188
[https://reddit.com/r/IndiaBusiness/comments/1p9lqil/indian_entrepreneurs_should_really_look_at_the/](https://reddit.com/r/IndiaBusiness/comments/1p9lqil/indian_entrepreneurs_should_really_look_at_the/)

**Post body:**
> I’ve been dealing with a lot of UAE business setups recently, and honestly, I’m surprised more Indian entrepreneurs aren’t taking advantage of it.
> 
> Setting up a company there is ridiculously fast, sometimes literally the same day. No endless paperwork, no running around departments. The whole system is built to make life easy for businesses.
> 
> And the benefits are huge: low taxes, strong banking, access to GCC/African markets, high spending power, and a very stable environment. Even if you keep India as your main base, having a UAE entity just opens doors especially for payments, partnerships, and international clients.
> 
> It’s also not as expensive or complicated as people assume. If you’re building something in tech, trading, e-commerce, services… the UAE is honestly worth a look.
> 
> If anyone wants to know how the process actually works, I’m happy to share what I’ve seen firsthand.

**Top comments:**
- **[deleted]** (32↑): Most small businesses in India don't need license to setup business in India. Not even GST.  In UAE even if you want to sell popsicle you need to take license. The cost of doing business in UAE is very very very high..
- **[deleted]** (8↑): Setting up company anywhere on earth is easier than in India . Obviously with  favorable laws on taxes ,  dubai is a  better  option   Kindly explain how registering in dubai helps one if they have    1. Physical  products    2. Digital products   . This knowledge would be more useful to one and all here !!
- **[deleted]** (2↑): This is largely true but with one caveat: local banks in the UAE are extremely cautious about opening accounts for entities with non-resident owners, especially if the activity isn't low-risk. Software is fine but trading is risky. Digital banks like Wio might help, but one should be prepared to face issues when trying to open a corporate bank account. Being a UAE resident helps.
- **[deleted]** (2↑): Any scope in exporting  Agri products from INDIA?
- **akhileshrao** (1↑): I’ve been reading about the recent exodus of small business and people selling their flats in Dubai

---

### 40. Lease out EVs
**r/IndiaBusiness** · 2026-03-29 · 88↑ · 44💬 · pain=186
[https://reddit.com/r/IndiaBusiness/comments/1s6ogh7/lease_out_evs/](https://reddit.com/r/IndiaBusiness/comments/1s6ogh7/lease_out_evs/)

**Post body:**
> I am looking for an investment opportunity in logistics space and leaned towards leasing out vehicles to ecommerce platforms. Got to know that zepto primary partners with Zypp electric for vehicles leasing. If anyone has some knowledge, any help would be appreciated!

**Top comments:**
- **Training2Life** (29↑): These types of investments are sht and only good if you have a strong agreements and shtty vehicles.  Most of these vehicles will be used as sht &amp; be ready to deal with insurances too. 
- **stoplossftw** (15↑): &gt; ROI 26% in 3 Years  you can get that from corporate bond funds (Growth mode) and its lower risk than this investment
- **purp_rapbeat** (2↑): It's a scam. Do not fall for it. 
- **jono0009** (1↑): You will buy EV scooters and rent it out to these guys?
- **Zealousideal-Goat178** (1↑): They will pay you monthly, yearly or how? 

---
