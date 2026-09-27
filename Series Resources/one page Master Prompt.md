Act as a Senior Technical Information Designer specializing in AEC, BIM Automation, and Computational Design.

I have attached a PDF and/or video for an episode of my technical series, "BIM && YOU."
Your task is to analyze the workflow and create Page 1 (the Cover Page) as a high-level, visually scannable 16:9 (1920x1080px) "One-Pager Cheat Sheet" for LinkedIn.

The goal is for an engineer or BIM specialist scrolling LinkedIn to immediately understand the core problem, the conceptual logic, and the final payoff in 5 seconds—without squinting at tiny text or reading the same information twice.

### 1. CONTENT & STORYTELLING RULES (HIGH-LEVEL & SEQUENTIAL)
- **Conceptual Over Literal:** Focus on the high-level problem-solving idea and workflow logic. Do NOT copy-paste raw sheet numbers, every minor node label, or cluttered UI text verbatim. Summarize the engineering intent of each step clearly.
- **Zero File/Consultant Names:** Strictly omit any Revit model file names (e.g., .rvt strings), company names, or "bim consultant" references visible in the screenshots.
- **Zero Redundancy:** Never repeat the same parameter, view name, or outcome in multiple steps. Each step must move the story forward linearly.

Structure the page into these 6 sequential elements:
1. **Series Header:**
   - Title: "BIM && YOU | EP.[#]: [Episode Title]"
   - Subtitle: A bold, 1-sentence high-level summary of the problem this workflow solves.
2. **STEP 1 — The Problem (Manual Bottleneck):**
   - Explain the core manual pain point in native Revit and why doing it by hand wastes time or causes coordination errors (2–3 concise bullet points max).
3. **STEP 2 — The Inputs (What You Feed It):**
   - List only the essential high-level user inputs required to run the workflow (e.g., Target Category, Filter Parameter, Target View/Set Names).
4. **STEP 3 — The Core Logic (How It Works):**
   - A clean, 3-to-4 stage visual flow diagram showing the high-level automation concept (e.g., Collect Elements ➔ Filter by Rule ➔ Combine Data ➔ Create in Revit). Mention only the primary nodes/concepts that drive the logic.
5. **STEP 4 — The Result (The Automated Output):**
   - Show the final state achieved in a single click and the practical payoff for the BIM team.
6. **Footer Bar:**
   - Left: "BIM && YOU // Workflow Cheat Sheet"
   - Right: A high-contrast badge reading "Swipe for the step-by-step breakdown" (strictly NO directional arrows, as swipe direction varies by language/interface).

### 2. STRICT READABILITY, CONTRAST & ANTI-OVERFLOW RULES (1920x1080 HTML/TAILWIND)
Output a complete, self-contained 1920x1080px HTML/Tailwind CSS file:
- **ZERO BOX OVERFLOW (CRITICAL LAYOUT GUARDRAIL):**
  * Sub-cards/inner boxes must NEVER bleed or overflow outside the bottom border of their parent STEP card.
  * Body container must use `w-[1920px] h-[1080px] p-6 flex flex-col gap-4 overflow-hidden`.
  * The `<main>` grid must use `flex-1 min-h-0 grid grid-cols-12 grid-rows-2 gap-5`.
  * Every parent `<section>` card MUST use `flex flex-col justify-between p-5 overflow-hidden min-h-0`. Do NOT wrap all children in a single unconstrained `<div>`.
  * Every inner sub-card grid MUST be a direct flex child using `flex-1 min-h-0 grid gap-3.5` so sub-boxes stay 100% contained inside the parent card with clean bottom padding.
- **High-Contrast Color Rules:**
  * Background Canvas: `#1A1D21` (Brand Black) with `#23272E` for step cards and `#16191D` for inner sub-cards.
  * Structural Borders ONLY: `#666666` (Brand Gray). **NEVER use `#666666` for readable body text or explanations.**
  * Primary Text: `#FFFFFF` (Crisp White) for all headings, bullet points, and descriptions.
  * Technical Accents & Badges: `#38BDF8` (Electric Blue) for Step numbers, internal flow arrows, key technical terms, and the footer callout (use dark `#1A1D21` text inside `#38BDF8` badges for maximum contrast).
- **LinkedIn-Friendly Typography (Balanced to Fit Without Overflow):**
  * Main Title: `text-4xl` to `text-5xl`, bold sans-serif (Inter).
  * Step Headers: `text-2xl` to `text-3xl`, bold White with high-contrast Electric Blue step badges.
  * Body & Sub-card Text: `text-base` to `text-lg` (`16px–18px`) in crisp White (`#FFFFFF`) with `leading-snug`.
  * Technical Terms/Nodes: `text-sm` to `text-base` (`14px–16px`) in monospace (`JetBrains Mono`) tinted in Electric Blue (`#38BDF8`).

### 3. STRICT ANTI-SLOP GUARDRAILS
- ZERO AI buzzwords ("revolutionize," "unleash," "game-changer," "seamless," "elevate," "empower," "supercharge"). Use direct, peer-to-peer engineering language.
- ZERO off-brand colors, decorative gradients, or emojis.

Output the complete, self-contained 1920x1080px HTML/Tailwind CSS code block.