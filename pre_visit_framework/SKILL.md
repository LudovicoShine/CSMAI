---
name: pre-visit-framework
description: 为帆软 CSM 生成拜访前调研框架、主场景清单、现场追问、钩子词雷达与推进建议。适用于新客户首次拜访、老客户新部门破圈、既有场景深化、数据问题与业务场景并行摸底；输入客户名称、行业、拜访部门、拜访背景后，输出 6 个精准主场景，可选 3 个补充场景，并结合可索引场景库与钩子词库提高复用质量。
metadata:
  short-description: 帆软 CSM 拜访前调研与场景生成
---

# Pre-Visit Framework

用于 CSM 在拜访前准备客户背景判断、访谈框架、场景设计与首轮推进建议。

## 何时使用

- 用户要做访前准备、客户背景梳理、部门破圈切入、场景设计
- 需要基于客户名称、行业、部门、既有 BI 使用情况生成 6 个主场景
- 需要根据客户原话快速识别切入点，或参考历史行业/部门场景模板

## 输入要求

### 必填

- `customer_industry`
- `visit_target_dept`
- `visit_context`

### 建议补充

- `customer_name`
- `visit_goal`
- `customer_scale`
- `customer_bi_status`
- `visit_target_role`
- `visit_target_name`
- `known_pain_points`
- `known_boards`
- `known_communication_log`

### 信息不完整时

若只提供必填三项，且缺少角色、目标、痛点信息，先返回补齐问卷，不直接生成场景。问卷字段见 [references/interview_questions.md](references/interview_questions.md) 中的输入提醒部分。

## 执行流程

1. 先检查信息是否足够，不足则返回补齐问卷。
2. 若 `customer_name` 明确，优先结合公开资料判断客户业务与拜访部门职责；无法确认时明确标注“基于行业推测”。
3. 先判断这是“业务场景挖掘”“数据问题治理”还是“双线并行”，再决定是否输出补充场景。
4. 优先从可复用知识库召回行业/部门交叉场景，再根据本次 `visit_context` 与 `visit_goal` 做裁剪，不要从零空想。
5. 逐个输出主场景表，并把看板目标、页面结构、故事链、产品分层写进“与产品的相关性”字段。
6. 生成完整版现场引导问题、钩子指标雷达、推进建议表（预测）与场景地图。
7. 生成完成后，必须按 [references/quality_checklist.md](references/quality_checklist.md) 逐条自检；若任一关键项不满足，先修正再输出。

## 输出要求

按以下顺序输出：

```text
0. 开头目录
1. 客户与部门业务情况介绍和推测
2. 拜访基本信息摘要（30 字内）
3. 总调研框架
4. 6 个精准主场景
5. 3 个补充贴切场景（仅在双线并行时输出）
6. 钩子指标雷达
7. 推进建议表（预测）
8. 场景地图
```

### 硬性约束

- 6 个主场景必须贴着 `visit_context` 与 `visit_goal`
- 假设必须可证伪，并显式写“需客户确认”
- 数据治理场景不能孤立存在，必须绑定具体业务场景
- 默认 Markdown 表格输出；需要富文本时可参考 [assets/output_template.html](assets/output_template.html)
- 若用户需要打印、转 PDF、复制到飞书或钉钉，优先使用 print 样式或 [assets/markdown_only_template.md](assets/markdown_only_template.md)

## 参考资料导航

按需读取，不要一次性全加载：

- 场景表字段定义：[references/scene_table_schema.md](references/scene_table_schema.md)
- 场景地图结构：[references/scene_map_schema.md](references/scene_map_schema.md)
- 现场引导问题框架：[references/interview_questions.md](references/interview_questions.md)
- 产品分层判断：[references/product_layers.md](references/product_layers.md)
- 跨域破圈识别：[references/cross_domain.md](references/cross_domain.md)
- 行业 × 部门场景库：[references/scene_library.md](references/scene_library.md)
- 钩子词与追问词库：[references/hook_keywords.md](references/hook_keywords.md)
- 输出自检清单：[references/quality_checklist.md](references/quality_checklist.md)

## 示例

- Pre-Visit 端到端示例：[examples/中建政研集团-示例输出.md](examples/中建政研集团-示例输出.md)
- 对应 Post-Visit 闭环示例：[`../post_visit_landing/examples/中建政研集团-示例输出.md`](../post_visit_landing/examples/中建政研集团-示例输出.md)
