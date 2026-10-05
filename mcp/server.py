from mcp.server import Server
from mcp.types import Tool, TextContent
import asyncio

# Initialize MCP server
app = Server("pakistan-law-mcp")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available Pakistan law tools."""
    return [
        Tool(
            name="search_pakistan_law",
            description="Search for Pakistani laws, acts, or sections based on a query.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The legal term, act name, or section to search for (e.g., Pakistan Penal Code Section 302, Cyber Crime Act)."
                    }
                },
                "required": ["query"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Execute the requested tool."""
    if name == "search_pakistan_law":
        query = arguments.get("query", "").lower()
        
        # Sample mock database for demonstration of Pakistan Law
        # In a real application, you can connect this to a vector DB or full database
        laws_db = {
            "302": "Pakistan Penal Code (PPC) Section 302: Punishment of qatl-i-amd (Premeditated murder). Death-sentence or imprisonment for life as ta'zir.",
            "420": "Pakistan Penal Code (PPC) Section 420: Cheating and dishonestly inducing delivery of property. Imprisonment up to 7 years and fine.",
            "cyber": "Prevention of Electronic Crimes Act (PECA) 2016: Governs cybercrimes, electronic fraud, unauthorized access, and cyberstalking in Pakistan."
        }
        
        # Simple search logic
        results = []
        for key, value in laws_db.items():
            if key in query or any(word in query for word in value.lower().split()):
                results.append(value)
                
        if not results:
            response_text = f"No direct legal match found for query: '{query}'. Please consult official Pakistan Code records for detailed jurisprudence."
        else:
            response_text = "\n\n".join(results)
            
        return [TextContent(type="text", text=response_text)]
    
    raise ValueError(f"Unknown tool: {name}")

async def main():
    from mcp.server.stdio import stdio_server
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())