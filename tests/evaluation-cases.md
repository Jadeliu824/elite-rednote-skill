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

## 10. Opening — rejects a cliché

**Input:** a draft that opens with "在当今这个快速变化的时代……".

**Pass:** the opening is rejected per `editorial-guidelines.md` §6.1; the piece is reopened at a concrete entry (event / 反差 / 数据冲击).

## 11. Specificity — abstract claims fail

**Input:** a draft of only abstract claims ("这背后反映了更深层次的逻辑") with no case or number.

**Pass:** fails the §8 delete test and the ≥2 concrete-source-types rule; revised to include at least two of: case, data, primary source, decision, history, stakeholder interest, mechanism, scene.

## 12. Contrast test — draft → edit → score

Run for at least three topics (WORLD, CAPITAL, BUSINESS). For each: produce an unedited first draft; run the three editing rounds (`workflows/content-production.md` Step 5); show the before/after and what each round fixed; score the final via `workflows/quality-assurance.md` §2.

**Pass:** each final ≥ 85, with concrete reasons per dimension; the draft's AI-flavor/template problems are visibly gone.

## 13. Commercial — Traffic note does not sell

**Input:** a WORLD traffic note (content role = Traffic).

**Pass:** no product promotion, no Product Bridge, CTA limited to 关注/收藏/讨论 (or none); free value complete.

## 14. Commercial — natural Product Bridge

**Input:** a CAPITAL trust note whose topic has a verified 已存在 entry in `product-inventory.md`.

**Pass:** the Product Bridge leads naturally from the reader's next learning need; no "完整版请购买"; references only content the inventory confirms.

## 15. Commercial — no product connection

**Input:** a note whose topic has no matching inventory entry.

**Pass:** recorded as "无直接产品关联"; no product CTA; no forced link.

## 16. Commercial — no fabricated product claims

**Input:** a draft that advertises a knowledge-base feature not in `product-inventory.md`.

**Pass:** the claim is rejected (QA §3 commercial check); the piece cannot pass until the claim is removed or the inventory updated and dated.

## 17. Notion 选题读取（Test 1）

**Input:** query the content-plan Data Source (`references/notion-content-plan.md`).

**Pass:** reads 栏目/日期/优先级/状态; excludes 取消 and 已发布; does not invent topics not in the DB; records each record's page_id for backfill. If the DB is 404 (not shared), it stops and asks the user to connect it — never fabricates tasks.

## 18. 标题优化（Test 2）

**Input:** the Anthropic IPO case ("1.5万亿市值，背后是一张9000亿的账单").

**Pass:** identifies it as abstract/news-like (no conflict, no reader why); produces 5 directions (冲突/反常识/悬念/数字/读者利益) each with click motive + risks; final title promises only what the post delivers; no number inflation.

## 19. 封面优化（Test 3）

**Input:** the same topic.

**Pass:** rejects the generic server-room stock photo; produces ≥3 visual directions (editorial photography / conceptual / data-financial) each with subject, composition, light/color, mood, title placement; follows Midnight Sky brand rules; has a real visual subject.

## 20. 发布后回填（Test 4）

**Input:** user provides link + partial data.

**Pass:** updates the original page_id (not a new record); status → 已发布; link written; structured 复盘 written; missing data marked 未采集 (not invented); time window labeled.

## 21. 经验反哺（Test 5）

**Input:** a prior 复盘 exists (e.g. "封面机房图 → 低点击").

**Pass:** the next production reads the learning log and proposes a different cover direction + title test; distinguishes fact (low exposure) from hypothesis (cover caused it).
