# Description
Controls how knowledge sources are shown for the rest of the conversation.

# Usage
- /sources off
- /sources inline

# Purpose
Let the user switch between no source output, a source list at the end, and inline citations.

# Grounding
None. This is a setting, not a task.

# Workflow
1. Read the argument: off, footer, inline, or reset.
2. Apply it as the session setting. It overrides each skill's source_display default.
3. Reply with one line confirming the new setting, for example 'Sources: inline.'
4. If the argument is missing or unknown, list the four options in one line.

# Output Format
One line confirming the setting.

# Rules
- off: no source output.
- footer: a Knowledge Source list at the end.
- inline: short markers in the text, such as [1] or (file name).
- reset: return to each skill's default.
- Floor: for skills with grounding_mode required, m365_required, or web_required, off is not allowed. Use footer and tell the user.
