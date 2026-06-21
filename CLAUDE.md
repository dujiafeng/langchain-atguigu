# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

LangChain 学习教程项目，包含 10 个循序渐进的模块（01-10），每个 `.py` 文件是独立可执行的脚本，无共享库代码。技术栈：LangChain >= 1.3.8、阿里云百炼 DashScope（主力 LLM）、DeepSeek、Ollama。

## 环境与包管理

```bash
# 安装依赖（使用 uv，非 pip）
uv sync

# 添加新包
uv add <package-name>

# 运行任意脚本
python 01_helloworld/LangChainV1.0.py
```

- `pyproject.toml` 已配置清华 PyPI 镜像为默认源
- Python >= 3.11
- `.env` 文件存放 API 密钥（DASHSCOPE_API_KEY、DEEPSEEK_API_KEY、DASHSCOPE_BASE_URL），通过 `python-dotenv` 加载
- **禁止提交 `.env` 文件**（已在 `.gitignore` 中）

## 模块架构

```
01_helloworld/    入门：多模型接入、LangChain 版本差异
02_models_io/     模型 I/O：init_chat_model() 统一入口 + 各供应商适配
03_ollama/        本地模型：Ollama 部署与 Agent
04_prompt/        提示词工程：PromptTemplate / ChatPromptTemplate / 外部加载、各种调用方式
05_parser/        输出解析：StrOutputParser / JsonOutputParser / Pydantic / TypedDict 结构化输出
06_lcel/          表达式语言：| 管道链式组合、RunnableParallel / RunnableBranch / RunnableLambda
07_memory/        对话记忆：InMemory / Redis 持久化、RunnableWithMessageHistory
08_tools/         工具定义：@tool 装饰器、Pydantic 参数校验、工具绑定与调用链
09_embedding/     文本向量化：DashScope / OpenAI 嵌入、余弦相似度、Redis 向量存储
10_rag/           RAG 管道：文档加载（TXT/CSV/JSON/PDF/Markdown/DOCX）、文本分割、向量检索 + LLM 回答
```

## 项目约定

- **模型初始化**：统一使用 `init_chat_model()` 入口，指定 `model`、`model_provider="openai"`、`api_key`、`base_url`
- **环境变量**：DashScope 密钥使用 `os.getenv("DASHSCOPE_API_KEY")`，不是 `"aliQwen-api"`（旧代码混用，新增代码统一 DashScope 变量名）
- **日志**：使用 `loguru`（`from loguru import logger`），不用 `print` 做调试输出
- **注释**：中文
- **Redis 版本**：锁定 `==5.3.1`，不要升级
- **文件命名**：`<Module>_<Concept>.py`
- **向量存储**：Redis（`langchain-redis`），连接地址 `redis://localhost:6379`（单机）或 `redis://localhost:26379`（示例中的 Sentinel 端口）
- **无测试/无 CI/CD/无 linter** — 纯学习项目

## 参考

- 更详细的开发约定见 `AGENTS.md`
- 更详细的学习路径见 `README.md`
