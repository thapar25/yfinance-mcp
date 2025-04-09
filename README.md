# Yahoo Finance MCP Server

A simple MCP server for Yahoo Finance using yfinance. This server provides a set of tools to fetch stock data, news, and other financial information.

## Tools

- **get_ticker_info**

  - Retrieve stock data including company info, financials, trading metrics and governance data.
  - Inputs:
    - `symbol` (string): The stock symbol.

- **get_ticker_news**

  - Fetches recent news articles related to a specific stock symbol with title, content, and source details.
  - Inputs:
    - `symbol` (string): The stock symbol.

- **search_quote**

  - Search for stock quotes with company name, exchange, sector and industry information by keyword.
  - Inputs:
    - `query` (string): The search query.
    - `max_results` (number, optional): Maximum number of results (default 8).

- **search_news**

  - Search for financial news articles matching a keyword with title, source and publication details.
  - Inputs:
    - `query` (string): The search query.
    - `news_count` (number, optional): Number of news articles (default 8).

- **get_top_etfs**

  - Retrieve popular ETFs for a sector, returned as a list in 'SYMBOL: ETF Name' format.
  - Inputs:
    - `sector` (string): The sector to get ETFs for.

- **get_top_mutual_funds**

  - Retrieve popular mutual funds for a sector, returned as a list in 'SYMBOL: Fund Name' format.
  - Inputs:
    - `sector` (string): The sector to get mutual funds for.

- **get_top_companies**

  - Get top companies in a sector with name, analyst rating, and market weight as JSON array.
  - Inputs:
    - `sector` (string): The sector to get companies for.
    - `top_n` (number): Number of top companies to retrieve.

- **get_top_growth_companies**

  - Get top growth companies grouped by industry within a sector as JSON array with growth metrics.
  - Inputs:
    - `sector` (string): The sector to get companies for.
    - `top_n` (number): Number of top growth companies to retrieve.

- **get_top_performing_companies**

  - Get top performing companies grouped by industry within a sector as JSON array with performance metrics.
  - Inputs:
    - `sector` (string): The sector to get companies for.
    - `top_n` (number): Number of top performing companies to retrieve.

## Usage

1. [Install uv.](https://docs.astral.sh/uv/getting-started/installation/)
2. Add the following configuration to your MCP server configuration file.

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

```json
{
  "mcpServers": {
    "yfmcp": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "narumi/yfinance-mcp"]
    }
  }
}
```
