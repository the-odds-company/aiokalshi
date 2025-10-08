from httpx import AsyncClient
from yarl import URL
from aiokalshi.models.markets import (
    GetMarketOrderBookRequest,
    GetMarketRequest,
    GetMarketResponse,
    GetMarketorderBookResponse,
    GetMarketsRequest,
    GetMarketsResponse,
    GetTradesRequest,
    GetTradesResponse,
)
from typing import Any, Unpack


def clean(query):
    clean_query: dict[str, Any] = {k: v for k, v in query.items() if v is not None}
    return clean_query


class Trades:
    BASE: URL = URL("https://api.elections.kalshi.com/trade-api/v2/markets")

    def __init__(self, client: AsyncClient):
        self.client: AsyncClient = client

    async def list(
        self, id: str, **query: Unpack[GetTradesRequest]
    ) -> GetTradesResponse:
        response = await self.client.get(
            str(self.BASE / id / "trades"), params=clean(query)
        )
        return GetTradesResponse(**response.json())


class OrderBook:
    BASE: URL = URL("https://api.elections.kalshi.com/trade-api/v2/markets")

    def __init__(self, client: AsyncClient):
        self.client: AsyncClient = client

    async def get(
        self, id: str, **query: Unpack[GetMarketOrderBookRequest]
    ) -> GetMarketorderBookResponse:
        response = await self.client.get(
            str(self.BASE / id / "orderbook"), params=clean(query)
        )

        return GetMarketorderBookResponse(**response.json())


class Markets:
    BASE: URL = URL("https://api.elections.kalshi.com/trade-api/v2/markets")

    def __init__(self, client: AsyncClient):
        self.client: AsyncClient = client
        self.orderbook: OrderBook = OrderBook(client)
        self.trades: Trades = Trades(client)

    async def list(self, **query: Unpack[GetMarketsRequest]) -> GetMarketsResponse:
        response = await self.client.get(str(self.BASE), params=clean(query))
        return GetMarketsResponse(**response.json())

    async def get(
        self, id: str, **query: Unpack[GetMarketRequest]
    ) -> GetMarketResponse:
        response = await self.client.get(str(self.BASE / id), params=clean(query))
        return GetMarketResponse(**response.json())
