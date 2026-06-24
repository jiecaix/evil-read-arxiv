# 快速开始指南

这是使用 evil-read-arxiv skills 的三步快速设置指南。

## 第一步：安装 CLI 依赖环境

推荐使用 `uv tool`，依赖会安装到隔离环境，不污染全局 Python：

```bash
# 本地开发
uv tool install -e .

# 从 Git 仓库安装时
uv tool install git+https://github.com/<owner>/evil-read-arxiv.git
```

确认命令可用：

```bash
evil-read-arxiv --help
```

## 第二步：安装需要的 skills

仓库中的 skills 位于：

```text
skills/evil-read-arxiv/<skill-name>/SKILL.md
```

使用 cc-switch 时：

```bash
cc-switch skills repos add <repo-url>
cc-switch skills discover evil-read-arxiv
cc-switch skills install start-my-day
cc-switch skills install paper-analyze
cc-switch skills install extract-paper-images
cc-switch skills install paper-search
cc-switch skills install conf-papers
```

手动安装时，只复制你需要的单个 skill 目录：

```bash
cp -r skills/evil-read-arxiv/start-my-day ~/.claude/skills/
cp -r skills/evil-read-arxiv/paper-analyze ~/.claude/skills/
```

`skills/evil-read-arxiv` 是唯一的 skill 源目录；CLI 安装时会把这份目录作为资源安装，不需要维护第二份脚本。

## 第三步：配置 Obsidian Vault

设置 `OBSIDIAN_VAULT_PATH` 环境变量：

```bash
# macOS/Linux
export OBSIDIAN_VAULT_PATH="/Users/yourname/Documents/Obsidian Vault"

# Windows PowerShell
[System.Environment]::SetEnvironmentVariable("OBSIDIAN_VAULT_PATH", "C:/Users/YourName/Documents/Obsidian Vault", "User")
```

创建配置文件：

```bash
cp config.example.yaml config.yaml
mkdir -p "$OBSIDIAN_VAULT_PATH/99_System/Config"
cp config.yaml "$OBSIDIAN_VAULT_PATH/99_System/Config/research_interests.yaml"
```

Vault 目录至少包含：

```text
你的Vault/
├── 10_Daily/
├── 20_Research/
│   └── Papers/
└── 99_System/
    └── Config/
        └── research_interests.yaml
```

## 开始使用

在 Claude/Codex 中调用已安装的 skill，例如：

```text
start my day
paper-analyze 2602.12345
conf-papers 2025 ICLR,CVPR
```

也可以直接运行底层 CLI：

```bash
evil-read-arxiv search-arxiv --help
evil-read-arxiv extract-images --help
```
