# Yahoo Finance MCP Server

## Tools

- get_ticker_info
- get_ticker_news
- search_quote
- search_news
- get_market
- get_sector_industy_mapping
- get_sector
- get_industry

TODO:

- An unified tool can handle all of the above tools

## Usage

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
