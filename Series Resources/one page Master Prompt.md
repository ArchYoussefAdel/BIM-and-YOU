Act as a Senior Technical Information Designer specializing in AEC, BIM Automation, and Computational Design.

I have attached a PDF and/or video for an episode of my technical series, "BIM && YOU."
Your task is to analyze the workflow and create Page 1 (the Cover Page) as a high-level, visually scannable 16:9 (1920x1080px) "One-Pager Cheat Sheet" for LinkedIn.

The goal is for an engineer or BIM specialist scrolling LinkedIn to immediately understand the core problem, the technical inputs/nodes, and the final payoff in 5 seconds—with big, hooky typography, high technical signal, and zero tiny text.

### 1. CONTENT, MICRO-COPY & VISUAL HOOK RULES
- **Telegraphic Micro-Copy (STRICT WORD CAPS):**
  * Sub-card Titles: **2 to 4 words max** (punchy and direct, e.g., `"Loaded" — But Where?!`, `Find DWGs`).
  * Sub-card Descriptions: **6 to 10 words max** (1 to 2 short lines). Cut filler prose and articles. Never write multi-sentence paragraphs inside sub-cards.
- **Single-Line Technical Callout Boxes (NO Micro-Labels):**
  * Every sub-card in Steps 2 and 3 MUST include a centered monospace Technical Callout Box (`bg-[#23272E] border-2 border-[#38BDF8] text-[#38BDF8]`) containing **ONLY the single-line technical value** (e.g., `OST_Sheets`, `Drawn By == "AB"`, `ImportInstance`, `WriteText + OpenView`).
  * **STRICTLY FORBIDDEN:** Never put tiny secondary headers or category labels inside the technical callout box. Keep it to 1 large, high-impact line of code/node text (`text-xl` to `text-2xl`).
  * Never let technical node names truncate with `...`—use concise, recognizable node/API names that fit cleanly on a single line.
- **Conceptual Over Literal:** Focus on the high-level engineering logic. Strictly omit raw sheet numbers, Revit `.rvt` file names, company names, or "bim consultant" references visible in screenshots.
- **Zero Redundancy:** Never repeat the same parameter, view name, or outcome in multiple steps. Each step must move the story forward linearly.

Structure the page into these 6 sequential elements:
1. **Series Header:**
   - Title: "BIM && YOU | EP.[#]: [Episode Title]"
   - Subtitle: A bold, 1-sentence hook (max 15 words) summarizing what the workflow achieves in one click.
2. **STEP 1 — The Problem (Manual Bottleneck):**
   - 3 horizontal sub-cards showing the native Revit pain points. Each card must have a bold 2–4 word title, a right-aligned technical status pill (`text-base`), and a single-line description (max 10 words).
3. **STEP 2 — The Inputs (What You Feed It):**
   - 3 vertical sub-cards showing the essential inputs. Each card must feature: Top Input badge (`text-base`), bold title (`text-2xl`), a centered single-line Technical Callout Box (`text-xl` to `text-2xl` bold monospace), and a 6–10 word bottom explanation (`text-lg`).
4. **STEP 3 — The Core Logic (How It Works):**
   - 4 vertical sub-cards showing the 4-stage computational pipeline. Each card must feature: Stage number + arrow (`➔`), bold 2–3 word title (`text-2xl`), a centered single-line Technical Callout Box (`text-xl` bold monospace), and a 6–10 word bottom explanation (`text-lg`).
5. **STEP 4 — The Result (The Automated Output):**
   - 3 horizontal sub-cards showing the automated payoff. Each card must have a bold 2–4 word title, a right-aligned payoff pill (`text-base`), and a single-line description (max 10 words).
6. **Footer Bar:**
   - Left: "BIM && YOU // Workflow Cheat Sheet"
   - Right: A high-contrast badge reading "Swipe for the step-by-step breakdown" (strictly NO directional arrows).

### 2. STRICT READABILITY, CONTRAST & ANTI-OVERFLOW RULES (1920x1080 HTML/TAILWIND)
Output a complete, self-contained 1920x1080px HTML/Tailwind CSS file:
- **STRICT MINIMUM FONT SIZE GUARDRAIL (NO SMALL TEXT):**
  * **NEVER use `text-xs` (`12px`), `text-sm` (`14px`), or custom pixel sizes below `16px` anywhere in the HTML.**
  * Minimum allowed text size for any badge or tag is `text-base` (`16px`).
  * Main Title: `text-5xl` (`48px`), extrabold sans-serif (`Inter`).
  * Header Subtitle: `text-xl` (`20px`), bold White.
  * Step Headers: `text-3xl` (`30px`), extrabold White with `text-lg` Electric Blue step badges.
  * Sub-card Titles: `text-2xl` (`24px`), extrabold White.
  * Technical Callout Boxes (Steps 2 & 3): `text-xl` (`20px`) to `text-2xl` (`24px`), extrabold monospace (`JetBrains Mono`) in `#38BDF8`.
  * Status Pills & Badges: `text-base` (`16px`), bold monospace (`JetBrains Mono`).
  * Sub-card Micro-Copy: `text-lg` (`18px`), medium/semibold White (`#FFFFFF`) with `leading-snug`.
- **ZERO BOX OVERFLOW (CRITICAL LAYOUT GUARDRAIL):**
  * Sub-cards/inner boxes must NEVER bleed or overflow outside the bottom border of their parent STEP card.
  * Body container must use `w-[1920px] h-[1080px] p-6 flex flex-col gap-4 overflow-hidden`.
  * The `<main>` grid must use `flex-1 min-h-0 grid grid-cols-12 grid-rows-2 gap-5`.
  * Every parent `<section>` card MUST use `flex flex-col justify-between p-5 overflow-hidden min-h-0`. Do NOT wrap all children in a single unconstrained `<div>`.
  * Every inner sub-card grid MUST be a direct flex child using `flex-1 min-h-0 grid gap-3.5` so sub-boxes stay 100% contained inside the parent card.
- **High-Contrast Color & Visual Anchor Rules:**
  * Background Canvas: `#1A1D21` (Brand Black) with `#23272E` for step cards and `#16191D` for inner sub-cards.
  * Sub-card Left Accent: Add `border-l-4 border-l-[#38BDF8]` to inner sub-cards so the eye locks onto each block immediately.
  * Structural Borders ONLY: `#666666` (Brand Gray). **NEVER use `#666666` for readable body text or explanations.**
  * Primary Text: `#FFFFFF` (Crisp White) for all headings, micro-copy, and descriptions.
  * Technical Accents & Badges: `#38BDF8` (Electric Blue) for Step numbers, flow arrows, technical callout boxes, and the footer callout (use `#1A1D21` dark text inside solid `#38BDF8` badges).

### 3. STRICT ANTI-SLOP GUARDRAILS
- ZERO AI buzzwords ("revolutionize," "unleash," "game-changer," "seamless," "elevate," "empower," "supercharge"). Use direct, peer-to-peer engineering language.
- ZERO off-brand colors, decorative gradients, or emojis.

Output the complete, self-contained 1920x1080px HTML/Tailwind CSS code block.