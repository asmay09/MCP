from fastmcp import FastMCP

mcp = FastMCP()


@mcp.tool()
def fetch():
    """use this tool to fetch data from a source"""
    return {"data": "Hello MCP"}


@mcp.tool()
def process(path: str):
    """Use this tool to process the fetched data."""
    return {"processed_data": "Data has been processed at path: " + path}


if __name__ == "__main__":
    mcp.run(transport="stdio")
