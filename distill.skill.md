# Description
Extracts the context, intent, and core message of a long paper or document, separates what carries the argument from the chaff, and maps what is worth reading.

# Usage
- /distill this paper [attach]
- /distill this 40-page strategy doc. I need to decide whether to fund it.
- /distill [paste]. I only have five minutes.

# Purpose
Go beyond a shorter copy of the document. Work out what it is for, what it asks of the reader, and which parts carry the argument, and set the rest aside.

# Grounding
Use the document from user content or attached files as the primary source. Use other sources in the search order only to supply context the document assumes, such as the author's earlier work, the thread it belongs to, or defined terms, and label that as coming from outside the document. If only part of the document is available, say so before anything else.

# Workflow
1. Identify the document: type, author, audience, date, and length. Note whether you have all of it or only part.
2. Read for structure first: headings, abstract, introduction, conclusion, and repeated terms. Find where the author states their own purpose, thesis, and ask.
3. Establish the context: what prompted the document, what decision or conversation it belongs to, and what the reader is assumed to know.
4. Find the intent: the job the document is doing, such as informing, persuading, justifying, requesting a decision, defending, selling, or exploring. Note any gap between the stated and the apparent intent, and mark it as inferred.
5. State the core message in one sentence a non-expert could repeat, then the so what and the ask.
6. Map the argument: the main claims, the reasons and evidence for each, and how they connect. Mark each part load-bearing (the argument fails without it) or supporting.
7. Set aside the chaff: background the audience already knows, repetition, hedging, tangents, citation padding, and restated results. Note where each sits so the user can check.
8. Test the spine: the weakest link, unsupported leaps, thin evidence, and what is new versus restated.
9. Give a reading map: sections to read in full, skim, and skip. If the user said what they need the document for, weight everything to that purpose. If not, assume they need to decide whether and how to engage with it.

# Output Format
**Context:** 2-3 lines: who wrote it, for whom, and what prompted it

**Intent:** what the document is trying to do, and the ask. Stated versus apparent, with a confidence

**Core message:** one sentence, then the so what

**Argument spine:** 3-5 claims, each with its key support, tagged load-bearing or supporting

**Set aside:** the chaff by type, with section references

**Weak points:** 2-4, limited to the argument and its evidence

**Reading map:** Read, Skim, Skip, with section references

**Limits:** anything you could not see, and anything inferred

# Rules
- Extract, do not compress. Do not shorten everything evenly. Drop what does not carry weight and say what you dropped.
- Add nothing the document does not say. Point to sections for key claims. Use short quotes only and paraphrase the rest.
- Mark intent and context that you inferred as inferences. If the purpose is ambiguous, give the two most plausible readings.
- Judge the argument, not the writing. Do not rate quality unless asked.
- Differs from a summary: a summary shrinks the document proportionally and keeps the chaff, /distill finds what it is for and what carries the weight. Differs from /steal, which extracts a reusable pattern.
