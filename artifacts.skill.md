# Description
Produces visual or structured output the user can use directly, instead of plain text.

# Usage
- /artifacts a diagram of how our signup flow works
- /artifacts a one-page summary table of this data [paste]

# Purpose
Deliver output in a usable form: a table, diagram, chart-ready data, or content laid out for Word, Excel, or PowerPoint.

# Grounding
Use only the user prompt and any data pasted in it. Do not retrieve external information.

# Workflow
1. Choose the right form: table, diagram (Mermaid), chart-ready data, slide-by-slide outline, or Excel-ready rows.
2. If the agent can create the file natively, create it. Otherwise produce paste-ready content.
3. Use the user's real data and details where provided.
4. Describe the result in one line without repeating its contents.

# Output Format
The output itself, then a one-line summary and one suggested tweak.

# Rules
- Make it usable on the first try. No placeholder text when real content exists.
- If plain text would serve better, say so in one line and offer both.
