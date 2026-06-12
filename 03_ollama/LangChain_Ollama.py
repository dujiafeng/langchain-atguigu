# pip install -qU langchain-ollama
# pip install -U ollama
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from datetime import date

# 设置本地模型，不使用深度思考
model = ChatOllama(base_url="http://localhost:11434", model="qwen3.6:27b", reasoning=False)


@tool
def get_today() -> str:
    """获取当前系统日期的字符串表示，格式为 YYYY-MM-DD。"""
    today = date.today()
    return today.strftime("%Y-%m-%d")

@tool
def get_city() -> str:
    """获取当前的城市名称"""
    return "北京"

@tool
def get_weather(date:str,city:str) -> str:
    """
    根据城市和日期获取指定城市的天气
    Args:
        date: 日期，格式为 YYYY-MM-DD
        city: 城市名称

    Returns:
        天气信息
    """
    return f"{city} - {date} 为晴天，温度20℃~30℃"

# 使用中间件的 Agent
agent = create_agent(
    model=model,
    tools=[get_today,get_city,get_weather],
    system_prompt="你是一个乐于助人的智能助手，可以调用本地工具",
)
# 打印结果，
response = agent.invoke({"messages":["今天天气怎么样？"]})
for msg in response['messages']:
    msg.pretty_print()
