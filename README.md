# SCI Writing Expert for Codex

一个面向科研论文写作的 Codex Skill，覆盖：

- 中文科研内容翻译为自然、克制、符合 SCI 习惯的英文；
- 英文句子、段落和章节润色；
- 逻辑、衔接、时态、语态、冠词、因果与语气强度检查；
- Introduction、Methods、Results、Discussion/Conclusion、Abstract 和 Title 的功能结构诊断；
- 全文故事线、章节排布、证据链和前后呼应审查；
- 目标期刊与代表性论文语料适配；
- 在不改变数据、引用、公式、术语和证据强度的前提下修改。

## 设计原则

```text
科学含义与证据
> 全文故事线
> 章节功能
> 段落逻辑
> 句子清晰度
> 语法与词汇
```

该 Skill 不会虚构数据、引用、机制、结果、局限或未经支持的结论。

## Codex 结构

```text
sci-writing-expert-skill/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── scripts/
├── tests/
└── .github/workflows/validate.yml
```

`SKILL.md` 负责路由与核心约束，`references/` 按任务渐进加载，避免每次把整套知识全部塞入上下文。

## 安装

### 用户级安装

```bash
mkdir -p "$HOME/.agents/skills"
cp -R sci-writing-expert-skill "$HOME/.agents/skills/sci-writing-expert"
```

或建立符号链接：

```bash
ln -s "$(pwd)/sci-writing-expert-skill" \
  "$HOME/.agents/skills/sci-writing-expert"
```

### 项目级安装

```bash
mkdir -p .agents/skills
cp -R sci-writing-expert-skill .agents/skills/sci-writing-expert
```

Codex 会扫描 `.agents/skills` 和 `$HOME/.agents/skills`。安装后若未出现，重启 Codex。

## 使用

显式调用：

```text
$sci-writing-expert
```

也可以直接描述任务，由 Codex 根据 `description` 自动匹配。

### 中文翻译

```text
$sci-writing-expert
把下面中文翻译为地道的 SCI 英文。保持结论强度，不增加机制：
...
```

### 句段润色

```text
$sci-writing-expert
润色下面的 Results 段落。先判断句子顺序和结果解释是否合理，再修改英文：
...
```

### 结构审查

```text
$sci-writing-expert
审查这篇初稿的 Introduction、Results 和 Discussion 是否前后呼应。
先给出结构诊断和优先级，不要立即逐句改写。
```

### 摘要与标题

```text
$sci-writing-expert
把这个 Abstract 压缩到 200 词以内，保留关键定量结果，
并给出 5 个中性、可检索的标题。
```

## 推荐输入

为了提高稳定性，可同时提供：

- 目标期刊和文章类型；
- 论文所属领域；
- 文本所在章节；
- 术语表或必须保留的表达；
- 3-5 篇目标期刊近期代表性文章；
- 修改深度：轻度润色、深度重写、结构诊断或全文审查。

## 验证

```bash
python scripts/validate_skill.py
```

## 一键发布到 GitHub

已安装并登录 GitHub CLI 后：

```bash
bash scripts/publish_to_github.sh shizaishiwo323 sci-writing-expert-skill public
```

脚本会初始化远程仓库、设置 `origin` 并推送当前分支；若仓库已存在则只推送。

## 来源与版权

该 Skill 受到 Hilary Glasman-Deal 的 *Science Research Writing for Non-Native Speakers of English* 的教学框架启发，但仓库内容为独立归纳、重新组织和改写，不包含原书 PDF、章节转录、练习答案或大段原文。

详见 `NOTICE.md` 与 `references/source_notes.md`。
