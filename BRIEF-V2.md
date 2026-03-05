# V2 Build Brief — Pixel-Perfect Rebuild

Rebuild index.html to be an EXACT visual clone of danny8im8.manus.space but for Comfort/Apollo.

## Critical Design Details from Danny's site:

### Fonts
- Headings: Cormorant Garamond (serif, italic for accent words)
- Body: Outfit (sans-serif)  
- Code/tags: JetBrains Mono

### Colors
- Background: near-black (#0a0a0a to #0f0f0f)
- Accent: Deep red (#dc2626 / #ef4444) → WE USE GOLD (#D4A853 / #E8C06A)
- Cards: rgba(255,255,255,0.03) with subtle borders
- Text: white for headlines, gray for body

### Expanded Card Layout (CRITICAL)
When a team card is clicked, it expands to show:
- LEFT SIDE: About paragraph, then sections with headers (e.g., "Daily Intelligence", "CEO Decision Support", "Setup Note") with bullet lists
- RIGHT SIDE: "Base Access" (tools/integrations with emoji), "Paired With" (other agent name tags), "Tools & Integrations" (more tags)
- Full-width expansion with smooth animation

### Nav Bar
- Fixed/sticky, transparent with blur backdrop
- Left: Logo "☀️ Apollo" + "AI Workforce Blueprint"  
- Center: Tab buttons (Overview, The Team, How It Works, Roadmap) - currently active tab has a background highlight
- NO stock ticker (remove that from Danny's)

### Team Section
- Has a secondary nav bar that appears when scrolling to that section
- Cards are full-width rows (not grid), with avatar, name, role, status badge, quote, and chevron
- Grouped by: Master Orchestrator, Operations Stack, Growth Stack

### Workflow Section  
- 3 vertical workflow cards side by side
- Each has numbered steps with colored dots matching the agent's color
- Step numbers in circles connected by vertical lines

### Roadmap Section
- Sprint cards in 2x2 grid
- Big sprint number (01, 02, etc.)
- Agent tags with colored left borders
- Task list with arrow bullets

## Agent Expanded Card Content

### Apollo — Master Orchestrator
**About:** Apollo is the AI digital twin of Hudson Leogrande — founder of Comfort (COMFRT), the fastest-growing apparel brand in America. He sits at the apex of the entire operation: the only agent with full visibility across every department. He synthesizes signals from finance, operations, influencer, and growth into a single daily intelligence brief. He doesn't just execute — he decides what matters.

**Daily Intelligence:**
- Morning brief: Shopify revenue + Meta spend + top 3 issues  
- Telegram message triage — flags what needs Hudson, archives the rest
- Calendar management — meetings, launches, creator calls
- Cross-function anomaly detection — spots when something is off

**CEO Decision Support:**
- Synthesizes inputs from all 13 agents into one weekly CEO brief
- Flags decisions that require Hudson's attention vs. can be delegated
- Tracks OKRs across all departments in real time

**Setup Note:** Primary orchestrator — receives daily digests from all agents and compiles the CEO morning brief.

**Base Access:** 💬 Telegram (Full Access), 📝 Notion (Read/Write), 📧 Email, 📅 Calendar, 🌐 All Workspaces

**Paired With:** All 13 agents

**Tools:** OpenClaw, Notion API, Telegram API, Shopify API, Composio

### Fin — Finance & P&L Intelligence
**About:** Fin is the financial nerve center of Comfort. He monitors every dollar flowing through the business — from $500K/day ad spend to manufacturing payments to revenue recognition. He doesn't wait for month-end to tell you something's wrong. He knows in real time.

**Daily Operations:**
- Overnight P&L signals, margin alerts, cash position
- Ad spend vs revenue tracking across Meta, TikTok, Google
- Manufacturing payment schedules and net-90 term tracking
- Revenue forecasting against $1B target

**Setup Note:** Connect Shopify, banking APIs — daily P&L and cash position brief live.

**Base Access:** 💰 Shopify Revenue, 📊 Banking APIs, 📈 Northbeam, 🧮 P&L Dashboard

**Paired With:** Apollo, Maya, Chain, Sage

**Tools:** Shopify API, Banking API, Northbeam API

### Chain — Supply Chain & Inventory
**About:** Chain is the logistics brain of Comfort. She tracks every hoodie from manufacturer to customer — across China, Cambodia, and Vietnam. She knows when to reorder, when to shift production, and when a shipment is going to be late before the 3PL tells you.

**Daily Operations:**
- Inventory levels by SKU, color, and size across all warehouses
- Stockout predictions and automatic reorder alerts
- 3PL performance monitoring and shipping SLA tracking
- Manufacturing timeline tracking with net-90 payment terms

**Setup Note:** Connect Shopify inventory, 3PL API — stockout alerts and supplier tracking live.

**Base Access:** 📦 Shopify Inventory, 🚚 3PL API, 🏭 Manufacturing Dashboard, 📊 Demand Forecasting

**Paired With:** Apollo, Fin, Forge, Globe, Vault

**Tools:** Shopify API, 3PL API, Demand Planning Tools

### Globe — International Expansion
**About:** Globe is the advance team for Comfort's global takeover. He's building the playbook to duplicate the US creator-powered growth engine in UK, Australia, Canada, and Europe. Every new market gets the same proven formula — local creators, local fulfillment, local media buying.

**Key Focus Areas:**
- UK launch planning: creator recruitment, 3PL setup, Meta/TikTok localization
- Australia TikTok Shop first-mover strategy
- Canada cross-border infrastructure
- EU market analysis: Germany, Netherlands, Nordics

**Setup Note:** International expansion tracker — UK, AU, CA, EU market entry playbooks.

**Base Access:** 🌍 Market Research, 📊 International Analytics, 🤝 Local Partner Database

**Paired With:** Apollo, Chain, Kira, Pulse, Sage

**Tools:** Market Research APIs, Logistics Planning Tools

### Vault — Retail Operations
**About:** Vault is building Comfort's physical presence. Two flagship stores launching Q4 2026 — Mall of America and American Dream Mall — with a goal of 1 new store per month in 2027. She manages everything from lease negotiation to store buildout to hiring in-store teams.

**Key Focus Areas:**
- Mall of America (MN) and American Dream Mall (NJ) buildout tracking
- Store design standardization for rapid rollout
- In-store team hiring pipeline (8-10 people per location)
- Retail POS and inventory integration with Shopify

**Setup Note:** Retail buildout tracker — Mall of America + American Dream Mall progress.

**Base Access:** 🏬 Retail Dashboard, 📋 Construction PM Tools, 👥 Hiring Pipeline

**Paired With:** Apollo, Chain, Fin, Sage

**Tools:** Project Management, Shopify POS

### Scout — Intelligence & Research
**About:** Scout is the eyes and ears of the operation. She monitors competitors, tracks market trends, and finds opportunities before anyone else sees them. She scans everything — social media, industry reports, patent filings, job postings — to keep Comfort ahead.

**Key Focus Areas:**
- Competitive intelligence on DTC apparel brands
- Market trend analysis and emerging category opportunities
- Content trend monitoring across TikTok, Instagram, YouTube
- Partnership and M&A opportunity identification

**Setup Note:** Competitive intelligence, market trends, deal pipeline live.

**Base Access:** 🔍 Web Research, 📊 Industry Reports, 🏷️ Competitor Tracking

**Paired With:** Apollo, Sage, Brand, Pixel

**Tools:** Web Scraping, Social Listening, Market Research APIs

### Sage — Strategy & OKRs
**About:** Sage is the strategic brain. She maintains the company's North Star metrics, tracks OKRs across every department, and ensures every team is rowing in the same direction toward $1B. She sees around corners — connecting dots between departments that nobody else notices.

**Key Focus Areas:**
- Company-wide OKR tracking and alignment
- Weekly strategy digest and quarterly planning
- Department performance benchmarking
- Long-term growth modeling and scenario planning

**Setup Note:** OKR framework, weekly strategy digest, board narrative prep.

**Base Access:** 📊 OKR Dashboard, 📈 Analytics, 📋 Strategic Planning

**Paired With:** Apollo, Fin, Scout, Globe

**Tools:** Notion API, Analytics Tools

### Maya — Revenue & Performance
**About:** Maya lives in every dollar. She monitors Shopify revenue in real time, tracks Meta and TikTok ROAS, watches Northbeam attribution, and knows exactly which channels are printing money and which are bleeding. At $500K/day in ad spend, every percentage point matters.

**Daily Operations:**
- Real-time Shopify revenue monitoring
- Meta Ads ROAS and spend tracking ($500K+/day)
- TikTok Ads performance and TikTok Shop revenue
- Northbeam attribution analysis (the "Lamborghini of tracking")
- Channel-level profitability analysis

**Setup Note:** Connect Shopify, Meta Ads, TikTok, Northbeam — daily revenue brief live.

**Base Access:** 🛒 Shopify, 📊 Meta Ads, 🎵 TikTok Ads, 📈 Northbeam, 📧 Klaviyo

**Paired With:** Apollo, Fin, Pulse, Pixel, Kira

**Tools:** Shopify API, Meta Marketing API, TikTok API, Northbeam API

### Kira — Influencer & Creator Ops
**About:** Kira builds the army that builds the brand. She manages 600,000+ affiliates, 500 core creators, and a library of 1M+. She tracks who's producing, who's converting, and who needs to be recruited next. The Comfort creator machine produces 5,000 videos per day — Kira makes sure they're all working.

**Daily Operations:**
- Creator performance tracking (3-7 videos/day per creator)
- New creator recruitment and onboarding pipeline
- Yuka AI outreach integration (5,000 messages/day)
- Commission tracking and affiliate management
- Weekly call prep (5pm ET Thursdays)

**Setup Note:** Connect TikTok, Instagram — creator tracking, Yuka AI integration, affiliate management.

**Base Access:** 🎬 TikTok Creator, 📸 Instagram API, 🤖 Yuka AI, 💰 Affiliate Dashboard, 💬 Discord

**Paired With:** Apollo, Maya, Pixel, Pulse, Nexus

**Tools:** TikTok API, Instagram API, Yuka AI, Affiliate Platform API

### Pixel — Creative & Content Ops
**About:** Pixel turns data into the brief that wins. She analyzes which ad creatives are performing, what customer language resonates, and which content formats drive conversions. Every Monday, she synthesizes inputs from Maya, Cleo, Kira, and Pulse into the Weekly Creative Brief — the document that drives all content creation.

**Weekly Creative Flywheel:**
- Top-performing ad creatives by ROAS and CTR from Maya
- Customer language and review phrases from Cleo
- Best creator content for paid amplification from Kira
- Channel performance data and fatigue signals from Pulse
- Synthesizes into Weekly Creative Brief: hooks, angles, formats, AI tool recommendations

**Setup Note:** Connect ad libraries — weekly creative brief auto-generated.

**Base Access:** 📊 Ad Libraries, 🎨 Creative Analytics, 📝 Brief Generator

**Paired With:** Apollo, Maya, Kira, Pulse, Cleo

**Tools:** Meta Ad Library, TikTok Creative Center, AI Creative Tools

### Pulse — Performance Marketing
**About:** Pulse optimizes every ad dollar until it screams. He manages the performance marketing stack across Meta, TikTok, and Google — monitoring ROAS in real time, flagging creative fatigue, and identifying scaling opportunities. At $500K/day heading to $1M/day in Q4, precision is everything.

**Daily Operations:**
- Real-time ROAS monitoring across Meta, TikTok, Google
- Creative fatigue detection and rotation alerts
- Budget allocation optimization across channels
- Whitelisting performance tracking (Jen Selter, Josh Goldie, etc.)
- Spark Ads performance monitoring on TikTok

**Setup Note:** Connect Meta, TikTok, Google Ads — performance monitoring and ROAS alerts live.

**Base Access:** 📊 Meta Ads Manager, 🎵 TikTok Ads, 🔍 Google Ads, 📈 Northbeam

**Paired With:** Apollo, Maya, Pixel, Kira

**Tools:** Meta Marketing API, TikTok Ads API, Google Ads API

### Cleo — Customer Intelligence
**About:** Cleo listens so you don't have to. She monitors every customer review, support ticket, and social mention to understand what customers love and what needs fixing. With a 50% repeat purchase rate, keeping customers happy is everything.

**Daily Operations:**
- Review monitoring across all platforms
- Support ticket categorization and trend analysis
- NPS tracking and sentiment analysis
- Customer language extraction for marketing use
- Overnight alert digest for urgent issues

**Setup Note:** Connect reviews, Gorgias — review digest and NPS monitoring live.

**Base Access:** ⭐ Review Platforms, 🎧 Gorgias, 📊 NPS Dashboard, 💬 Social Listening

**Paired With:** Apollo, Pixel, Kira, Forge

**Tools:** Gorgias API, Review Platform APIs, Sentiment Analysis

### Forge — Product Development
**About:** Forge builds what the customer demands. He tracks product performance data, monitors competitor launches, and works with VP of Product May to plan the next collection. From the original hoodie that started it all to blankets and loungewear — Forge knows what's coming next.

**Key Focus Areas:**
- Product performance analytics (sell-through, return rates, reviews)
- Competitor product monitoring and gap analysis
- New product development pipeline tracking
- Manufacturing coordination with China, Cambodia, Vietnam suppliers
- Seasonal collection planning and trend forecasting

**Setup Note:** Connect product roadmap — weekly NPD digest live.

**Base Access:** 🏭 Product Pipeline, 📊 Sales Analytics, 🔬 Trend Research

**Paired With:** Apollo, Chain, Cleo, Maya

**Tools:** Shopify Product API, Trend Analysis Tools

### Nexus — Community & Affiliates
**About:** Nexus turns customers into evangelists. He manages the Discord community (education hub, weekly breakdowns, tier-based channels), tracks affiliate engagement, and ensures the community flywheel keeps spinning. It takes 13 touchpoints for a Comfort customer to buy — Nexus makes sure every touchpoint counts.

**Key Focus Areas:**
- Discord community management and engagement metrics
- Affiliate program health (600K+ affiliates)
- Customer-to-affiliate conversion tracking
- Community content curation (top videos, bestsellers, color trends)
- Weekly onboarding call coordination

**Setup Note:** Connect Discord — affiliate engagement and community health monitoring.

**Base Access:** 💬 Discord, 🤝 Affiliate Platform, 📊 Community Analytics

**Paired With:** Apollo, Kira, Cleo, Maya

**Tools:** Discord API, Affiliate Platform API

## SVG Icons
Generate simple, clean SVG icons for each agent. Style: minimalist, single-color line art or geometric shapes.
- Apollo: Sun/star icon
- Fin: Chart/graph icon
- Chain: Chain links icon
- Globe: Globe/earth icon
- Vault: Building/store icon
- Scout: Magnifying glass/binoculars icon
- Sage: Brain/lightbulb icon
- Maya: Dollar/revenue icon
- Kira: Camera/creator icon
- Pixel: Palette/brush icon
- Pulse: Heartbeat/pulse icon
- Cleo: Ear/listening icon
- Forge: Hammer/anvil icon
- Nexus: Network/connected nodes icon

Build as single index.html with everything inlined. Make it IDENTICAL to Danny's site layout.
