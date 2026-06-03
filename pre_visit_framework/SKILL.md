---
name: pre-visit-framework
description: 为帆软 CSM 生成拜访前调研框架、主场景清单、现场追问、钩子词雷达与推进建议。适用于新客户首次拜访、老客户新部门破圈、既有场景深化、数据问题与业务场景并行摸底；输入客户名称、行业、拜访部门、拜访背景后，输出 6 个精准主场景，可选 3 个补充场景，并结合可索引场景库与钩子词库提高复用质量。
metadata:
  short-description: 帆软 CSM 拜访前调研与场景生成
---

# Pre-Visit Framework

用于 CSM 在拜访前准备客户背景判断、访谈框架、场景设计与首轮推进建议。

## 平台适配说明

本 Skill 按公司平台结构组织，仅依赖：

- `SKILL.md`
- `REFERENCES/`
- `SCRIPTS/`

不要依赖 `examples/`、`assets/` 或 `README.md`。若需要模板，读取 `REFERENCES/templates/`。

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
- `customer_core_business_flow`：客户公司主要业务流程、钱和项目如何运转
- `dept_core_workflow`：对接部门的日常工作流程、上下游、交付物和汇报链路
- `visit_target_role`
- `visit_target_name`
- `known_pain_points`
- `known_boards`
- `known_communication_log`

### 信息不完整时

若只提供必填三项，且缺少角色、目标、痛点信息，先返回补齐问卷，不直接生成场景。问卷字段见 [REFERENCES/interview_questions.md](REFERENCES/interview_questions.md) 中的输入提醒部分。

## 执行流程

1. 先检查信息是否足够，不足则返回补齐问卷。
2. 若 `customer_name` 明确，优先结合公开资料判断客户业务与拜访部门职责；无法确认时明确标注“基于行业推测”。
3. 必须先用白话写清客户公司怎么挣钱、业务怎么流转、对接部门每天/每周怎么运转，再进入场景设计。
4. 先判断这是“业务场景挖掘”“数据问题治理”还是“双线并行”，再决定是否输出补充场景。
5. 优先从可复用知识库召回行业/部门交叉场景，再根据本次 `visit_context` 与 `visit_goal` 做裁剪，不要从零空想。
6. 逐个输出主场景表，并把日常工作拆解、痛点强度、帆软方案、看板目标、页面结构、故事链、产品分层写进场景。
7. 生成完整版现场引导问题、钩子指标雷达、推进建议表（预测）与场景地图。
8. 生成完成后，必须按 [REFERENCES/quality_checklist.md](REFERENCES/quality_checklist.md) 逐条自检；若任一关键项不满足，先修正再输出。

## 弱模型输出策略

当运行在 GLM、DeepSeek 或其他上下文/推理能力一般的模型上时，不追求一次性输出所有深度。优先分段 handoff：

1. 第 1 次只输出：客户业务流程、部门工作流程、拜访判断、待确认问题。
2. 第 2 次输出：6 个主场景，每个场景写清“日常工作怎么做、为什么痛、痛到什么程度、帆软怎么解”。
3. 第 3 次输出：现场怎么聊、数据流转怎么问、已有系统边界怎么判断、落地复杂度怎么估。
4. 第 4 次输出：推进建议、场景地图、自检结果。

每段结尾必须给出“handoff 摘要”，包括已完成内容、仍缺什么、下一段要继续输出什么，避免上下文长度限制导致广度和深度下降。

## 表达风格

你的讲述对象是一个完全不了解客户业务的新手。必须用最白话、最容易懂的方式讲清：

- 这个公司日常靠什么业务运转
- 对接部门每天/每周在做什么
- 这个岗位和其他部门怎么联系
- 为什么这些事会痛，痛在哪里
- 帆软具体用什么方案解决
- 这个场景落地时要先聊什么、确认什么、谁配合

## 输出要求

按以下顺序输出：

```text
0. 开头目录
1. 客户与部门业务情况介绍和推测
   1.1 公司主要业务流程与运转思路
   1.2 对接部门业务流程与日常工作
   1.3 岗位/部门/公司之间的协作关系
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
- 每个场景必须把日常工作拆解清楚，让新手能看懂具体做哪些事
- 每个痛点必须写清痛因、痛感强度、影响对象和业务后果
- 默认 Markdown 表格输出；需要富文本时可参考 [REFERENCES/templates/output_template.html](REFERENCES/templates/output_template.html)
- 若用户需要打印、转 PDF、复制到飞书或钉钉，优先使用 print 样式或 [REFERENCES/templates/markdown_only_template.md](REFERENCES/templates/markdown_only_template.md)

## 参考资料导航

按需读取，不要一次性全加载：

- 场景表字段定义：[REFERENCES/scene_table_schema.md](REFERENCES/scene_table_schema.md)
- 场景地图结构：[REFERENCES/scene_map_schema.md](REFERENCES/scene_map_schema.md)
- 现场引导问题框架：[REFERENCES/interview_questions.md](REFERENCES/interview_questions.md)
- 产品分层判断：[REFERENCES/product_layers.md](REFERENCES/product_layers.md)
- 跨域破圈识别：[REFERENCES/cross_domain.md](REFERENCES/cross_domain.md)
- 行业 × 部门场景库：[REFERENCES/scene_library.md](REFERENCES/scene_library.md)
- 钩子词与追问词库：[REFERENCES/hook_keywords.md](REFERENCES/hook_keywords.md)
- 输出自检清单：[REFERENCES/quality_checklist.md](REFERENCES/quality_checklist.md)
- 使用反馈记录：[REFERENCES/feedback_log.md](REFERENCES/feedback_log.md)
