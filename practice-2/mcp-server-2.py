import json

from fastmcp import FastMCP

mcp = FastMCP(name= "test",port=3000)

@mcp.tool(description= "if anything about python asks, then call this tool")
def get_data():
    '''
    retrieves entire sample data as a formated string.

    :return:
    formatted string contains all Q&A pairs from the sample data file.
    '''
    with open("sample_data/sample_data.json", "r") as f:
        data = json.load(f)

        return f"sample input data: {json.dump(data, f, indent=4)}"

if __name__ == "__main__":
    # transport types : "stdio", "sse", "streamable-http"
    transport = 'stdio'
    if transport == 'stdio':
        mcp.run(transport='stdio')
    elif transport == 'sse':
        mcp.run(transport='sse')
    elif transport == 'streamable-http':
        mcp.run(transport='streamable-http')
    print("Server is running...")  # This will be printed when the server starts

