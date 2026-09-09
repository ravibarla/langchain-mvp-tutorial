from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain.agents import create_agent
from dotenv import load_dotenv
import os

import asyncio

load_dotenv()

raw_llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",  # Or your chosen Qwen model
    task="conversational"                # Must match provider's supported task
)

async def main():
    client=MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                 "args":["mathserver.py"], ## ensure absolute path,
                "transport": "stdio"
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
            },
        }
    )

    tools=await client.get_tools()
    model = ChatHuggingFace(
    llm=raw_llm
    )
    agent=create_agent(
    model,tools
    )

    math_response=await agent.ainvoke({"messages":[{"role": "user","content": "What is (10 + 20) * 3?"}]})
    print(math_response['messages'][-1].content)

    weather_response=await agent.ainvoke({"messages":[{"role": "user","content":  "What is the weather in Tokyo?"}]})
    print(weather_response['messages'][-1].content)

asyncio.run(main())