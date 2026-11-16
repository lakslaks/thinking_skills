# Description
Applies first-principles reasoning to payments: decomposes a flow, cost, or risk into money movement, cost stack, and risk ownership, then rebuilds it from the hard constraints.

# Usage
- /fp-payments why does cross-border settlement take three days for us?
- /fp-payments rethink our cost per transaction [paste pricing schedule]

# Purpose
Separate what payments physics, law, and contracts actually fix from what is only habit, then derive better designs from the fixed parts.

# Grounding
Use the problem and any documents from user content first. Then use M365 content for contracts, pricing schedules, partner terms, runbooks, and incident reports. Use web sources for public rail and regulation details. Any fee, timing, or rule not found in a source is unverified. If nothing is found, reason from the flow and say so.

# Workflow
1. State the problem, the goal, the jurisdiction, and the rails and parties involved. If the jurisdiction is missing, state your assumption.
2. Map the flow from fundamentals: authorization (who agrees to pay and how they are authenticated), clearing (exchange of transaction data), settlement (actual movement of funds between institutions), reconciliation, and exceptions (refunds, chargebacks, failures). Note the timing of each step.
3. Lay out the cost stack and who earns what at each step: interchange or rail fees, scheme or network fees, processor margin, fraud and chargeback losses, operations, and the cost of funding float. No numbers unless sourced.
4. Identify who bears each risk (fraud, credit, counterparty, liquidity, operational) and where the money sits at each moment.
5. Sort every belief about the current setup: Fundamental (accounting identities, law and regulation, scheme rules you cannot change, partner terms fixed in contract), Convention (default routing, settlement timing, fee structure, product habits), or Unknown.
6. Rebuild: derive 2-3 designs from the fundamentals, for example a different rail, routing, timing, funding model, or party.
7. Test each design against the hard constraints: licensing, AML and KYC, strong customer authentication, PCI scope, partner and scheme rules, liquidity, and failure handling.
8. Recommend one and give the cheapest test: a sandbox run, a pricing request, or an analysis of past transactions.

# Output Format
**Problem and scope:** goal, jurisdiction, rails, parties

**Money flow:** authorization, clearing, settlement, reconciliation, with timing

**Cost stack and risk owners:** a short table

**Beliefs sorted:** Fundamental / Convention / Unknown

**Rebuilt designs:** 2-3, each with trade-offs and a constraints check

**Verdict:** what to keep, what to change, why

**Cheapest test:** one step

**Verify with:** compliance, legal, or the partner bank, for anything regulatory or contractual

# Rules
- Never state fees, settlement times, rail rules, or regulations from memory as fact. Ground them or label them unverified.
- Always state the jurisdiction or the assumption you used.
- Keep terms exact: authorization is not settlement, and a refund is not a chargeback.
- Do not treat a scheme or partner rule as convention because it seems arbitrary. Check the contract.
- General analysis, not legal, compliance, or financial advice.
- Differs from /firstprinciples: this skill uses payments structure and constraints as its decomposition.


# Description
Applies first-principles reasoning to payments: decomposes a flow, cost, or risk into money movement, cost stack, and risk ownership, then rebuilds it from the hard constraints.

# Usage
- /fp-payments why does cross-border settlement take three days for us?
- /fp-payments rethink our cost per transaction [paste pricing schedule]

# Purpose
Separate what payments physics, law, and contracts actually fix from what is only habit, then derive better designs from the fixed parts.

# Grounding
Use the problem and any documents from user content first. Then use M365 content for contracts, pricing schedules, partner terms, runbooks, and incident reports. Use web sources for public rail and regulation details. Any fee, timing, or rule not found in a source is unverified. If nothing is found, reason from the flow and say so.

# Workflow
1. State the problem, the goal, the jurisdiction, and the rails and parties involved. If the jurisdiction is missing, state your assumption.
2. Map the flow from fundamentals: authorization (who agrees to pay and how they are authenticated), clearing (exchange of transaction data), settlement (actual movement of funds between institutions), reconciliation, and exceptions (refunds, chargebacks, failures). Note the timing of each step.
3. Lay out the cost stack and who earns what at each step: interchange or rail fees, scheme or network fees, processor margin, fraud and chargeback losses, operations, and the cost of funding float. No numbers unless sourced.
4. Identify who bears each risk (fraud, credit, counterparty, liquidity, operational) and where the money sits at each moment.
5. Sort every belief about the current setup: Fundamental (accounting identities, law and regulation, scheme rules you cannot change, partner terms fixed in contract), Convention (default routing, settlement timing, fee structure, product habits), or Unknown.
6. Rebuild: derive 2-3 designs from the fundamentals, for example a different rail, routing, timing, funding model, or party.
7. Test each design against the hard constraints: licensing, AML and KYC, strong customer authentication, PCI scope, partner and scheme rules, liquidity, and failure handling.
8. Recommend one and give the cheapest test: a sandbox run, a pricing request, or an analysis of past transactions.

# Output Format
**Problem and scope:** goal, jurisdiction, rails, parties

**Money flow:** authorization, clearing, settlement, reconciliation, with timing

**Cost stack and risk owners:** a short table

**Beliefs sorted:** Fundamental / Convention / Unknown

**Rebuilt designs:** 2-3, each with trade-offs and a constraints check

**Verdict:** what to keep, what to change, why

**Cheapest test:** one step

**Verify with:** compliance, legal, or the partner bank, for anything regulatory or contractual

# Rules
- Never state fees, settlement times, rail rules, or regulations from memory as fact. Ground them or label them unverified.
- Always state the jurisdiction or the assumption you used.
- Keep terms exact: authorization is not settlement, and a refund is not a chargeback.
- Do not treat a scheme or partner rule as convention because it seems arbitrary. Check the contract.
- General analysis, not legal, compliance, or financial advice.
- Differs from /firstprinciples: this skill uses payments structure and constraints as its decomposition.
