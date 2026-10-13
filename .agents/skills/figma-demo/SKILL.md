---
name: figma-demo
description: Turn screens already in a Figma file into a demo that plays itself — a link that walks the flow like a video, no clicking and no presenter, for a client call, a standup or a ticket. Use when someone says "quay demo", "cho khách xem luồng này", "làm bản tự chạy".
allowed-tools: Read, Glob, Grep, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_write
user-invocable: true
argument-hint: "<what to demo> [who is watching]"
---
<!-- Licensed to test.innvie@gmail.com — Order 3D3A2HZRY -->

# /figma-demo — a prototype that plays itself‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Read the connection gate in `../reqwise-diagram-rules.md` first (§ 5, *Before
anything else: is the write path open?*): plugin connected, one window,
`figma_status` before anything else, and a dry run is NOT a connection probe.
The rest of that file is about diagrams; a demo reel is not one, so the steps
below replace its drawing rules.

Field tables and defaults: `figma_docs(section="demo", level="cheat")`. Read
that once before your first build. The full section only when a finding needs
explaining.

## Goal‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

One link the user can open in front of an audience, where the screens advance
by themselves. The mechanism is trivial — Figma's *After delay* trigger — so
the mechanism is not the work.

**The script is the work.** Which screens, in what order, how long each one
holds, and what one line of narration goes with it. A machine cannot decide
that: it depends on who is watching and what they need convincing of. That is
what this conversation produces.

Output: a `Demo` page in the file, a play link, and a row in the plugin panel's
Demo list with a ▶ button the user can press again next month with no agent
running.

## The one rule that makes or breaks this‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

**Never wire After-delay onto the real screens.** `figma.buildDemo` clones them
onto a page of its own for exactly this reason. Reaching for
`figma.setReactions` to flip a real screen's trigger from On-click to After
delay is the trap: the file then holds *either* a working prototype *or* a demo,
and the user is one forgotten toggle away from sending a client a file whose
screens jump on their own. If you catch yourself writing `AFTER_TIMEOUT` by
hand, stop — the op exists.

## Step 1 — find out what is already there‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Do not ask the user for node ids. Read them.

1) `figma_read` op `get_page_model` — if the page has a **userflow**, the flow
   already knows the order the screens go in, and that is the best starting
   point for a script there is.
2) `figma_read` op `get_design_context` (sparse, page-level) — the screens that
   exist, with ids.
3) `figma_read` op `list_demos` — a demo for this flow may already exist. If it
   does, **rebuild or edit it**; a second demo of the same flow is how a file
   ends up with four pages nobody trusts.

## Step 2 — propose the whole script, then let the user edit it‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Write the script out in full and show it. **Do not interview step by step** —
six questions cost six round-trips and produce a worse script than one draft the
user corrects in a sentence.

```
Kịch bản: "Luồng đặt vé" — 6 bước, ~14s, lặp lại

1. Trang chủ            1.5s  "Khách mở app"
2. Kết quả tìm kiếm     2.0s  "Chọn chuyến phù hợp"
3. Chọn ghế             3.0s  "Chọn 4 ghế cạnh nhau"
4. Thanh toán           3.0s  "Chuyển khoản, giữ ghế 10 phút"
5. Đang xử lý           0.6s  —
6. Đặt vé thành công    2.5s  "Vé về ngay trong app"
```

Then ask — with `AskUserQuestion`, and only about what actually changes the
script. **Always ask the pace**; it is the one setting nobody's default is right
about, because the same reel wants 10 seconds in a standup and 25 in front of a
client who has never seen the product.

* **Tốc độ?** — `pace: "fast" | "normal" | "slow"` (×0.6 / ×1 / ×1.5 on every
  dwell time). Put the resulting total in each option's description, computed
  from your own draft — "Nhanh · ~10s", "Vừa · ~16s", "Chậm · ~24s" — so the
  choice is about a number the user can picture, not an adjective.
* **Ai xem?** — khách hàng (câu chuyện, có phụ đề) / nội bộ (nhanh, không phụ
  đề) / dev (từng state, chậm). This one you may skip when the user already
  said who it is for.
* **Có phụ đề không?** — and in which language. Captions are the narration; with
  no presenter they are the only voice.

Everything else has a default that is right more often than a question about it
is worth. Do not ask about `transition`, `loop`, `gap`, `captionAt`,
`introCard` or `endCard` — but DO pass `introText`/`endText` in the same
language as the captions (see *The bookends*, below): those two cards are the
first and last thing the audience reads.

After the build, say the real total back (`seconds` in the result) — the pace
multiplies, so a script the user pictured at 16s runs at 24s on slow.

### The timing table

The single thing that separates a demo from a slideshow. A demo where every
screen holds for two seconds reads as a PowerPoint.

| the screen is | seconds | why |
| --- | --- | --- |
| a pass-through (loading, splash, a toast) | 0.4–0.8 | It only has to be seen, not read |
| a normal step | 1.5–2 | Long enough to take in one change |
| the point of the demo | 3–4 | The thing you want remembered |
| a screen with a caption to read | +1 | The caption is text; text takes time |

Total under ~60s for a client, under ~30s for a standup. Past 90s the tool warns
and it is right.

### Captions

* One idea, under about 60 characters. It is a subtitle, not a paragraph.
* Say what the **user** is doing ("Khách chuyển khoản"), not what the screen is
  ("Màn hình thanh toán" — the audience can see that).
* Leave a pass-through screen without one. Silence is a beat, not a hole; the
  tool only warns when *some* steps have captions and others do not, because
  that is narration that stops mid-sentence.
* **The position is not yours to vary.** Every caption sits in the same place
  for the whole reel — bottom, or top when a cursor lands low on any screen.
  Subtitles that move between steps read as broken, and the transition makes
  the pill visibly fly across the screen. `captionAt: "top" | "bottom"` forces
  it; there is deliberately no per-step option.

### The bookends

A reel that starts on screen 1 and restarts the instant the last screen is done
is unreadable from the outside: a viewer who glanced away cannot tell the second
pass from the first, and a recording of it opens mid-flow with no idea what it
is. So the build wraps the steps in two cards, each drawn over a dimmed clone of
the screen beside it:

* **Opening**, 4s — the demo's name. It is the reel's starting point, so it is
  also the first frame `figma_record` captures.
* **Closing**, 4s — "✓ Demo complete", and nothing under it. That pause is what
  tells the room the flow is over and what comes next is a repeat; a countdown
  line was tried and cut, because the last thing the audience reads should not
  be plumbing.

* Put both in the audience's language: `introText: "Luồng đặt vé"`,
  `endText: "Đã xong demo"`. `introSubtext` takes a smaller second line (who it
  is for, which build).
* `introSeconds` / `endSeconds` (1–15) are the dwell times `pace` does NOT
  scale — "fast" is exactly the reel where the loop is hardest to spot.
* Turn them off only when the user explicitly wants a seamless loop (a screen on
  a wall at a booth). The tool warns when a looping reel has no ending.

## Step 3 — build it, in one call

The script goes in as one object. Write it as JSON first when it helps you think
— the fields are the same:

### The script‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

```json
{
  "name": "Luồng đặt vé",
  "steps": [
    { "screenId": "12:340", "seconds": 1.5, "caption": "Khách mở app" },
    { "screenId": "12:411", "seconds": 2, "caption": "Chọn chuyến phù hợp" },
    { "screenId": "12:508", "seconds": 3, "caption": "Chọn 4 ghế cạnh nhau" },
    { "screenId": "12:560", "seconds": 3, "caption": "Chuyển khoản, giữ ghế 10 phút" },
    { "screenId": "12:588", "seconds": 0.6 },
    { "screenId": "12:602", "seconds": 2.5, "caption": "Vé về ngay trong app" }
  ],
  "pace": "normal",
  "loop": true,
  "introText": "Luồng đặt vé",
  "endText": "Đã xong demo"
}
```

```js
const demo = await figma.buildDemo(script);
console.log(demo.demoId, demo.seconds, demo.link);
```

One call clones the screens, wires the delays, draws the moving cursor and the
caption pills, sets the flow starting point and returns the play link. Do not
split it into per-screen calls.

Each step becomes **two** frames when the cursor has somewhere to travel (the
screen with the cursor where the last click left it, then the same screen with
it on the button), so `frames` in the result is larger than `steps` — that is
the glide, not a bug. The two bookend cards are one frame each on top of those.
`seconds` counts the glides and the cards, so quote `seconds` back to the user
and not your own arithmetic.

**Rebuilding is the same call** with the same `demoId` — the old copies are
removed first. That is the answer to "the design changed": rebuild, never build a
second one.

That stored script froze the defaults it was built with — `buildDemo` persists
the normalized plan, so every default is an explicit value in it. Changing a
default in the tool does not reach a demo that already exists: to pick up a new
one, DELETE that field from the spec before rebuilding.

`getDemoSpec` gives you that script back, and its seconds are REAL seconds:
`pace` comes back `"normal"` because the factor is already in them. So a second
`pace` compounds — "chậm lại chút" on a reel already built fast is `pace:
"slow"` over what is there (×1.5), which is what the user means. Never re-apply
the original pace on a rebuild.

## Step 4 — act on the warnings

`warnings` are findings about the **script**, and they are part of the
deliverable. Never pad a field to silence one.

| warning | what to actually do |
| --- | --- |
| runs Xm — past ~90s an audience stops watching | Cut steps. Ask which two matter least |
| steps N and N+1 are the same screen | Nothing happens between them — merge or replace |
| step N has no caption while the rest do | Add one, or drop the others' |
| no prototype link from this screen to the next | The cursor could not be placed. Either the real On-click link is missing (tell the user — that is a finding about the *prototype*), or pass `hotspot: {x,y}` |
| PAGE_LIMIT: built on "<page>" instead | Starter files cap at 3 pages. Say so; the demo works, it just shares a canvas |
| endCard is off on a looping reel | Turn it back on unless the user asked for a seamless loop — without it nobody sees where the flow ends |
| No file key available | Ask the user for the file URL once (see below) |

## Step 5 — play it, and hand it over

```js
await figma.playDemo({ demoId: demo.demoId });
```

`figma://proto/…` goes to the OS, which opens **presentation view inside the
Figma desktop app**. There is no Plugin API for entering presentation mode; this
is the only path, and it is why "play" is a URL.

Pass `open: false` when the user asked for a link rather than for the demo to
start — do not take over someone's screen mid-sentence.

Then tell them the part that outlives this session: **the plugin panel has a
Demo list with a ▶ button**, and it works with no MCP server running. Authoring
needed you; replaying must not.

### The file key, once

`figma.fileKey` is exposed only to private organization plugins, so on any other
plan the link cannot be built until someone pastes a URL of the file. Ask for it
plainly — "dán giúp tôi link file Figma (copy trên thanh địa chỉ)" — and pass it
as `fileUrl`. It is remembered in the file itself, so this happens once, not once
per demo.

## Step 6 — a video file, only if they need one

A link is the better deliverable almost every time: it is current, it is small,
and it opens in the app. Reach for a video only when the audience cannot open a
Figma link — a chat thread, a slide deck, an email to a client.

**Probe before you promise.** Machines differ here in a way nothing else in this
API does, so never say "I'll record it" before this returns `ready: true`:

```
figma_record({ op: "check" })
```

If it is not ready, relay `blockers` and `howToFix` verbatim — they are written
to be actioned, and they already name the exact app, menu and command for this
machine. Do not improvise a workaround; there usually is not one. On macOS in
particular, installing ffmpeg does **not** get past a missing Screen Recording
grant, so do not suggest it as a fix.

```
figma_record({ op: "demo", demoId: "checkout" })
→ { path: "/Users/…/Desktop/checkout.mp4", seconds: 19, bytes: 4_210_233, … }
```

**Warn the user before you start it.** It records a WHOLE DISPLAY for the
length of the reel, on their machine, right now. Anything visible on that
screen goes in the file. Let them close things first — do not fire this off
mid-sentence because it sounded like the helpful next step.

**Never ask the user how big their screen is.** `check` already measured it:
`displays` and `suggestedRegion` are in that same result. Omit `region` and the
recording crops to the main display; on a two-monitor setup where Figma is on
the other one, pass `region: "screen:2"`. Only reach for `region: "x,y,w,h"` to
crop to the Figma *window*, which is the one thing that is not measured.

Then hand over the path, the length and the size. `startedAt` says whether the
first frame is trustworthy — `prototype-rendered` means it waited for the real
render, anything else means the video may open on the app loading, and is worth
one sentence to the user rather than a surprise.

## What the machine does NOT check

The tool proof-reads the script's shape. It cannot see any of this:

* **Whether the story lands.** Six screens that each make sense can still add up
  to a demo that never shows what the product is *for*. Read the caption list top
  to bottom as prose: if it does not tell a story, the demo does not either.
* **Whether the screens are the current design.** The clones were copies taken at
  build time. A demo shown three weeks later may be showing three-week-old
  screens with total confidence. Rebuild before every showing that matters.
* **Whether the captions are true.** "Giữ ghế 10 phút" is a claim about the
  system. If the spec says 15, you have just put a lie in front of a client.
  Check narration against the spec, or against `@policies` if the page's diagrams
  carry the rule.
* **Whether the happy path is honest.** A demo of a flow that only ever succeeds
  is normal and fine — as long as nobody is deciding anything based on it. If the
  audience is deciding, say out loud that the error paths are not in this reel.
* **Whether this should have been a video at all.** If the user needs a *file*
  to send over Zalo rather than a link, say so and offer `figma_record` — see
  Step 6.

## Constraints

### Hard rules — never violate

* **Never invent a screen.** Every `screenId` is a node that exists and that you
  read from the file. A demo that references a screen the designer has not drawn
  fails loudly, which is the good case; guessing an id that happens to exist is
  the bad one.
* **Never touch the real screens' reactions.** See the rule above.
* **One demo per flow.** Check `list_demos` first; rebuild instead of adding.
* **Do not silently drop a step the user asked for.** If a screen cannot be part
  of the demo (it does not exist, it is not a frame), say which and why.

### What it cannot do, and say so when asked

No pause, no scrub, no sound. Presentation view takes no commands once it is
running — that would need Embed Kit 2.0 on a page of your own, which is a
different feature and a bigger build. A demo reel is a link that plays; that is
the whole of it.

A video file is a separate step, not a property of the reel: `figma_record`
screen-records the reel playing. See Step 6.‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍


<!-- wm:10031a355241b873619b88f1cbdef99a -->
<sub>Tài liệu thuộc bộ AI4BA Reqwise Figma MCP — bản quyền ai4ba.com</sub>
