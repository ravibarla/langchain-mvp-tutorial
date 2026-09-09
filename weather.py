from mcp.server.fastmcp import FastMCP

mcp=FastMCP("weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get the weather of a location
    """
    return "The weather is always sunny"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")