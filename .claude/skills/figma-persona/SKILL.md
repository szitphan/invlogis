---
name: figma-persona
description: Draw a set of user personas on Figma — who the product is for, who it is NOT for, and which one the next release belongs to — when the open question is whose problem we are solving. Use after research, before scoping anything.
allowed-tools: Read, Glob, Grep, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_diagram, mcp__reqwise-figma__figma_write
user-invocable: true
argument-hint: "<product or segment> [research file or @tag]"
---
<!-- Licensed to test.innvie@gmail.com — Order 3D3A2HZRY -->

# /figma-persona — Who this is for, and who it is not‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Read `../reqwise-diagram-rules.md` first — connection gate, the four levels of correct, the
findings loop, frame placement, verification. This file carries only what is specific to a
persona set.

## Goal‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Settle whose problem the next release is for. Every other artefact here assumes an answer to
that: a journey map is one persona's, a use case has actors, a userflow has somebody walking
it. When nobody has written it down, the answer defaults to "the user" — which is the average
of people who each wanted something different, and the average wants nothing.

Output: one Figma frame `Persona · <title>` holding the whole SET, plus the list of cards that
are still assumptions and any two cards that turned out to be one person.

## The one rule that makes or breaks this diagram‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

**You cannot invent a persona.** It is the artefact in this repo that is easiest to fabricate
and hardest to catch being fabricated: a wrong card looks exactly like a right one — sections
full, face friendly, nothing on it checkable — and it gets quoted in roadmap meetings for a
year after the person who made it up has left.

So:

- **With research** (interviews, support tickets, sales calls, analytics segments, a survey) —
  derive, and put where each card came from in `source`.
- **Without research** — you may draw an **assumption set**: same shape, `source` left out, and
  every card is drawn with a **`▲ GIẢ ĐỊNH — chưa phỏng vấn`** badge on its face. Say plainly
  which one you built, and turn every questionable line into an interview question.
- **Never** write a `quote` nobody said. A quote is the one field that cannot be reasoned out,
  which is exactly why a fabricated card always has a beautiful one.

## Constraints‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

### Hard rules — never violate‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

- **Never draw from an understanding you have not read back.** Before the first `figma_diagram`
  call, say the set back — one line per person, plus what you are unsure of — and get a yes.
  Phase 3.5 says how. A persona board goes on a wall and is quoted for a year; the cost of
  drawing the wrong one is not a wasted call.
- **Ask first: research, or assumption?** It changes the deliverable, the badge and whether the
  set can be cited at all. Do not skip it to get to the drawing.
- **Segment by BEHAVIOUR, not by demographics.** "25–34, thành thị" is a census row, not a
  persona: two people that age can want opposite things. The segments worth a card are the ones
  that behave differently — who they go with, how they decide, what they do when it goes wrong.
- **One set is ONE product decision.** Four cards that each justify a different feature is a
  backlog with faces on it. If two cards would lead to the same build, they are one card.
- **Exactly one `primary`.** The set exists to rank, and a set that ranks nobody decides
  nothing. Two primaries is the argument the set was drawn to settle, still unsettled.
- **A pain point is observed, not deduced.** If nobody said it, it is a hypothesis and it goes
  in the interview list, not on the card.
- **Every pain gets a `need`,** or an explicit note that it is accepted. A card that names what
  hurts and asks for nothing is research stopped at the diagnosis.
- **The face is asked for, never guessed.** Every card carries a drawn face,
  picked by hashing the name so a person looks the same on every redraw — and a
  hash knows nothing about them, so on a real set it put a man's face on a
  woman's card. Do NOT fix that by reading the name: "Linh", "Anh" and "Hà"
  belong to anybody, and a tool that assigns a gender from a given name is
  wrong often enough to be offensive and confident enough to be believed. Write
  `face nữ` / `face nam` / `face trung tính` from what the research says, or
  `face 11` to pick one exactly. If the research does not say, leave it out and
  say so — an unstated face is honest, a guessed one is not.
- **When something is unclear, ASK — with options, not with a blank.** "Persona của ai?" puts
  the work back on the user and gets "người dùng nói chung", which is the one answer the set
  cannot use. Put two or three concrete readings with `AskUserQuestion` and let them correct it.

### Write it in the compact form

`text` is one verb per fact, and it is what you should write — the arrays cost roughly three
times the tokens for the same set, most of it `"painpoints": [`.

```
source "4 phỏng vấn sâu · 8/2026"

persona tu "Nguyễn Đình Tú" primary
  tag   "Solo Explorer"
  fact  "Tuổi: 25"
  fact  "Nghề: Nhà thiết kế nội thất"
  face  nữ                            # nam · trung tính · hoặc 1–24
  quote "Tôi muốn đi đâu đó theo mood của mình, đừng bắt tôi tìm cả tiếng."
  bio   "Đi một mình, thỉnh thoảng rủ một người bạn."
  behav "Tần suất: 2-3 lần/tuần"
  behav "Discovery: TikTok → Google Maps → quyết trong 10 phút"
  goal  "Chọn được chỗ hợp mood dưới 5 phút"
  pain  "Review không đáng tin, ảnh không giống thật"
  pain  "Mất cả buổi tối để chọn một quán"
  need  "Review thực tế, có ảnh người thật chụp"
  want  "Hidden gems của dân địa phương"
  level "Social media" 4
  app   "TikTok"

persona "Phạm Thuỳ Linh"            # id suy ra từ tên: pham-thuy-linh
  tag   "Family Together"
  fact  "Tuổi: 30 · Giáo viên"
  quote "Một chỗ rất tốt với người này lại không hợp với người khác."
  bio   "Đi đâu cũng cả nhà, có bố mẹ và hai cháu nhỏ."
  behav "Lên kế hoạch trước cuối tuần, hỏi ý kiến cả nhà rồi mới đặt"
  pain  "Ít chỗ vừa an toàn cho trẻ vừa hợp người lớn"
  pain  "Không thống nhất được với cả nhóm, cuối cùng bỏ kế hoạch"
  need  "Bộ lọc theo tiêu chí gia đình: ghế trẻ em, chỗ đỗ xe, không ồn"
  want  "Gợi ý sẵn một lịch trình cả nhà đều gật đầu"
  level "Social media" 2
  app   "Facebook"
```

Aliases: `about`=bio · `behaviour`/`routine`=behav · `frustration`=pain · `needed`=need ·
`wanted`=want · `role`/`archetype`=tag · `scale`/`rate`=level · `tool`=app · `evidence`=source.
`level "X" 4` is 0..5 and draws as dots; `8/10` is rescaled rather than refused.

### The sections, and what each one is for

| verb | section | the question it answers | the mistake |
|---|---|---|---|
| `bio` | Bio | who are they, in context | writing a stereotype |
| `behav` | Routine behaviour | what do they DO, how often, through what | writing what you wish they did |
| `goal` | Goals | what does "done well" mean to them | writing your roadmap |
| `pain` | Pain points | what goes wrong today | listing a missing feature instead |
| `need` | Needs | what must be true for them | writing a solution |
| `want` | Wants | what would delight them | filing a need here, where it gets cut |

The order is fixed and it IS the argument: context → behaviour → goal → what hurts (the
evidence) → what they need (the output, and the tinted pair). Pain points stay neutral on
purpose — evidence that shouts as loudly as the conclusion makes the conclusion harder to find.

### Pick the SHAPE first — it is the bigger decision

| `options.layout` | what it is | pick it when |
| --- | --- | --- |
| `board` | **default** — one card per person, in rows | the wall, 2–6 people, a working session |
| `card` | one person per row, full width, three columns | a document or a deck: one person per page |
| `compare` | the MATRIX: sections down the side, people across the top | **deciding.** Two personas saying the same thing become impossible to miss |

**`compare` is the one nobody draws by hand, and the one worth offering.** On a board, two
cards whose needs are identical sit two screens apart and nobody notices; in a matrix they are
adjacent cells with the same words in them. It is also where a scale everybody scores the same
on becomes a visibly pointless row.

**Propose one, then offer the alternatives.** Count the people, ask where it will be shown,
say which you picked and why in one line, then put it and the closest alternative to the user
with `AskUserQuestion`.

### Pick the look with the user, not for them

`options.theme` changes how the set is **drawn**, never what it says.

| theme | what it is for | trình bày |
| --- | --- | --- |
| `workshop` | **default** — dán tường lúc workshop, cả nhóm đứng đọc | có avatar |
| `report` | chèn vào tài liệu, slide, tài liệu bàn giao | không avatar |
| `bold` | chiếu lên màn hình lớn, đọc cách 4 mét | có avatar |
| `mono` | in đen trắng, photocopy, không đụng màu thương hiệu | không avatar |

Ask it **once**, together with the shape — never as a second round trip after the set is drawn.
A theme is a redraw (`update` the same frame), so it is cheap to fix and still costs a turn.

### Pitfalls — easy to get wrong

- **A persona is not an actor.** An actor is a role with permissions and belongs in
  `/figma-usecase`. A persona is a person with a life, and the life is the part that decides
  what to build.‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍
- **A persona set is not a market segmentation deck.** No TAM, no percentages. If a card has a
  market size on it and no quote, it is a slide wearing a face.
- **Don't average two people to make the set tidier.** Draw both and let them disagree — the
  disagreement is the finding.
- **Don't write one card per feature idea.** That is a backlog with faces on it, and every card
  will conveniently need exactly the feature somebody already wanted to build.
- **The people you are NOT building for are worth a card.** A set with no anti-persona has
  never said no to anybody, which is why its roadmap has no shape.
- **`wants` is where good ideas go to be cut, honestly.** Filing a real need there is how it
  gets dropped in the first scoping meeting; filing a nice-to-have in `needs` is how the
  release slips.

## Inputs

```
/figma-persona "App gợi ý địa điểm"                        # interview from scratch
/figma-persona "App gợi ý địa điểm" @research/interviews-2026-08.md   # derive, ask the gaps
/figma-persona                                             # asks what product, and for whom
```

Any source works: interview notes, support tickets, sales-call summaries, a pasted survey, an
analytics segment breakdown, or the answers to the questions below. If the workspace holds
`research/`, `interviews/` or `docs/{feature}/`, read them — but never require them.

## Approach

### Phase 0 — Connection

Per shared rules §5. Do not proceed until you know a write can land.

### Phase 1 — The provenance gate, before anything else

**Ask: is there research, or are we assuming?** Everything downstream changes with the answer —
whether `source` is written, what the badges say, and whether a `quote` may exist at all. A set
whose provenance nobody recorded is treated as evidence within a week.

### Phase 2 — Segments first, people second

A persona is a segment with a face on it, so the segments come first. From the source, list the
ways these users actually **differ in behaviour** — and put the axis to the user, with options:

> "Tôi thấy hai cách chia: theo **người đi cùng** (một mình / nhóm bạn / gia đình / người mới
> đến), hoặc theo **cách quyết định** (quyết nhanh theo mood / phải hỏi cả nhóm / nghiên cứu kỹ
> trước). Hai cách này ra hai bộ persona khác hẳn nhau — anh/chị thấy cách nào đúng với người
> dùng thật hơn?"

Then settle, in the same breath: **how many cards** (3–4 is usually right; more than six and
nobody remembers any) and **who is primary**.

### Phase 3 — The interview kit

Anything the source does not say, ask in business language — never "bio của persona là gì".
Two or three per section is enough:

| section | ask |
|---|---|
| Bio | *"Người này sống và làm việc thế nào? Cái gì về hoàn cảnh của họ ảnh hưởng tới việc này?"* |
| Routine behaviour | *"Lần gần nhất họ làm việc này là khi nào, và họ mở cái gì ra trước?"* · *"Một tháng bao nhiêu lần?"* · *"Họ tin ai/nguồn nào khi quyết?"* |
| Goals | *"Với họ, thế nào là xong việc tốt đẹp?"* |
| Pain points | *"Chỗ nào họ bực tới mức kêu ra thành lời?"* · *"Lần gần nhất họ bỏ cuộc giữa chừng là vì gì?"* |
| Needs | *"Thiếu cái gì thì họ không dùng được?"* |
| Wants | *"Cái gì có thì họ thích, không có cũng không sao?"* |
| Scales | *"Họ rành công cụ tới đâu — tự làm được hay phải có người chỉ?"* |
| Apps | *"Họ đang dùng cái gì để làm việc này?"* |
| Face | không hỏi thành câu riêng — lấy từ những gì research đã nói về người đó. Không suy từ tên. |

If you would be inventing more than half of it, stop and say so: draw the assumption set with
the questions on it, or go and talk to three people first.

### Phase 3.5 — Read the set back, and get a yes

**The gate.** Everything so far was you understanding; this is the user confirming you
understood. Nothing is drawn until they say so. Read back compactly — one line per person:

```
1. Đình Tú · Solo Explorer   — đi một mình, quyết theo mood, ghét review giả   [PRIMARY]
2. Thuỳ Linh · Family Together — đi cả nhà, phải hợp ý mọi người, sợ chọn sai
3. Khánh Ly · Người mới đến  — không quen khu vực, quỹ thời gian hẹp
Nguồn:   4 phỏng vấn sâu, 8/2026   (hoặc: GIẢ ĐỊNH — chưa phỏng vấn ai)
Chưa rõ: nhóm "đi công tác" có phải một persona riêng, hay là Khánh Ly lúc khác?
```

Then ask **one** question, not eight — the one that is actually shaky. A "Chưa rõ" line is not
a failure, it is this phase's deliverable: listing what you do not know is how the user finds
out you were about to guess it.

### Phase 3.6 — Agree the shape, then the look

One `AskUserQuestion`, with a recommendation and a reason. If they have no opinion, use
`board` + `workshop` and say so.

### Phase 4 — Check, then draw, in one call

Call `figma_diagram` with `type: "persona"` and `options: { checkFirst: true }`: it proof-reads
and **draws only if there are no findings**. Dirty → `checkedOnly: true` + the findings and
nothing is drawn; clean → it draws and returns `audit` in the same call.

Read every warning (shared rules §3). The ones specific to this kind:

| Warning | What it usually means |
|---|---|
| "X" has no `quote` | nothing on that card is in their words — it may be invented |
| demographics but nothing they DO | a census row, not a persona |
| pain points with nothing asked for against them | research stopped at the diagnosis |
| needs things but nothing hurts | a feature looking for a justification |
| X and Y share N lines word for word | **the finding.** One person wearing two names |
| X and Y want the same things (N%) | two cards, one segment — say what the product would do differently for each |
| nobody is `primary` | the set describes people and decides nothing |
| every persona scores N on "…" | a scale that separates nobody — drop the row |
| no `source` anywhere | every card is drawn as an ASSUMPTION, and says so on its face |
| Only one persona | a set of one is a stereotype — unless `layout:"card"` was what you meant |

Fix the model by **going back to the research**, not by inventing a line, and re-run.

### Phase 5 — Draw, verify, report

1) Place the frame clear of what is already on the page (shared rules §7).
2) Draw.
3) Read `audit` from the same result. Fix anything it reports. No second call for it.
4) One `screenshot` per SET at the end, not one per card.
5) Report per shared rules §11 — and lead with which cards are still assumptions and which two
   turned out to be one person, because those are the decisions the set was drawn to force.

### Phase 6 — Hand it on

A persona set is an input, not an end:

- the primary persona + one situation → `/figma-journey` (where does it hurt for them?)
- a pain worth building for → `/figma-userflow` (what do they see next?)
- an argument about who is in scope → `/figma-usecase`
- "we don't even store that about them" → `/figma-erd`

A journey on the same page is cross-checked: `consistency` reports
`persona-drift` when its `persona` line matches no card, by name, loosely.
Cards no journey walks are not reported.

## What the machine does NOT check

Level 4, in this kind, is nearly all of the value:

- whether the person exists, or is three people flattened into one;
- whether a quote is a quote, or your paraphrase of a feeling;
- whether the segments are the ones that actually behave differently, or just the ones that
  were easy to name;
- whether the `primary` is primary because of evidence or because of who was in the room;
- whether the people you left out are the ones who would have paid.

Put these in front of a human. `figma_docs(section="persona")` has the full field reference.
The set is how the conversation starts; deciding whose problem to solve is the deliverable.‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍


<!-- wm:aca59f6017c1910577c791eb8337d44e -->
<sub>Tài liệu thuộc bộ AI4BA Reqwise Figma MCP — bản quyền ai4ba.com</sub>
