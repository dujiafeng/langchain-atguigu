# AGENTS.md

## 包管理
- 使用 `uv` 管理依赖，非 pip
- `pyproject.toml` 已配置清华 PyPI 镜像为默认源
- 同步依赖: `uv sync`，添加包: `uv add <pkg>`

## 运行方式
- 10 个编号模块 (01-10)，每个 `.py` 文件是独立的可执行脚本
- 直接运行: `python 04_prompt/invoke/LLM_Invoke.py`
- 无统一入口点，`main.py` 是 PyCharm 生成的占位文件

## 环境与密钥
- 环境变量通过 `.env` + `python-dotenv` 加载
- 密钥文件已被 `.gitignore` 忽略，切勿手动提交

## 开发约定
- **模型初始化**: 优先使用 `init_chat_model()` 统一入口
- **日志**: 统一使用 `loguru` (`from loguru import logger`)
- **代码注释**: 中文
- **Redis 版本**: 锁定 `==5.3.1`，勿随意升级

## 主要后端
- 主力 LLM 后端：阿里云百炼 DashScope（OpenAI 兼容接口）
- 嵌入模型：DashScope 或 langchain-community 集成
- 本地模型：Ollama

## 文件命名
- 模式: `<Module>_<Concept>.py`

## 测试与 CI
- 无测试框架、无 CI/CD、无 linter/formatter 配置
