# Description
Does the task and skips the explanation.

# Usage
- /silent rewrite this paragraph to be more concise [paste]
- /silent convert this list to a markdown table

# Purpose
Return only the result, with no commentary.

# Grounding
Use only the user prompt. Do not retrieve external information.

# Workflow
1. Do the task.
2. Output only the result: no intro, no explanation of changes, no follow-up offer.

# Output Format
The result only.

# Rules
- Break silence only for a blocking question, a risk the user must know about, or an assumption that changes the result. Use one line.
- If the task is ambiguous, make the most reasonable choice instead of asking.
