# Memo

# **Pre-configured Payment Form templates & KYC Journeys**

| Author | [Mothi Venkatesh](mailto:mothi.venkatesh@cashfree.com) |
| :---- | :---- |
| Contributors | [Lavika Aggarwal](mailto:lavika.aggarwal@cashfree.com)[Abhisikta Guha Niyogi](mailto:abhisikta.niyogi@cashfree.com)[Jayant Kaushik](mailto:jayant.kaushik@cashfree.com)[Abhishek Das](mailto:abhishek.das@cashfree.com) |
| Engineering | TBD |

**Context**: We want to create a library of ready-made templates that cover both sides of the Cashfree merchant journey: collecting payments and verifying identity.

Today, these are disconnected experiences. 

1. A jewellery merchant needs PAN verification for orders above ₹2L before accepting payment.   
2. A SEBI-registered investment advisor must collect Aadhaar e-sign before processing a transaction.   
3. A forex company needs PAN \+ Aadhaar verification that can happen before or after payment. 

In each case, the merchant stitches together separate KYC and payment flows, creating a broken customer experience and heavy developer effort.

Templates solve this by giving merchants pre-configured, compliance-ready workflows they can pick and deploy, across 2 categories:

## **1\. Payment Form Templates**

Pre-built payment collection forms with embedded verification blocks. Instead of merchants building separate KYC \+ payment flows, we offer integrated journeys where verification happens inline with checkout.

**The core insight**: There's a large segment of merchants who must adhere to KYC and regulatory requirements before collecting payments. The market today forces them to connect individual journeys together. The customer sees 2 disconnected flows. Developers spend weeks stitching them. Analysts pull data from different sources to reconcile results.

**What templates include**: Each Payment Form template is a pre-configured combination of **verification blocks \+ payment checkout**, tailored to a specific merchant LOB.

**Verification blocks available**: PAN (with name/DOB match), Aadhaar (with UIDAI OTP), GSTIN, BAV, Aadhaar e-Sign, Document Upload, Terms & Conditions consent.

**Two user journeys per template**: 

1. **First-time users**: Verify and validate data pre-payment. Once verified against a phone number, data stored in Cashfree Vault for future use.  
2. **Returning users**: See pre-filled, masked details for confirmation. Zero friction on repeat transactions.

**Merchant controls**: Enable via Dashboard or API at per-transaction level. Define verification rules (capture only, verify valid/invalid, verify with name match, verify with Aadhaar OTP).

Live reference: [https://template-hub-1641daf7.base44.app/TemplateGallery](https://template-hub-1641daf7.base44.app/TemplateGallery)   
Template detail page: [https://template-hub-1641daf7.base44.app/TemplateDetail?id=tmpl\_007](https://template-hub-1641daf7.base44.app/TemplateDetail?id=tmpl_007)

**Why this matters for Cashfree**: Deeper embedded integration \= harder to replace. Merchants route more traffic to Cashfree for verification \+ payment combined. Increased wallet share. Retention hook.

## **2\. KYC Journey Templates**

Pre-configured, compliance-mapped verification workflows for banks, NBFCs, fintechs, and regulated entities. Each template defines the exact API bundle, call sequence, risk thresholds, fallback logic, and escalation rules for a specific use case.

**The core insight**: The hardest part of selling Secure ID is not convincing banks our APIs work. It's showing the assembled workflow. "Show me how your products fit into my savings account opening journey" is the \#1 ask. Compliance heads know they need EDD. Fintech PMs know they need Video KYC bypass for small tickets. But translating RBI master directions, PMLA guidelines, and FIU circulars into an actual API workflow takes months.

**Component-level selling**: Regulated entities rarely replace their entire journey. They plug in components. So each template also breaks down into sellable modules: 

1. CDD component,   
2. EDD component,   
3. Lead Screening component,   
4. Mule Detection component. 

A bank might take just the EDD module (which bundles FRI, Mobile360, PAN, Penny Drop) and plug it into their existing flow.

### **How the 2 categories connect**

1. Payment Form Templates serve merchants who need verification embedded in their payment flow (jewellers, forex, insurance, gaming).  
2. KYC Journey Templates serve regulated entities who need standalone onboarding workflows (banks, NBFCs, fintechs opening accounts or disbursing loans).

Both feed into the same product roadmap: 

1. **Journeys** (pre-configured onboarding product, live today)  
2. **Template Gallery** (peer-contributed templates with private/public options, building now)

**The long-term vision**: merchants and peers contribute their own templates (payment forms, KYC journeys, or hybrid verify-and-pay flows) creating a network effect where the library grows beyond what we build alone. Think Spotify playlists for payment forms. Think of the Figma community for KYC workflows.

### **How to read each template**

1. **Payment Form Templates**: LOB → Verification blocks needed → Mandatory vs. Optional → Pre-payment vs. Post-payment → User journey (first-time vs. returning)  
2. **KYC Journey Templates**: Use Case → Industries → Risk Profile → Regulatory Compliance → API Workflow Bundle → API Descriptions (non-obvious APIs only) → Input/Output → Turnaround Time → Compliance Note

This structure is intentional. The business team should pick up any template, understand the journey in 2 minutes, and present it to a client without additional context.

## **Next Steps:**

1. Build component-level modules (CDD, EDD, Lead Screening) sellable independently  
2. Expand KYC templates to PPI, crypto (FIU guidelines), NBFC-specific use cases  
3. Feed all templates into Journeys product and KYC Studio for self-serve deployment

## **References & Vibe coded Prototypes:**

* [Form Templates](https://template-hub-1641daf7.base44.app/TemplateGallery)  
* [Template detail page](https://template-hub-1641daf7.base44.app/TemplateDetail?id=tmpl_007)  
* [Payment Forms PRD](https://cashfree.atlassian.net/wiki/spaces/CE/pages/1005813774/Verify+and+Pay+on+hosted+checkout%20)

# 🛡️ KYC Templates

| KYC Pre-configured Journeys | Status | Compliance Approval |
| :---- | :---- | :---- |
| Gig Onboarding |  |  |
| Low-Risk CDD (Video KYC Bypass) |  |  |
| Standard CDD with Video KYC |  |  |
| EDD for High-Risk Profiles |  |  |
| Mule Prevention at Onboarding |  |  |
| RM-Assisted Lending Existing Customer Cross-Sell |  |  |
| Post-Onboarding Continuous Monitoring |  |  |
| Small Ticket Lending	 |  |  |
| PSU Bank Post-Merger Onboarding Stack |  |  |
| GIFT City VideoKYC		 |  |  |
| Gold Verify & Pay |  |  |

# Lead Screening

## **Component 1: Lead Screening**

**What it does:** Pre-qualifies an applicant before any KYC spend happens. Answers one question: should we invest in verifying this person?

**When to use:** First step in any onboarding journey. Runs before PAN, Aadhaar, Video KYC, or any paid verification API. Rejects bad applicants upfront so you don't waste ₹50-100 on KYC for someone who would fail anyway.

**Regulatory basis:** RBI risk-based approach to CDD. PMLA Section 11A (risk assessment before establishing business relationship).

**API Bundle:**

* **1-Click Onboarding (Mobile360 prefill)**: Fetches 15+ verified data points using just mobile number \+ OTP. Sources: Credit Bureau, EPFO, Telco, PAN, Masked Aadhaar. DPDP compliant with user consent. Prefills forms, reduces drop-offs by 45%.  
* **Bank Account Verification (BAV) with Name Match**: Confirms bank account ownership. Name match cross-validates account holder name against declared name.  
* **Global AML/PEP/Sanctions Check**: Screens against 200+ databases (OFAC, UN, EU, HMT, DFAT). Catch sanctioned individuals before you spend on KYC.  
* **Basic Fraud Indicators**: Negative PIN code screening, device velocity checks, IP reputation.  
* **Email Verification**: Validates email existence and domain reputation.

**Output:** → Pass \= proceed to CDD (Component 2\) or EDD (Component 3\) based on risk signals → Fail (AML/sanctions hit) \= reject immediately, no further KYC → Review \= flag for manual assessment before proceeding

**Turnaround Time:** \<10 seconds

**Sell this to:** Any regulated entity that wants to reduce KYC cost by filtering bad applicants upfront. Especially valuable for high-volume digital lenders and banks with 10,000+ daily applications.

# CDD

## **Component 2: Customer Due Diligence (CDD)**

**What it does:** Core identity verification. Confirms the applicant is who they claim to be. This is the minimum regulatory requirement for account opening or transaction processing.

**When to use:** After Lead Screening passes. Required for all customer onboarding under RBI Master Directions on KYC. The "must-have" component.

**Regulatory basis:** RBI Master Directions on KYC (updated 2023). PMLA Rules. CDD is mandatory for all regulated entities.

**API Bundle:**

**Identity Verification:**

* **PAN 360 Verification**: Name, DOB, Aadhaar linkage status, address, contact info from NSDL database.  
* **Aadhaar Verification**: Two paths available: → Path A (Primary): Pinless Digilocker. Government database verification. No OTP dependency on UIDAI. Higher reliability. → Path B (Fallback): SmartOCR (Aadhaar OCR \+ QR). 6 quality checks (blur, glare, partial, B\&W, face presence, QR). 4 forgery checks (screenshot, alteration, photo imposition, AI-generated). QR-OCR cross-validation.  
* **CKYC Download/Upload**: Fetches existing verified records. Uploads new records post-verification.

**Biometric Verification:**

* **Face Match & Liveness**: Compare selfie with ID photo. Anti-spoofing. Age-gap verification (handles 10-15 year photo differences). Passive liveness detection.  
* Name Match: Fuzzy logic, phonetic matching, regional dialect handling. Returns confidence score for RE to threshold.

**Contextual Signals:**

* Mobile360 (EPFO employment verification): Validates employment status, employer name, UAN.  
* Telco Data Check: 3-4 years postpaid payment history. Consistent payments \= financial discipline indicator.  
* Behavioral Risk Scoring: Bank statement analysis for SIP investments, savings patterns, spending behavior.

**CDD Signal Categories (for risk tiering):**

1. **Identity Integrity**: PAN-Aadhaar-Digilocker consistency, face match confidence, tampered/synthetic ID detection.  
2. **Behavioural & Device**: SIM age, device reuse patterns, abnormal navigation during onboarding.  
3. **Contextual & Environmental**: Geo-location consistency, IP velocity, time-of-day patterns.

**Output:** → Low Risk \= straight-through activation (no Video KYC needed for eligible profiles) → Medium Risk \= conditional onboarding, enhanced monitoring post-activation, or proceed to Video KYC → High Risk \= escalate to EDD (Component 3\)

**Turnaround Time:** \<30 seconds for automated checks

**Sell this to:** Every regulated entity. This is the foundational component. Banks, NBFCs, fintechs, insurance, PPI issuers. Can be sold without Video KYC for low-risk profiles (RBI risk-based approach allows this).

# EDD

## **Component 3: Enhanced Due Diligence (EDD)**

**What it does:** Deep verification for high-risk profiles. Goes beyond identity to assess intent, source of funds, network connections, and real-world presence. This is where compliance officers spend most of their time.

**When to use:** When CDD flags high risk. When there's a PEP match, sanctions hit, adverse media, mule indicators, high-value transactions (\>₹2L), or cross-border activity.

**Regulatory basis:** RBI Master Directions on KYC (Section 38-42). PMLA Rules 9(1A). RBI-mandated EDD for high-risk customers. Can't be skipped for certain triggers.

**API Bundle:**

Everything from CDD (Component 2), PLUS:

**Deep Screening:**

* Global Watchlists & AML/PEP Check (comprehensive): 200+ databases. More thorough than the basic check in Lead Screening. Includes fuzzy name matching across transliterations.  
* Adverse Media Screening: 10,000+ news sources. Weekly crawl. Covers 20+ years of media archives.  
* **Sanction List Screening**: OFAC SDN, UN Security Council, EU Sanctions, HMT, DFAT.  
* **Multi-Source Government Blacklist Aggregation**: Single API for 5+ government databases: National Informatics Portal, Cybercrime Coordination Center, National Cyber Crime Reporting Portal, Duty Portal (bank card fraud), DOT data from RBI.

**Risk Intelligence:**

* ~~Network Analysis: Related parties graph. Identifies connections to known fraudsters or mule accounts.~~  
* MCC Code Risk Intelligence: Transaction patterns by Merchant Category Code. Flags high-risk MCCs: gambling (7995), money orders (4829), crypto (6051). Leverages Cashfree PG data.  
* Negative PIN Code & Geographic Risk Screening: Flags known mule hotspot geographies.  
* Source of Funds Verification Support: Documentation workflow for income/wealth verification.  
* Beneficial Ownership Identification: For entity accounts. UBO discovery.

**Verification:**

* Video KYC (V-CIP): RBI-compliant video call with 2-layer or 3-layer maker-checker. Face Match \+ Liveness \+ Deepfake detection during call. IP Intelligence (VPN/TOR). Smart Scheduler \+ AI Nudges. 10+ languages. Low-bandwidth optimized.  
* Aadhaar eSign: For agreement/consent execution post-verification.  
* Physical CPV Scheduling Integration: For cases requiring in-person verification.

**Workflow:**

* EDD Workflow Orchestration: Case management system: automated blacklist checks → severity bucketing → branch assignment → physical CPV scheduling → documentation → senior management approval workflow. Audit trail for RBI inspections.  
* Continuous Monitoring Alert Setup: Activates ongoing surveillance post-onboarding.

**Manual Workflow Triggers:** 

1. PEP/sanction match \= senior management approval required  
2. Adverse media hit \= compliance team review  
3. Network analysis red flag \= physical CPV mandatory  
4. Source of funds unclear \= branch EDD with documentation  
5. Mule database match \= immediate block \+ investigation

**Output:** Automated checks → case created → manual review workflow → physical CPV if needed → senior approval → account decision

**Turnaround Time:** 2-7 days (includes physical verification where required)

**Sell this to:** Banks and NBFCs with high-risk customer segments. Cross-border businesses. Entities under RBI audit pressure. This is the compliance officer's best friend. Also sells as a standalone add-on to entities that already have CDD but need deeper screening.

# Mule Detection

## **Component 4: Mule Detection**

**What it does:** Prevents mule accounts from being created. Detects fraud patterns that pass standard KYC because the identity is real but the intent is fraudulent.

**When to use:** Overlays on top of CDD or EDD. Can run at Lead Screening (pre-KYC) for early rejection, or during CDD for richer signals. HDFC Bank's "Zero Block Account" philosophy: block upfront, not post-facto.

**Regulatory basis:** RBI mandate for mule account detection processes. NPCI MuleHunter.ai consortium. 90%+ mule accounts pass basic KYC because identity alone doesn't capture intent.

**API Bundle:**

*Consortium & Database Checks:*

* **MuleHunter.ai Consortium Database Check**: Real-time check against RBI/NPCI consortium of known mule accounts shared by participating banks.  
* **Multi-Source Government Blacklist**: Cybercrime portals, National Informatics Portal, Duty Portal, FRI (Financial Risk Intelligence) fraud blacklists.  
* **Cashfree Transaction Intelligence**: Blacklist data across 800K+ merchant network. Digital spend patterns. Device fingerprinting. Payout intelligence. This is what pure KYC vendors can't access.

*Behavioral & Device Signals:*

* **Device Velocity & Fingerprinting**: Multiple applications from same device. Device reuse across flagged accounts.  
* **Geographic Mismatch Detection**: KYC address (e.g., Mumbai) vs. login location (e.g., Assam). Immediate red flag if \>500km mismatch.  
* **SIM Age & Porting Intelligence**: Newly purchased SIM, recent porting, disposable number detection. Digital age of mobile number.  
* **IP Risk Scoring**: VPN/proxy/TOR detection. IP geolocation vs. declared address. IP velocity anomalies.

*Post-Activation Monitoring:*

* **Initial Deposit Withdrawal Pattern**: First deposit withdrawn within 2-3 days \= classic mule signal.  
* **Behavioral Anomaly Detection**: T+1, T+7, T+30 risk signals. Balance vs. transaction size monitoring (₹1L avg balance but ₹6-7L transactions \= mismatch).  
* **Profile Consistency Analysis**: Cross-validates declared profile against observed behavior.  
* **Network Graph Analysis**: Identifies relationships to known mules. Linkage alerts.

**Risk Score Calculation (Shield Mule Detection):**

**Positive signals**: Digital spend history, digital age of mobile/email, PAN-Aadhaar match, name match with UPI VPA, consistent email-phone combination.

**Negative signals**: Email-phone combination not found in payments data, risky IP/address, blacklisted UPI, temporary/blacklisted email, chargeback/dispute history.

**Real-Time Actions:** → High mule risk (score \>70) \= account opening blocked instantly → Medium mule risk (50-70) \= manual review required before approval → Low mule risk (\<50) \= approved with continuous monitoring setup → Consortium database hit \= automatic rejection \+ report to authorities

**Output:** Real-time risk score with decision recommendation. Prevents mule account creation vs. detecting post-facto.

**Turnaround Time:** \<30 seconds for automated screening. Continuous monitoring ongoing.

**Sell this to:** 

1. Banks (RBI mandate, especially post-audit observations).   
2. Lending companies (mule accounts for loan fraud).   
3. E-commerce (stolen card fraud via fake profiles). 

This is the fastest-growing product segment. Bureau, Signzy, and Perfios are all doing POCs with banks.

# Low-Risk CDD (Video KYC Bypass)

## **Template 1: Low-Risk CDD (Video KYC Bypass)**

**Use Case**: Existing customers opening additional accounts, low transaction limits (\<₹60,000), savings accounts, wallet-like products

**Industries**: Payments Banks, Small Finance Banks, Digital Banks

**Risk Profile**: Low Risk

**Regulatory Compliance**: RBI-compliant CDD for low-risk profiles per master directions

## **API Workflow Bundle:**

* 1-click Onboarding  
* PAN 360 Verification  
* Aadhaar e-KYC (OKYC via biometric/OTP)  
* CKYC Download (if existing customer)  
* Bank Account Verification (Penny Drop/Reverse Penny Drop)  
* Mobile360 (EPFO employment verification)  
* Email Verification  
* Behavioral Risk Scoring (bank statement analysis)  
* Telco Data Check (postpaid payment history)  
* Basic Fraud Indicators (negative PIN codes, device velocity)  
* Multi-Source Blacklist Check (Cybercrime, National Informatics Portal)

## **API Descriptions:**

**Behavioral Risk Scoring**: Analyzes bank statements for SIP investments, savings patterns, spending behavior. Saver mindset \= higher score. \[Kotak-validated in production\]

**Telco Data Check**: 3-4 years postpaid mobile payment history. Consistent payments \= financial discipline indicator. \[Kotak actively using\]

**Multi-Source Blacklist**: Aggregated check across Cybercrime portals, National Informatics Portal, Duty Portal (bank card fraud). \[Single API for 5+ government databases\]

**Output**: Pass/Fail with risk score. Pass \= instant account opening (no video KYC). Fail \= escalate to Template 2\.

**Turnaround Time**: \<30 seconds

**Cost Advantage**: 50% lower than video KYC

**Compliance Note**: Video KYC waiver per RBI risk-based approach for low-risk profiles.

# Standard CDD with Video KYC

## **Template 2: Standard CDD with Video KYC**

**Use Case**: New-to-bank customers, savings accounts (₹60K-₹2L limits), credit cards, personal loans (standard risk)

**Industries**: Banks, NBFCs, Fintechs

**Risk Profile**: Medium Risk

## **API Workflow Bundle:**

* PAN 360 Verification  
* Video KYC (with maker-checker workflow support)  
* SmartOCR (document intelligence \+ quality checks)  
* Pinless Digilocker (government database verification)  
* Face Match & Liveness Checks  
* Video KYC Quality Scoring (AI-based behavior analysis)  
* Address Verification (utility bill OCR)  
* CKYC Upload  
* Mobile360 (EPFO \+ telco validation)  
* Email Verification  
* Social Presence Check (phone \+ email across platforms)  
* Basic Watchlists & AML/PEP Check  
* Mule Account Database Check  
* Fraud Indicator Scoring

## **API Descriptions:**

**Video KYC**: RBI-compliant live video call with liveliness detection. Supports 2-level and 3-level maker-checker workflows. Auditor review for quality assurance. \[Supports emerging 3-layer checking trend \- Shon, Kotak\]

**Video KYC Quality Scoring**: AI analysis of video KYC call including document clarity, customer behavior (hesitation, call drops), background audio analysis (coaching detection), liveliness confidence. Assists auditors in prioritizing reviews. \[Kotak flags suspicious background voices\]

**Output**: Pass \= account opened. Review \= auditor approval required. Fail/High-Risk Match \= escalate to Template 3 (EDD).

**Turnaround Time**: 5-10 minutes (real-time video KYC \+ automated checks)

# EDD for High-Risk Profiles

## **Template 3: Enhanced Due Diligence (EDD) for High-Risk Profiles**

**Use Case**: PEP matches, sanction list hits, high-value transactions (\>₹2L), suspicious patterns, mule indicators, cross-border transactions

**Industries**: Banks, NBFCs (regulatory compliance)

**Risk Profile**: High Risk

**Regulatory Compliance**: RBI-mandated EDD for high-risk customers (AML/CFT compliance)

## **API Workflow Bundle:**

All APIs from Template 2(Standard CDD with Video KYC) PLUS:

* Global Watchlists & AML/PEP Check (comprehensive \- 200+ databases)  
* Adverse Media Screening (10,000+ news sources)  
* Sanction List Screening (OFAC, UN, EU, HMT, DFAT)  
* Multi-Source Government Blacklist Aggregation  
* Network Analysis (related parties graph)  
* Source of Funds Verification Support  
* Beneficial Ownership Identification  
* Negative PIN Code & Geographic Risk Screening  
* MCC Code Risk Intelligence (transaction patterns)  
* Continuous Monitoring Alert Setup  
* EDD Workflow Orchestration (case management)  
* Physical CPV Scheduling Integration

## **API Descriptions:**

**Multi-Source Govt Blacklist**: Aggregated API for 5+ government databases: National Informatics Portal, Cybercrime Coordination Center, National Cyber Crime Reporting Portal, Duty Portal (bank card fraud), DOT data from RBI. Single integration point. \[Kotak-validated critical need\]

**MCC Code Risk Intelligence**: Analyze transaction patterns by Merchant Category Code. Flag high-risk MCCs: gambling (7995), money orders (4829), crypto (6051). \[Leverages Cashfree PG data advantage\]

**EDD Workflow Orchestration**: Case management system: automated blacklist checks → severity bucketing → branch assignment → physical CPV scheduling → documentation → senior management approval workflow. Audit trail for RBI inspections. \[Integrates with Kotak's hybrid EDD process\]

**Physical CPV Scheduling**: Customer Point Verification scheduling integration. A bank representative visits the customer address for physical verification. \[Kotak-validated EDD stage 2\]

## **Manual Workflow Triggers:**

* PEP/sanction match \= senior management approval required  
* Adverse media hit \= compliance team review  
* Network analysis red flag \= physical CPV mandatory  
* Source of funds unclear \= branch EDD with documentation  
* Mule database match \= immediate block \+ investigation

**Output**: Automated checks → case created → manual review workflow → physical CPV if needed → senior approval → account decision

**Turnaround Time**: 2-7 days (includes physical verification)

**Compliance Note**: RBI-mandated EDD for high-risk profiles. Maker-checker process required. Physical verification cannot be skipped for certain triggers.

# Alternate version

**Template 1**: **KYC Verification with enhanced checks**

**​​Use case**: For Savings account opening, Credit card, Personal loans on high risk profiles at Banks & NBFCs.

**Industries used**: Banks

**API Workflow Bundle**: PAN 360 \+ SmartOCR (AND) Digilocker \+ Face Match & Liveness Checks \+ Watchlists & AML/PEP Check 

**API Description:**

1. **PAN 360**: Gain instant access to reliable information sourced directly from the National Securities Depository Limited (NSDL) database with the PAN Profile API. With just a PAN number, you can unveil comprehensive details about an individual or entity, including their name, address, date of birth, and contact information.  
2. **Pinless Digilocker \[AND\] SmartOCR**: This capability is an end-to-end solution for your KYC needs. First, an OCR is done on the document provided, followed by a government database check against that document. Additional document quality checks are also done on the document.  
3. **Face Match & Liveness Checks**: This capability verifies a selfie photo for signs of user liveness and additional parameters for evaluating the selfie. It then generates a match score based on a comparison between the user's selfie and the image of the government ID document.  
4. **(Global) Watchlists & AML/PEP check**: Enter a person's basic information in this capability, and our system will instantly scan them against global AML, PEP, and sanctions databases. We'll notify you if there's a potential match, helping you make informed decisions and stay compliant.

# Mule Prevention at Onboarding

## **Template 4: Mule Prevention at Onboarding (Zero Block Account)**

**Use Case**: All new account openings (savings, current) with focus on preventing mule accounts before creation

**Industries**: Banks (liability products), Payments Banks

**Risk Profile**: All Risk Levels (preventive screening)

**Regulatory Compliance**: HDFC Bank 'Zero Block Account' philosophy \- block upfront, not post-facto

## **API Workflow Bundle:**

Template 2(Standard CDD with Video KYC) APIs PLUS Mule-Specific Checks:

* MuleHunter.ai Consortium Database Check  
* Negative PIN Code Screening (mule hotspots)  
* Geographic Mismatch Detection (KYC address vs. login location)  
* Device Velocity & Fingerprinting (multiple applications same device)  
* Network Graph Analysis (related to known mules)  
* Behavioral Anomaly Detection (T+1, T+7, T+30 risk signals)  
* Initial Deposit Withdrawal Pattern Check  
* Profile Consistency Analysis

## **API Descriptions:**

**MuleHunter.ai Check**: Real-time check against RBI/NPCI consortium database of known mule accounts. Shared by all participating banks.

**Geographic Mismatch Detection**: Compare KYC address (e.g., Mumbai) with internet banking login/mobile registration location (e.g., Assam). Immediate red flag if \>500km mismatch. \[HDFC Bank T+1 signal\]

**Initial Deposit Withdrawal**: Monitor first deposit. If withdrawn within 2-3 days \= classic mule signal. \[HDFC Bank validated\]

## **Real-Time Actions:**

* High mule risk score (\>70) \= account opening blocked instantly  
* Medium mule risk (50-70) \= manual review required before approval  
* Low mule risk (\<50) \= approved with continuous monitoring setup  
* Consortium database hit \= automatic rejection \+ report to authorities

**Output**: Real-time decision: Block/Review/Approve with continuous monitoring. Prevents mule account creation vs. detecting post-facto.

**Turnaround Time**: \<30 seconds for automated screening

# RM-Assisted Lending

## **Template 5: RM-Assisted Physical Lending (Mortgage/Secured Loans)**

**Use Case**: Home loans, mortgage loans, loan against property, high-value secured lending

**Industries**: Banks, Housing Finance Companies, NBFCs

**Risk Profile**: Medium-High (large ticket sizes)

**Regulatory Compliance**: Physical verification mandatory (property exchange, not digital lending)

## **API Workflow Bundle:**

* PAN 360 Verification  
* Aadhaar e-KYC  
* CKYC Download/Upload  
* Field Investigation (FI) Report Integration  
* Telephonic Confirmation (TP) Integration  
* Income Verification (salaried vs. self-employed)  
* Employment Verification (official email domain check \+ office FI)  
* GST Verification (self-employed)  
* Shop Establishment Certificate Verification  
* Bank Account Verification  
* Credit Bureau Check (CIBIL, Experian, Equifax, CRIF)  
* Property Document OCR \+ Legal Verification  
* OSV (Original Seen Verified) Workflow  
* High-Value Discretion (credit officer meeting)

## **API Descriptions:**

**OSV Workflow**(Original Seen and Verified): Employee physically meets customer, verifies original documents (not photocopies), stamps with signature. Certifies to RBI that physical verification done. Must be an employee, not a third party. \[Ruchika validated requirement\]

## **Mandatory Physical Touchpoints:**

* Customer meeting with RM/credit officer (cannot be avoided)  
* Original document exchange (property papers)  
* Physical FI at customer address  
* Physical FI at employer office (salaried) or business address (self-employed)  
* OSV stamp by bank employee

**Output**: Credit approval based on physical verification \+ API checks. Video KYC not applicable (physical verification supersedes).

**Turnaround Time**: 3-7 days (includes FI, TP, credit officer meeting)

**Compliance Note**: Not covered under digital lending guidelines. Physical verification mandatory per RBI.

# Existing Customer Cross-Sell

## **Template 6: Existing Customer Cross-Sell (Perpetual KYC)**

**Use Case**: Existing bank customers opening credit cards, FDs, additional savings accounts, investment products

**Industries**: Banks (cross-sell to existing base)

**Risk Profile**: Low Risk (established relationship)

**Regulatory Compliance**: Perpetual KYC \- previous physical verification serves as reference

## **API Workflow Bundle:**

* CKYC Lookup (existing verified record)  
* Internal Customer Risk Score (relationship history)  
* Account Behavior Analysis (transaction patterns, credit history)  
* Fraud Indicator Refresh (any new red flags)  
* Watchlist/PEP Refresh (daily dedupe)  
* Consent Capture for New Product  
* Minimal Additional KYC (if CKYC \>2 years old)

**Video KYC Bypass Rationale**: Previous physical verification (account opening, branch visit, RM meeting) satisfies RBI norms. Low-risk established relationship. \[Shon (Kotak) validated practice \- how HDFC credit card issued without video KYC\]

**Output**: Instant product issuance (e.g., credit card approved in 2 minutes). No video KYC required.

**Turnaround Time**: \<2 minutes

# Post-Onboarding Continuous Monitoring

## **Template 7: Post-Onboarding Continuous Monitoring (PMLA Compliance)**

**Use Case**: All active accounts \- transaction monitoring for AML/CFT, mule detection, fraud prevention

**Industries**: Banks, NBFCs, Payments Banks (regulatory requirement)

**Risk Profile**: Dynamic (changes based on behavior)

**Regulatory Compliance**: PMLA (Prevention of Money Laundering Act) mandated continuous monitoring

## **API Workflow Bundle:**

* Daily Deduplication (terrorist lists, PEP, sanctions, mule databases)  
* Dynamic Trust Scoring (continuous risk assessment)  
* Transaction Pattern Analysis (anomalies detection)  
* MCC Code Risk Intelligence (merchant category monitoring)  
* Network Graph Updates (new relationships detected)  
* Geographic Anomaly Detection (login location changes)  
* Velocity Checks (transaction frequency spikes)  
* Balance vs. Transaction Size Monitoring  
* Automated EDD Triggers  
* Case Management Integration

## **API Descriptions:**

**Daily Deduplication**: Automated checks against updated databases: OFAC, UN sanctions (daily updates), terrorist financing lists, PEP lists, MuleHunter.ai (real-time updates), adverse media (weekly crawl). \[HDFC Bank runs this for millions of customers daily per Babita\]

**Dynamic Trust Scoring**: Continuous trust score evolution (not static). Factors: account lifecycle stage, transaction patterns, average balance trends, external data changes. Trust slopes positively or negatively. \[Prakash concept from webinar\]

**Balance Transaction Monitoring**: Average monthly balance ₹1L but ₹6-7L transaction \= mismatch with profile. Trigger enhanced scrutiny. \[Prakash example from webinar\]

**Monitoring Frequency**: Real-time for transactions, daily for dedupes, weekly for adverse media, monthly for comprehensive risk score refresh

**Output**: Alerts for suspicious activity → automated case creation → manual investigation → account action (block/limit/monitor/unblock)

# Small Ticket Lending

## **Template 8: Small Ticket Lending (\<₹60K) \- CDD Without Video KYC**

**Use Case**: Personal loans \<₹60K, buy-now-pay-later (BNPL), consumer durable loans, small business loans

**Industries**: NBFCs, Fintechs, Digital Lenders

**Risk Profile**: Low-Medium (small ticket, lower regulatory threshold)

**Regulatory Compliance**: RBI allows CDD for NBFCs on transactions \<₹60K (no video KYC mandate)

## **API Workflow Bundle:**

* PAN 360 Verification  
* Aadhaar e-KYC (OKYC)  
* Bank Account Verification (Penny Drop)  
* Mobile360 (EPFO employment verification)  
* Credit Bureau Check (all 4 bureaus)  
* Bank Statement Analysis (for income assessment)  
* Behavioral Risk Scoring (saver vs. spendthrift)  
* Fraud Indicator Scoring  
* Alternate Data Underwriting (digital footprint, app permissions)  
* Social Presence Check  
* Basic Watchlist/AML Check  
* Consent Manager Integration (Account Aggregator)

**Video KYC Bypass Justification**: NBFCs not mandated for \<₹60K transactions per RBI. CDD with Aadhaar e-KYC \+ bank statement analysis sufficient. Cost-effective for small tickets.

**Output**: Instant loan approval/rejection. No manual intervention for low-risk profiles. Entire journey \<5 minutes.

**Cost Advantage**: 70% lower customer acquisition cost vs. video KYC journey

**Compliance Note**: RBI compliant for NBFCs \<₹60K threshold. Fintechs like MoneyTap, KreditBee, Fibe target segment.

# PSU Bank Post-Merger Onboarding Stack

## **Template 9: PSU Bank Post-Merger Onboarding Stack**

**Use Case**: Newly merged PSU banks modernizing KYC infrastructure (Q2-Q4 2026 opportunity)

**Industries**: Public Sector Banks (post-merger entities)

**Risk Profile**: All Risk Levels (full-stack solution)

## **API Workflow Bundle:**

Complete Template 2 \+ Template 3 \+ Template 4 PLUS PSU-Specific:

* Government Database Native Integration (single sign-on with NIC)  
* Hindi \+ Regional Language Support (10+ languages)  
* Branch Integration APIs (legacy CBS: BaNCS, Finacle, Flexcube)  
* Physical Branch Fallback Workflows  
* Aadhaar-Based Authentication (primary)  
* Jan Dhan Account Special Workflows (zero balance)  
* Pradhan Mantri Schemes Integration (PMJDY, PMJJBY, APY)  
* Rural/Semi-Urban Geolocation Services  
* Low-Bandwidth Video KYC (2G/3G optimization)

**Competitive Advantage**: Positioning as 'merger integration de-risking' with government database expertise. Private bank practices adapted for PSU context.

**Target Timeline**: Q2-Q4 2026 (post-merger integration phase per Shon’s prediction)

**Pricing Model**: Bundled subscription (₹50L-1Cr ACV) for full stack vs. per-API for private banks

# GIFT City VideoKYC

\[WIP\]

## **GIFT City VideoKYC**

### **Template 10: GIFT City NRI Video KYC (IFSCA V-CIP Compliant)**

**Use Case:** NRI account opening, investment account onboarding, banking services activation for Non-Resident Indians through IFSCA-regulated entities operating in GIFT City IFSC.

**Industries:** IFSC Banking Units (IBUs), IFSC Brokers, Asset Management Companies, Insurance Entities, and other IFSCA-regulated entities in GIFT City.

**Risk Profile:** Medium-High (cross-border, NRI-specific controls required)

**Regulatory Compliance:** IFSCA (AML, CFT and KYC) Guidelines, 2022 as amended vide circular dated October 31, 2025\. Part-A of Annexure II (V-CIP for NRI onboarding). 4-month pilot phase requirements apply.

**Eligible NRI Jurisdictions (Phase 1):** USA, UAE, Singapore, UK, Japan, South Korea, Australia, Canada, Hong Kong, Germany, France (11 jurisdictions)

---

### **API Workflow Bundle:**

**Pre-Call Verification Stack**

1. PAN 360 Verification  
2. Passport Validation API (Live government database check)  
3. SmartOCR (Passport extraction \+ quality checks \+ forgery detection)  
4. Global Watchlists & AML/PEP Check (200+ databases)  
5. Adverse Media Screening  
6. Sanction List Screening (OFAC, UN, EU, HMT, DFAT)

**During Video KYC Call**

7. Video KYC (IFSCA-compliant V-CIP with 3-layer maker-checker)  
8. Face Match & Liveness (anti-deepfake, passive liveness, micro-expression analysis)  
9. IP Intelligence (VPN/TOR detection \+ jurisdiction validation)  
10. GPS Geo-tagging (validates NRI is physically in declared jurisdiction)

**Post-Call Verification**

11. Name Match (fuzzy logic, phonetics, cross-script matching for NRI name variations)  
12. Foreign Bank Account Verification (first credit validation for debit freeze release)  
13. Concurrent Audit Workflow (mandatory before account activation)  
14. CKYC Upload (where applicable)  
15. Continuous Monitoring Alert Setup

---

### **API Descriptions:**

1. **Passport Validation API:** Real-time validation of Indian passport against government database. Extracts and verifies passport number, name, DOB, place of issue, expiry date, and MRZ data. During the Video KYC call, the agent asks the NRI to show their physical passport. SmartOCR extracts data from the live video frame. Passport Validation API then cross-verifies extracted data against the official Passport Seva database in real-time. [https://www.cashfree.com/docs/secure-id/ovd/passport](https://www.cashfree.com/docs/secure-id/ovd/passport)  
2. **IP Intelligence (Jurisdiction Validation):** IFSCA mandates that the V-CIP session IP address must originate from the NRI's declared jurisdiction. Cashfree's IP Intelligence detects VPN/TOR usage and validates that the IP geolocation matches one of the 11 approved jurisdictions. If an NRI declares residence in the USA but connects from a non-USA IP, the session is flagged for review. This is a hard compliance requirement under the October 2025 IFSCA circular.  
3. **GPS Geo-tagging:** Captures the NRI's live GPS coordinates during the video call and cross-references with declared jurisdiction. Provides latitude/longitude, accuracy radius, and timestamp. Stored as part of the audit trail. IFSCA requires geo-tagging as an additional location validation layer alongside IP checks.  
4. **Face Match & Liveness (Anti-Deepfake):** IFSCA mandates anti-deepfake technology for all V-CIP sessions. Cashfree's Face Match compares the live video feed with the passport photo in real-time. Passive liveness detection \+ micro-expression analysis prevents deepfake video injection, face replay attacks, and screen-based spoofing. Confidence score returned to the agent during the call. Works reliably across international bandwidth conditions.  
5. **Video KYC (IFSCA V-CIP):** Full video-based customer identification process compliant with IFSCA's amended guidelines. Key GIFT City specific features include: (a) Browser-agnostic, works across all web browsers, iPad, iOS, Android, (b) Supports 10+ languages for multilingual NRI base, (c) Low-bandwidth optimized with WebRTC for international calls, (d) Session recording with watermarking for audit trail, (e) Randomized prompt integration per IFSCA requirements, (f) 3-layer workflow: Agent conducts call, Reviewer verifies demographics, Concurrent Auditor validates risk and compliance.  
6. **3-Layer Maker-Checker Workflow:** IFSCA (and RBI audit observations) mandate a 3-layer verification for V-CIP: Layer 1 (Agent) conducts the video call, verifies passport, captures OVD. Layer 2 (Reviewer/Checker) validates customer demographics, call quality, and document clarity. Layer 3 (Concurrent Auditor) reviews risk signals, compliance flags, and approves/rejects before account activation. Every case must pass a concurrent audit before the account goes live. This is a hard IFSCA requirement.  
7. **Global Watchlists & AML/PEP Check:** Comprehensive screening across 200+ global databases. Mandatory for all GIFT City onboarding given the cross-border nature. Includes OFAC SDN, UN Security Council, EU Sanctions, HMT, DFAT, and PEP databases across all 11 approved jurisdictions. Adverse media screening covers 10,000+ news sources. Single API integration, real-time results.  
8. **Foreign Bank Account Verification:** IFSCA mandates that NRI accounts opened via V-CIP are placed in "debit freeze" mode until the first credit is received from the NRI's verified foreign bank account. This confirms the NRI's overseas banking relationship. Once the first credit lands and is verified, the debit freeze is lifted and the account becomes fully operational. This is a fraud prevention control unique to GIFT City NRI onboarding.  
9. **Name Match (Cross-Script):** NRI passports often have name variations across documents (transliteration differences, middle name usage, abbreviated names). Cashfree's Name Match uses fuzzy logic, phonetic matching, and cross-script comparison to handle these variations. Returns a confidence score that the regulated entity can threshold based on their risk appetite. Critical for matching passport name with PAN name and foreign bank account holder name.

# Gig Onboarding

# Gold Verify & Pay

# 💰 PF Templates \[WIP\]

## **Template 1: KYC & Pay**

**​​Use case**: 

**Industries used:** 

**Form workflow:** 

---

## **Template 2: Aadhaar E-Sign & Pay**

**​​Use case**: 

**Industries used:** 

**Form workflow:** 

---

## **Template 3:** 

---

**Reference**: [https://cashfree.atlassian.net/wiki/spaces/CE/pages/1005813774/Verify+and+Pay+on+hosted+checkout](https://cashfree.atlassian.net/wiki/spaces/CE/pages/1005813774/Verify+and+Pay+on+hosted+checkout)

# Launch GTM

