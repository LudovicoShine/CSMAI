---
name: pre-visit-framework
description: 为帆软 CSM 生成拜访前调研框架、主场景清单、现场追问、钩子词雷达与推进建议。适用于新客户首次拜访、老客户新部门破圈、既有场景深化、数据问题与业务场景并行摸底；输入客户名称、行业、拜访部门、拜访背景后，输出 6 个精准主场景，可选 3 个补充场景，并结合可索引场景库与钩子词库提高复用质量。
metadata:
  short-description: 帆软 CSM 拜访前调研与场景生成
  version: v7
  trigger_keywords:
    - 拜访前
    - 客户背景
    - 访前准备
    - 调研框架
    - 破圈切入
    - 场景设计
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

若只提供必填三项，且缺少角色、目标、痛点等建议补充信息，先返回补齐问卷，不直接生成场景。

#### 补齐问卷交互规范

**交互方式**：优先使用 `ask_user_question` 工具在对话内弹出选项卡片；若工具不可用或用户明确要求文字回复，降级为 Markdown 列表输出。

**字段分类与规则**：

| 字段 | 题型 | 是否必填 | 说明 |
|------|------|---------|------|
| `visit_goal` | multiple_choice | 是 | 本次拜访核心目标，可多选 + 自由补充 |
| `visit_target_role` | multiple_choice | 是 | 对接人角色类型，可多选 + 自由补充 |
| `customer_bi_status` | multiple_choice | 是 | 当前 BI 使用状态，可多选 + 自由补充 |
| `known_pain_points` | multiple_choice | 是 | 已知痛点方向，可多选 + 自由补充 |
| `customer_scale` | single_choice | 是 | 企业规模区间，单选 |
| `visit_target_name` | text | 否 | 对接人姓名，不填默认空白 |
| `known_boards` | text | 否 | 已知看板/报表名称，不填默认空白 |
| `known_communication_log` | text | 否 | 历史沟通要点摘要，不填默认空白 |
| `customer_name` | text | 否 | 客户全称（若首轮未提供），不填默认空白 |

**硬性约束**：

- 所有 `multiple_choice` 题型必须设为必填，选项由 SKILL 预定义固定列表 + 用户可自由补充（`ask_user_question` 的选择题天然支持用户自行添加选项）
- 所有 `text` 题型**不得设为必填**，用户留空时必须能正常提交，Agent 将对应字段置为空字符串继续执行
- 问卷一次最多展示 5 个问题；超出时按优先级分批，第一批必须包含 `visit_goal`、`visit_target_role`、`customer_bi_status`
- 问卷回收后，将用户选择映射为结构化变量，再进入执行流程第 2 步

**固定选项列表**（供 `ask_user_question` 调用时直接使用）：

```
visit_goal:
  - 新部门/新场景探索
  - 既有场景深化与优化
  - 数据质量问题排查与治理
  - BI 平台升级或替换评估
  - 高层汇报支撑
  - 跨部门协同打通
  - 其他（请补充）

visit_target_role:
  - 高层/决策者
  - 部门负责人/管理者
  - 运营/业务执行人
  - IT/数据负责人
  - 财务/审计
  - HR/行政
  - 其他（请补充）

customer_bi_status:
  - 尚未使用任何 BI 工具
  - 已使用帆软产品（FR/FineBI/FDL/简道云）
  - 已使用竞品（Tableau/Power BI/永洪/Smartbi 等）
  - 有自研报表系统
  - 主要靠 Excel/手工
  - 不确定
  - 其他（请补充）

known_pain_points:
  - 数据口径不一致
  - 报表制作耗时过长
  - 缺乏实时数据
  - 看板没人看/不会用
  - 跨系统数据打不通
  - 领导要的指标说不清
  - 权限/安全管控不足
  - 移动端体验差
  - 其他（请补充）

customer_scale:
  - 100人以下
  - 100-500人
  - 500-2000人
  - 2000-10000人
  - 10000人以上
```

## 执行流程

1. 先检查信息是否足够。若缺少建议补充字段，按「补齐问卷交互规范」发起问卷；用户提交后（含部分留空），将结果映射为变量再继续。
2. 若 `customer_name` 明确，优先结合公开资料判断客户业务与拜访部门职责；无法确认时明确标注"基于行业推测"。
3. 先判断这是"业务场景挖掘""数据问题治理"还是"双线并行"，再决定是否输出补充场景。
4. 优先从可复用知识库召回行业/部门交叉场景，再根据本次 `visit_context` 与 `visit_goal` 做裁剪，不要从零空想。
5. 逐个输出主场景表，并把看板目标、页面结构、故事链、产品分层写进"与产品的相关性"字段。
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
- 假设必须可证伪，并显式写"需客户确认"
- 数据治理场景不能孤立存在，必须绑定具体业务场景
- 默认 Markdown 表格输出；需要富文本时可参考 [references/template_output.html](references/template_output.html)
- 若用户需要打印、转 PDF、复制到飞书或钉钉，优先使用 print 样式或 [references/template_markdown_only.md](references/template_markdown_only.md)

## 参考资料导航

按需读取，不要一次性全加载：

| 文件 | 用途 |
|------|------|
| [references/scene_table_schema.md](references/scene_table_schema.md) | 6 主场景表格 10 字段 schema |
| [references/scene_map_schema.md](references/scene_map_schema.md) | 场景地图三层结构 schema |
| [references/interview_questions.md](references/interview_questions.md) | 完整版 4 阶段引导问题库 |
| [references/product_layers.md](references/product_layers.md) | 帆软产品分层判断（FDL/BI/FR/简道云/Dora） |
| [references/cross_domain.md](references/cross_domain.md) | 跨域破圈连接模式 |
| [references/scene_library.md](references/scene_library.md) | 行业 × 部门场景库 |
| [references/hook_keywords.md](references/hook_keywords.md) | 钩子词与追问词库 |
| [references/quality_checklist.md](references/quality_checklist.md) | 输出自检清单 |
| [references/template_output.html](references/template_output.html) | 富文本 HTML 渲染模板（帆软蓝主题） |
| [references/template_markdown_only.md](references/template_markdown_only.md) | Markdown 纯文本输出模板（打印/飞书/钉钉） |
| [references/example_中建政研集团.md](references/example_中建政研集团.md) | Pre-Visit 端到端完整示例 |

## 核心能力速览

- **业务场景设计**：6 个精准主场景 + 可选 3 个补充场景，每个场景含 10 字段表格
- **完整引导问题**：4 阶段问题库，按干系人差异化提问
- **场景地图**：业务域 × 角色层级 × BI 落点三层结构
- **钩子指标雷达**：现场抓"客户说什么 = 命中"的关键词
- **产品分层匹配**：FDL / FineBI / FineReport / 简道云 / Dora 自动建议
- **跨域破圈识别**：销售→供应链→财务→HR 的业务断点串联

## 使用场景

| 输入 | 输出 |
|------|------|
| 客户行业 + 拜访部门 + 拜访契机（必填） | 客户业务判断 + 6 主场景 + 调研框架 |
| 客户名称（建议） | 公开资料融入业务判断 |
| 现有 BI 使用情况 + 已知痛点 | 钩子指标雷达 + 切入点提示 |
| 拜访目标（数据问题 / 业务场景 / 双线） | 6 主 + 3 补充场景双线输出 |

## 目录结构

```
pre_visit_framework/
├── SKILL.md                              # 技能主入口
├── scripts/                              # 预留脚本目录
└── references/
    ├── scene_table_schema.md             # 场景表字段定义
    ├── scene_map_schema.md               # 场景地图结构
    ├── interview_questions.md            # 现场引导问题框架
    ├── product_layers.md                 # 产品分层判断
    ├── cross_domain.md                   # 跨域破圈识别
    ├── scene_library.md                  # 行业×部门场景库
    ├── hook_keywords.md                  # 钩子词与追问词库
    ├── quality_checklist.md              # 输出自检清单
    ├── template_output.html              # 富文本 HTML 渲染模板
    ├── template_markdown_only.md         # Markdown 纯文本输出模板
    └── example_中建政研集团.md            # 端到端完整示例
```
