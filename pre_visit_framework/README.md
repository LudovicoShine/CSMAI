# Pre-Visit Framework

访前业务破圈框架生成器，帮助 CSM 在拜访客户前快速建立"带假设的访谈结构"。

## 快速开始

1. 阅读 [SKILL.md](SKILL.md) 了解 skill 指令
2. 查看 [assets/pre_visit_template_v1.yaml](assets/pre_visit_template_v1.yaml) 了解 HTML 输出模板
3. 参考 [references/](references/) 下的文档深入理解产品分层和跨域破圈模式

## 项目结构

```
pre_visit_framework/
├── SKILL.md                        # Skill 入口（必需）
├── README.md                        # 本文件
├── assets/                          # 静态资源
│   └── pre_visit_template_v1.yaml   # HTML 输出模板
├── references/                      # 参考资料
│   ├── product_layers.md            # 产品分层原则
│   └── cross_domain.md              # 跨域破圈连接模式
└── scripts/                         # 可执行脚本（预留）
```

## 核心能力

- **带假设的访谈框架**：不是给调研问题清单，而是帮 CSM 找到破圈切入点
- **6区块 HTML 输出**：客户画像 / 核心假设 / 信息清单 / 钩子雷达 / 开放式问题 / 风险预警
- **跨域破圈识别**：发现销售→供应链→财务→HR 的业务断点并串联

## 使用场景

| 输入 | 输出 |
|------|------|
| 客户背景（行业/规模/角色/已有产品） | 带置信度的业务假设 + 必问问题清单 |
| 客户描述的痛点关键词 | 钩子指标雷达表 + 推荐 BI 看板方向 |
| 拜访目标 | 结构化聊天框架（5阶段）|

## 触发关键词

- 拜访前、客户背景、聊天框架、访前准备、破圈切入

## 输出格式

HTML 单文件，帆软蓝 `#1A6FE8` 主题色，可直接发送到邮件/钉钉/飞书富文本预览。