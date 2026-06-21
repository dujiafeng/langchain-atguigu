import asyncio
import os

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

load_dotenv()

client = MultiServerMCPClient(
    {
        "time": {
            "transport": "stdio",
            "command": "python",
            "args": ["weather_mcp_server.py"]
        }
    }
)


async def main():
    tools = await client.get_tools()
    print("可用的 MCP 工具：", [tool.name for tool in tools])  # 应该看到 "get_weather"

    model = init_chat_model(
        model="qwen-plus",
        model_provider="openai",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url=os.getenv("DASHSCOPE_BASE_URL")
    )

    agent = create_agent(model=model, tools=tools,
                         system_prompt="你是一个天气查询助手，可以使用 get_weather 工具获取实时天气。")

    result = await agent.ainvoke({
        "messages": [HumanMessage("北京现在天气怎么样？")]
    })

    for message in result["messages"]:
        message.pretty_print()


    # get_weather_tool = next(t for t in tools if t.name == "get_weather")
    # direct_result = await get_weather_tool.ainvoke({"city": "上海"})
    # print("\n直接调用工具结果：", direct_result)


# ---------- 3. 启动 ----------
if __name__ == "__main__":
    asyncio.run(main())
