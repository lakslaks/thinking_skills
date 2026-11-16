# Description
Breaks a problem down to its fundamental truths, sorts them from convention, and rebuilds the answer from the ground up.

# Usage
- /firstprinciples why does onboarding take three weeks?
- /firstprinciples rethink our pricing model [paste]

# Purpose
Replace "that's how it's done" with a reasoned answer built only from what is actually true, and show what changes.

# Grounding
Use the problem and any documents from user content first. Use the other sources in the search order to verify the facts you treat as fundamental. Anything you cannot verify is labeled unverified. If nothing is found, reason from the problem alone and say so.

# Workflow
1. State the problem and the goal in one line, then name the conventional answer or current approach.
2. Break the problem into components and list the beliefs that support the current approach.
3. Sort each belief: Fundamental (physics, math, law, hard constraint, measured fact), Convention (habit, precedent, "how it's done"), or Unknown.
4. Keep only the fundamentals and say how each is known.
5. Rebuild: derive 2-3 approaches from the fundamentals alone, with the reasoning chain.
6. Compare with the conventional answer: what holds, what changes, and the cost or risk of departing.
7. Give the cheapest test of the key bet.

# Output Format
**Problem and goal:** one line

**Conventional answer:** one line

**Beliefs sorted:** Fundamental / Convention / Unknown, short lists

**Ground truths:** each with how you know it

**Rebuilt options:** 2-3, each with its derivation and what it changes

**Verdict:** what holds, what to challenge, and why

**Cheapest test:** one step

# Rules
- Do not call something fundamental without a reason. Label unverified facts.
- Convention is not automatically wrong. It often encodes lessons, so say what it protects against.
- Do not invent facts or numbers.
- Differs from /assumptions: /assumptions flags hidden assumptions, /firstprinciples rebuilds from what remains.
- For payments problems, use /fp-payments instead.