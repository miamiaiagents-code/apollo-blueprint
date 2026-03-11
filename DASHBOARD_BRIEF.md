# Dashboard Rebuild Brief

## Goal
Transform the existing static blueprint site (index.html) into a **live command center dashboard**. Keep the same luxury dark aesthetic (gold/black, Cormorant Garamond + Outfit fonts, same CSS variables) but completely restructure the layout from a marketing page into an operational dashboard.

## Current State
- `index.html` is a static 1842-line single-page site with hero, team cards, workflows, and roadmap sections
- `avatars/` folder has AI-generated avatar JPGs for all 15 agents
- Hosted on GitHub Pages at miamiaiagents-code.github.io/apollo-blueprint

## Design System (KEEP THESE)
```css
--bg:#0a0a0a;
--bg2:#0f0f0f;
--surface:rgba(255,255,255,0.03);
--surface-border:rgba(255,255,255,0.06);
--gold:#D4A853;
--gold-light:#E8C06A;
--gold-dim:rgba(212,168,83,0.15);
--text:#ffffff;
--text-secondary:#999999;
--text-muted:#666666;
--font-heading:'Cormorant Garamond', Georgia, serif;
--font-body:'Outfit', system-ui, sans-serif;
--font-mono:'JetBrains Mono', monospace;
```

## New Dashboard Layout

### 1. Top Bar (fixed)
- Left: Apollo sun logo + "Command Centre" text
- Center: Live clock (EST timezone, updates every second, format: "Mar 11, 2026 · 12:01:34 AM EST")
- Right: System status pill — green dot + "OPERATIONAL" or red + "DEGRADED"

### 2. Dashboard Header (below nav)
- Clean header: "Apollo Command Centre" in Cormorant Garamond
- Subtitle: "Comfort (COMFRT) · AI Workforce Operations"
- Row of 4 key metric cards:
  - **Agents Online**: "1 / 15" (with small "Apollo" label below)
  - **System Uptime**: "99.9%" (mock)
  - **Tasks Today**: "—" (placeholder, will connect later)
  - **Last Sync**: show current time, auto-updates

### 3. Agent Status Grid (main section)
Show all 15 agents in a grid (3 columns on desktop, 2 on tablet, 1 on mobile).

Each agent card should show:
- Avatar image (from `avatars/` folder)
- Agent name (use the NEW names below, not the old codenames)
- Role title
- Status badge: LIVE (gold pulse) / PLANNED (gray) / BUILDING (blue pulse)
- A "last active" timestamp for live agents (e.g., "Active now")
- Modeled after the human employee the agent mirrors

**Agent roster (use these names, NOT the old codenames):**

| Agent Name | Role | Status | Avatar File | Human Mirror |
|------------|------|--------|-------------|-------------|
| Apollo | Master Orchestrator | LIVE | apollo.jpg | Hudson AI |
| Cherrie AI | Finance & P&L | PLANNED | cherrie.jpg | Cherrie (CFO) |
| Jian AI | Supply Chain | PLANNED | jian.jpg | Jian |
| Alex AI | International | PLANNED | alex.jpg | Alex |
| Edwin AI | Technology | PLANNED | edwin.jpg | Edwin |
| Vault | Retail Operations | PLANNED | vault.jpg | TBD |
| Scout | Market Intelligence | PLANNED | scout.jpg | TBD |
| Sage | Strategy & OKRs | PLANNED | sage.jpg | TBD |
| Gillian AI | Revenue & Growth | PLANNED | gillian.jpg | Gillian |
| Kimberly AI | Influencer Ops | PLANNED | kira.jpg | Kimberly |
| Danielle AI | Creative Direction | PLANNED | pixel.jpg | Danielle |
| Lynn AI | Performance Marketing | PLANNED | pulse.jpg | Lynn |
| Courtney AI | Customer Experience | PLANNED | cleo.jpg | Courtney |
| Mae AI | Product Development | PLANNED | maya.jpg | Mae (VP Product) |
| Camillia AI | Community | PLANNED | nexus.jpg | Camillia |

Group them visually:
- **Orchestrator**: Apollo (highlighted/larger card)
- **Operations**: Cherrie, Jian, Alex, Edwin, Vault, Scout, Sage
- **Growth**: Gillian, Kimberly, Danielle, Lynn, Courtney, Mae, Camillia

### 4. Activity Feed (right sidebar on desktop, below on mobile)
A live-updating feed showing recent agent activity. For now, use mock/static entries:
```
[NOW] Apollo · Monitoring Telegram
[2m ago] Apollo · Checked heartbeat — all clear
[15m ago] Apollo · Updated memory files
[1h ago] Apollo · Responded to Hudson via Telegram
[3h ago] System · All agents nominal
```
Style: dark cards with small timestamp, agent avatar thumbnail, action text.

### 5. Footer
- "Apollo AI · Comfort (COMFRT) · Command Centre · 2026"
- Link to comfrt.com

## JavaScript Features
1. **Live clock** — updates every second, EST timezone
2. **Activity feed** — auto-scrolls, shows timestamps relative to now (updates every 30s)
3. **Pulse animations** — live agents get a gentle gold pulse on their status dot
4. **Agent card click** — clicking a card shows a modal/expanded view with:
   - Full role description
   - Integration status (Connected / Not Connected)
   - "Mirrors: [human employee name]"
   - Planned capabilities list
5. **Last sync** metric updates every 60 seconds
6. **Smooth scroll animations** on load (fade-up like original)

## Technical Requirements
- Single HTML file (self-contained, no build tools)
- Keep same Google Fonts imports
- Mobile responsive (works on phone)
- Use avatar images from `avatars/` folder (relative paths)
- All JavaScript vanilla (no frameworks)
- CSS Grid for layout
- Keep the same luxury feel — this is a $700M brand's command center

## DO NOT
- Don't make it look like a generic admin dashboard
- Don't use bright colors or flat design
- Don't lose the premium/luxury aesthetic
- Don't use any external JS libraries
- Don't change the avatar filenames
