import random
from fastmcp import FastMCP
import json

mcp=FastMCP(name="Demo Server1")

@mcp.tool
def roll_dice(n_dice:int =1) -> list[int]:
    """Roll n dice 6 sided dice and return the result"""
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.tool
def add_number(a:float,b:float)-> float:
    """This function is two add two numbers and print the result"""
    return a+b

@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server"""
    info={
        "name":"Simple Calculator Server",
        "version":"1.0.0",
        "description":"A basic MCP server with math tools",
        "tools":['add_number','roll_dice'],
        "author":"Mohit Singla"
    }
    return json.dumps(info,indent=2)


if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000 )
