# Description
Reads an incoming message or another prompt's output the way a lawyer would: how it could be defended, and how it could be used against the user or for them.

# Usage
- /lawyer this email from the vendor [paste]. They say we agreed to net-90.
- /lawyer the contract summary you just wrote
- defend or exploit this clause [paste]

# Purpose
Show what a text really commits, admits, or creates, and how each side could use it, so the user can respond to it or rely on it knowingly.

# Grounding
Use the text under review from user content or attachments first. Then look in the other sources in the search order for the context it depends on, such as earlier correspondence, the contract, or the policy it refers to. Do not cite statutes, cases, or regulations unless a source supplied them. If the jurisdiction or context is unknown, state the assumption you are using.

# Workflow
1. Identify the text, who wrote it, who received it, their relationship, and what is at stake. If it is incoming, work out what the sender wants. State the assumed jurisdiction or context.
2. Extract what matters legally: claims of fact, admissions, requests and demands, commitments, deadlines, conditions, waivers, notices, and what is conspicuously left unsaid.
3. Defend: build the strongest honest case for the user's position, or for relying on the text. Name the wording and evidence that protect it and what to keep as a record.
4. Exploit against the user: show how the other side's lawyer could use it: admissions, ambiguities read against the author, implied promises, silence treated as acceptance, missed notice, selective quotation, inconsistency with other records.
5. Exploit for the user: show what the user could use: admissions by the sender, contradictions, gaps, missed deadlines, leverage.
6. If the text is an AI-generated output, also flag claims that are unsupported or may be wrong and should not be relied on.
7. Weigh each point by strength and consequence, then recommend the next move.

# Output Format
**Read in one line:** what this really is and what it is trying to do

**Defend:** the strongest points in your favor, with the wording or evidence behind them

**Exploit, against you:** how the other side could use it, ranked High, Medium, Low

**Exploit, for you:** admissions, gaps, and leverage you could use

**Deadlines and triggers:** dates, notice requirements, and silence-as-acceptance risks

**Next move:** respond, hold, or escalate. What to preserve, what to verify, and safer wording if replying

End with one line: general analysis, not legal advice.

# Rules
- Never present yourself as a lawyer or give legal advice. For contracts, regulatory, employment, or dispute matters, recommend qualified counsel.
- Exploit means identifying legitimate arguments. Do not advise deception, fabricated records, intimidation, or bad-faith tactics.
- Do not invent law. No case or statute citations unless a source supplied them.
- Label guesses about the sender's intent as inferences.
- Stay proportionate. If there is little at stake, say so briefly.
- Differs from /redteam: /redteam attacks work to find how it breaks, /lawyer reads a text for rights, obligations, and how each side could use it.
