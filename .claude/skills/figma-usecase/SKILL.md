---
name: figma-usecase
description: Draw a UML use case diagram on Figma — actors outside a named system boundary, goals inside it — when the open question is what is in scope and whose goal it is. Use at a kickoff, a change request, or any time someone asks "is that in scope?".
allowed-tools: Read, Glob, Grep, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_diagram, mcp__reqwise-figma__figma_write
user-invocable: true
argument-hint: "<what is being built> [source file or @tag]"
---
<!-- Licensed to test.innvie@gmail.com — Order 3D3A2HZRY -->

# /figma-usecase — Scope, drawn‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Read `../reqwise-diagram-rules.md` first — connection gate, the four levels of correct, the
findings loop, frame placement, verification. This file carries only what is specific to a use
case diagram.

## Goal‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Settle the boundary. Every other diagram assumes it: a userflow draws screens that exist, a
sequence draws systems that already talk. This one is the argument **before** that — what is
inside the thing we are building, what is outside it, and which roles get to start which piece
of work.

Output: one Figma frame `Use case · <title>`, plus a written list of the scope questions the
diagram exposed.

## Constraints‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

### Hard rules — never violate‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

* **The label of a use case is a GOAL and a verb**, in the user's words: "Ký hợp đồng",
  "Nộp hồ sơ vay". Not a noun, not a screen, not a CRUD row.
* **An actor is a ROLE, not a person and not a job title held by one human.** "Khách hàng",
  "Chuyên viên thẩm định". If two roles do exactly the same set of use cases, they are one
  actor with two names — say so rather than drawing both.
* **Decide each actor's `side` deliberately.** `left` = the **primary** actor, whose goal the
  use case serves. `right` = a **supporting** actor the system reaches out to (a payment
  gateway, a core banking system, another team). Everyone on one side is the single commonest
  reason these diagrams read as spaghetti.
* **Always pass `system`.** Without the boundary box you have drawn a feature list, not a
  statement of scope. The tool reports its absence; do not ignore that.
* **Link kinds are not interchangeable** — see the table below. The server DROPS a link that
  is not a meaning UML has, so **compare `stats.links` to the number you sent**.
* **Never invent a use case to fill the box.** A thin diagram is a finding about the spec.

### Write it in the compact form‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

`text` is one line per thing, and it is what you should write — the arrays cost about three
times the tokens and say the same thing.

```
system "Online movie ticket booking website"     # the boundary box. Always set it.
actor  visitor "Visitor" / not logged in         # primary actor, drawn LEFT
actor  member  "Member"
actor> psp     "Payment Gateway" sys             # the ">" puts it on the RIGHT; "sys" = a box
uc book    "Book seats for a showtime"
uc hold    "Hold the seats for 10 minutes"
uc login   "Log in"
uc history "See my past bookings"
visitor - book        # association: this actor can start it. NO arrow head.
member  - history     # what a Member can do that a Visitor cannot
member :> visitor     # generalize: a Member is a special kind of Visitor
login  +> book        # extend: sometimes adds to — points at the BASE
book   => hold        # include: book ALWAYS performs hold
hold   - psp          # a use case reaching a supporting actor is still an association
```

The `>` on `actor>` is the field that decides whether the drawing reads at all, and it is one
character — that is the reason to write it here rather than in an object.

### The link table — read this before writing a single link

The correct way here is the opposite of the habit. `-->` is the default edge in every other
diagram language, and an arrow between any two things is what fingers type. In a use case
diagram most links are **not** arrows at all, and the four tokens are shaped so the direction
is visible in the glyph.

| Want to say | Write | NOT |
|---|---|---|
| This actor can start this use case | `visitor - book` — actor ↔ use case, **no arrow head** | an arrow; or a link between two use cases |
| This use case **always** performs that one | `book => hold` — use case → use case | `=>` touching an actor |
| That behaviour **sometimes** adds to this one | `login +> book` — points at **the case being extended** | pointing it at the optional behaviour |
| This actor/use case is a special kind of that one | `member :> visitor` — both ends the same kind | generalizing an actor into a use case |
| This use case calls out to a supporting system | `hold - psp`, with `actor> psp … sys` | an `=>` to a "system use case" you invented |

`+>` is the one people reverse. Read it as a sentence and the direction falls out:
**"Nhắc nợ quá hạn *extends* Trả nợ theo kỳ"** — the optional behaviour names the thing it
hangs off, so it points at the base.

### Pitfalls — easy to get wrong

* **A use case reached only through an `include` needs no actor.** The tool knows this and
  stays quiet about it. Do not add a fake association to "fix" a warning that never fired.
* **CRUD is not four use cases.** "Tạo / Sửa / Xoá / Xem hợp đồng" is one goal — "Quản lý hợp
  đồng" — unless the spec really gives them different actors or different rules.
* **A use case is not a step.** "Nhập mật khẩu" is a step inside "Đăng nhập". If the label
  would be a box in a flowchart, it belongs in `/figma-activity`, not here.
* **A supporting system is an actor** (`kind: "system"`, `side: "right"`), not a use case. It
  is outside the boundary by definition.
* **Do not draw the include chain three deep.** Two levels is the readable limit; deeper means
  the top-level use case is really a process — draw that with `/figma-activity`.
* **`generalize` is rare.** If you are reaching for it to avoid repeating two associations,‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍
  just write the two associations.

## Inputs

```
/figma-usecase "App vay tín chấp"                    # interview from scratch
/figma-usecase "App vay tín chấp" @docs/srs/spec.md  # derive from a source, ask only the gaps
/figma-usecase                                        # asks what is being built
```

Any source works: a pasted spec, a tagged file, a meeting note, or the answers to the
questions below. If the workspace happens to hold `docs/{feature}/srs/` or `brainstorms/`
files, read them — but never require them.

## Approach

### Phase 0 — Connection

Per shared rules §5. Do not proceed until you know a write can land.

### Phase 1 — Derive the model, and name the gaps

From the source, list — in your head or in a scratch note, this is the **fact-list** you will
check the drawing against later:

1. **The system being built**, as it would be named on a boundary box.
2. **Roles** that interact with it, and for each: are they pursuing a goal (primary, left) or
   being called by the system (supporting, right)?
3. **Goals** — one line each, verb first.
4. **Which role starts which goal.**
5. **Shared behaviour**: does a goal always perform another (`include`), or sometimes extend
   one (`extend`)?

Anything the source does not say, **ask**. Batch the questions in business language, never
technical: *who else touches this?* · *what does the branch office do that the customer
cannot?* · *is reporting in this release or the next?*

If the source is thin enough that you would be inventing more than half the model, say so and
stop — a made-up scope diagram is worse than none.

### Phase 2 — Ask the one question that changes the drawing

Before drawing, confirm with the user: **what is OUT of scope but adjacent?** It is the
question a boundary box exists to answer, it is almost never in the spec, and the answer often
moves an actor from left to right — or removes a use case entirely.

### Phase 3 — Check, then draw, in one call

Call `figma_diagram` with `type: "usecase"` and `options: { checkFirst: true }`: it checks the model and
**draws only if there are no findings**. Dirty → `checkedOnly: true` + the findings and nothing
is drawn; clean → it draws and returns `audit` in the same call. (`options: { dryRun: true }`
is still there for iterating on a model you expect to be wrong.)

Read every warning (shared rules §3). The ones specific to this kind:

| Warning | What it usually means |
|---|---|
| Nobody can start "X" | you drew scope with no owner, or forgot an association |
| Actor with nothing to do | the role does not belong here, or a goal of theirs is missing |
| Link UML cannot mean, dropped | you used the wrong `kind` — go back to the link table |
| `<<include>>` runs in a circle | two goals each claim to always perform the other |
| No system boundary | you did not pass `system` |

Fix the model, re-dry-run, and only then draw.

### Phase 4 — Draw, verify, report

1. Place the frame clear of what is already on the page (shared rules §7).
2. Draw.
3. Read `audit` from the same result — the render-side check on the frame just drawn.
   Fix anything it reports. No second call for it.
4. One `screenshot` per SET of diagrams at the end, not one per frame.
5. Report per shared rules §11 — and say plainly that whether this is **the right scope** is a
   business judgement no checker made.

## What the machine does NOT check

Level 4, in this kind, is most of the value:

* whether a use case is genuinely in this release;
* whether the actor list is missing a role nobody mentioned (compliance, ops, support);
* whether a goal is at the right altitude — "Đăng nhập" and "Vay tín chấp" on one diagram is a
  level mismatch a linter cannot see;
* whether the boundary matches what the team has actually agreed to build.

Put these in front of a human. That conversation is the deliverable; the picture is how you
get it started.‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍


<!-- wm:aca59f6017c1910577c791eb8337d44e -->
<sub>Tài liệu thuộc bộ AI4BA Reqwise Figma MCP — bản quyền ai4ba.com</sub>
