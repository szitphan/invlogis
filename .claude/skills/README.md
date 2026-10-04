# Diagram skills for Reqwise Figma MCP‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Ten diagram skills that turn the diagram tools into a working method: read the source, derive the
model, ask the questions the source left open, draw once, and read what came back.
Plus two that are not diagrams: `/figma-design-system`, which builds a design system into the file, and `/figma-demo`, which writes the script for a demo that plays itself out of screens the file already has.

The tools already refuse to invent content and already proof-read the model you hand them.
What they cannot do is decide *which* diagram answers the question in front of you, interview
for the parts the spec never wrote down, or insist that somebody act on the findings. That is
what these are for.

| Skill | The open question it settles |
|---|---|
| `/figma-usecase` | What is in scope, and whose goal is it? |
| `/figma-userflow` | What does the user see next? |
| `/figma-activity` | Who does each step, and what gets handed over? |
| `/figma-bpmn` | Same process, in the OMG BPMN 2.0 notation the industry agreed on? |
| `/figma-sequence` | What is sent between systems, in what order? |
| `/figma-state` | What can this one record be, and what moves it? |
| `/figma-erd` | What do we store, and how do the pieces refer to each other? |
| `/figma-journey` | How does this feel for one person, and where does it hurt? |
| `/figma-persona` | Who are we building for, and who are we NOT? |
| `/figma-sitemap` | What pages exist, and how are they nested? |
| `/figma-design-system` | Which tokens, text styles and components does this file build on? |
| `/figma-demo` | Which screens does the client see, for how long, with what narration? |

`reqwise-diagram-rules.md` holds what the ten diagram skills share — the connection gate, the four levels of
"correct", the findings loop, frame placement, verification, redrawing. Each `SKILL.md`‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍
references it and carries only what is genuinely its own.

## Install‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Copy the whole directory into your workspace's skills folder, keeping the layout — the
`SKILL.md` files reference `../reqwise-diagram-rules.md` by relative path. They live under
`.claude/skills/` in this repo, which is both their home and the folder you copy from: an
agent working in the MCP repo itself gets them for free.

**Claude Code**

```bash
mkdir -p .claude/skills
cp -R /path/to/reqwise-figma-mcp/.claude/skills/* .claude/skills/
```

For every project rather than one, copy to `~/.claude/skills/` instead.

**Anything else** — point your agent at the folder:

```
Read the .claude/skills/ folder of the reqwise-figma-mcp package and install those twelve skills
the way this tool expects them.
```

They assume the MCP server is registered as `reqwise-figma` (tools appear as
`mcp__reqwise-figma__figma_diagram` and so on). Registered under another name, adjust the
`allowed-tools` line in each `SKILL.md`.

## Standalone, with a workspace bonus‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Nothing here requires a particular folder layout. Give a skill a pasted spec, a tagged file, a
meeting note, or nothing at all and it will interview you. If the workspace happens to hold
BA documents — an SRS, a brainstorm, a schema, a wireframe index — the skills read them
instead of asking questions you have already answered.

## What they will not do for you‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍

Each skill closes by saying which of its findings a machine checked and which it did not. The
short version, worth internalising before you use any of them:

> A drawing that returns no warnings has passed **call shape**, **rendering** and **notation**.
> It has said nothing at all about whether it matches reality.

That last check is yours. The diagram is how you start the conversation that makes it true.‍​‌‌‌​​‌‌‌​‌‌‌‌​‌‌‌‌‌‌‌​​​​‌​​​‌​‌​​‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​​​​​​‌‌​‌​‌‌​​​​‌‌​​​​​​‌​​​​​​​​‌‌‌‌​‌‌‌‌‌‌‌​​‌​​‌‌‌​​‌​​​​‌‌‌​‌‌‌‌‌​‌​​‍


<!-- wm:aca59f6017c1910577c791eb8337d44e -->
<sub>Tài liệu thuộc bộ AI4BA Reqwise Figma MCP — bản quyền ai4ba.com</sub>
