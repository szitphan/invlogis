---
name: figma-sequence
description: Draw a UML sequence diagram on Figma — participants as columns, messages in time order, activation bars, alt/loop blocks — when the open question is what is sent between systems and what comes back. Use it for an integration or an API contract.
allowed-tools: Read, Glob, Grep, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_diagram, mcp__reqwise-figma__figma_write
user-invocable: true
argument-hint: "<the exchange> [source file or @tag]"
---
<!-- Licensed to test.innvie@gmail.com — Order 3D3A2HZRY -->

# /figma-sequence — What is sent, and in what order‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Read `../reqwise-diagram-rules.md` first — connection gate, the four levels of correct, the
findings loop, frame placement, verification. This file carries only what is specific to a
sequence diagram.

## Goal‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Pin down an exchange between systems. This is the diagram for the part of an integration spec
that is vague until someone draws it: __what__ is sent, in __which order__, and **what comes
back** — including on the unhappy path.

Output: one Figma frame `Sequence · <title>`, plus the contract questions the diagram exposed.

## Constraints‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

### Hard rules — never violate‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

* **The order of `messages` IS the time order.** There is no timestamp field and no sorting.
  The array is the diagram. Reordering the array reorders the picture.
* **Every message has an `id`** — fragments reference them, and findings name them.
* **Every message has a `label` that says WHAT is sent**, not that something is sent.
  `POST /contracts/{id}/sign-otp` and `202 { otpSentAt }`, not "gọi API" and "trả về".
  This is the field people argue about six months later; it is why the diagram exists.
* __Order the participants so the exchange mostly flows one way.__ Arrows crossing back and
  forth across five columns is a layout problem you fix by reordering the array, not by
  fiddling with the drawing.
* __Never invent a reply.__ If the spec does not say what comes back, that is the finding.

### Write it in the compact form‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

`text` is mermaid-shaped on purpose — that is the sequence notation everyone already knows —
and it drops the two things that were pure overhead in the array form: __message ids__, and the
`messages: ["m3","m4"]` list inside each fragment. A block's extent is simply where it is
written.

```
actor       user  "User"
participant api   "Booking API" / booking-svc
db          store "Bookings DB" / postgres
external    psp   "Payment Gateway"
user ->> api: POST /holds { seatIds }        # ->>  a call, and it opens an activation bar
api  ->> store: INSERT booking_seats
store -->> api: ok                            # -->> a reply, and it closes the bar
alt seats free
  api -->> user: 201 { bookingId }
  note: hold lasts 10 minutes
else already booked
  api -->> user: 409 seats_unavailable !err   # !err colours the failure path
end
api --) psp: capture(bookingId)               # --)  fire and forget
```

Indentation inside `alt`/`else`/`loop` is for you, not the parser — but write it, because the
extent of a block is now something a reader checks by eye.

### The message table — read this before writing a single message

The habit is one arrow per "thing that happens". A sequence diagram distinguishes three, and
the activation bars are __derived__ from that distinction — get the arrow wrong and the bars
are wrong.

| Want to say | Write | NOT |
|---|---|---|
| A calls B and waits | `a ->> b: POST /pay` — opens a bar on B | `--)` because it "feels" fast |
| B answers A | `b -->> a: 201 { id }` — __closes__ the bar | another `->>` pointing back |
| Fire and forget; nobody waits | `a --) b: emit(paid)` | `->>` with no reply, which reads as unanswered |
| A person taps a button | declare them `actor u "User"` | expecting a reply arrow back to them |
| A system does its own work | `los ->> los: sinh mã 6 số` | a note with no arrow |
| Something the reader must know | `note: tối đa 5 lần nhập sai` under the message | a participant called "Rules" |
| Two alternative outcomes | `alt … else … end` | two diagrams, or two branches in sequence |

__Do not declare activation bars.__ They are derived, because book-keeping activate/deactivate
by hand is exactly how these diagrams drift out of step with themselves. If a bar looks wrong,
an arrow is wrong.

### Pitfalls — easy to get wrong

* __A fragment must cover a CONTIGUOUS run of messages.__ `messages: ["m3","m5"]` skipping
  `m4` is not a thing a sequence diagram can draw; reorder, or split the fragment.
* **`alt` needs an `else`.** An alternative with one branch is an `opt` — the tool says so.
* __A person is not waiting for a reply.__ A `sync` message from an `actor` never gets reported
  as unanswered; do not add a fake `return` to the human.
* **`kind: "actor"` is for people.** A third-party API is `kind: "external"` (dashed); a
  queue is `queue`; a database is `db`. The shapes carry meaning — use them.
* __Do not draw the whole system.__ A sequence diagram is one scenario. "Ký hợp đồng bằng OTP",
  not "Toàn bộ luồng vay". If you need branches for six different outcomes, you need six
  diagrams or an `/figma-activity`.
* __Error paths are the point, not an appendix.__ A diagram with only the happy path is half a‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍
  spec. Ask for the timeout, the rejection, the retry.
* **A `note` is short.** Two lines. Anything longer belongs in the spec, not on the canvas.

## Inputs

```
/figma-sequence "Ký hợp đồng bằng OTP"                    # interview from scratch
/figma-sequence "Thanh toán" @docs/srs/api-contract.md    # derive from a source
/figma-sequence                                            # asks which exchange
```

Any source works: an API contract, a integration spec, a Postman collection someone described,
or the answers to the questions below.

## Approach

### Phase 0 — Connection

Per shared rules §5.

### Phase 1 — Derive the model, and name the gaps

Build the __fact-list__:

1) __The one scenario__ this diagram covers, named as a sentence.
2) __Participants__, in the order the exchange flows, each with its `kind`.
3) __Every message in order__: from, to, what is actually sent, and whether it is a call, a
   reply or fire-and-forget.
4) __What comes back__ for each call — status, payload shape, and the failure.
5) __Branches__: where the exchange forks, and on what condition.
6) __Timing and limits__: timeouts, TTLs, retry counts, idempotency keys.

Anything the source does not say, __ask__: *what comes back if the gateway times out?* ·
*is that call retried, and how many times?* · *who is told when it fails?*

### Phase 2 — Ask the one question that changes the drawing

__Which failure path do you want in this diagram?__ A sequence diagram carries one scenario
well and three badly. Ask which single failure matters most (timeout / rejection / wrong
input), draw that one as the `alt`'s else branch, and offer the others as separate diagrams
rather than cramming them in.

### Phase 3 — Check, then draw, in one call

Call `figma_diagram` with `type: "sequence"` and `options: { checkFirst: true }`: it checks the model and
__draws only if there are no findings__. Dirty → `checkedOnly: true` + the findings and nothing
is drawn; clean → it draws and returns `audit` in the same call. (`options: { dryRun: true }`
is still there for iterating on a model you expect to be wrong.)

Read every warning. The ones specific to this kind:

| Warning | What it usually means |
|---|---|
| Reply with no call to answer | the reply's `from`/`to` are the wrong way round, or the call is missing |
| Call with no reply | the spec never says what comes back — ask, or mark it `async` |
| `alt` has no else | say what happens otherwise, or make it an `opt` |
| Fragment skips a message | the block is not a contiguous run of time — reorder or split |
| Message has no label | an arrow that does not say what is sent is the argument you will have later |
| Participant with no messages | it is not in this scenario |

Fix the model, re-dry-run, then draw.

### Phase 4 — Draw, verify, report

1) Place the frame clear of what is on the page (shared rules §7).
2) Draw.
3) Read `audit` from the same result — it is the render-side check (overflow, clipping,
   truncation). Fix anything it reports. No second call for it.
4) One `screenshot` per SET of diagrams at the end, not one per frame — skip it when
   `audit` is clean and the human is watching Figma live.
5) Report per shared rules §11.

Tell the user the one live-editing fact that matters here: **dragging a participant moves its
whole column** — lifeline, bars, every arrow touching it, the fragment boxes spanning it — and
nothing moves in time, because the row a message sits on IS its order.

## What the machine does NOT check

* whether the endpoints, payloads and status codes are the real ones;
* whether the order is the order the systems actually run in;
* whether a retry is safe to retry (idempotency is a business fact, not a drawing one);
* whether the failure you drew is the failure that actually happens most.

Those are for the person who owns the integration. Put the diagram in front of them and ask.‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍


<!-- wm:10031a355241b873619b88f1cbdef99a -->
<sub>Tài liệu thuộc bộ AI4BA Reqwise Figma MCP — bản quyền hoangphan.blog</sub>
