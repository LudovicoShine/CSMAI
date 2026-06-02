---
name: pre_visit_framework
description: 访前业务破圈框架生成器。基于有限客户背景，生成带假设的拜访框架，帮助 CSM 在 30 分钟内建立"带假设的访谈结构"。触发词：拜访前、客户背景、聊天框架、访前准备、破圈切入
when_to_use: 拜访客户前需要准备访谈框架时使用
allowed-tools: Read Grep Write
---

# Skill 主体指令

## 何时使用
当 CSM 需要在拜访客户前准备访谈框架时使用。不是给调研问题清单，而是帮 CSM 找到破圈切入点。

## 核心能力
- 熟知供应链、财务、HR、营销、生产、运营等领域的经典 BI 落地场景和刚需指标
- 用模式匹配 + 结构化提问快速补齐信息，不冒充行业专家
- 识别跨域连接模式：销售预测偏差 → 供应链库存积压 → 财务现金流压力 → HR用工计划调整

## 输出结构（6区块 HTML）
1. **客户业务画像速写** - 用 .fr-card 呈现，单段不超过 80 字
2. **核心业务假设** - 3 个假设各用一个 .fr-card，含置信度标签（高/中/低）
3. **必问核心信息清单** - 4 组：业务现状 / 数据现状 / 痛点确认 / 决策推动
4. **钩子指标雷达** - 表格：指标名 / 客户说什么词=命中 / 业务含义 / 引用条目
5. **临门一脚开放式问题** - 3 个问题，顶部加"用于拜访末尾"标签
6. **风险预警** - 2 条预警，左边框黄色

## 计算口径标准
- MoM/Yoy = (Current - Prior) / Prior
- Cohort = 按首次发生时间分组跟踪后续表现
- 数据粒度：日 / 周 / 月（必须说明）
- 对比基线：必须明确

## 产品分层提示
- **FineDataLink (FDL)**：多源数据接入、ERP/WMS/CRM同步、数据清洗、宽表构建、库存/订单快照
- **FineBI**：经营驾驶舱、指标趋势分析、同比环比、钻取筛选预警
- **FineReport (FR)**：中国式复杂报表、固定格式日报月报、填报采集、打印导出

## 输出约束
- 基于有限背景做出合理假设，标注"需客户确认"
- 结构化聊天框架分阶段：开场破冰 → 现状调研 → 痛点深挖 → 破圈机会引导 → 下一阶段约定
- 每个 BI 看板建议必须包含核心指标和计算口径
- 总问题不超过 15 个，宁可少而准
- 假设必须可证伪，不写废话

## 附加资源
- 详细产品分层参考：[references/product_layers.md](references/product_layers.md)
- 跨域破圈连接模式参考：[references/cross_domain.md](references/cross_domain.md)

---

# HTML 输出模板

将以下模板中的 {placeholder} 变量替换为实际内容后输出。

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>拜访准备框架 - {customer_name} - {date}</title>
<style>
  :root {
    --fr-primary: #1A6FE8;
    --fr-primary-light: #3A8DFF;
    --fr-primary-dark: #0F4FB8;
    --fr-bg-soft: #F5F7FA;
    --fr-bg-tint: #E8EEF7;
    --fr-border: #D4DEED;
    --fr-text: #1F2937;
    --fr-text-sub: #6B7280;
    --fr-warn: #F59E0B;
    --fr-danger: #EF4444;
    --fr-success: #10B981;
  }
  body {
    font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
    color: var(--fr-text);
    line-height: 1.7;
    max-width: 860px;
    margin: 0 auto;
    padding: 32px;
    background: #fff;
  }
  .fr-header {
    border-left: 4px solid var(--fr-primary);
    padding: 8px 16px;
    background: linear-gradient(90deg, var(--fr-bg-tint) 0%, #fff 100%);
    margin-bottom: 24px;
  }
  .fr-header .title {
    font-size: 22px;
    font-weight: 600;
    color: var(--fr-primary-dark);
    margin: 0;
  }
  .fr-header .subtitle {
    font-size: 13px;
    color: var(--fr-text-sub);
    margin-top: 4px;
  }
  .fr-section {
    margin-bottom: 28px;
  }
  .fr-section-title {
    font-size: 16px;
    font-weight: 600;
    color: var(--fr-primary);
    border-bottom: 2px solid var(--fr-bg-tint);
    padding-bottom: 6px;
    margin-bottom: 14px;
  }
  .fr-section-title .num {
    display: inline-block;
    background: var(--fr-primary);
    color: #fff;
    width: 22px; height: 22px;
    text-align: center; line-height: 22px;
    border-radius: 50%;
    font-size: 13px;
    margin-right: 8px;
  }
  .fr-card {
    background: var(--fr-bg-soft);
    border-left: 3px solid var(--fr-primary-light);
    padding: 12px 16px;
    margin: 8px 0;
    border-radius: 4px;
  }
  .fr-card .label {
    font-size: 12px;
    color: var(--fr-text-sub);
    margin-bottom: 4px;
  }
  .fr-card .value {
    font-size: 14px;
    color: var(--fr-text);
  }
  .fr-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }
  .fr-table th {
    background: var(--fr-primary);
    color: #fff;
    padding: 8px 12px;
    text-align: left;
    font-weight: 500;
  }
  .fr-table td {
    padding: 8px 12px;
    border-bottom: 1px solid var(--fr-border);
  }
  .fr-table tr:nth-child(even) td {
    background: var(--fr-bg-soft);
  }
  .fr-tag {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 3px;
    font-size: 12px;
    margin-right: 4px;
  }
  .fr-tag-high   { background: #FEE2E2; color: var(--fr-danger); }
  .fr-tag-mid    { background: #FEF3C7; color: var(--fr-warn); }
  .fr-tag-low    { background: #D1FAE5; color: var(--fr-success); }
  .fr-tag-info   { background: var(--fr-bg-tint); color: var(--fr-primary-dark); }
  .fr-quote {
    border-left: 3px solid var(--fr-primary);
    padding: 8px 14px;
    background: var(--fr-bg-tint);
    color: var(--fr-primary-dark);
    margin: 8px 0;
    font-style: italic;
    font-size: 13px;
  }
  .fr-placeholder {
    color: var(--fr-warn);
    background: #FFF7E6;
    padding: 2px 6px;
    border-radius: 3px;
    border: 1px dashed var(--fr-warn);
    font-size: 12px;
  }
  .fr-footer {
    margin-top: 40px;
    padding-top: 16px;
    border-top: 1px solid var(--fr-border);
    font-size: 12px;
    color: var(--fr-text-sub);
    text-align: center;
  }
  .fr-footer .brand {
    color: var(--fr-primary);
    font-weight: 600;
  }
  ul.fr-list { padding-left: 20px; }
  ul.fr-list li { margin-bottom: 6px; }
</style>
</head>
<body>

<div class="fr-header">
  <div class="title">客户拜访准备框架</div>
  <div class="subtitle">客户：{customer_name} ｜ 行业：{industry} ｜ 对接人：{contact_role} ｜ 目标领域：{target_domains}</div>
</div>

<div class="fr-section">
  <div class="fr-section-title"><span class="num">01</span>客户业务画像速写</div>
  {customer_profile_cards}
</div>

<div class="fr-section">
  <div class="fr-section-title"><span class="num">02</span>核心业务假设</div>
  {hypothesis_cards}
</div>

<div class="fr-section">
  <div class="fr-section-title"><span class="num">03</span>必问核心信息清单</div>
  <h4 style="color: var(--fr-primary);">业务现状</h4>
  <ul class="fr-list">{business_status_questions}</ul>
  <h4 style="color: var(--fr-primary);">数据现状</h4>
  <ul class="fr-list">{data_status_questions}</ul>
  <h4 style="color: var(--fr-primary);">痛点确认</h4>
  <ul class="fr-list">{pain_point_questions}</ul>
  <h4 style="color: var(--fr-primary);">决策推动</h4>
  <ul class="fr-list">{decision_questions}</ul>
</div>

<div class="fr-section">
  <div class="fr-section-title"><span class="num">04</span>钩子指标雷达</div>
  <table class="fr-table">
    <thead>
      <tr>
        <th>指标名</th>
        <th>客户说什么词 = 命中</th>
        <th>业务含义</th>
        <th>引用条目</th>
      </tr>
    </thead>
    <tbody>{hook_radar_rows}</tbody>
  </table>
</div>

<div class="fr-section">
  <div class="fr-section-title"><span class="num">05</span>临门一脚开放式问题</div>
  {open_questions}
</div>

<div class="fr-section">
  <div class="fr-section-title"><span class="num">06</span>风险预警</div>
  {risk_warnings}
</div>

<div class="fr-footer">
  本文档由 <span class="brand">帆软客户成功团队</span> · 拜访准备助手 生成<br>
  生成时间：{timestamp} ｜ 模板版本：Skill-A v1.0 ｜ 文档编号：PRE-{customer_abbr}-{datecompact}
</div>

</body>
</html>
```