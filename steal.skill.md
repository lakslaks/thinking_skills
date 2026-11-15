# Description
Reverse engineers why something works (a presentation, idea, post, product, or thought process) and extracts a reusable pattern.

# Usage
- /steal this pitch deck [attach]. Give me the structure and techniques I can reuse for my seed round.
- /steal how Notion grew. Which moves transfer to a small B2B tool?

# Purpose
Turn an example into a reusable pattern adapted to the user's own context.

# Grounding
If the user supplied the source (pasted or attached), treat it as primary. If they only named it, use the other sources in the search order to understand it. Separate what is observed in the source from what is inferred about why it works.

# Workflow
1. Identify the source. If it is missing, ask for it in one line.
2. Break it into parts: structure, techniques, reasoning, incentives.
3. Explain the mechanism behind each part: why it works, not just what it says.
4. Turn the mechanisms into a reusable pattern or template.
5. If the user named where they will apply it, adapt the pattern to that context. If not, ask once.

# Output Format
**Why it works:** 3-5 mechanisms, one line each

**The pattern:** the reusable skeleton

**Your version:** the pattern applied to the user's context

**What doesn't transfer:** anything that only worked because of the original's context

# Rules
- End with something the user can use, not analysis alone.
- Do not reproduce long passages from the source. Describe and paraphrase.
- Label inferences as inferences.
