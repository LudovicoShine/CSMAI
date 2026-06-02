---
name: post-visit-landing
description: 为帆软 CSM 生成拜访后收敛材料、场景优先级、指标建设路径、Quick Win MVP、客户汇报材料与下次跟进建议。适用于录音转写、会议纪要、现场标注已形成但需要快速沉淀业务经验和落地方案的场景；如提供 Pre-Visit 输出，可自动做前后对照与场景收敛。
metadata:
  short-description: 帆软 CSM 拜访后收敛与落地方案
---

# Post-Visit Landing

用于 CSM 在拜访后把录音、纪要和现场反馈收敛成可推进、可汇报、可交接的方案。

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
8. 生成完成后，必须按 [references/quality_checklist.md](references/quality_checklist.md) 逐条自检；若任一关键项不满足，先修正再输出。

## transcript_quality 处理规则

- `完整清晰`：正常输出 8 节，业务经验建议不少于 5 条
- `部分模糊`：只写有原文支撑的判断，并给关键结论标注置信度
- `碎片化`：不输出完整方案，只输出“场景对齐草稿 + 待确认清单”

详细规则见 [references/transcript_quality_rules.md](references/transcript_quality_rules.md)。

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
- 默认 Markdown 表格输出；需要富文本可参考 [assets/output_template.html](assets/output_template.html)
- 若用户需要打印、转 PDF、复制到飞书或钉钉，优先使用 print 样式或 [assets/markdown_only_template.md](assets/markdown_only_template.md)

## 参考资料导航

按需读取，不要一次性全加载：

- 产出结构定义：[references/deliverable_schema.md](references/deliverable_schema.md)
- transcript 质量规则：[references/transcript_quality_rules.md](references/transcript_quality_rules.md)
- 业务经验分类：[references/business_experience_taxonomy.md](references/business_experience_taxonomy.md)
- CSM BA 分层：[references/csm_ba_layers.md](references/csm_ba_layers.md)
- 分阶段实施路径：[references/implementation_phases.md](references/implementation_phases.md)
- 输出自检清单：[references/quality_checklist.md](references/quality_checklist.md)
- 客户版简报模板：[assets/customer_brief_template.html](assets/customer_brief_template.html)

## 示例

- Post-Visit 端到端示例：[examples/中建政研集团-示例输出.md](examples/中建政研集团-示例输出.md)
- 对应 Pre-Visit 基准：[`../pre_visit_framework/examples/中建政研集团-示例输出.md`](../pre_visit_framework/examples/中建政研集团-示例输出.md)

## 客户汇报材料切片

第 7 节“客户汇报材料”默认先在主文档中完整生成，再按 [assets/customer_brief_template.html](assets/customer_brief_template.html) 切片输出客户版。

客户版只保留：

- 一句话总结
- 推荐场景一页纸
- 预期价值
- 建议交付时间
- 需要客户配合事项
- 下一步安排

客户版不得暴露内部判断、置信度、当前阻塞、否定标签、风险评估或其他 CSM 内部备注。
