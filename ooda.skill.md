# Description
Runs the OODA loop (Observe, Orient, Decide, Act) on a fast-moving situation.

# Usage
- /ooda a competitor just cut prices and my sales dropped 15% this week
- /ooda I got a counter-offer from my current employer

# Purpose
Give a quick structured decision under uncertainty, with a concrete next step and a trigger to loop again.

# Grounding
Use the situation from user content first. Use the other sources in the search order for relevant facts when available. If none is found, proceed on what the user said and flag the gaps under Observe.

# Workflow
1. Observe: list the known facts, separated from assumptions, and note what is missing.
2. Orient: interpret the facts: context, constraints, biases, what changed, what the other parties likely want.
3. Decide: give 2-3 options and recommend one with a reason.
4. Act: give the first concrete step and what to re-observe afterwards.

# Output Format
**Observe:** facts and gaps

**Orient:** what it means

**Decide:** options, then the pick

**Act:** next step and when to loop again

# Rules
- Speed over completeness. Keep it short enough to act on.
- Always end with the re-observe trigger. OODA is a loop, not a one-off.
