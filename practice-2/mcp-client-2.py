from fastmcp import FastMCP
from contextlib import AsyncExitStack
from mcp import StdioServerParameters, stdio_client,ClientSession
from mistralai import Mistral
stack = AsyncExitStack()
async def connect_to_server():
    server_params = StdioServerParameters(command = "python", args = ["practice-2/mcp-server-2.py"])

    client = await stack.enter_async_context(stdio_client(server_params))
    reader, writer = client
    session = await stack.enter_async_context(ClientSession(reader, writer))
    await session.initialize()
    s = await session.list_tools()
    return session


async def get_mcp_tools(server_session=None):
    tools = await server_session.list_tools()
    return [
        {
            "type" : "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema
            }
        } for tool in tools.tools
    ]

async def process_query(query, server_session):
    key = "TH010EVBGKkYN0TxFGX4jhmXmSoH6Ldz"
    client: Mistral  = Mistral(api_key = key)
    tools = await get_mcp_tools(server_session)
    model = "mistral-large-latest"
    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "user", "content": query}
        ],
        tools=tools,
        tool_choice="required"
    )
    return response


async def main():
    server_session = await connect_to_server()
    query = "What is Python?"
    res = await process_query(query, server_session)
    print(res)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    print("Client is running...")  # This will be printed when the client starts