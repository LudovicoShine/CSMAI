# Post-Visit Landing

访后 BI 落地推进与方案生成，帮助 CSM 在拜访客户后快速生成落地推进路径。

## 快速开始

1. 阅读 [SKILL.md](SKILL.md) 了解 skill 指令
2. 查看 [assets/post_visit_template_v1.yaml](assets/post_visit_template_v1.yaml) 了解 HTML 三档输出模板
3. 参考 [references/](references/) 下的文档深入理解 CSM BA 分层和实施路径

## 项目结构

```
post_visit_landing/
├── SKILL.md                        # Skill 入口（必需）
├── README.md                        # 本文件
├── assets/                          # 静态资源
│   └── post_visit_template_v1.yaml  # HTML 三档输出模板
├── references/                      # 参考资料
│   ├── csm_ba_layers.md             # CSM BA 深度分层框架
│   └── implementation_phases.md     # 分阶段实施路径
└── scripts/                         # 可执行脚本（预留）
```

## 核心能力

- **三档输出**：当天回复版 / 可行性评估 / Demo 草图，可独立切片
- **Quick Win MVP**：每个推荐必须包含 2-4 周可上线的 MVP
- **跨域破圈**：识别销售→供应链→财务→HR 的业务断点

## 使用场景

| 输入 | 输出 |
|------|------|
| 拜访录音/纪要 | 三档内容（24h/1周/2周） |
| 客户原话 | 业务诉求归纳 + 可行性矩阵 |
| 痛点/需求 | 落地优先级 + 实施路径 |

## 触发关键词

- 拜访后、录音、转录、会议纪要、BI看板、实施路径、Demo、落地

## 输出格式

HTML 单文件三档结构，档位间用虚线分隔，每档可独立选中复制。
帆软蓝 `#1A6FE8` 主题色，可直接发送到邮件/钉钉/飞书富文本预览。