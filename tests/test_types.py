from yfinance.const import SECTOR_INDUSTY_MAPPING

from yfmcp.types import Industry
from yfmcp.types import Sector


def test_sector() -> None:
    for s1, s2 in zip(Sector, SECTOR_INDUSTY_MAPPING, strict=True):
        assert s1.value == s2


def get_yfinance_industry() -> list[str]:
    result = []
    for industries in SECTOR_INDUSTY_MAPPING.values():
        for industry in industries:
            result.append(industry)
    return result


def test_industry() -> None:
    expected_industries = get_yfinance_industry()
    assert len(expected_industries) == len(Industry)
    for industry in Industry:
        assert industry.value in expected_industries
