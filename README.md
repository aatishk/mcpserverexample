# Installation Steps

To install the `add_tool` MCP server, add the following to your mcp server json config file.

```json
"mcp server": {
    "command": "uvx",
    "args": [
        "--from",
        "git+https://github.com/aatishk/mcpserverexample.git",
        "mcp-server"
    ]
}
```

Run the command directly if needed:

```bash
uvx --from git+https://github.com/aatishk/mcpserverexample.git mcp-server
```