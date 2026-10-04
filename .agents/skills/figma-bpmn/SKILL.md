---
name: figma-bpmn
description: Draw a business process on Figma as standard BPMN 2.0 — pools for the participants, typed events, gateways, message flows between organisations — and hand it over as a .bpmn file that opens in Camunda or Bizagi. Use it when the notation has to be the STANDARD, not ours.
allowed-tools: Read, Glob, Grep, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_diagram, mcp__reqwise-figma__figma_write
user-invocable: true
argument-hint: "<the process> [source file or @tag]"
---
<!-- Licensed to test.innvie@gmail.com — Order 3D3A2HZRY -->

# /figma-bpmn — The same process, in the notation the industry agreed on‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Read `../reqwise-diagram-rules.md` first — connection gate, the four levels of correct, the
findings loop, frame placement, verification. This file carries only what is specific to BPMN.

## Goal‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Draw a process in the **OMG BPMN 2.0 standard notation** so that a reader who was not in the
room can read it literally, and so that the file can be handed to a BPM tool.

Output: one Figma frame `BPMN · <title>`, the process questions the diagram exposed, and —
with `options.xml` — the same diagram as a `.bpmn` file that opens in Camunda Modeler, Bizagi,
Signavio or draw.io.

## Choose this, or choose /figma-activity‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Ask yourself who the drawing is FOR before you pick.

| The reader | The kind |
|---|---|
| A stakeholder in a meeting, following along while you talk | `/figma-activity` |
| Somebody reading it alone, who must not have to ask what a shape means | `/figma-bpmn` |
| A BPM tool, a process engine, an auditor | `/figma-bpmn` |
| Two organisations exchanging messages | `/figma-bpmn` — activity has no message flow |

An activity diagram is our own notation and cannot be *wrong*. BPMN is a standard, and a
"nearly BPMN" drawing is **worse** than an activity diagram, because it claims a precision it
does not have. If you are not going to get the notation right, draw the activity diagram.

## Constraints‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

### Hard rules — never violate‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

- **An illegal model is REFUSED, not drawn.** Unlike every other diagram kind here, a BPMN
  model that breaks the standard produces an error and no frame. The error lists each rule.
  Do not work around it by weakening the model — fix the model.
- **A message flow goes BETWEEN pools. Never inside one.** This is the most common BPMN
  mistake in the world. Inside one pool, what you want is a sequence flow.
- **A sequence flow NEVER crosses a pool boundary.** A token lives in one process. What crosses
  to another participant is a message, always.
- **A black-box pool must be EMPTY.** That is what makes it say "we do not know, and have no
  business guessing, how they do this". If you know their steps, it is not a black box.
- **A gateway is a QUESTION and every branch is an ANSWER.** Label the gateway with the
  question and each outgoing flow with its condition. An unlabelled branch is not a style
  problem, it is a diagram nobody can read.
- **An end event names an END STATE**, not "Kết thúc". "Đã hoàn tiền" and "Đã từ chối" are two
  outcomes a reader can compare; two boxes both called "End" are not.
- **Never invent a step, an actor or a trigger.** If the source stops at "rồi duyệt", that is
  the finding.

### The event matrix — check before you write

BPMN's event rules are a matrix over (trigger × position), and the tool enforces every cell.
The ones people get wrong:

- **A timer cannot be THROWN.** Time passes on its own; nothing announces it. A timer can be a
  start event, an intermediate catch, or a boundary event.
- **An error cannot start a top-level process** — something has to have thrown it. It is
  exactly right as the start of an event sub-process, which is what an error handler is.
- **Terminate is end-only**, and it kills every token in the scope, not just its own branch.
  Do not reach for it where a plain end event was meant.
- **A start event inside an ordinary sub-process must be blank.** A typed one belongs to an
  event sub-process, which is a different shape and different semantics.
- **Error, cancel and compensation boundary events cannot be non-interrupting** — after one of
  those there is nothing left to carry on with.

### Write it in the compact form

`text` is one line per thing. The `<lane>:` prefix comes first because in BPMN "who does this"
is answered before "what is it", and `@` separates a position from its trigger because those
are two axes of one decision — writing them apart makes an illegal pairing visible as you type.

```
rankdir LR
pool cust "Khách hàng" blackbox
pool shop "Cửa hàng"
lane cs  "CSKH"    in shop
lane fin "Kế toán" in shop
cs:  s1     start@message "Nhận yêu cầu hoàn tiền"
cs:  check  user "Kiểm tra đơn hàng"
cs:  gw     ? "Hợp lệ?"
cs:  late   bound@timer on check "Quá 48 giờ"
cs:  reject end "Đã từ chối"
fin: refund service "Hoàn tiền vào ví"
fin: notify send "Gửi xác nhận cho khách"
fin: done   end "Đã hoàn tiền"
s1 > check
check > gw
gw > refund "hợp lệ"
gw > reject "không hợp lệ" default
refund > notify
notify > done
late > reject "hết hạn"
cust >> s1 "Yêu cầu hoàn tiền"
notify >> cust "Xác nhận đã hoàn"
```

`>` is a sequence flow and `>>` a message flow — one character apart, and deliberately not
interchangeable, because that is the distinction the standard cares most about. `..` ties an
annotation to what it comments on.

### The element table — read this before writing a single node

| Word | Element | When |
|---|---|---|
| `start` `end` `catch` `throw` | events | add `@trigger`: `start@message`, `end@error`, `catch@timer`, `throw@signal` |
| `bound@<trigger> on <id>` | boundary event | something that can happen WHILE that activity runs. Add `weak` for non-interrupting |
| `task` | a task | work with no stated doer |
| `user` | user task | a PERSON does it at a screen |
| `service` | service task | software does it with nobody watching |
| `send` / `receive` | send / receive task | sends or waits for a message |
| `manual` | manual task | a person does it away from any system |
| `rule` | business rule task | a decision table or rule engine |
| `script` | script task | the engine runs a script |
| `sub` | sub-process | a block of work; add `expand` to draw its contents |
| `call` | call activity | a process that lives elsewhere and is reused |
| `esub` | event sub-process | an in-line handler. Triggered, never flowed into |
| `?` `?+` `?o` `?e` `?*` | exclusive / parallel / inclusive / event-based / complex gateway | |‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍
| `data` `store` | data object / data store | what a step reads or writes |
| `note` | text annotation | tie it with `..` |

Markers after the label: `loop` · `mi` (parallel multi-instance) · `mis` (sequential) ·
`adhoc` · `comp`.

## Phase 1 — Read the source, and ask what it does not say

Read the spec, the use cases, the SRS. Then ask the user, in one batch, only what the source
genuinely left open:

- **Who are the participants?** One pool is a process; two or more is a collaboration, and the
  messages between them become the point. Anyone whose internals you do not know — a customer,
  a bank, a portal — is a **black-box pool**.
- **Which roles inside our own pool?** Those are the lanes.
- **What starts it, and what starts it in each case?** A form submitted, a message arriving, a
  timer at month end — the trigger is part of the notation, not flavour text.
- **What are the outcomes?** Every one, including the unhappy ones. Each is an end event with
  its own name.
- **What can go wrong WHILE a step is running?** A timeout, a cancellation, an error. Those are
  boundary events, and they are the part a spec almost never writes down.

Do not ask about anything the source already answers.

## Phase 2 — Draw it

```
figma_diagram({ type: "bpmn", title, subtitle, text, options: { rankdir: "LR", xml: true } })
```

`rankdir: "LR"` (horizontal pools, process runs left→right) is what ~90% of real BPMN does and
is the right default. Only use `"TB"` if the user asks.

`options.checkFirst: true` proof-reads and draws only if the model comes back clean. It is
worth more here than on other kinds when you are working from a thin source: an illegal model
is refused either way, but `checkFirst` also holds back the drawing when the process deadlocks
or a gateway has no question — so you fix it before the user sees a diagram they will quote.

The `audit` that comes back with the draw is a different question again: it measures the
DRAWING (overflow, clipping, truncated text), not the model. A BPMN frame is denser than our
other diagrams — long Vietnamese labels inside a 100×80 activity are where it bites — so read
it rather than assuming the layout coped.

## Phase 3 — Act on the findings

`warnings` and `findings` are the deliverable. Act on each one; **never fill a field just to
silence one** — an invented label is worse than a visible gap.

Two of them are worth explaining to the user in words, because they are facts about the
BUSINESS and they are invisible on the canvas:

- **Deadlock** — an exclusive split chooses one branch, and a parallel join downstream waits for
  both. It waits forever. The drawing looks symmetric and reads fine, which is why nobody
  catches it by eye.
- **Work that happens twice** — a parallel split starts both branches, and an exclusive join
  lets each one through on its own, so everything after it runs twice. It does not jam; it
  quietly duplicates, which is harder to notice and more expensive.

Neither is a drawing problem. Take each one back to the person who owns the process.

## Pitfalls — easy to get wrong

- **Reaching for BPMN when an activity diagram was wanted.** If nobody needs the standard, the
  standard is overhead — and a BPMN diagram with the notation slightly wrong loses the argument
  it was drawn to win.
- **A gateway with one way out.** That is not a decision; delete it.
- **An exception path that goes nowhere.** A boundary event with no outgoing flow says "this can
  happen" and never says what is done about it. The tool refuses it, and it is right to.
- **Modelling the other party's internals** because you can guess them. Draw the black box and
  the messages; the guess will be wrong and it will be quoted back at you.
- **One diagram for two processes.** One BPMN = one process with one goal. Split it.

## What the machine does NOT check

The conformance checking here is real — the model is held against the OMG rules, and the file it
produces is validated by tools that are not ours. That makes it tempting to read a clean result
as "this process is right". It is not what a clean result means.

- **Whether this is the process people actually follow**, as opposed to the one in the SOP.
- **Whether the branches are exhaustive.** The checker counts the ways out of a gateway; it
  cannot know the third case exists. That is why it suggests a default branch rather than
  insisting — the question "what happens when none of these match?" is yours to ask.
- **Whether a condition can ever be true.** A branch that is dead because of the DATA looks
  identical to one that is live; deciding that needs the rules, not the graph.
- **Inclusive (OR) gateways.** Their join semantics are genuinely undecidable in the general
  case — there is a literature on it and no complete answer. A mismatched OR-join comes back as
  "verify this one by hand", and that is an honest limit, not a gap to be optimised away.
- **How long anything takes, or where it really gets stuck.** BPMN shows structure, not
  queueing. If the real problem is that approval waits three days, that fact belongs beside the
  diagram, not in it.

And the one that matters most: a diagram can pass every check and still be the wrong process
modelled beautifully. The findings tell you the drawing is legal and will run. Only the person
who owns the process can tell you it is true.

## Read the reference

`figma_docs(section="bpmn")` — the full field tables, the whole event matrix, the connector
kinds, and what each finding means.‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍


<!-- wm:aca59f6017c1910577c791eb8337d44e -->
<sub>Tài liệu thuộc bộ AI4BA Reqwise Figma MCP — bản quyền hoangphan.blog</sub>
