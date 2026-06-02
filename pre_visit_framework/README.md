# Pre-Visit Framework｜拜访前调研框架

帆软 CSM 拜访客户前的**场景生成 + 调研框架设计**工具。基于客户名称、行业、拜访部门、既有 BI 使用情况和本次拜访契机，结合公开资料判断客户业务阶段，输出 6 个精准主场景（可选 3 个补充场景）、完整版现场引导问题、场景地图与推进建议。

## 快速开始

1. 阅读 [SKILL.md](SKILL.md) 了解 skill 指令与输入 schema
2. 参考 [examples/中建政研集团-示例输出.md](examples/中建政研集团-示例输出.md) 看一份完整产出
3. 需要富文本渲染时，引用 [assets/output_template.html](assets/output_template.html)

## 项目结构

```
pre_visit_framework/
├── SKILL.md                              # Skill 主入口（Claude Skills 格式）
├── README.md                             # 本文件
├── assets/
│   └── output_template.html              # 可选 HTML 渲染模板（帆软蓝主题）
├── references/
│   ├── scene_table_schema.md             # 6 主场景表格 10 字段 schema
│   ├── scene_map_schema.md               # 场景地图三层结构 schema
│   ├── interview_questions.md            # 完整版 4 阶段引导问题库
│   ├── product_layers.md                 # 帆软产品分层判断（FDL/BI/FR/简道云/Dora）
│   └── cross_domain.md                   # 跨域破圈连接模式
└── examples/
    └── 中建政研集团-示例输出.md          # 端到端示例
```

## 核心能力

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
| 客户名称（建议）| 公开资料融入业务判断 |
| 现有 BI 使用情况 + 已知痛点 | 钩子指标雷达 + 切入点提示 |
| 拜访目标（数据问题 / 业务场景 / 双线）| 6 主 + 3 补充场景双线输出 |

## 触发关键词

- 拜访前、客户背景、访前准备、调研框架、破圈切入、场景设计

## 输出格式

默认 Markdown 表格输出；如需富文本渲染，调用 `assets/output_template.html`，帆软蓝 `#1A6FE8` 主题色，可直接发送至邮件 / 钉钉 / 飞书富文本预览。

## 版本

- 当前版本：v7（合并 v6 业务深度结构 + 钩子指标雷达增量模块，统一 Claude Skills 格式）
