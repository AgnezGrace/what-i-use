---
name: color-palettes-are-bullshit
description: Select and implement distinctive, context-driven UI color systems using curated tonal ramps, accessible semantic tokens, and explicit safeguards against generic AI aesthetics. Use for visual design, branding, theming, redesigns, and color audits.
---

# Color Palettes Are Bullshit

> A pile of fashionable HEX codes is a mood board. A color system has a job.

## 1. The premise

Fuck the autopilot palette. Choose color because the product, audience, content, and task justify it. Make every color earn its place. A catalog is a starting point, not an excuse to make every product look alike.

These names are internal creative shorthand. Keep them out of production UI, public copy, accessibility labels, and client-facing design tokens unless the brief explicitly asks for that wording. The jokes describe aesthetics, never people, social class, sexuality, religion, or suitability for a demographic.

## 2. Execute in this order

1. Read explicit user requirements, existing brand assets, platform constraints, and accessibility targets.
2. Identify the product's primary activity, lighting conditions, content type, and desired emotional register.
3. Preserve established brand colors when a redesign concerns unrelated features. Ask for direction when contradictory brand choices materially affect the result.
4. Select one principal tonal family or derive a fresh one. Treat the names as memory aids and the descriptions as the actual selection criteria.
5. Select the light or dark token set; honor system theme where the product supports it. Map the colors into semantic roles before building components.
6. Reserve an accent for action, focus, selection, or identity. Choose separate semantic colors for status when needed.
7. Render representative screens and component states; test contrast and inspect visual hierarchy before delivery.
8. Record the chosen palette, role overrides, and reasons for any deliberate exception in the agent's implementation summary.

## 3. Stop recycling the same damn color scheme

The following combinations are heuristic warnings about generic design, not proof that a human or an AI created a page.

| Reflex | Preferred response |
|---|---|
| Electric indigo-to-violet hero, especially #6366F1, #8B5CF6, #A855F7 | Choose a product-specific solid accent; reserve gradients for meaningful imagery. |
| Generic framework blue #3B82F6 applied indiscriminately | Derive a steel, ink, marine, or other brand-specific blue. |
| Cyan or acid-green glow on black with decorative blur | Use opaque, grounded surfaces and controlled accents. |
| Cream, beige, sepia and terracotta as the automatic alternative to purple | Start with neutral or cool surfaces; warm families require deliberate direction. |
| Gradient headlines, gradient buttons, rainbow borders and repeated mesh backgrounds | Use solid typography and flat component fills. |
| Pink-purple-blue pastel SaaS wallpaper | Define a single coherent tonal hierarchy. |
| Transparent cards over noisy colored backgrounds | Use stable, legible surfaces. |
| Identical accent on every badge, icon, outline and paragraph | Reserve saturation for meaningful priority. |

A requested gradient, warm palette, vivid campaign, or established brand may override these defaults. Evaluate the composition as a whole. Replacing purple with another fashion trend while keeping the same visual template solves nothing.

## 4. Choose according to the product

- Business, finance, administration: matte surfaces, modest chroma, stable contrast, clear status distinctions. Start with I'm Rich, Corporate Hostage, My Lawyer Said No, Tax Evasion, or Trust Issues.
- Editorial, publishing, galleries: preserve content as the dominant visual element; use an intentional accent or a true monochrome family.
- Casual and creative: expressive composition with decisive accent placement; use saturated color as a focal point instead of an ambient wash.
- Nature and wellness: Green Flag or Touch Grass; keep the interface functional and check green against status colors.
- Dark fantasy, dramatic brands: Lucifer Is God or Villain with a Pension; retain high-contrast text and neutral breathing space.
- Technical and privacy products: Cold-Blooded, Please Delete My History, Emotionally Unavailable, or Corporate Hostage.
- Food and craft: warm colors are valid when they serve the subject or explicit art direction.
- Celebration and expressive identity: the rainbow family is an opt-in exception with a neutral functional foundation.

## 5. Tonal ramps and semantic roles

Each ordinary palette has seven opaque sRGB stops in increasing relative luminance, T1 (darkest) through T7 (lightest). The middle stops are interpolated between selected anchors; perceptual spacing is approximate. A ramp is a set of solid choices, not a requirement to render a gradient.

The following role tables include suggested values for both themes. `BG` is the canvas, `Surface` is an opaque panel, `Text` is ordinary foreground, `Muted` is secondary foreground, `Accent` is a link/action/selected-state candidate, `On accent` is text on a solid accent button, `Border` is a functional boundary, and `Focus` is a focus-ring candidate. Decorative separators may be subtler if their function is purely decorative.

Apply tokens to components rather than scattering literal colors. Keep neutral and accent roles separate even if they happen to share a hue. For a monochrome family, use spacing, weight, outline and position to express hierarchy. A focus ring should have a visible offset on filled controls. Use native system high-contrast support and preserve keyboard focus.

## 6. Catalog

### 01. I'm Rich

`im-rich` — Matte graphite with restrained green-gray undertones; private banking, luxury goods, executive tools.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#111918` | `#1F2A28` | `#2D3B37` | `#52625C` | `#778A80` | `#AEBBB4` | `#E5ECE8` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E5ECE8` | `#FFFFFF` | `#111918` | `#2D3B37` | `#2D3B37` | `#FFFFFF` | `#778A80` | `#2D3B37` |
| Dark | `#111918` | `#1F2A28` | `#E5ECE8` | `#AEBBB4` | `#AEBBB4` | `#000000` | `#778A80` | `#AEBBB4` |

### 02. Lucifer Is God

`lucifer-is-god` — Matte oxblood and wine; dark editorial, fantasy, dramatic identity.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#1D1015` | `#3A1A21` | `#57232D` | `#803E4A` | `#A85A66` | `#CE9DA5` | `#F4E0E4` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F4E0E4` | `#FFFFFF` | `#1D1015` | `#57232D` | `#57232D` | `#FFFFFF` | `#A85A66` | `#57232D` |
| Dark | `#1D1015` | `#3A1A21` | `#F4E0E4` | `#CE9DA5` | `#CE9DA5` | `#000000` | `#A85A66` | `#CE9DA5` |

### 03. Green Flag

`green-flag` — Deep fern and jade leaf; wellness, environmental products, calm workspaces.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#101F19` | `#1A3A2A` | `#23553C` | `#437C5C` | `#63A27B` | `#A4CAB2` | `#E5F2E8` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E5F2E8` | `#FFFFFF` | `#101F19` | `#23553C` | `#23553C` | `#FFFFFF` | `#437C5C` | `#23553C` |
| Dark | `#101F19` | `#1A3A2A` | `#E5F2E8` | `#A4CAB2` | `#A4CAB2` | `#000000` | `#63A27B` | `#A4CAB2` |

### 04. Red Flag

`red-flag` — Dry brick red with a clear, bold character; editorial and fashion.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#251517` | `#4C2225` | `#742F33` | `#9C5456` | `#C57878` | `#DEAEAD` | `#F8E4E2` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F8E4E2` | `#FFFFFF` | `#251517` | `#742F33` | `#742F33` | `#FFFFFF` | `#9C5456` | `#742F33` |
| Dark | `#251517` | `#4C2225` | `#F8E4E2` | `#DEAEAD` | `#DEAEAD` | `#000000` | `#C57878` | `#DEAEAD` |

### 05. Corporate Hostage

`corporate-hostage` — Cool steel blue-gray; business tools, administration and reports.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#141C25` | `#243442` | `#354C60` | `#5C7488` | `#829DB0` | `#B4C6D2` | `#E7EFF4` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E7EFF4` | `#FFFFFF` | `#141C25` | `#354C60` | `#354C60` | `#FFFFFF` | `#5C7488` | `#354C60` |
| Dark | `#141C25` | `#243442` | `#E7EFF4` | `#B4C6D2` | `#B4C6D2` | `#000000` | `#829DB0` | `#B4C6D2` |

### 06. Emotionally Unavailable

`emotionally-unavailable` — Neutral graphite; technical writing, productivity, monochrome branding.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#141518` | `#26282C` | `#383B40` | `#60646A` | `#898D93` | `#BBBEC2` | `#EDEEF0` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#EDEEF0` | `#FFFFFF` | `#141518` | `#383B40` | `#383B40` | `#FFFFFF` | `#60646A` | `#383B40` |
| Dark | `#141518` | `#26282C` | `#EDEEF0` | `#BBBEC2` | `#BBBEC2` | `#000000` | `#898D93` | `#BBBEC2` |

### 07. Divorced at Midnight

`divorced-at-midnight` — Ink navy; archives, serious reading environments, finance.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#101823` | `#1B2C3E` | `#263F59` | `#4C6882` | `#7290AB` | `#ABBED0` | `#E4ECF5` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E4ECF5` | `#FFFFFF` | `#101823` | `#263F59` | `#263F59` | `#FFFFFF` | `#4C6882` | `#263F59` |
| Dark | `#101823` | `#1B2C3E` | `#E4ECF5` | `#ABBED0` | `#ABBED0` | `#000000` | `#7290AB` | `#ABBED0` |

### 08. Tax Evasion

`tax-evasion` — Muted evergreen with mineral undertones; financial dashboards and private offices.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#141D18` | `#28372D` | `#3D5142` | `#627663` | `#879C84` | `#B8C5B4` | `#E8EEE5` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E8EEE5` | `#FFFFFF` | `#141D18` | `#3D5142` | `#3D5142` | `#FFFFFF` | `#627663` | `#3D5142` |
| Dark | `#141D18` | `#28372D` | `#E8EEE5` | `#B8C5B4` | `#B8C5B4` | `#000000` | `#879C84` | `#B8C5B4` |

### 09. Trust Issues

`trust-issues` — Dusty petroleum teal; analytics and restrained contemporary branding.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#101D20` | `#1C383C` | `#275359` | `#4F7A7E` | `#77A1A3` | `#ACC8C9` | `#E2F0EF` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E2F0EF` | `#FFFFFF` | `#101D20` | `#275359` | `#275359` | `#FFFFFF` | `#4F7A7E` | `#275359` |
| Dark | `#101D20` | `#1C383C` | `#E2F0EF` | `#ACC8C9` | `#ACC8C9` | `#000000` | `#77A1A3` | `#ACC8C9` |

### 10. Dead Inside

`dead-inside` — Cold ash; minimalist studios, documentation, utilitarian products.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#191B1E` | `#2E3236` | `#43484E` | `#6F747B` | `#9BA1A8` | `#C6CACE` | `#F1F3F5` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F1F3F5` | `#FFFFFF` | `#191B1E` | `#43484E` | `#43484E` | `#FFFFFF` | `#6F747B` | `#43484E` |
| Dark | `#191B1E` | `#2E3236` | `#F1F3F5` | `#C6CACE` | `#9BA1A8` | `#000000` | `#9BA1A8` | `#9BA1A8` |

### 11. The Ocean Owes Me Money

`the-ocean-owes-me-money` — Deep marine blue; travel, mapping, maritime editorial.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#10212B` | `#1A3A4C` | `#23546C` | `#467A92` | `#68A0B9` | `#A4C8D8` | `#E1F1F7` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E1F1F7` | `#FFFFFF` | `#10212B` | `#23546C` | `#23546C` | `#FFFFFF` | `#467A92` | `#23546C` |
| Dark | `#10212B` | `#1A3A4C` | `#E1F1F7` | `#A4C8D8` | `#A4C8D8` | `#000000` | `#68A0B9` | `#A4C8D8` |

### 12. Romance Is a Scam

`romance-is-a-scam` — Muted rose with cool undertones; romance publishing, apparel and beauty.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#241923` | `#452C3B` | `#664053` | `#8E6578` | `#B68A9D` | `#D5B8C6` | `#F4E7EE` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F4E7EE` | `#FFFFFF` | `#241923` | `#664053` | `#664053` | `#FFFFFF` | `#8E6578` | `#664053` |
| Dark | `#241923` | `#452C3B` | `#F4E7EE` | `#D5B8C6` | `#D5B8C6` | `#000000` | `#B68A9D` | `#D5B8C6` |

### 13. My Therapist Quit

`my-therapist-quit` — Quiet lavender-gray, predominantly slate rather than electric violet; journals and contemplative interfaces.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#201C27` | `#383243` | `#51475F` | `#766C87` | `#9C91AF` | `#C6BED2` | `#F0EAF5` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F0EAF5` | `#FFFFFF` | `#201C27` | `#51475F` | `#51475F` | `#FFFFFF` | `#766C87` | `#51475F` |
| Dark | `#201C27` | `#383243` | `#F0EAF5` | `#C6BED2` | `#C6BED2` | `#000000` | `#9C91AF` | `#C6BED2` |

### 14. Villain with a Pension

`villain-with-a-pension` — Dusty aubergine; theatrical luxury, fiction and art portfolios.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#241826` | `#412A41` | `#5E3B5C` | `#83607F` | `#A885A2` | `#CDB6C8` | `#F2E6EF` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F2E6EF` | `#FFFFFF` | `#241826` | `#5E3B5C` | `#5E3B5C` | `#FFFFFF` | `#83607F` | `#5E3B5C` |
| Dark | `#241826` | `#412A41` | `#F2E6EF` | `#CDB6C8` | `#CDB6C8` | `#000000` | `#A885A2` | `#CDB6C8` |

### 15. The Moon Has Receipts

`the-moon-has-receipts` — Lunar silver-blue; reading apps, research and restrained futuristic interfaces.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#181F29` | `#2E3A4A` | `#45566C` | `#708298` | `#9AAEC3` | `#C5D1DE` | `#F0F4F9` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F0F4F9` | `#FFFFFF` | `#181F29` | `#45566C` | `#45566C` | `#FFFFFF` | `#708298` | `#45566C` |
| Dark | `#181F29` | `#2E3A4A` | `#F0F4F9` | `#C5D1DE` | `#9AAEC3` | `#000000` | `#9AAEC3` | `#9AAEC3` |

### 16. Touch Grass

`touch-grass` — Matte moss; nature, gardens and outdoors. Olive undertones require intentional warmth.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#1A2218` | `#313E26` | `#485A35` | `#6E8054` | `#93A572` | `#BFCBA8` | `#EBF1DE` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#EBF1DE` | `#FFFFFF` | `#1A2218` | `#485A35` | `#485A35` | `#FFFFFF` | `#6E8054` | `#485A35` |
| Dark | `#1A2218` | `#313E26` | `#EBF1DE` | `#BFCBA8` | `#BFCBA8` | `#000000` | `#93A572` | `#BFCBA8` |

### 17. Coffee Is a Personality

`coffee-is-a-personality` — Roasted brown; food and craft. Explicit warm-theme opt-in.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#261B18` | `#47332C` | `#684B40` | `#8C6A5C` | `#B08A78` | `#D2B8AC` | `#F3E6DF` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F3E6DF` | `#FFFFFF` | `#261B18` | `#684B40` | `#684B40` | `#FFFFFF` | `#8C6A5C` | `#684B40` |
| Dark | `#261B18` | `#47332C` | `#F3E6DF` | `#D2B8AC` | `#D2B8AC` | `#000000` | `#B08A78` | `#D2B8AC` |

### 18. Rent Is Due

`rent-is-due` — Dry copper and clay; independent retail and maker brands. Explicit warm-theme opt-in.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#291A15` | `#563225` | `#824A35` | `#A56C52` | `#C88D70` | `#DFBAA6` | `#F6E7DB` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F6E7DB` | `#FFFFFF` | `#291A15` | `#824A35` | `#824A35` | `#FFFFFF` | `#A56C52` | `#824A35` |
| Dark | `#291A15` | `#563225` | `#F6E7DB` | `#DFBAA6` | `#DFBAA6` | `#000000` | `#C88D70` | `#DFBAA6` |

### 19. The Sun Is a Liability

`the-sun-is-a-liability` — Restrained ochre and amber; signage, editorial and outdoor goods. Explicit warm-theme opt-in.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#292113` | `#513F1E` | `#795D28` | `#A08043` | `#C6A45E` | `#DEC99A` | `#F7EED7` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F7EED7` | `#FFFFFF` | `#292113` | `#795D28` | `#795D28` | `#FFFFFF` | `#A08043` | `#795D28` |
| Dark | `#292113` | `#513F1E` | `#F7EED7` | `#DEC99A` | `#DEC99A` | `#000000` | `#C6A45E` | `#DEC99A` |

### 20. Cold-Blooded

`cold-blooded` — Glacial cyan with blue mineral shadows; scientific tools and clean technical products.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#102329` | `#1C404C` | `#275E70` | `#548C9C` | `#80B9C8` | `#B3D7E0` | `#E6F5F7` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E6F5F7` | `#FFFFFF` | `#102329` | `#275E70` | `#275E70` | `#FFFFFF` | `#548C9C` | `#275E70` |
| Dark | `#102329` | `#1C404C` | `#E6F5F7` | `#B3D7E0` | `#80B9C8` | `#000000` | `#80B9C8` | `#80B9C8` |

### 21. My Lawyer Said No

`my-lawyer-said-no` — Blue-black with neutral pewter; legal products and institutional records.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#161C22` | `#2A333C` | `#3E4A55` | `#68747E` | `#929DA7` | `#BEC5CC` | `#E9EDF1` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E9EDF1` | `#FFFFFF` | `#161C22` | `#3E4A55` | `#3E4A55` | `#FFFFFF` | `#68747E` | `#3E4A55` |
| Dark | `#161C22` | `#2A333C` | `#E9EDF1` | `#BEC5CC` | `#929DA7` | `#000000` | `#929DA7` | `#929DA7` |

### 22. Please Delete My History

`please-delete-my-history` — Smoky desaturated blue-green; privacy, security and quiet utility interfaces.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#131F22` | `#243639` | `#364C50` | `#5E7476` | `#859B9B` | `#B6C5C4` | `#E7EFEE` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E7EFEE` | `#FFFFFF` | `#131F22` | `#364C50` | `#364C50` | `#FFFFFF` | `#5E7476` | `#364C50` |
| Dark | `#131F22` | `#243639` | `#E7EFEE` | `#B6C5C4` | `#B6C5C4` | `#000000` | `#859B9B` | `#B6C5C4` |

### 23. The Artist Is Broke

`the-artist-is-broke` — Raspberry red, crisp and expressive; creative portfolios and cultural events.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#291422` | `#512438` | `#79334E` | `#9E5471` | `#C37694` | `#DEAEC1` | `#F9E5EE` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F9E5EE` | `#FFFFFF` | `#291422` | `#79334E` | `#79334E` | `#FFFFFF` | `#9E5471` | `#79334E` |
| Dark | `#291422` | `#512438` | `#F9E5EE` | `#DEAEC1` | `#DEAEC1` | `#000000` | `#C37694` | `#DEAEC1` |

### 24. White Room, No Witnesses

`white-room-no-witnesses` — True neutral grayscale; high contrast editorial, galleries and writing.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#141414` | `#2A2A2A` | `#414141` | `#6C6C6C` | `#969696` | `#C6C6C6` | `#F5F5F5` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F5F5F5` | `#FFFFFF` | `#141414` | `#414141` | `#414141` | `#FFFFFF` | `#6C6C6C` | `#414141` |
| Dark | `#141414` | `#2A2A2A` | `#F5F5F5` | `#C6C6C6` | `#969696` | `#000000` | `#969696` | `#969696` |

### 25. The Deadline Is Fiction

`the-deadline-is-fiction` — Dry cobalt with a restrained mineral character; creative tools and editorial.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#172239` | `#263860` | `#354F86` | `#5C75A8` | `#829BC9` | `#B5C4E1` | `#E8EEF9` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#E8EEF9` | `#FFFFFF` | `#172239` | `#354F86` | `#354F86` | `#FFFFFF` | `#5C75A8` | `#354F86` |
| Dark | `#172239` | `#263860` | `#E8EEF9` | `#B5C4E1` | `#B5C4E1` | `#000000` | `#829BC9` | `#B5C4E1` |

### 26. The Vampire Has an HR Department

`the-vampire-has-an-hr-department` — Muted burgundy-gray; dark business, fiction and formal editorial.

| T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|---|---|---|---|---|---|
| `#221B20` | `#392A30` | `#503941` | `#785A64` | `#9F7C87` | `#C8B2B8` | `#F0E7EA` |

| Theme | BG | Surface | Text | Muted | Accent | On accent | Border | Focus |
|---|---|---|---|---|---|---|---|---|
| Light | `#F0E7EA` | `#FFFFFF` | `#221B20` | `#503941` | `#503941` | `#FFFFFF` | `#9F7C87` | `#503941` |
| Dark | `#221B20` | `#392A30` | `#F0E7EA` | `#C8B2B8` | `#C8B2B8` | `#000000` | `#9F7C87` | `#C8B2B8` |

### 27. If You're Gay (or Just Like Rainbows)

`if-youre-gay` — Deliberate high-chroma rainbow for expressive campaigns, identity and celebratory artwork. The title is a joke about a visual motif, never a rule about anyone’s identity.

| Hue | T1 | T2 | T3 (vivid) | T4 | T5 |
|---|---|---|---|---|---|
| Red | `#361019` | `#942634` | `#F13C50` | `#F88C99` | `#FFDDE2` |
| Orange | `#381D10` | `#90441A` | `#E96A24` | `#F4A77A` | `#FFE4D1` |
| Yellow | `#352B0A` | `#8C730E` | `#E3BB12` | `#F1D668` | `#FFF2BE` |
| Green | `#102C1B` | `#1A6434` | `#249B4E` | `#7EC996` | `#D9F7DF` |
| Blue | `#11243A` | `#1A507C` | `#237DBD` | `#7EB5DE` | `#D8EDFF` |
| Violet | `#2D1536` | `#682C73` | `#A343B0` | `#CC90D4` | `#F5DEF9` |

Use White Room, No Witnesses as the neutral functional base. Apply the six hues to intentional artwork, segmented graphics, expressive branding, or explicitly requested rainbow compositions. For rainbow text or controls, calculate contrast on the actual local background; choose a solid fallback for legibility. Pair each data series with a label, marker, or pattern. Keep a single functional action color per screen unless the workflow genuinely needs multiple roles. The spectrum supplies six parallel dark-to-light ramps rather than pretending that a sequence of different hues is a tonal scale.

## 7. Status colors are language

Give error, warning, success, and information independent semantic roles when the product needs them. A green brand does not automatically mean success. A red brand does not make every action destructive. Use visible text or recognizable symbols with status indicators, and pair destructive actions with their actual risk. Choose appropriate status colors per theme and test them against the surfaces where they appear. The catalog does not prescribe universal status colors because these depend on the selected theme and workflow.

## 8. Interaction and contrast contract

- Target a minimum contrast ratio of 4.5:1 for normal text, 3:1 for qualifying large text, and 3:1 for essential non-text control boundaries and indicators against adjacent colors, following WCAG 2.2 AA criteria and their applicable exceptions.
- Measure actual foreground/background pairs after opacity, overlays, gradient compositing, and state changes. Test links, placeholders when meaningful, secondary text, focus, errors, selected states, disabled behavior and visited states where applicable.
- Keep a visible non-color cue for links in text, selection, validation, and data meaning. Preserve system high-contrast modes.
- Use a tested solid fill for buttons. For hover and pressed states, adjust the fill or outline, recalculate text contrast and preserve the state cue. Never assume a neighboring ramp stop automatically passes.
- Distinguish focus rings from their surrounding colors; use offset or double rings where necessary. Test the rendered focus state.
- Inspect dark mode independently; reversing a light ramp mechanically is insufficient.
- Use flat matte color for business UI; avoid glow, false depth, decorative gradients, and shiny surface effects unless explicitly relevant.

## 9. Implementation example

```css
.app {
  background: var(--color-background);
  color: var(--color-text);
}
.panel { background: var(--color-surface); }
.secondary { color: var(--color-muted); }
.action {
  background: var(--color-accent);
  color: var(--color-on-accent);
  border: 1px solid var(--color-accent);
}
.control { border: 1px solid var(--color-border); }
:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 3px;
}
```

Test the surrounding background at each focus location. Use semantic HTML, appropriate roles and existing component interaction behavior. Define separate state tokens as required. The sample illustrates role mapping; it is not a complete component library.

## 10. Verification and acceptance

- Confirm palette selection is grounded in the brief and brand.
- Confirm all tonal stops increase in relative luminance and CSS/JSON values match the catalog.
- Check every actual normal text pair against 4.5:1, and every applicable essential boundary or focus pair against 3:1.
- Review a dense work screen, a form, a dialog, an empty state, and a content screen in the relevant modes and widths.
- Check hover, pressed, focus, error, success, selection and disabled states when they exist.
- Review with grayscale and color-vision simulation where information depends on color; supply redundant cues.
- Confirm default framework colors are replaced where the product has a defined identity, while preserving user-specified brand values.
- Review the interface without decorative color: the hierarchy and task path should remain evident.
- Report measured results and untested states separately. A passing swatch test does not certify a complete application.

## 11. Final instruction

A color palette is bullshit when it is selected by habit, pasted into a template, and called a design system. Make color communicate the product's priorities. The user came to do something. Let them do it.
