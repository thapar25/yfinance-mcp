# Yahoo Finance MCP Server

### GitHub

```json
{
  "mcpServers": {
    "yfmcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/narumiruna/yfinance-mcp",
        "yfmcp"
      ]
    }
  }
}
```

### PyPI

```json
{
  "mcpServers": {
    "yfmcp": {
      "command": "uvx",
      "args": ["yfmcp"]
    }
  }
}
```

### Local

```json
{
  "mcpServers": {
    "yfmcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/home/<user>/workspace/yfinance-mcp",
        "yfmcp"
      ]
    }
  }
}
```
