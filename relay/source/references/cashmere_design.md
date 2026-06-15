# Cashmere Design System

> The design system for **Cashfree Payments** — an Indian payments and banking platform that powers merchant checkout, payouts, settlements, and verification flows.
>
> Cashmere is a quiet, near-monochrome system. Black text on near-white surface, electric blue used as signal, dense data tables, no decoration. Designed to let payment numbers and status do the talking.

---

## Table of contents

1. [Brand snapshot](#brand-snapshot)
2. [Content fundamentals](#content-fundamentals)
3. [Color](#color)
4. [Typography](#typography)
5. [Spacing](#spacing)
6. [Radii](#radii)
7. [Elevation & shadows](#elevation--shadows)
8. [Borders & dividers](#borders--dividers)
9. [Iconography](#iconography)
10. [Logo](#logo)
11. [Layout & density](#layout--density)
12. [States & interactions](#states--interactions)
13. [Motion](#motion)
14. [Components](#components)
15. [Patterns](#patterns)
16. [Anti-patterns](#anti-patterns)

---

## Brand snapshot

Cashfree serves businesses processing payments in India. The product tone is **precise, operational, matter-of-fact**. Designers prioritise **information density** and **clarity** over flourish.

- **Audience:** merchants, finance ops, developers integrating Cashfree APIs.
- **Voice:** direct, calm, neutral-to-slightly-warm.
- **Person:** "you" for the merchant; "we" for Cashfree.
- **Default mode:** dense data, calm chrome, no celebration.

---

## Content fundamentals

### Tone & voice
- **Operational, not marketing.** Copy reads like an ops console: *"Payment captured"*, *"Settlement scheduled for 17 Apr"*, *"Refund failed — retry"*. Avoid adjectives, avoid hype.
- **Second person** for the merchant: *"Your settlement has been initiated."*
- **First person plural** ("we") only for Cashfree's own actions: *"We've notified your acquirer."*
- **Imperative** for CTAs, no pleasantries: **Create payment link**, **Download report**, **Refund ₹1,250**. Never "Click here", never "Please".
- **State before verb** in status copy: *"Pending: Bank confirmation"*, *"Failed: Insufficient funds"*.

### Casing
- **Sentence case** everywhere except tags and overlines.
  - Page title: *"Payment details"*, not *"Payment Details"*.
  - Button: *"Create order"*, not *"Create Order"*.
- **UPPERCASE with letter-spacing** only on tags, overlines, and status chips: `SUCCESS`, `PENDING`, `FAILED`.
- **Code / IDs** always in mono: `order_Lx4yqR8`, `cf_pay_1234`. Never wrap IDs in quotes.

### Numbers, currency, dates
- Currency: prefix `₹`, Indian lakhs/crores grouping (`₹12,45,670.00`). Two decimals for fiat.
- Dates in tables: `17 Apr 2026, 14:32`. Short form `17 Apr` when year is implied.
- "No data" → `—` (em dash). Never blank, never "N/A".
- Numerics: tabular figures (`font-variant-numeric: tabular-nums`) in tables and totals.

### Emoji & exclamations
- **No emoji** in product UI. Not in empty states, not in success toasts.
- **Exclamation marks** reserved for actual errors and warnings only. Success is understated: *"Refund initiated."* — full stop, not bang.

### Worked examples
| Don't | Do |
|---|---|
| *"Copied! 🎉"* | **"Payment link copied"** |
| *"Oops, nothing here!"* | **"No refunds yet. Issue a refund from any captured payment."** |
| *"Sorry, something went wrong."* | **"Couldn't process refund. The original payment is older than 180 days."** |
| *"Submit"* | **"Capture ₹4,500"** (amounts inline in CTAs) |
| *"Click here to download"* | **"Download report"** |

---

## Color

A near-monochrome system. Black text (`#1B1B1B`) on near-white surface (`#FFFFFC`) is the default page. Color appears as **signal**, not decoration.

### Primitives — accent (brand blue)
| Token | Hex | Usage |
|---|---|---|
| `--accent-50`  | `#F2F6FF` | Subtle backgrounds, selected-row tint (lightest) |
| `--accent-100` | `#E5EDFF` | Banner backgrounds, hover on accent surfaces |
| `--accent-200` | `#CCDAFF` | Borders on tinted accent containers |
| `--accent-300` | `#9EB9FF` | — |
| `--accent-400` | `#6B95FF` | — |
| `--accent-500` | `#3870FF` | Hover state on links/buttons |
| `--accent-600` | `#094EFF` | **Brand primary.** Buttons, links, active nav, focus rings |
| `--accent-700` | `#003BD1` | Pressed/active state for primary button |
| `--accent-800` | `#002C9E` | Text on `accent-100` backgrounds |
| `--accent-900` | `#001E6B` | — |
| `--accent-950` | `#000E33` | — |

### Primitives — semantic
| Family | 50 (subtle bg) | 500/600 (primary) | 700/800 (text on subtle) |
|---|---|---|---|
| **Negative** (red) | `#FFE0E0` | `#B80000` | `#700000` |
| **Positive** (green) | `#DCFFE9` | `#009B54` | `#005B21` |
| **Warning** (amber) | `#FFF7E6` | `#FBB016` | `#A06D03` |
| **Info** (blue) | `#E5EDFF` | `#094EFF` | `#002C9E` *(same scale as accent)* |

### Primitives — neutral (greys)
13-step ramp. Critical anchors:

| Token | Hex | Role |
|---|---|---|
| `--neutral-0`    | `#000000` | Pure black (rare; logo only) |
| `--neutral-50`   | `#1B1B1B` | **Default text** |
| `--neutral-200`  | `#494949` | Secondary text |
| `--neutral-400`  | `#767676` | Tertiary text, meta, captions |
| `--neutral-600`  | `#A4A4A4` | Disabled text, strong border |
| `--neutral-800`  | `#D1D1D1` | **Default border** (inputs, cards) |
| `--neutral-900`  | `#E8E8E8` | Subtle divider, muted bg |
| `--neutral-950`  | `#F2F2F2` | Subtle page bg, table header bg |
| `--neutral-1000` | `#FFFFFC` | **Surface white** (note: not pure white) |

### Overlays (transparent black)
`rgba(21,21,21, α)` from `0.10` (`--overlay-100`) to `0.90` (`--overlay-900`). Modal scrim is `--overlay-500`.

### Semantic mapping
```
text-primary    → neutral-50    (#1B1B1B)
text-secondary  → neutral-200   (#494949)
text-tertiary   → neutral-400   (#767676)
text-disabled   → neutral-600   (#A4A4A4)
text-inverse    → neutral-1000
text-accent     → accent-600
text-negative   → negative-500
text-positive   → positive-600
text-warning    → warning-700

bg-default        → neutral-1000  (#FFFFFC)
bg-subtle         → neutral-950   (#F2F2F2)
bg-muted          → neutral-900   (#E8E8E8)
bg-inverse        → neutral-50
bg-accent-subtle  → accent-100
bg-accent         → accent-600

border-default → neutral-800  (#D1D1D1)
border-subtle  → neutral-900  (#E8E8E8)
border-strong  → neutral-600  (#A4A4A4)
border-accent  → accent-600

icon-default   → neutral-50
icon-secondary → neutral-300
icon-tertiary  → neutral-500
icon-accent    → accent-600

focus-ring     → 0 0 0 3px rgba(9,78,255,0.28)
```

### Color rules
- **One accent, one alert, neutral elsewhere.** A typical screen uses `accent-600` for one or two intentional moments and neutrals for everything else.
- **No gradients in chrome.** Flat fills only. Gradients allowed in marketing illustration, never in dashboard surfaces.
- **No colored shadows.** Shadows are warm black (`rgba(27,27,27, α)`), never tinted.
- **Status tone discipline:** `SUCCESS` → positive, `PENDING` → warning, `FAILED` / `REFUNDED` → negative or neutral. Never invent new status colors.
- **Accent-only on Cashfree-product tags.** Tech-stack tags (Node, React, AWS) stay neutral.
- **Surface white is `#FFFFFC`** — slightly off-white. Pure `#FFFFFF` is reserved for input fields against `#FFFFFC` cards to maintain field/card contrast.

---

## Typography

Three families. **DM Sans** for display/UI, **Inter** for body/data, **DM Mono** for IDs and code.

```
--font-display : "DM Sans", ui-sans-serif, system-ui, sans-serif
--font-body    : "Inter",   ui-sans-serif, system-ui, sans-serif
--font-mono    : "DM Mono", "JetBrains Mono", ui-monospace, monospace
```

Loaded from Google Fonts. Weights used: 400 / 500 / 600 / 700, plus 800 on DM Sans for hero headings only.

### Type scale — semantic classes
1:1 with the Figma text styles.

| Class | Family · weight · size / line-height | Used for |
|---|---|---|
| `cm-page-heading`     | DM Sans 700 · 32 / 40 (-0.01em) | Page H1 |
| `cm-page-subheading`  | DM Sans 500 · 18 / 23 | Lede paragraph under H1 |
| `cm-section-heading`  | DM Sans 600 · 20 / 25 | Section titles |
| `cm-section-subheading` | DM Sans 500 · 16 / 22 | Card titles |
| `cm-section-overline` | DM Sans 600 · 11 / 16 · 0.08em · UPPER | Section dividers, pre-titles |
| `cm-body`             | Inter 400 · 13 / 19 | **Default paragraph** |
| `cm-body-sm`          | Inter 400 · 12 / 17 | Dense UI, captions |
| `cm-body-xs`          | Inter 400 · 11 / 15 | Meta text, used sparingly |
| `cm-datacard-title`   | DM Sans 500 · 14 / 19 | KPI label |
| `cm-datacard-numeric` | DM Sans 700 · 24 / 29 (-0.01em) | KPI value |
| `cm-input-label`      | DM Sans 500 · 12 / 17 | Form labels |
| `cm-input-value`      | DM Sans 500 · 14 / 20 | Form value text |
| `cm-input-placeholder`| DM Sans 500 · 14 / 20 (tertiary) | Placeholder |
| `cm-input-assistive`  | DM Sans 500 · 12 / 17 (tertiary) | Helper, error |
| `cm-nav-item`         | DM Sans 500 · 14 / 20 | Nav link |
| `cm-nav-item-active`  | DM Sans 600 · 14 / 20 | Active nav link |
| `cm-nav-section`      | DM Sans 600 · 11 / 16 · 0.08em · UPPER | Nav group label |
| `cm-tab` / `cm-tab-active` | DM Sans 500/600 · 14 / 20 | Tabs |
| `cm-btn-text-lg`      | DM Sans 500 · 14 / 18 | Button label (default) |
| `cm-btn-text-sm`      | DM Sans 500 · 12 / 16 | Button label (small) |
| `cm-tag`              | DM Sans 700 · 11 / 15 · 0.04em · UPPER | Status tags |
| `cm-chip`             | DM Sans 500 · 12 / 16 | Filter chips |
| `cm-mono`             | DM Mono 400 · 11 / 16 | IDs, hashes, timestamps as raw |
| `cm-table-cell`       | Inter 400 · 13 / 19 | Table body |
| `cm-table-cell-subtext` | Inter 400 · 12 / 17 (tertiary) | Sub-value in table cell |
| `cm-table-header`     | DM Sans 600 · 12 / 17 (0.02em) | Table column header |
| `cm-toast-heading`    | DM Sans 700 · 16 / 23 | Toast title |
| `cm-toast-body`       | DM Sans 500 · 14 / 20 | Toast body |
| `cm-tooltip`          | DM Sans 500 · 12 / 17 (inverse) | Tooltip |

### Display (decks, heroes, marketing)
| Class | Size / line-height |
|---|---|
| `cm-h1` | 56 / 1.05 (-0.02em) |
| `cm-h2` | 40 / 1.10 (-0.015em) |
| `cm-h3` | 32 / 1.15 (-0.01em) |
| `cm-h4` | 24 / 1.20 |

### Type rules
- **Body default is 13/19, not 16.** Cashmere is a dense system; whitespace is earned.
- **DM Sans for UI chrome, Inter for data.** Never mix: don't use Inter for buttons, don't use DM Sans for table body.
- **Mono only for raw machine values.** IDs, hashes, UTRs, signatures. Not for prices, not for dates rendered for humans.
- **Lock to the scale.** Six sizes per page is the ceiling, three is healthy. Avoid inventing in-between sizes.
- **Letter-spacing:** tighten on large headings (`-0.01em` to `-0.02em`), loosen only on overlines and tags (`+0.04em` to `+0.08em`).

---

## Spacing

8-pt-aligned scale with refinement steps below 8.

| Token | Value |
|---|---|
| `--space-0`  | `0` |
| `--space-1`  | `2px` |
| `--space-2`  | `4px` |
| `--space-3`  | `8px` |
| `--space-4`  | `12px` |
| `--space-5`  | `16px` |
| `--space-6`  | `20px` |
| `--space-7`  | `24px` |
| `--space-8`  | `32px` |
| `--space-9`  | `40px` |
| `--space-10` | `48px` |
| `--space-11` | `56px` |
| `--space-12` | `64px` |
| `--space-13` | `80px` |

### Common applications
- **Section padding inside cards:** `24px` (`--space-7`).
- **Form field vertical rhythm:** `12px` (`--space-4`) between label and field, `20px` (`--space-6`) between fields.
- **Page gutter:** `24–28px` horizontal.
- **Card grid gap:** `12px` (`--space-4`).
- **KPI strip gap:** `12px`.

---

## Radii

| Token | Value | Used on |
|---|---|---|
| `--radius-xs`  | `2px`   | Histogram bars, fine details |
| `--radius-sm`  | `4px`   | Tags, status pills (rectangular variant) |
| `--radius-md`  | `6px`   | **Buttons, inputs, chips** |
| `--radius-lg`  | `8px`   | **Cards, panels, drawers** |
| `--radius-xl`  | `12px`  | Modals, hero avatars |
| `--radius-2xl` | `16px`  | Marketing hero shapes |
| `--radius-3xl` | `24px`  | Marketing only |
| `--radius-pill` | `999px` | Pill chips, avatars, status dots |

**Rule:** never mix more than two radii in a single component. A card (8px) with buttons inside (6px) is fine; adding a 12px sub-card makes it noisy.

---

## Elevation & shadows

Cashmere is **low-elevation**. Pages are mostly flat. Shadow is for "this thing detached from the page" — popovers, modals, drawers — not for visual interest.

| Token | Value | Use on |
|---|---|---|
| `--shadow-xs` | `0 1px 2px rgba(27,27,27,0.06)` | Sticky header on scroll |
| `--shadow-sm` | `0 1px 2px rgba(27,27,27,.06), 0 1px 3px rgba(27,27,27,.08)` | Hover on interactive cards |
| `--shadow-md` | `0 2px 4px rgba(27,27,27,.06), 0 4px 8px rgba(27,27,27,.08)` | Dropdown menus |
| `--shadow-lg` | `0 4px 8px rgba(27,27,27,.06), 0 12px 24px rgba(27,27,27,.10)` | Popovers, tooltips |
| `--shadow-xl` | `0 8px 16px rgba(27,27,27,.08), 0 24px 48px rgba(27,27,27,.12)` | Modals, side drawer |
| `--shadow-focus` | `0 0 0 3px rgba(9,78,255,0.28)` | Focus rings |

**Rules**
- No neumorphism. No inner glow. No colored shadows.
- Cards are flat by default. Shadow appears on **hover for interactive cards only**, and it's `--shadow-sm`.
- Inputs use an inset `1px` border (`--shadow-inset-input`), never an outer shadow.

---

## Borders & dividers

| Role | Token | Value |
|---|---|---|
| Default border | `--border-default` | `1px solid #D1D1D1` |
| Subtle divider | `--border-subtle` / `--divider` | `1px solid #E8E8E8` |
| Strong border | `--border-strong` | `1px solid #A4A4A4` |
| Accent border | `--border-accent` | `1px solid #094EFF` |

**Rules**
- Single border, single weight. No double borders, no inner-shadow-as-border.
- Card border is **subtle** (`#E8E8E8`); input border is **default** (`#D1D1D1`). The hierarchy: input border > card border, because inputs need to look interactive against cards.
- Divider lines between table rows are `#E8E8E8`. Last row drops the divider.

---

## Iconography

- **Library:** ~250 custom icons in the Figma Icon Library, 16 / 20 / 24 / 32 px sizes.
- **Style:** outline, **1.5px stroke**, rounded caps, rounded joins.
- **Two-tone allowed** for status icons only (check, x, warning, info) — fill + stroke combinations.
- **Format:** SVG with `currentColor` so icons inherit from parent text color.
- **Substitution:** in this build, **Lucide** (CDN, `lucide@latest`) is used as a close substitute — same outline style, same stroke weight, same rounded caps. **Flagged: not the production icon set.** For exact parity, export Cashmere Icon Library from Figma and drop SVGs into `assets/icons/`.
- **Inline arrows** (`→`, `↗`) acceptable in body copy but not in UI chrome.

### Sizing
| Context | Size |
|---|---|
| Inside table cells, chips, small buttons | `14–16px` |
| Default UI (nav, larger buttons, inline meta) | `16px` |
| Card header, drawer header | `18–20px` |
| Empty states, illustrations | `24–32px` |

---

## Logo

- **Wordmark + mark** — `assets/logo-cashfree-wordmark.svg` (full lockup) and `assets/logo-cashfree-mark.svg` (the "C" mark alone).
- **Mark color:** `#094EFF` on light surfaces; `#FFFFFF` on dark surfaces. Never coloured otherwise.
- **Wordmark color:** `#1B1B1B` on light, `#FFFFFF` on dark.
- **Clear space:** half the cap-height of the wordmark on every side.
- **Minimum size:** wordmark at 80px width; mark at 16px.
- **Don't:** drop shadow, outline, gradient fill, rotate, recolor, place on photographs without an `--overlay-500` scrim.

---

## Layout & density

- **App frame:** 256px left nav, 56px top nav, content area fluid.
- **Content max-width:** `1440px`, with `24–28px` horizontal gutter.
- **Table rows:** 48px default, 40px compact.
- **Form field height:** 36px default, 32px compact.
- **Section padding:** 24px.
- **Two columns of dense tables is normal**, not cramped. Cashmere rewards density.

---

## States & interactions

| State | Treatment |
|---|---|
| **Hover (filled)** | +5% darken (`#094EFF` → `#003BD1`). No transform. |
| **Hover (ghost / tertiary)** | `neutral-950` (`#F2F2F2`) background appears. |
| **Pressed / active** | One step deeper darken (`accent-700` → `accent-800`). |
| **Focus** | 3px outer ring `rgba(9,78,255,0.28)` + inner 1px `#094EFF`. Always visible for keyboard. Ring **snaps in**, no animation. |
| **Disabled** | Text → `neutral-600`, fill → `neutral-900`. Opacity stays 1. Never grey via opacity. |
| **Selected row (table)** | `accent-100` background, text unchanged, left border `2px accent-600` optional. |
| **Loading (page)** | Horizontal 2px progress bar in `accent-600` at top. |
| **Loading (card)** | Skeleton shimmer 200ms. |
| **Empty** | Small monochrome line icon + sentence-case lede + one CTA. No cartoons. |

---

## Motion

Subtle and functional.

- **Default duration:** 150–200ms.
- **Default easing:** `cubic-bezier(0.2, 0, 0, 1)` (standard ease-out).
- **No bounces, no springs, no choreography.**
- **Allowed:** opacity fades, 4–8px Y translation, color crossfade, height slide for accordions.
- **Forbidden:** scale-up on hover, parallax, scroll-jacking, decorative entrance animations.
- **Focus ring** snaps without animation.
- **Toast** slides in from top-right, 200ms, dismisses after 4s unless action present.

---

## Components

### Button
- Heights: 36px default, 32px small, 40px large.
- Padding: `9px 16px` default, `7px 12px` small.
- Radius: `--radius-md` (6px).
- Variants: **primary** (filled accent), **secondary** (`#FFFFFC` fill, `#D1D1D1` border), **tertiary / ghost** (transparent), **negative** (filled negative), **negative-secondary** (negative text + border).
- Icon position: leading is default; trailing only for "next/forward" affordance (`→`).
- Label always sentence case.

### Input field
- Height: 36px default, 32px compact.
- Border: `1px solid #D1D1D1`. Focus border: `1px solid #094EFF` + focus ring.
- Background: `#FFFFFF` (pure white inside `#FFFFFC` cards).
- Label above (DM Sans 500 12/17), helper below (DM Sans 500 12/17 tertiary), error below in `negative-500`.
- Placeholder: `text-tertiary`.

### Tag (status)
- Uppercase, DM Sans 700 11/15, 0.04em letter-spacing.
- Padding: `3px 8px`. Radius: `--radius-sm` (4px) for status, `--radius-pill` for filter chips.
- Tones: `accent` · `success` · `warning` · `negative` · `neutral`. Each pairs subtle bg (`-50`/`-100`) with strong text (`-700`/`-800`).

### Chip (filter)
- DM Sans 500 12/16, padding `6px 12px`, radius pill.
- Inactive: `#FFFFFC` bg, `#D1D1D1` border, `#1B1B1B` text.
- Active: `#094EFF` bg, `#094EFF` border, white text.

### Card
- Background `#FFFFFC`, border `1px solid #E8E8E8`, radius 8px, no shadow.
- Padding `16–20px` (compact) or `24px` (default).
- Hover (interactive only): border → `#D1D1D1`, shadow → `--shadow-sm`.

### Data card (KPI)
- Same shell as card, padding 16px.
- Label `cm-datacard-title` (DM Sans 500 14/19, secondary).
- Value `cm-datacard-numeric` (DM Sans 700 24/29).
- Optional delta line: positive/negative arrow + percentage + comparison label.

### Table
- Header bg `#F2F2F2`, header text `cm-table-header` (DM Sans 600 12/17, secondary, 0.02em).
- Cell padding `12–14px`. Row height 48px default.
- Row hover: `#F2F2F2` bg.
- Selected row: `accent-100`.
- Numeric columns: tabular figures, right-aligned.
- ID columns: mono, secondary text color.
- Customer columns: 2-line (name `13/500 primary` + email `11 tertiary`).

### Top navigation
- Height 56px, white surface, `1px solid #E8E8E8` bottom border.
- Logo + product label + nav links + environment switch + user avatar.

### Left navigation
- Width 256px, white surface, `1px solid #E8E8E8` right border.
- Section labels in `cm-nav-section`.
- Active item: `accent-100` bg, `accent-700` text, optional 2px left accent strip.
- Items 36px tall, 12px padding, 8px gap to icon.

### Toast
- 320px wide, white bg, radius `--radius-lg`, `--shadow-lg`.
- Slides in top-right, auto-dismiss 4s.
- Icon left (status color), title `cm-toast-heading`, body `cm-toast-body`, close button top-right.

### Drawer
- Right-aligned, 460px wide on desktop.
- Scrim `--overlay-500` (no blur).
- Shadow `--shadow-xl`.
- Header 56px with title + close.

### Modal
- Centered, 480/640/800/960 widths.
- Radius `--radius-xl` (12px).
- Padding 24px.
- Footer right-aligned, primary CTA on the right.

---

## Patterns

### Status display
Always **state before details**. `SUCCESS · 17 Apr, 14:32 · UPI` — not the other way.

### Empty states
- Small monochrome icon (24px) + sentence-case explanation + one primary action.
- Never a cartoon. Never an apology.
- Example: *"No refunds yet. Issue a refund from any captured payment."* + **Open payments**.

### Confirmation
- Destructive actions get a modal: title states the outcome ("Refund ₹4,500?"), body explains the consequence, footer has **Cancel** (secondary, left) and the destructive verb (negative, right).
- Non-destructive saves: a toast, no modal.

### Page header
- `cm-page-heading` + `cm-page-subtext` (one line) + right-aligned action buttons.
- 20px gap between header block and first content card.

### Filter bar
- Search field on the left (with leading icon).
- Inline filter chips for common filters.
- "More filters" secondary button on the far right that opens a filter drawer.

---

## Anti-patterns

Things Cashmere explicitly **does not** do. If you see these, you're off-system.

- ✘ Gradient backgrounds in chrome.
- ✘ Emoji in product UI.
- ✘ Exclamation marks on success.
- ✘ Rounded-corner containers with a left-border accent stripe (drag-bar look).
- ✘ Colored or glowing shadows.
- ✘ Drop-shadowed buttons.
- ✘ Cartoon empty-state illustrations.
- ✘ Hand-drawn or sketchy icons.
- ✘ Backdrop blur in app chrome.
- ✘ Black mid-page CTA blocks (dark surfaces are reserved for footer + dark-mode toasts).
- ✘ Neumorphism, glassmorphism, skeuomorphism.
- ✘ Springy/bouncy animations.
- ✘ Title-case headings or buttons.
- ✘ "N/A" or blank cells (use `—`).
- ✘ Pure `#FFFFFF` page surface (use `#FFFFFC`).
- ✘ Body type smaller than 11px or larger than 14px.
- ✘ More than two corner radii in one component.
- ✘ More than one accent color per screen moment.

---

## Reference files in this project

| File | Contains |
|---|---|
| `colors_and_type.css` | All CSS variables + `.cm-*` typography classes (1:1 with Figma) |
| `assets/logo-cashfree-wordmark.svg`, `logo-cashfree-mark.svg` | Logo lockups |
| `assets/icons/` | Sample icon SVGs (Lucide is used as substitute set via CDN) |
| `preview/` | Color/type/component cards rendered in the Design System tab |
| `ui_kits/dashboard/` | Hi-fi merchant dashboard — top nav, left nav, payments table, detail drawer, settlements |
| `ui_kits/partner-marketplace/` | Cashfree Partner Marketplace — partner detail page (v2 IA) |

---

## Quick start (CSS)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="colors_and_type.css">
```

```html
<h1 class="cm-page-heading">Payments</h1>
<p class="cm-page-subtext">All payment attempts across methods · Last 24 hours</p>

<button style="background:var(--accent-600); color:var(--white);
  padding:9px 16px; border-radius:var(--radius-md); border:0;"
  class="cm-btn-text-lg">Create payment link</button>

<span class="cm-tag" style="background:var(--positive-50); color:var(--positive-800);
  padding:3px 8px; border-radius:var(--radius-sm);">SUCCESS</span>

<span class="cm-mono">order_Lx4yqR8VkM91</span>
```

---

*One accent. One alert. Neutral elsewhere. Density over decoration. Status before flourish.*
