from mcp.server.fastmcp import FastMCP

mcp=FastMCP("math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """__summary__
    Add two numbers
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """__summary__
    Subtract two numbers
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """__summary__
    Multiply two numbers
    """
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")