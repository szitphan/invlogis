---
name: figma-design-system
description: Build a design system into the open Figma file — tokens, text styles, COMPONENT_SETs with variants, and the doc pages. Use when someone says "sinh design system", "dựng DS", "làm bộ token + component", or wants a kit they can instance from.
allowed-tools: Read, Glob, Grep, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_design_system
user-invocable: true
argument-hint: "<product name> [primary hex] [light|dark|both]"
---
<!-- Licensed to test.innvie@gmail.com — Order 3D3A2HZRY -->

# /figma-design-system — a kit the file can keep‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Read the connection gate in `../reqwise-diagram-rules.md` first (§ 5, *Before
anything else: is the write path open?*): plugin connected, one window,
`figma_status` before anything else, and a dry run is NOT a connection probe.
The rest of that file is about diagrams; a design system is not one, so the
steps below replace its drawing rules.

Field tables and defaults: `figma_docs(section="designsystem", level="cheat")`.
Read that once before your first plan. The full section only when a finding
needs explaining.

## The one rule that makes or breaks this‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

**`plan` decides. `generate` executes that plan and infers nothing.** Never
hand-write a plan. Never put a fallback colour inside `generate`. A UI can put
`generate` behind a button only because this is true.

```
figma_status()
figma_design_system({ op: "plan", source, brief, select?, options? })
# → ask every entry of `questions`, plan again until it is empty
# → show findings + estimate, get a yes
figma_design_system({ op: "generate", plan })   # the object plan returned, unmodified
figma_design_system({ op: "audit" })            # must be ≈ 1.00
```

Omit `stage` to run all six (each is its own round trip). Pass one
(`tokens` | `typography` | `atoms` | `molecules` | `organisms` | `docs`)
when a full run would hit the write timeout — then continue with the same plan.

## Step 1 — the brand colour, then let the plan ask‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

**Brand colour** is the one thing to ask before any call: `brief.brand.primary`
is required and plan refuses without it. Never pick one.

Then plan with what you have — product description included, it drives the
recommendations:

```js
figma_design_system({ op: "plan", source: "brief",
  brief: { name, product, brand: { primary } },
  options: { pageStrategy: "single" } }) // Starter is 3 pages/file
```

**Do not keep your own list of questions.** The plan returns `questions` —
theme, style, platforms, scope (which components), docs — only the ones the
input has not answered, and `generate` refuses the plan while any are open.

For each question, ask the user with `AskUserQuestion`:
- the `recommended` option first, marked recommended, with its `detail`
  (the reason, in the user's terms — "CRM → Data-dense");
- the `estimate` beside every option that has one — "Cả hai theme: 424 biến
  thể, ~58 giây". Both themes and "everything" double and triple a generate;
  people choose differently when they see the number.

Put each chosen `value` where the question's `answer` says (`brief.theme`,
`brief.style`, `brief.platforms`, `select`, `options.docPages`) and plan again.
Repeat until `questions` is empty.

**Offer to show the styles, not just list them.** `figma_design_system({ op:
"preview", brief })` draws every style side by side in their brand colour, beside
the work — one frame, nothing else created. Offer it with the style question.

**"Chọn giúp tôi"** — the user delegates: plan with `options.acceptDefaults:
true`. Tell them which answers the tool took (`plan.defaulted`).

**A style of their own** ("Enterprise but compact, filled fields"): pass‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍
`style: { name, base, ...changes }`. After the plan, show `style.designMd` and
offer to save it to the project's design.md — ask first, the tool never writes it.

Do not interview density, radius, fonts, text size or borders one by one —
that is what the style is for.

## Step 2 — show the plan, then stop‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Show `findings` and `estimate`. Blocking findings stop generate — they are not
style opinions. A review finding is a decision; ask, do not silently accept.
`brand-status-clash` is the common one: a red brand next to a red error. Its
hint carries a status colour to pass as `brief.status`; offer it, re-plan.

**Starter / 3-page files:** pass `options.pageStrategy:"single"`. The generator
will not guess the plan; if `createPage` throws it folds onto one `DS · `
page and never onto `currentPage`.

## Step 3 — generate the same plan‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Hand the plan object back unmodified. Re-running **rewrites in place** and
keeps ids (instances survive). Nothing is deleted — dropped variants move to
`DS · Archive`.

After it returns, `figma_design_system({ op: "audit" })`. A generated subtree
scores **1.00**; anything less is a bug in the generator, not in the file.
Report it. Do not bind the missing token by hand.

A visual property (`effectStyleId`, a shadow, a border you cannot see in
`get_node`) is not proven by a `null` field. `figma_read({ op: "export_node" })`
and look.

## What this skill is not

It is not a diagram. There is no `type:`, no compact `text` form, no
`checkFirst`. Catalogue entries live in `src/shared/dsgen/catalogue/*.ts` —
adding a component is an entry there, not a change to the generator.

`source:"design_md"` reads the file: pass `learn: { path: "<absolute path>" }`.
Show the user `evidence` (the line each value came from) and `notes` (what it
could not place) before generating. No primary colour in the file → ask for
one; never invent it.

## Constraints

- Never invent `brand.primary`.
- Never hand-write a plan.
- Never tell the user a component was "deleted".
- Do not turn every border into 3:1. WCAG 1.4.11 is the edge the user needs
  in order to *see* a control (a text field). A card outline is decoration.
- On two connected windows, pass `file` (fuzzy is fine). Restarting MCP in *this* window
  does not restart a stale leader — `figma_status` first.‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍


<!-- wm:10031a355241b873619b88f1cbdef99a -->
<sub>Tài liệu thuộc bộ AI4BA Reqwise Figma MCP — bản quyền hoangphan.blog</sub>
