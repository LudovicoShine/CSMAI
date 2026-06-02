# CSMAI｜帆软 CSM 拜访闭环 Skills

帆软客户成功（CSM）团队的**拜访闭环 AI 助手**，由两个 Claude Skills 组成：

| Skill | 用途 | 触发时机 |
|---|---|---|
| [`pre_visit_framework/`](pre_visit_framework/) | 拜访前调研框架与场景生成 | 接到拜访任务、准备入场谈资 |
| [`post_visit_landing/`](post_visit_landing/) | 拜访后录音/纪要收敛与落地方案 | 完成现场拜访、形成闭环交付 |

两个 Skill **弱衔接**：Post-Visit 若有 Pre-Visit 输出则做前后对照，没有也能独立运行。

---

## 整体设计

```
┌─────────────────────────────────────────────────────────────┐
│  拜访前 Pre-Visit Framework                                  │
│  ├─ 客户与部门业务判断（含公开资料融入）                       │
│  ├─ 6 个精准主场景（+ 3 个补充场景）                          │
│  ├─ 完整版现场引导问题（4 阶段，按干系人差异化）               │
│  ├─ 钩子指标雷达                                              │
│  ├─ 推进建议表（预测）                                        │
│  └─ 场景地图（业务域 × 角色 × BI 落点）                       │
└────────────────────────┬────────────────────────────────────┘
                         │ skill1_output（可选，弱衔接）
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  拜访后 Post-Visit Landing                                   │
│  ├─ Step 1: transcript_quality 分级处理                      │
│  ├─ Step 2-9: 8 节产出                                       │
│  │   1. 拜访总结摘要                                          │
│  │   2. 业务经验性内容（指标逻辑/管理规则/隐性约束）          │
│  │   3. 场景收敛清单（认可/否定/未涉及/新增）                  │
│  │   4. 指标建设路径                                          │
│  │   5. 看板搭建建议（含 Quick Win MVP）                      │
│  │   6. 推进建议表（Phase 0-3）                               │
│  │   7. 客户汇报材料（可直接 PPT）                            │
│  │   8. 下次跟进建议                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 帆软产品矩阵覆盖

两个 Skill 在生成场景与看板建议时，都会从以下 5 个产品层匹配最合适的方案：

| 产品 | 定位 | 典型场景 |
|---|---|---|
| **FineDataLink (FDL)** | 数据集成 + 治理底座 | 多源接入、宽表、口径治理 |
| **FineBI** | 自助分析 + 经营驾驶舱 | 经营总览、专题分析、钻取预警 |
| **FineReport** | 中国式复杂报表 + 填报 | 固定格式报表、监管报表、填报采集 |
| **简道云** | 业务采集 + 轻流程 + 移动协同 | 数据采集入口、跨部门流程、移动填报 |
| **Dora（Data Agent）** | AI 数字员工 | 智能问数、异常推送、自动报告 |

详细产品分层判断与组合决策见 [`pre_visit_framework/references/product_layers.md`](pre_visit_framework/references/product_layers.md)。

---

## 文件结构

```
CSMAI/
├── README.md                                # 本文件
├── pre_visit_framework/                     # Skill 1：访前调研框架
│   ├── SKILL.md                             # Skill 入口（YAML frontmatter + 主指令）
│   ├── README.md
│   ├── assets/
│   │   └── output_template.html             # 可选 HTML 渲染模板
│   ├── references/                          # 按需加载的详细 schema 与知识库
│   │   ├── scene_table_schema.md
│   │   ├── scene_map_schema.md
│   │   ├── interview_questions.md
│   │   ├── product_layers.md
│   │   └── cross_domain.md
│   └── examples/
│       └── 中建政研集团-示例输出.md
└── post_visit_landing/                      # Skill 2：访后落地方案
    ├── SKILL.md
    ├── README.md
    ├── assets/
    │   └── output_template.html
    ├── references/
    │   ├── transcript_quality_rules.md
    │   ├── business_experience_taxonomy.md
    │   ├── deliverable_schema.md
    │   ├── csm_ba_layers.md
    │   └── implementation_phases.md
    └── examples/
```

---

## 设计原则（两个 Skill 共享）

1. **先判断信息是否足够，不全则返补齐问卷**，不硬写
2. **基于原文与证据**，不扩展客户没说过的需求
3. **结构化表格输出**，便于复制到 PPT / 邮件 / 群消息
4. **不冒充行业专家**，用模式匹配 + 结构化提问补齐信息
5. **每个推荐必须可落地**：含口径、含责任人、含 Quick Win
6. **客户与产品双视角**：既理解客户业务动作，又能匹配帆软 5 个产品层

---

## 版本

- Pre-Visit Framework：v7
- Post-Visit Landing：v5
- 整体规范化时间：2026-06

## 触发关键词速查

**Pre-Visit**：拜访前、客户背景、访前准备、调研框架、破圈切入、场景设计
**Post-Visit**：拜访后、录音、转录、会议纪要、BI看板、实施路径、Demo、落地、客户汇报
