# Description
Puts every option into one comparison table with criteria and a recommendation.

# Usage
- /matrix Notion vs Obsidian vs Coda for a 5-person team, budget matters most
- /matrix three job offers: [paste details]

# Purpose
Make options comparable side by side and recommend one against the user's stated priorities.

# Grounding
Use options and priorities from user content first. For facts such as prices and features, use the other sources in the search order when available. Mark any figure that could not be verified as unverified.

# Workflow
1. List the options. If the user gave none, suggest the realistic ones.
2. Pick 5-8 criteria that matter, using the user's priorities if given.
3. Fill one table with short, specific cells, using numbers where possible.
4. Add a recommendation based on the stated priorities.

# Output Format
One table: options as columns, criteria as rows.

Then:

**Best for [priority]:** pick

**Recommendation:** one line, with the deciding factor

**Caveat:** anything the table cannot capture

# Rules
- One table, not several. Keep cells to a few words.
- Never fill a cell with a guess presented as fact. Use 'unverified' or 'n/a'.
