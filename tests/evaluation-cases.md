# Evaluation Cases

Run these to validate that the skill produces the right behavior. Each case states the input, what to check, and the pass criteria. A case is a *test*, not a demonstration — it must be able to fail.

## 1. Topic scoring — rejects a weak topic

**Input:** candidate topic "5 个高效工作习惯" with no source, no development, no tension.

**Check:** run Stage 1 scoring.

**Pass:** weighted score < 3.0, topic rejected, reason recorded (low originality / no discussion potential). It must not be polished into content.

## 2. Topic scoring — accepts a strong topic

**Input:** candidate topic "Figma 主动退出 Adobe 200 亿美元并购" (see `examples/good-examples.md`).

**Check:** run Stage 1 scoring.

**Pass:** weighted score ≥ 4.0, with a rationale naming *why this one* and its known weakness (2023 事件，需说明为何今天仍值得看).

## 3. Angle test — rejects a summary

**Input:** a well-sourced but argument-free draft ("2022 年 Adobe 宣布收购 Figma… 2023 年 12 月终止").

**Check:** run Stage 3 angle tests.

**Pass:** fails "originality / judgment" test; the piece is returned to Stage 3, not rescued in writing.

## 4. Writing — removes AI flavor

**Input:** the "在当今时代…底层逻辑…总而言之" paragraph from `examples/bad-examples.md` §2.

**Check:** run the Stage 4 rewrite passes.

**Pass:** every banned phrase removed; sentences ≤ ~40 chars; the rewrite says something concrete and reads as a person.

## 5. Visual — correct tokens and composition

**Input:** a completed `editorial-brief` for a BUSINESS topic.

**Check:** run Stage 5 and produce a `visual-spec`.

**Pass:** background is exactly `#16151D`; primary text `#F2EFE9`; at most one accent (`#D4AF37` or `#C7C5BF`); cover uses the split-page structure (image upper field + type lower field) with a single dominant headline.

## 6. Optimization — no keyword stuffing

**Input:** a finished carousel copy.

**Check:** run Stage 6.

**Pass:** title reads as a real claim (not a keyword dump); 2-5 natural search phrases; 3-8 hashtags; description is prose with the search terms appearing once and no CTA.

## 7. QA gate — rejects weak output instead of shipping it

**Input:** a carousel whose central claim is a summary (no judgment) and whose cover uses a gold-bordered marble background.

**Check:** run Stage 7 against it.

**Pass:** "argument quality" and "visual consistency" checks fail; the verdict is *return to Stage 3* (not "fix a phrase"). The piece is not delivered.

## 8. Fabrication refusal — drops an unverifiable claim

**Input:** a draft that cites a "据内部人士透露" statistic that cannot be traced to any source.

**Check:** run Stage 2 verification + Stage 7 factual accuracy.

**Pass:** the claim is dropped (or explicitly labeled unsupported), never silently kept with "据传/大概" softening. No fabricated source is produced.

## 9. End-to-end — one full production

**Input:** any fresh, real candidate topic in WORLD/BUSINESS/CAPITAL/BUILD.

**Check:** run the full 8-stage pipeline.

**Pass:** all eight templates/records are filled; the QA checklist passes all nine checks; the output is brand-consistent, fact-checked, and judgment-driven. A defect found at any later stage routes back to the correct earlier stage, not to a hack at the end.
