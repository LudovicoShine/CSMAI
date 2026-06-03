# Post-Visit Scripts

本目录用于 Post-Visit 的轻量自动化预处理。

本轮只做 Phase 1：**先把 transcript 入口规范化**，不是完整音频转写系统。

## 当前包含

- `prepare_post_visit.py`：读取 transcript 与可选补充文件，自动判断 `transcript_quality`，输出可直接喂给 `post-visit-landing` Skill 的标准化 JSON payload

## 当前不包含

- 音频文件转写
- OpenAI Whisper 真接入
- Dora 真接入
- 网络调用、重试、鉴权、批量处理

这些能力属于 Phase 2 预留，不在本轮实现。

## 用法

```bash
python SCRIPTS/prepare_post_visit.py \
  --transcript-file path/to/transcript.txt \
  --annotations-file path/to/annotations.md \
  --skill1-output-file path/to/pre_visit.md \
  --meeting-date 2026-06-02 \
  --customer-industry "政策研究咨询"
```

在公司平台目录中使用大写脚本目录时：

```bash
python SCRIPTS/prepare_post_visit.py \
  --transcript-file path/to/transcript.txt \
  --annotations-file path/to/annotations.md
```

追加使用反馈：

```bash
python SCRIPTS/append_feedback.py \
  --issue "输出漏掉客户配合事项" \
  --impact "客户版简报无法直接发出" \
  --suggestion "强化第 7 节客户配合事项检查"
```

## 支持参数

- `--transcript-file`：必填，录音转写文本或详细会议纪要
- `--annotations-file`：选填，CSM 对现场反馈的结构化标注
- `--skill1-output-file`：选填，Pre-Visit 输出
- `--meeting-date`：选填
- `--customer-industry`：选填
- `--transcript-quality`：选填，手动覆盖自动判断结果

## 输出字段

输出为一个 JSON payload，字段固定如下：

- `transcript`
- `transcript_quality`
- `transcript_quality_signals`
- `csm_annotations`
- `skill1_output`
- `meeting_date`
- `customer_industry`
- `needs_manual_review`
- `notes`

## transcript_quality 自动判断规则

识别模糊标记：

- `[听不清]`
- `[不清楚]`
- `[模糊]`
- `???`

统计：

- `N`：transcript 总字符数
- `M`：模糊标记总数

默认判定：

- `碎片化`：`N < 1200` 或 `M >= 12`
- `部分模糊`：`1200 <= N < 2500`，或 `3 <= M < 12`
- `完整清晰`：`N >= 2500` 且 `M < 3`

若满足以下任一条件，会把 `needs_manual_review` 置为 `true`：

- 命中边界值或接近边界值
- 未提供 `annotations`
- 自动判断结果不是 `完整清晰`

若手动传入 `--transcript-quality`：

- `transcript_quality` 以手动值为准
- 自动判断仍保留在 `transcript_quality_signals.inferred_quality`

## Phase 2 预留方向

- 增加 `--audio-file`
- 设计 OpenAI Whisper provider
- 设计 Dora provider
- 补重试、鉴权、成本控制与批量处理
