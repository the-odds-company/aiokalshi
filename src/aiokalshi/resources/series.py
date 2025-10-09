from httpx import AsyncClient
from yarl import URL
from aiokalshi.models.series import (
    GetSeriesRequest,
    GetSeriesResponse,
    GetSeriesListRequest,
    GetSeriesListResponse,
)
from typing import Any, Unpack


def clean(query):
    clean_query: dict[str, Any] = {k: v for k, v in query.items() if v is not None}
    return clean_query


class Series:
    BASE: URL = URL("https://api.elections.kalshi.com/trade-api/v2/series")

    def __init__(self, client: AsyncClient):
        self.client: AsyncClient = client

    async def list(
        self, **query: Unpack[GetSeriesListRequest]
    ) -> GetSeriesListResponse:
        """Get a list of series filtered by category and optionally by tags"""
        response = await self.client.get(str(self.BASE), params=clean(query))
        return GetSeriesListResponse(**response.json())

    async def get(
        self, series_ticker: str, **query: Unpack[GetSeriesRequest]
    ) -> GetSeriesResponse:
        """Get details for a specific series by its ticker"""
        response = await self.client.get(
            str(self.BASE / series_ticker), params=clean(query)
        )
        return GetSeriesResponse(**response.json())
