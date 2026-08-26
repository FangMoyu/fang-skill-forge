# Fang Skill Forge

> 把长期学习与真实实践，锻造成可复用的 Skill。
>
> Forge reusable skills from long-term learning and real practice.

这是一个用于长期沉淀个人 Codex Skill 的开源仓库。每个 Skill 都以独立目录维护，并保留自己的说明、引用资料、脚本和界面元数据。

## Skill 目录

| Skill | 用途 | 依赖 |
| --- | --- | --- |
| [`prepare-project-interview`](skills/prepare-project-interview/) | 从源码证据出发准备真实、可追问的简历项目内容 | 无 |
| [`grilling-resume-projects`](skills/grilling-resume-projects/) | 进行简历优先、逐题评分、阶梯难度的项目面试拷打 | 源码对齐场景需要 `prepare-project-interview` |

## 安装

### PowerShell

```powershell
$codexRoot = if ([string]::IsNullOrWhiteSpace($env:CODEX_HOME)) {
  Join-Path $env:USERPROFILE '.codex'
} else {
  $env:CODEX_HOME
}

Copy-Item -Recurse .\skills\prepare-project-interview (Join-Path $codexRoot 'skills\prepare-project-interview')
Copy-Item -Recurse .\skills\grilling-resume-projects (Join-Path $codexRoot 'skills\grilling-resume-projects')
```

### Bash

```bash
CODEX_ROOT="${CODEX_HOME:-$HOME/.codex}"
cp -R skills/prepare-project-interview "$CODEX_ROOT/skills/prepare-project-interview"
cp -R skills/grilling-resume-projects "$CODEX_ROOT/skills/grilling-resume-projects"
```

如果目标目录已经存在，请先备份并确认差异，不要直接覆盖正在使用的版本。

## 使用示例

```text
$prepare-project-interview 帮我为这个项目准备校招面试。
$grilling-resume-projects 请基于我的简历项目逐题拷打我。
```

## 两个 Skill 如何配合

`prepare-project-interview` 负责项目结构、源码链路、证据卡、简历 Claim 和掌握度；`grilling-resume-projects` 负责逐题提问、评分、答案纠错和难度调整。

只有简历内容时，可以直接使用 `grilling-resume-projects`。存在项目源码或需要核对简历与源码时，应同时安装两个 Skill。

## 真实性边界

- 源码能力、个人贡献和建议优化必须分开。
- 源码检查不能证明个人作者身份或生产使用情况。
- 没有可复现实验时，不写QPS、延迟和提升比例。
- 优化方案不能描述成当前已经实现的功能。

## 贡献与许可证

提交新的 Skill 或修改现有内容前，请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

本仓库使用 [MIT License](LICENSE)。

