---
name: post_visit_landing
description: 访后 BI 落地推进与方案生成。从录音/纪要中提取痛点，生成含 Quick Win 的 BI 落地路径。触发词：拜访后、录音、转录、会议纪要、BI看板、实施路径、Demo、落地
when_to_use: 拜访客户后需要生成落地推进方案时使用
allowed-tools: Read Grep Write
---

# Skill 主体指令

## 何时使用
当 CSM 完成客户拜访后，需要根据录音/纪要生成 BI 落地推进方案时使用。先提取客户明确提到的痛点、指标、部门，再推荐看板。

## 核心能力
- 熟知供应链、财务、HR、营销、生产、运营等领域的经典 BI 落地场景和刚需指标
- 不冒充行业专家，用模式匹配 + 结构化提问快速补齐信息

## 三档输出结构

### 档1：当天回复（24小时内）
一段不超过 200 字的话术，可直接复制粘贴至客户群/邮件。特殊样式：白底蓝边。

### 档2：BI 落地可行性评估（1周内）
- **2.1 业务诉求归纳** - 表格：诉求编号 / 客户原话 / 归纳后的业务动作
- **2.2 落地可行性矩阵** - 表格：诉求 / 数据可得性 / 加工复杂度 / 业务价值 / 综合判断
- **2.3 推荐落地优先级** - 有序列表
- **2.4 关键口径澄清清单** - 卡片列表，左边框黄色
- **2.5 风险与依赖** - 带 ⚠ 符号的列表

### 档3：Demo 草图与实施路径（2周内）
- **3.1 推荐看板结构** - 表格：看板名称 / 给谁看 / 什么场合看 / 看完做什么决定
- **3.2 主看板布局线框** - 模拟线框图（含 KPI 卡区、主图区、下钻入口）
- **3.3 关键指标加工口径表** - 表格：指标名 / 业务定义 / 计算公式 / 数据源 / 刷新频率 / 引用条目
- **3.4 分阶段实施路径** - 表格：阶段 / 周次 / 关键动作 / 产出物 / 责任方
- **3.5 给客户 sponsor 的一页价值陈述** - 渐变色卡片，禁止出现技术词

## 归因模型特殊处理（营销领域）
当检测到归因相关诉求时：
- 必须把"归因模型选择"放进口径澄清清单的第一条
- 常见归因模型：首次触点、末次触点、线性归因、时间衰减、位置归因（U型）
- 品牌广告适合首次触点或时间衰减，效果广告适合末次触点

## 数据源对接评估（营销/生产领域）
涉及这两个领域时，必须自动把"数据源对接评估"作为第 1 周必做事项：
- 营销数据源：投放后台（巨量/腾讯广告）/ CRM / 电商平台 / 客服系统
- 生产数据源：MES / SCADA / QMS / ERP

## CSM BA 深度分层
- **L1 问题恢复层**：先恢复客户当前问题（报表打不开、BI 更新失败等）
- **L2 场景诊断层**：判断技术问题还是业务设计问题
- **L3 价值实现层**：判断问题如何影响客户业务价值
- **L4 经营改善层**：推动跨部门、跨产品经营闭环

## 输出约束
- 所有推荐必须包含 Quick Win（2-4周可上线MVP），这是增加粘性的关键
- 落地可行性评估必须包含数据 readiness、技术难度、预估周期、风险、ROI 假设
- 业务诉求必须来自录音原文，不扩展客户没说过的需求
- 描述模糊的放进"口径澄清清单"，不替客户决定

## 附加资源
- CSM BA 深度分层参考：[references/csm_ba_layers.md](references/csm_ba_layers.md)
- 分阶段实施路径参考：[references/implementation_phases.md](references/implementation_phases.md)

---

# HTML 输出模板（三档可独立切片）

将以下模板中的 {placeholder} 变量替换为实际内容后输出。三档之间用虚线分隔，每档可独立选中复制。

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>访后落地路径 - {customer_name} - {date}</title>
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
  .档位导航条 {
    background: var(--fr-bg-soft);
    padding: 10px 16px;
    border-radius: 4px;
    margin-bottom: 24px;
    font-size: 13px;
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
  .档1-highlight {
    background: #fff;
    border: 2px solid var(--fr-primary);
    border-left-width: 4px;
    padding: 16px;
    margin: 12px 0;
  }
  .fr-card {
    background: var(--fr-bg-soft);
    border-left: 3px solid var(--fr-primary-light);
    padding: 12px 16px;
    margin: 8px 0;
    border-radius: 4px;
  }
  .fr-card-warn {
    border-left-color: var(--fr-warn);
  }
  .fr-card-value {
    background: linear-gradient(135deg, var(--fr-primary) 0%, var(--fr-primary-dark) 100%);
    color: #fff;
    padding: 20px;
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
  .fr-tag-high { background: #FEE2E2; color: var(--fr-danger); }
  .fr-tag-mid { background: #FEF3C7; color: var(--fr-warn); }
  .fr-tag-low { background: #D1FAE5; color: var(--fr-success); }
  .fr-tag-info { background: var(--fr-bg-tint); color: var(--fr-primary-dark); }
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
  .看板线框 {
    border: 2px solid var(--fr-primary);
    border-radius: 6px;
    padding: 16px;
    background: var(--fr-bg-soft);
  }
  .看板线框-标题 {
    background: var(--fr-primary);
    color: #fff;
    padding: 8px;
    text-align: center;
    margin-bottom: 12px;
    font-weight: 600;
  }
  .看板线框-KPI区 {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 12px;
  }
  .看板线框-KPI卡 {
    flex: 1;
    min-width: 140px;
    background: #fff;
    padding: 10px;
    border: 1px solid var(--fr-border);
    border-radius: 4px;
  }
  .看板线框-主图区 {
    background: #fff;
    padding: 14px;
    border: 1px dashed var(--fr-border);
    text-align: center;
    color: var(--fr-text-sub);
    margin-bottom: 12px;
  }
  .看板线框-下钻入口 {
    font-size: 12px;
    color: var(--fr-text-sub);
  }
  hr.档位分隔线 {
    border: none;
    border-top: 2px dashed var(--fr-bg-tint);
    margin: 32px 0;
  }
</style>
</head>
<body>

<div class="fr-header">
  <div class="title">拜访后 BI 落地路径建议</div>
  <div class="subtitle">客户：{customer_name} ｜ 拜访日期：{visit_date} ｜ 参与方：{participants}</div>
</div>

<div class="档位导航条">
  <span class="fr-tag fr-tag-info">档1·当天回复</span>
  <span class="fr-tag fr-tag-info">档2·可行性评估（1周内）</span>
  <span class="fr-tag fr-tag-info">档3·Demo草图（2周内）</span>
</div>

<!-- 档1：当天回复版 -->
<div class="fr-section">
  <div class="fr-section-title">档 1 · 当天回复（建议 24 小时内发出）</div>
  <div class="档1-highlight">
    {档1_话术内容}
  </div>
  <div style="font-size:12px; color:var(--fr-text-sub); margin-top:6px;">
    提示：可直接复制粘贴至客户群 / 邮件
  </div>
</div>

<hr class="档位分隔线">

<!-- 档2：BI 落地可行性评估 -->
<div class="fr-section">
  <div class="fr-section-title">档 2 · 可行性评估（1 周内交付）</div>

  <h4 style="color: var(--fr-primary);">2.1 业务诉求归纳</h4>
  <table class="fr-table">
    <thead>
      <tr><th>诉求编号</th><th>客户原话</th><th>归纳后的业务动作</th></tr>
    </thead>
    <tbody>{档2_诉求表格}</tbody>
  </table>

  <h4 style="color: var(--fr-primary);">2.2 落地可行性矩阵</h4>
  <table class="fr-table">
    <thead>
      <tr><th>诉求</th><th>数据可得性</th><th>加工复杂度</th><th>业务价值</th><th>综合判断</th></tr>
    </thead>
    <tbody>{档2_可行性矩阵}</tbody>
  </table>

  <h4 style="color: var(--fr-primary);">2.3 推荐落地优先级</h4>
  <ol>
    {档2_优先级列表}
  </ol>

  <h4 style="color: var(--fr-primary);">2.4 关键口径澄清清单</h4>
  {档2_口径澄清卡片}

  <h4 style="color: var(--fr-primary);">2.5 风险与依赖</h4>
  <ul class="fr-list">
    {档2_风险列表}
  </ul>
</div>

<hr class="档位分隔线">

<!-- 档3：Demo草图与实施路径 -->
<div class="fr-section">
  <div class="fr-section-title">档 3 · Demo 草图与实施路径（2 周内交付）</div>

  <h4 style="color: var(--fr-primary);">3.1 推荐看板结构</h4>
  <table class="fr-table">
    <thead>
      <tr><th>看板名称</th><th>给谁看</th><th>什么场合看</th><th>看完做什么决定</th></tr>
    </thead>
    <tbody>{档3_看板结构表}</tbody>
  </table>

  <h4 style="color: var(--fr-primary);">3.2 主看板布局线框</h4>
  <div class="看板线框">
    <div class="看板线框-标题">{主看板标题}</div>
    <div class="看板线框-KPI区">
      {KPI卡片列表}
    </div>
    <div class="看板线框-主图区">
      [主图区域：{图表类型}]<br>
      <span style="font-size:12px;">用于展示：{展示内容}</span>
    </div>
    <div class="看板线框-下钻入口">
      下钻入口：{子看板1} ｜ {子看板2} ｜ {子看板3}
    </div>
  </div>

  <h4 style="color: var(--fr-primary);">3.3 关键指标加工口径表</h4>
  <table class="fr-table">
    <thead>
      <tr><th>指标名</th><th>业务定义</th><th>计算公式</th><th>数据源</th><th>刷新频率</th><th>引用条目</th></tr>
    </thead>
    <tbody>{档3_指标口径表}</tbody>
  </table>

  <h4 style="color: var(--fr-primary);">3.4 分阶段实施路径</h4>
  <table class="fr-table">
    <thead>
      <tr><th>阶段</th><th>周次</th><th>关键动作</th><th>产出物</th><th>责任方</th></tr>
    </thead>
    <tbody>{档3_实施路径表}</tbody>
  </table>

  <h4 style="color: var(--fr-primary);">3.5 给客户 sponsor 的一页价值陈述</h4>
  <div class="fr-card fr-card-value">
    <div style="font-size:12px; margin-bottom:8px;">致 {sponsor_role} 的价值简报</div>
    <div>{价值陈述内容}</div>
  </div>
</div>

<div class="fr-footer">
  本文档由 <span class="brand">帆软客户成功团队</span> · 访后落地助手 生成<br>
  生成时间：{timestamp} ｜ 模板版本：Skill-B v1.0 ｜ 文档编号：POST-{customer_abbr}-{datecompact}<br>
  <span style="color:var(--fr-text-sub); font-size:11px;">
    本建议基于客户拜访信息生成，最终方案需结合现场调研与技术评估
  </span>
</div>

</body>
</html>
```