# Post-Visit Landing｜拜访后收敛与落地方案

帆软 CSM 拜访客户后的**录音/纪要收敛 + 落地方案生成**工具。从录音转写、会议纪要、CSM 现场标注中提炼业务经验、收敛真实场景、生成指标建设路径、看板搭建建议、推进计划与客户汇报材料。

与 [Pre-Visit Framework](../pre_visit_framework/) 弱衔接：有 Pre-Visit 输出时做前后对照，没有也能独立运行。

## 快速开始

1. 阅读 [SKILL.md](SKILL.md) 了解 skill 指令与输入 schema
2. 查看 [references/transcript_quality_rules.md](references/transcript_quality_rules.md) 理解 transcript 三档分级
3. 查看 [references/deliverable_schema.md](references/deliverable_schema.md) 看完整 8 节产出 schema
4. 需要富文本三档渲染时，引用 [assets/output_template.html](assets/output_template.html)

## 项目结构

```
post_visit_landing/
├── SKILL.md                                # Skill 主入口（Claude Skills 格式）
├── README.md                               # 本文件
├── assets/
│   └── output_template.html                # 可选 HTML 三档渲染模板
├── references/
│   ├── transcript_quality_rules.md         # 录音质量三档分级规则
│   ├── business_experience_taxonomy.md     # 业务经验三大分类
│   ├── deliverable_schema.md               # 8 节产出 schema
│   ├── csm_ba_layers.md                    # CSM BA 深度分层（L1-L4）
│   └── implementation_phases.md            # Phase 0-3 分阶段实施路径
└── examples/                               # 端到端示例（占位）
```

## 核心能力

- **transcript_quality 三档处理**：完整清晰 / 部分模糊 / 碎片化，分别对应不同输出深度
- **业务经验沉淀**：指标判断逻辑 / 内部管理规则 / 隐性约束 三大类型
- **场景收敛**：来自 Pre-Visit 基准 + 现场新增 + 否定淘汰
- **Quick Win MVP**：每个推荐必须含 2-4 周可上线的 MVP
- **CSM BA 分层**：L1 问题恢复 → L2 场景诊断 → L3 价值实现 → L4 经营改善
- **客户汇报材料**：可直接复制到 PPT / 邮件

## 输出 8 节顺序

1. 拜访总结摘要（50 字内）
2. 业务经验性内容（最大价值产物，必须 ≥ 5 条）
3. 场景收敛清单（P0/P1/P2 优先级 + 可行性）
4. 指标建设路径（每个 P0/P1 场景一表）
5. 看板搭建建议（含 Quick Win 标记）
6. 推进建议表（含 Phase 0-3）
7. 客户汇报材料（一句话 + 一页纸 + 配合事项）
8. 下次跟进建议

## 使用场景

| 输入 | 输出 |
|------|------|
| 现场录音转写 + 质量等级 + CSM 标注 | 8 节完整方案 |
| + Pre-Visit 输出 | 含"基准 vs 现场"前后对照 |
| 部分模糊 | 关键判断含置信度，下次跟进列补什么 |
| 碎片化 | 仅出场景对齐草稿 + 待确认清单 |

## 触发关键词

- 拜访后、录音、转录、会议纪要、BI看板、实施路径、Demo、落地、客户汇报

## 输出格式

默认 Markdown 表格输出；如需富文本三档时间切片（24h 当天回复 / 1 周可行性 / 2 周 Demo）渲染，调用 `assets/output_template.html`，帆软蓝 `#1A6FE8` 主题色。

## 版本

- 当前版本：v5（合并 v4 业务收敛逻辑 + 三档时间切片 HTML 模板 + Quick Win MVP 硬约束，统一 Claude Skills 格式）
