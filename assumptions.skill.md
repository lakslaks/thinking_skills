# Description
Surfaces the hidden assumptions behind a plan or belief and flags the ones most likely to be wrong.

# Usage
- /assumptions my plan to launch a paid newsletter
- /assumptions this revenue forecast [paste]

# Purpose
Make unstated assumptions visible, rank them by risk, and give the cheapest way to test each.

# Grounding
Use the plan or belief from user content or attached files. Use the other sources in the search order to check whether an assumption is supported by data when available. If none is found, rank by reasoning and say so.

# Workflow
1. List the assumptions the plan depends on, especially unstated ones.
2. Score each on how likely it is to be wrong and how bad it would be if it were.
3. Pick the top 3-5 that matter most.
4. Suggest a cheap way to test each.

# Output Format
A short table:

| Assumption | Risk if wrong | Likelihood wrong | Cheapest test |
|---|---|---|---|

Then one line: **Riskiest:** the single assumption to test first.

# Rules
- Focus on assumptions the user has not noticed, not the obvious ones.
- Keep each cell short. Skip trivial assumptions.
- Do not claim an assumption is false without evidence. Say 'likely weak' or 'untested'.
