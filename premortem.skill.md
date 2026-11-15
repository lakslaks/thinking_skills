# Description
Assumes a plan has already failed and works backwards to find why.

# Usage
- /premortem our Q1 product launch [paste plan]
- /premortem I quit my job to freelance, 12 months

# Purpose
Find the most plausible causes of failure before starting, and set up early warnings and prevention.

# Grounding
Use the plan from user content or attached files as the base. Use the other sources in the search order for relevant precedent or constraints when available. If none is found, continue from the plan alone.

# Workflow
1. State the plan and what success looked like.
2. Write as if the failure already happened and list the most plausible causes across people, process, market, tech, timing, and dependencies.
3. Rank causes by likelihood and impact.
4. For the top causes, give an early-warning sign and a prevention step to take now.
5. Define kill criteria: the point at which to stop or change course.

# Output Format
**What went wrong:** 4-6 causes, ranked, in the past tense

**Early warnings:** what you would see first, for the top 3

**Do now:** prevention steps before starting

**Kill criteria:** when to stop or change course

# Rules
- Be concrete and plausible, not dramatic.
- Include at least one cause about people or process, not only external events.
- Mark hypotheses as hypotheses. Do not present predictions as facts.
