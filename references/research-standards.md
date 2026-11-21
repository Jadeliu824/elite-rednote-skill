# ELITE Research Standards

Load this before Stage 2 (research). These rules are non-negotiable: ELITE content is only as good as its evidence.

## 1. Source hierarchy

Work down the hierarchy; prefer the top.

1. **Primary sources** — the thing itself: the original interview/transcript, the filing, the financial statement, the product, the person's own published words, the dataset. Use whenever possible.
2. **Reliable secondary sources** — reputable outlets, well-sourced summaries, expert commentary that cites its own sources. Use for context and to confirm interpretation.
3. **Weak sources** — unsourced social posts, rumor threads, anonymous quotes, "据传/网传". Use only as a lead to chase back to a primary source, never as the basis for a claim.

## 2. Source quality by pillar

- **WORLD / CAPITAL:** prefer primary data and official statements — filings, central-bank or regulator releases, official company communications, reputable financial/business press. Market commentary is secondary, not the claim.
- **BUSINESS:** prefer first-person founder/investor accounts, earnings calls, teardowns, and sourced reporting. Watch for PR spin; verify "the real reason" against more than one source.
- **BUILD:** first-person by definition. Own experience is primary; external claims still need their own sources.

## 3. Verification rules (run on every claim)

- Verify **every date, statistic, name, and number** against a source. If you cannot find a source, drop the claim — do not soften it with "大概/据说/有报道称" and keep it.
- Verify **quotations** against the original. A quote that is paraphrased, translated, or second-hand is labeled as such, or dropped.
- Confirm **freshness**: a "recent" event must be dated. If a source is old, say so and say why it is still relevant (see Stage 1 note in `workflows/topic-discovery.md`).
- Distinguish **fact / interpretation / opinion** and keep them separate in the output:
  - **Fact:** what happened, verifiable.
  - **Interpretation:** a reasoned reading of the facts (yours or a source's).
  - **Opinion:** a preference or value judgment.
  - A post may contain all three, but must not blur them — the reader should always know which is which.

## 4. Hard red lines

- **Never fabricate** sources, quotations, statistics, or case studies. Inventing a source to fill a gap is worse than leaving the gap.
- **Never attribute** a claim to a named source you did not actually find. If you cannot name the source, the claim is unsupported.
- **Never inflate** numbers or outcomes to make a point land. If the real number is weak, that is the content.
- If asked to cite something you could not verify, say so plainly instead of producing a plausible-looking reference.

## 5. Source tracking

Every research pass produces a `research-notes` record (template: `templates/research-notes.md`) that ties each claim to its source. The record exists so that:

- The QA stage can re-verify the claim.
- A future performance review or correction can trace a claim to its origin.

Record at minimum: the claim, the source (name/URL/date), and whether it is primary or secondary.

## 6. Stopping rule

Research supports the argument — it is not an end in itself. Stop when:

- The central claim is verified and the argument has enough evidence to stand.
- You are adding sources that change nothing about what the post will say.

Do not collect sources for volume. A post with three solid sources beats a post with fifteen thin ones.
