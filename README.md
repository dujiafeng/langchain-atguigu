# LangChain 学习教程

基于 LangChain 框架的循序渐进学习教程，涵盖从基础到 RAG 的完整知识体系。

## 环境要求

- Python >= 3.11
- [uv](https://docs.astral.sh/uv/) 包管理器
- (可选) Ollama 本地模型服务

## 快速开始

```bash
# 1. 克隆仓库
git clone <repo-url>
cd langchain_new

# 2. 创建虚拟环境并安装依赖
uv sync

# 3. 配置环境变量
# 复制 .env 文件并填入你的 API Key：
# - DASHSCOPE_API_KEY: 阿里云百炼 API 密钥
# - DEEPSEEK_API_KEY: DeepSeek API 密钥

# 4. 运行任意脚本
python 01_helloworld/LangChainV1.0.py
```

## 学习路径

| 模块 | 主题 | 内容 |
|------|------|------|
| 01_helloworld | 入门与环境验证 | 多模型接入、版本差异 |
| 02_models_io | 模型 I/O | OpenAI / DeepSeek / Qwen / Ollama 多供应商适配 |
| 03_ollama | 本地模型 | Ollama 本地部署与工具调用 Agent |
| 04_prompt | 提示词工程 | PromptTemplate / ChatPromptTemplate / 外部加载 |
| 05_parser | 输出解析 | Str / JSON / Pydantic 解析器与结构化输出 |
| 06_lcel | 表达式语言 | 链式组合、并行、分支、Lambda 转换 |
| 07_memory | 对话记忆 | 内存 / Redis 持久化、对话历史管理 |
| 08_tools | 工具定义 | @tool 装饰器、Pydantic 参数校验、API 工具 |
| 09_embedding | 文本向量化 | 多供应商嵌入、余弦相似度、向量存储 |
| 10_rag | 检索增强生成 | 文档加载、文本分割、向量检索、RAG 管道 |

## 技术栈

- **核心框架**: LangChain >= 1.3.8
- **LLM 后端**: 阿里云百炼 DashScope（默认）、DeepSeek、Ollama
- **向量存储**: Redis (==5.3.1)
- **工具集成**: OpenWeatherMap API
- **包管理**: uv

## 备注

- 所有脚本独立运行，无框架依赖顺序
- 代码注释及文档均为中文
- 日志统一使用 loguru
