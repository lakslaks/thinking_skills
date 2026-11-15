# Description
Answers in three lines maximum.

# Usage
- /brief should I use Postgres or MongoDB for this?
- /brief summarize this article [paste]

# Purpose
Give the shortest useful answer.

# Grounding
Use only the user prompt. Do not retrieve external information.

# Workflow
1. Give the answer in at most 3 lines.
2. Line 1 is the answer. Lines 2-3 are the most important reason or caveat.
3. No preamble, no lists, no closing offer.

# Output Format
Plain text, 3 lines or fewer.

# Rules
- Never exceed 3 lines. Cut the least important point instead.
- If the question truly cannot be answered in 3 lines, say so in one line and give the best short answer.
