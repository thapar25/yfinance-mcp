# Yahoo Finance MCP Server

A simple MCP server for Yahoo Finance using yfinance. This server provides a set of tools to fetch stock data, news, and other financial information.

## Tools

- get_ticker_info
- get_ticker_news
- search_quote
- search_news
- get_market
- get_sector_industy_mapping
- get_sector
- get_industry

## Usage

Add the following configuration to your MCP server configuration file.

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
