import json
from typing import Annotated

import yfinance as yf
from mcp.server.fastmcp import FastMCP
from pydantic import Field

from .types import Industry
from .types import Market
from .types import Sector

# https://github.com/jlowin/fastmcp/issues/81#issuecomment-2714245145
mcp = FastMCP("Yahoo Finance MCP Server", log_level="ERROR")


@mcp.tool()
def get_ticker_info(symbol: Annotated[str, Field(description="The stock symbol")]) -> str:
    """Retrieve information about a specific stock symbol using Yahoo Finance API."""
    ticker = yf.Ticker(symbol)
    return json.dumps(ticker.info, ensure_ascii=False)


@mcp.tool()
def get_ticker_news(symbol: Annotated[str, Field(description="The stock symbol")]) -> str:
    """Fetches news articles for a given stock ticker symbol."""
    ticker = yf.Ticker(symbol)
    news = ticker.get_news()
    return str(news)


@mcp.tool()
def search_quote(
    query: Annotated[str, Field(description="The search query")],
    max_results: Annotated[int, Field(description="The maximum number of results")] = 8,
) -> str:
    """Search for quotes using a query string."""
    search = yf.Search(query, max_results=max_results)
    return str(search.quotes)


@mcp.tool()
def search_news(
    query: Annotated[str, Field(description="The search query")],
    news_count: Annotated[int, Field(description="The number of news articles")] = 8,
) -> str:
    """Search for news articles using a query string."""
    search = yf.Search(query, news_count=news_count)
    assert len(search.news) == news_count, f"Expected {news_count} news articles, but got {len(search.news)}"
    return str(search.news)


@mcp.tool()
def get_market(
    market: Annotated[Market, Field(description="The market to get.")],
) -> str:
    """Retrieve information about a specific market."""
    m = yf.Market(market.value)
    return str(m.status) + "\n" + str(m.summary)


# @mcp.tool()
def get_sector_info(
    sector: Annotated[Sector, Field(description="The sector to get.")],
) -> str:
    """Retrieve information about a specific sector."""
    s = yf.Sector(sector.value)
    return "\n\n".join(
        [
            f"<overview>\n{s.overview}\n</overview>",
            f"<top_companies>\n{s.top_companies}\n</top_companies>",
            f"<top_etfs>\n{s.top_etfs}\n</top_etfs>",
            f"<top_mutual_funds>\n{s.top_mutual_funds}\n</top_mutual_funds>",
            f"<research_reports>\n{s.research_reports}\n</research_reports>",
        ]
    )


@mcp.tool()
def get_top_etfs(sector: Annotated[Sector, Field(description="The sector to get")]) -> str:
    """Retrieve the top ETFs in a specific sector."""
    s = yf.Sector(sector.value)
    return "\n".join(f"{symbol}: {name}" for symbol, name in s.top_etfs.items())


@mcp.tool()
def get_top_mutual_funds(sector: Annotated[Sector, Field(description="The sector to get")]) -> str:
    """Retrieve the top mutual funds in a specific sector."""
    s = yf.Sector(sector.value)
    return "\n".join(f"{symbol}: {name}" for symbol, name in s.top_mutual_funds.items())


# @mcp.tool()
def get_industry_info(
    industry: Annotated[Industry, Field(description="The industry to get")],
) -> str:
    """Retrieve information about a specific industry."""
    i = yf.Industry(industry.value)
    return "\n\n".join(
        [
            f"<overview>\n{i.overview}\n</overview>",
            f"<top_growth_companies>\n{i.top_growth_companies}\n</top_growth_companies>",
            f"<top_companies>\n{i.top_companies}\n</top_companies>",
            f"<top_performing_companies>\n{i.top_performing_companies}\n</top_performing_companies>",
            f"<research_reports>\n{i.research_reports}\n</research_reports>",
        ]
    )


# @mcp.tool()
def get_research_reports(
    sector: Annotated[Sector | None, Field(description="The sector to get")] = None,
    industry: Annotated[Industry | None, Field(description="The industry to get")] = None,
) -> str:
    if industry is not None:
        resp = yf.Industry(industry.value)
    elif sector is not None:
        resp = yf.Sector(sector.value)
    else:
        raise ValueError("Either sector or industry must be provided.")

    if not resp.research_reports:
        return "No research reports available."

    return str(resp.research_reports)


@mcp.tool()
def get_top_companies(
    sector: Annotated[Sector, Field(description="The sector to get")],
    top_n: Annotated[int, Field(description="Number of top companies to retrieve")],
) -> str:
    """Retrieve the top companies in a specific sector."""
    s = yf.Sector(sector.value)
    df = s.top_companies
    if df is None:
        return f"No top companies available for {sector.value} sector."

    return df.iloc[:top_n].to_json(orient="records")


def main():
    mcp.run()
