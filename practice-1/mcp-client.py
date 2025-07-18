from mcp import StdioServerParameters,stdio_client, ClientSession

async def main():
    server_params = StdioServerParameters(command = "python", args = ["practice-1/mcp-server.py"])

    async with stdio_client(server_params) as (reader, writter):
        async with ClientSession(reader, writter) as session:
            await session.initialize()
            res = await session.call_tool("add", arguments={'a':2, 'b':3})
            print(res.content[0].text)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())