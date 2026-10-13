---
name: figma-journey
description: Draw a user journey map on Figma — one persona, one scenario, phases across the top, and the emotion curve underneath — when the open question is where the experience actually hurts. Use after research or interviews, before deciding what to build.
allowed-tools: Read, Glob, Grep, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_diagram, mcp__reqwise-figma__figma_write
user-invocable: true
argument-hint: "<who, doing what> [source file or @tag]"
---
<!-- Licensed to test.innvie@gmail.com — Order 3D3A2HZRY -->

# /figma-journey — Where it actually hurts‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Read `../reqwise-diagram-rules.md` first — connection gate, the four levels of correct, the
findings loop, frame placement, verification. This file carries only what is specific to a
journey map.

## Goal‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Find the pain point worth spending money on. Every other diagram here is structure: a sequence
says what is sent, a state machine says what a record can be, a userflow says which screen is
next. None of them can hold the fact that the customer is anxious at checkout — and that fact
is what decides which of ten possible improvements is worth building.

Output: one Figma frame `Journey · <title>`, plus a written list of the pain points that have
__no__ opportunity against them yet, which is the decision the map exists to force.

## The one rule that makes or breaks this diagram‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

__You cannot invent a journey map.__ A persona, a quote, a feeling score — every one of them is
either something a real person said or a fabrication that will be cited in a roadmap meeting
for the next year. This is the only kind here where making the model up is not merely useless
but actively harmful, because it launders a guess into evidence.

So:

* __With research__ (interviews, support tickets, session recordings, a survey) — derive, and
  cite where each row came from.
* __Without research__ — you may draw an __assumption map__: same shape, but say so in
  `subtitle` ("Giả định — chưa phỏng vấn"), and every questionable cell becomes an interview
  question rather than a finding. Tell the user plainly which one you built.
* __Never__ score `feeling` from your own intuition on a map presented as research. Leave the
  row out entirely — no curve is honest, a fabricated curve is not. The tool stays quiet about
  a map with no scores for exactly this reason.

## Constraints‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

### Hard rules — never violate‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

* __Never draw from an understanding you have not read back.__ Before the first `figma_diagram`
  call, say the map back to the user in their language — persona, scenario, goal, the phase
  chain — and get a yes. This is a gate, not a courtesy: the cost of drawing the wrong map is
  not a wasted call, it is a poster on a wall that people quote for a year. Phase 3.5 says how.
* __When something is unclear, ASK — and ask with options, not with a blank.__ "Journey của ai?"
  puts the work back on the user and gets "khách hàng nói chung", which is the one answer the
  map cannot use. Put two or three concrete readings to them with `AskUserQuestion` and let them
  pick or correct. Guessing quietly is the one thing never allowed here: an invented persona is
  indistinguishable from a researched one once it is drawn.
* __One map is ONE persona in ONE scenario.__ A map of "users" is the average of people who
  each wanted something different, and the average wants nothing. Two personas = two frames.
* __Phases are the user's, not yours.__ "Tìm chuyến", "Chờ xác nhận" — the phases as the person
  experienced them, not your internal stages. If a phase name only makes sense to the team, it
  is the wrong phase name.
* __A touchpoint is where it happened__, and it is often not your product: a phone call, a
  Zalo message, a queue at the counter, a friend. A map where every touchpoint is your app is a
  map that stopped looking at the edges.
* **`painpoints` are observed, not deduced.** If nobody said it, it is not a pain point; it is
  a hypothesis, and it goes in the interview list.
* **Every pain point gets an `opportunity` or an explicit reason it is accepted.** This is the
  finding the whole diagram exists to produce, and the tool reports it.
* __Score every phase or none.__ A half-scored curve cannot be read, and the tool reports it.

### Write it in the compact form

`text` is one verb per fact, and it is what you should write — the arrays cost roughly three
times the tokens for the same map, most of it `"actions": [`.

```
persona  "Chị Hoa · 34, nhân viên văn phòng, đi làm bằng xe máy"
scenario "Đặt vé xe khách về quê dịp Tết cho cả gia đình"
goal     "Mua 4 vé cạnh nhau trước khi hết chỗ"

phase search "Tìm chuyến"
  do    "Mở app, chọn ngày và tuyến"
  at    "App · Trang tìm kiếm"
  think "Không biết còn chỗ cạnh nhau không"
  feel  0
  pain  "Không thấy còn bao nhiêu ghế trống"
  fix   "Hiện số ghế còn lại ngay trên kết quả"

phase pay "Thanh toán"
  do    "Chọn 4 ghế, nhập thông tin, chuyển khoản"
  at    "App · Trang thanh toán"
  at    "App ngân hàng"                     # repeat a verb for a second item
  think "Chuyển khoản xong ghế còn giữ không?"
  feel  -2                                  # the trough. This is the finding.
  pain  "Không biết ghế được giữ trong bao lâu"
  fix   "Đếm ngược @hold-minutes phút trên màn thanh toán"
```

`feel` also takes `awful|bad|ok|good|great`. Aliases: `act`, `touch`, `thought`, `opp`.

### The rows, and what each one is for

| verb | row | the question it answers | the mistake |
|---|---|---|---|
| `do` | Doing | what did they __do__? | writing what the system did |
| `at` | Touchpoint | __where__ — screen, channel, person | assuming it was always your app |
| `think` | Thinking | in __their__ words | paraphrasing into your words |
| `feel` | Feeling | −2..2, and it becomes the curve | scoring from intuition |
| `pain` | Pain points | what went __wrong__ | listing a missing feature instead |
| `fix` | Opportunities | what could be __done__ | writing a spec instead of one line |

`fix` is one line naming what could be done, not a design. The design is what
`/figma-userflow` and the wireframes are for.

### Pick the SHAPE first — it is the bigger decision

`options.layout` decides how the map is arranged. It matters more than the
palette, and the wrong one is the difference between a map people read and a
map that gets shrunk into a slide until nobody can.

| layout | what it is | pick it when |
| --- | --- | --- |
| `table` | __default__ — the grid: phases across, rows down | 3–6 phases, and the map lives on a wall or a big screen |
| `columns` | transposed: phases run DOWN, row types become columns | __7+ phases__ — the grid passes 3,000px and stops being printable |
| `cards` | one outlined card per phase, no gutter, each section labelled inside | somebody who was not in the workshop has to read it alone |
| `curve` | the emotion line as a tall chart at the top, detail hanging beneath | the argument IS the shape of the experience — a steering meeting |
| `poster` | three rows only (feeling · pain · opportunity), huge faces, big type | a wall, read at four metres. It __drops the evidence rows by design__ |

__Propose one, then offer the alternatives.__ Work out the recommendation from
what you already know — count the phases, ask where the map will be shown —
say which you picked and why in one line, then put it and the two closest
alternatives to the user with `AskUserQuestion`. Never make them choose from
five with no steer: that is the same as not asking.

A worked steer: *"7 phases and it's going in the sprint review deck — I'd use
`columns`, because the grid would run to 3,000px and get shrunk to nothing on
a slide. Alternatives: `table` if you'll project it full-screen, `cards` if
people will read it on their own."*

Two things the shape never changes: the rows and their order, and which row is
highlighted. `poster` is the one that drops rows, and it drops them honestly —
it is a summary, so say in `subtitle` which map it summarises.

`layout` and `theme` are separate axes. Ask about the shape; only ask about
the palette if they care, and otherwise pair it yourself — `poster` wants
`bold`, `curve` and `table` want `workshop`, anything going into a document
wants `report` or `mono`.

### Pick the look with the user, not for them

`options.theme` changes how the map is __drawn__, never what it says. The same
map at a stand-up, in a board pack and taped to a wall wants three different
answers, and you cannot guess which room this one is for.

| theme | what it is for | trình bày |
| --- | --- | --- |
| `workshop` | __default__ — a wall poster for a working session; warm, mid-contrast, room to write | biểu đồ · 3 thẻ · có avatar |
| `report` | a figure inside a document or a deck: hairline rules, tight rows, one accent | biểu đồ · 1 dòng · không avatar |
| `bold` | read from across a room: saturated, large type, generous rows | __mặt cười__ · 3 thẻ · có avatar |
| `mono` | greyscale + one accent — survives a B/W printer, never fights a brand palette | biểu đồ · 1 dòng · không avatar |
| `soft` | warm and rounded, for a session with people outside the team | biểu đồ · 3 thẻ · có avatar |

**Ask with `AskUserQuestion`, in one question, phrased by the ROOM rather than
by the id** — "dán tường lúc workshop" / "chèn vào tài liệu, slide" / "chiếu
lên trình chiếu" / "in đen trắng". Offer at most four and let `workshop` be the
first, because it is the one that needs no justification.

Ask it __once__, together with the LR/TB-style questions this kind does not
have — never as a second round trip after the map is already drawn. A theme is
a redraw (`update` the same frame), so getting it wrong is cheap to fix and
still costs the user a turn.

What a theme cannot do: move the highlight or reorder the rows. `opportunities`
is the tinted row in every theme, because it is the map's output. If somebody
asks for the pain points to be the loud row, that is a request to change the‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍
argument, and the answer is that the evidence should not shout as loudly as
the conclusion.

### Pitfalls — easy to get wrong

* __A journey map is not a userflow.__ A userflow says which screen comes next and is drawn
  from screens that exist. If what you have is screens and arrows, use `/figma-userflow`.
* __A journey map is not an activity diagram.__ That one is the inside view — who does each
  step in the business. This is the outside view: one customer, their words.
* __The trough is the deliverable.__ If the curve comes out flat and positive, either nobody
  was interviewed or you are mapping the demo. Say which.
* __Don't average two people into one persona__ to make the map tidier. Draw two frames and
  let them disagree — the disagreement is a finding.
* **`opportunities` is not a backlog.** One line per pain point. If it needs acceptance
  criteria, it has outgrown this diagram.
* __Post-purchase exists.__ Maps routinely stop at "paid", which is exactly where support cost
  and churn live.

## Inputs

```
/figma-journey "Chị Hoa đặt vé xe khách dịp Tết"                    # interview from scratch
/figma-journey "Đặt vé Tết" @research/interviews-2026-08.md          # derive, ask only the gaps
/figma-journey                                                       # asks who, doing what
```

Any source works: interview notes, support tickets, a session-recording summary, a pasted
survey, or the answers to the questions below. If the workspace holds `research/`,
`interviews/` or `docs/{feature}/` files, read them — but never require them.

## Approach

### Phase 0 — Connection

Per shared rules §5. Do not proceed until you know a write can land.

### Phase 1 — Establish what kind of map this is

__Ask first, before anything else: is there research, or are we assuming?__ The answer changes
the deliverable, the `subtitle`, and whether `feeling` is scored at all. Do not skip this to
get to the drawing — a map whose provenance nobody recorded is treated as evidence within a
week.

### Phase 2 — Derive the model, and name the gaps

From the source, list — this is the __fact-list__ you will check the drawing against later:

1) __The persona__, concretely: who, and what about them matters here.
2) __The scenario__, as one situation with a beginning and an end.
3) __Their goal__ — what "done well" would have meant to them.
4) __Phases__, in the order they lived them, in their language.
5) Per phase: what they did, where, what they said they thought, how it landed, what went
   wrong.

Anything the source does not say, __ask__, in business language: *what did they try first?* ·
*where did they get stuck long enough to complain?* · *what did they do when it went wrong —
call, give up, ask a friend?* · *what happened after they paid?*

If you would be inventing more than half of it, stop and say so: draw an assumption map with
the questions on it, or go and interview three people first.

### Phase 3 — Ask the question that changes the drawing

Before drawing, confirm: __where does this journey actually end?__ Almost every map is drawn
one phase too short — it stops at the transaction and misses the wait, the confirmation, the
thing that went wrong afterwards, the support call. That phase is usually where the cheapest
improvement is.

### Phase 3.5 — Read the map back, and get a yes

__The gate.__ Everything so far has been you understanding; this is the user confirming you
understood. Nothing is drawn until they say so.

Read back, compactly — six lines, not the whole model:

```
Persona:   Quản trị viên · 32 tuổi, phụ trách dữ liệu khách hàng
Scenario:  Nhập một lead mới từ hội thảo vào CRM
Goal:      Lead vào đúng chủ sở hữu, không trùng, dưới 2 phút
Phases:    Nhận danh sách → Nhập vào hệ thống → Kiểm tra lại
Nguồn:     3 buổi quan sát tháng 8  (hoặc: GIẢ ĐỊNH — chưa phỏng vấn)
Chưa rõ:   sau khi nhập xong thì ai kiểm? có bước duyệt không?
```

Then ask __one__ question, not six. Which one depends on what is actually shaky:

* __The whole reading might be wrong__ → put the two or three readings you can see to them with
  `AskUserQuestion` ("Journey này là của *người nhập liệu* hay của *người quản lý đội sale*? —
  hai người này gặp vấn đề khác hẳn nhau"), and say what changes with each.
* __One field is missing__ → propose a concrete value and ask them to correct it, never ask for
  it blank. "Tôi đang hiểu mục tiêu là *dưới 2 phút mỗi lead* — có phải không, hay là *không sai
  chủ sở hữu* mới là cái quan trọng?"
* __Everything reads right__ → one line: "Đúng thì tôi vẽ. Sai chỗ nào thì sửa giúp tôi."

Two rules for this step:

* __A "Chưa rõ" line is not a failure, it is the deliverable of this phase.__ Listing what you
  do not know is how the user finds out you were about to guess it.
* __Do not read back and draw in the same breath.__ If you print the summary and then draw
  without waiting, the gate does not exist — you have just narrated a guess.

### Phase 3.6 — Agree the shape, then the look

While you have the user, settle the __shape__ — `layout` — and, if they care,
the palette. One `AskUserQuestion`, not two rounds.

Recommend before you ask. Count the phases and ask where it will be shown;
those two answers pick the layout most of the time. Lead with your choice and
one line of reason, then offer the two closest alternatives. Say what a shape
changes and what it does not: where things sit, never the rows and never what
the map says.

If they have no opinion, use `table` + `workshop` and say so. A default nobody
chose is fine; a shape nobody was offered is how a seven-phase map ends up
3,000px wide in a slide.

### Phase 4 — Check, then draw, in one call

Call `figma_diagram` with `type: "journey"` and `options: { checkFirst: true }`: it proof-reads
and __draws only if there are no findings__. Dirty → `checkedOnly: true` + the findings and
nothing is drawn; clean → it draws and returns `audit` in the same call.

Read every warning (shared rules §3). The ones specific to this kind:

| Warning | What it usually means |
|---|---|
| No persona / No scenario | you are about to average several people into nobody |
| Nothing the user does in "X" | that is a heading, not a phase — fold it in or fill it |
| "X" says what the user does but not where | the touchpoint is missing, and it is often the interesting one |
| Pain point with nothing proposed in "X" | __the__ finding. Propose something, or record that it is accepted |
| Opportunity with no pain point behind it in "X" | a feature looking for a justification |
| Feeling is scored on N of M phases | finish the curve or drop the row |
| No phase scores below neutral | the demo, not the user — or genuinely fine, in which case look elsewhere |
| Unknown journey theme "x" | the map was drawn in `workshop`. Check the id against the table above |
| a map past ~6 phases in `table` | nothing reports it yet — count them yourself and switch to `columns` |

Fix the model — by __going back to the research__, not by inventing a cell — and re-run.

### Phase 5 — Draw, verify, report

1) Place the frame clear of what is already on the page (shared rules §7).
2) Draw.
3) Read `audit` from the same result. Fix anything it reports. No second call for it.
4) One `screenshot` per SET of diagrams at the end, not one per frame.
5) Report per shared rules §11 — and lead with the list of pain points that still have no
   opportunity against them, because that list is the reason the map was drawn.

### Phase 6 — Hand it on

A journey map is an input, not an end. Say which follow-on the findings point at:

* a pain point in a specific step → `/figma-activity` (who owns that handoff?)
* a pain point spread across screens → `/figma-userflow` (what does the user see next?)
* "we don't even store that" → `/figma-erd`
* a scope argument breaking out → `/figma-usecase`

## What the machine does NOT check

Level 4, in this kind, is nearly all of the value:

* whether the persona is real, or three people flattened into one;
* whether a quote is a quote, or your paraphrase of a feeling;
* whether the `feeling` scores reflect what people said or what you expected;
* whether the phase the map is missing is the one where the money leaks;
* whether an opportunity is worth its cost — the map ranks pain, never effort.

Put these in front of a human. The map is how the conversation starts; the decision about
which trough to spend money on is the deliverable.‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍


<!-- wm:10031a355241b873619b88f1cbdef99a -->
<sub>Tài liệu thuộc bộ AI4BA Reqwise Figma MCP — bản quyền hoangphan.blog</sub>
