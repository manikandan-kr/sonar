import asyncio
from mcp_use import MCPClient

async def main():

    client = MCPClient({
        "mcpServers": {
            "ga": {
                "url": "http://localhost:8123/mcp"
            }
        }
    })

    # 1️⃣ Connect
    await client.create_all_sessions()

    # 2️⃣ List tools
    tools = await client.search_tools(detail_level="full")
    print(tools)

    # print("\n=== AVAILABLE TOOLS ===")
    # for t in tools:
    #     print(t)
    #     print(f"- {t.name}")
    #     if hasattr(t, 'inputSchema') and t.inputSchema:
    #         props = t.inputSchema.get('properties', {})
    #         print(f"  inputs: {list(props.keys())}")
    # print("\n=== DETAILED TOOL INFO ===")
    # for t in tools["results"]:
    #     print(f"- {t['server']}.{t['name']}")
    #     print(f"  inputs: {list(t['inputSchema'].get('properties', {}).keys())}")

    # 3️⃣ Get GA session
    ga = client.get_session("ga")

    # 4️⃣ Call get_account_summaries
    result = await ga.call_tool("get_account_summaries", {})
    print("\n=== ACCOUNT SUMMARIES ===")
    print(result)

    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())
