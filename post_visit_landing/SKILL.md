---
name: post-visit-landing
description: 为帆软 CSM 生成拜访后收敛材料、场景优先级、指标建设路径、Quick Win MVP、客户汇报材料与下次跟进建议。适用于录音转写、会议纪要、现场标注已形成但需要快速沉淀业务经验和落地方案的场景；如提供 Pre-Visit 输出，可自动做前后对照与场景收敛。
metadata:
  short-description: 帆软 CSM 拜访后收敛与落地方案
---

# Post-Visit Landing

用于 CSM 在拜访后把录音、纪要和现场反馈收敛成可推进、可汇报、可交接的方案。

## 平台适配说明

本 Skill 按公司平台结构组织，仅依赖：

- `SKILL.md`
- `REFERENCES/`
- `SCRIPTS/`

不要依赖 `examples/`、`assets/` 或 `README.md`。若需要模板，读取 `REFERENCES/templates/`。

## 何时使用

- 用户要把拜访录音、转写、会议纪要整理成落地方案
- 需要从现场材料里提炼业务经验、真实场景、指标口径和推进路径
- 需要把 Pre-Visit 的预判与现场反馈做前后对照，验证哪些场景成立、哪些要调整

## 输入要求

### 必填

- `transcript`
- `transcript_quality`：`完整清晰` / `部分模糊` / `碎片化`
- `csm_annotations`

### 建议补充

- `skill1_output`
- `meeting_date`
- `meeting_participants`
- `audio_clarifications`
- `customer_industry`
- `customer_bi_status`
- `visit_goal`

### 信息不完整时

- `transcript_quality` 缺失：先追问质量等级
- `transcript` 太短或 `csm_annotations` 基本为空：先返回补齐问卷
- `skill1_output` 缺失：不中断，但在摘要中明确“仅基于现场材料收敛，无 Pre-Visit 基准做对照”

## 执行流程

1. 先做信息完整性检查。
2. 根据 `transcript_quality` 选择输出深度。
3. 先提取业务经验性内容，再收敛场景，不要反过来。
4. 若有 `skill1_output`，逐项判断：被验证、被否定、未涉及、现场新增。
5. 只对 P0/P1 场景展开指标建设路径和看板建议。
6. 所有推荐都必须带至少 1 个 `Quick Win MVP`，周期控制在 2-4 周。
7. 客户汇报材料必须能直接复制到邮件或 PPT。
8. 生成完成后，必须按 [REFERENCES/quality_checklist.md](REFERENCES/quality_checklist.md) 逐条自检；若任一关键项不满足，先修正再输出。

## 弱模型输出策略

当运行在 GLM、DeepSeek 或其他上下文/推理能力一般的模型上时，不要一次性追求完整大文档。优先分段 handoff：

1. 第 1 次只输出：拜访摘要、录音质量判断、业务经验性内容。
2. 第 2 次输出：场景收敛清单，逐项判断 Skill1 基准、现场新增、现场否定。
3. 第 3 次输出：P0/P1 指标建设路径和看板搭建建议。
4. 第 4 次输出：推进建议、客户汇报材料、下次跟进建议、自检结果。

每段结尾必须给出“handoff 摘要”，包括已完成内容、仍缺什么、下一段要继续输出什么。

## transcript_quality 处理规则

- `完整清晰`：正常输出 8 节，业务经验建议不少于 5 条
- `部分模糊`：只写有原文支撑的判断，并给关键结论标注置信度
- `碎片化`：不输出完整方案，只输出“场景对齐草稿 + 待确认清单”

详细规则见 [REFERENCES/transcript_quality_rules.md](REFERENCES/transcript_quality_rules.md)。

## 输出要求

按以下顺序输出：

```text
0. 开头目录
1. 拜访总结摘要
2. 业务经验性内容
3. 场景收敛清单
4. 指标建设路径
5. 看板搭建建议
6. 推进建议表
7. 客户汇报材料
8. 下次跟进建议
```

### 硬性约束

- 业务诉求必须能回溯到录音原文、纪要或 `csm_annotations`
- 模糊内容进入“口径澄清清单”，不要替客户做决定
- 落地可行性判断至少覆盖：数据 readiness、技术难度、周期、风险、ROI 假设
- 默认 Markdown 表格输出；需要富文本可参考 [REFERENCES/templates/output_template.html](REFERENCES/templates/output_template.html)
- 若用户需要打印、转 PDF、复制到飞书或钉钉，优先使用 print 样式或 [REFERENCES/templates/markdown_only_template.md](REFERENCES/templates/markdown_only_template.md)

## 参考资料导航

按需读取，不要一次性全加载：

- 产出结构定义：[REFERENCES/deliverable_schema.md](REFERENCES/deliverable_schema.md)
- transcript 质量规则：[REFERENCES/transcript_quality_rules.md](REFERENCES/transcript_quality_rules.md)
- 业务经验分类：[REFERENCES/business_experience_taxonomy.md](REFERENCES/business_experience_taxonomy.md)
- CSM BA 分层：[REFERENCES/csm_ba_layers.md](REFERENCES/csm_ba_layers.md)
- 分阶段实施路径：[REFERENCES/implementation_phases.md](REFERENCES/implementation_phases.md)
- 输出自检清单：[REFERENCES/quality_checklist.md](REFERENCES/quality_checklist.md)
- 客户版简报模板：[REFERENCES/templates/customer_brief_template.html](REFERENCES/templates/customer_brief_template.html)
- 使用反馈记录：[REFERENCES/feedback_log.md](REFERENCES/feedback_log.md)

## 客户汇报材料切片

第 7 节“客户汇报材料”默认先在主文档中完整生成，再按 [REFERENCES/templates/customer_brief_template.html](REFERENCES/templates/customer_brief_template.html) 切片输出客户版。

客户版只保留：

- 一句话总结
- 推荐场景一页纸
- 预期价值
- 建议交付时间
- 需要客户配合事项
- 下一步安排

客户版不得暴露内部判断、置信度、当前阻塞、否定标签、风险评估或其他 CSM 内部备注。
