from mcp.server.fastmcp import FastMCP

# Crete and MCP server
mcp = FastMCP("Demo")

# add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

