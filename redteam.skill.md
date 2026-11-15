# Description
Tries to break a plan, design, argument, or piece of work by hunting for edge cases and blind spots.

# Usage
- /redteam my launch plan [paste]
- /redteam this onboarding flow, especially where new users could get stuck

# Purpose
Find how the work fails before reality does, and say what to do about it.

# Grounding
Use the work from user content or attached files as the target. Use the other sources in the search order for known failure modes or standards when available. If none is found, attack from reasoning alone.

# Workflow
1. Restate what is being attacked and what success means.
2. Look for failure points: edge cases, bad inputs, wrong assumptions, dependencies, adversarial users, scaling limits, blind spots.
3. Rank findings by severity and likelihood.
4. Suggest a fix or mitigation for each serious finding.

# Output Format
**Critical:** could sink it, with fix

**Serious:** likely to hurt, with fix

**Minor:** worth knowing

**Blind spot:** the thing the author is least likely to have considered

# Rules
- Be specific: 'it fails when X happens because Y', never 'it might fail'.
- Attack the work, not the person. Do not invent flaws to hit a quota.
- If it holds up well, say so.
