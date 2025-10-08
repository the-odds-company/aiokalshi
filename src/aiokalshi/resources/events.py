from httpx import AsyncClient
from yarl import URL
from aiokalshi.models.events import (
    GetEventMetadataRequest,
    GetEventMetadataResponse,
    GetEventsRequest,
    GetEventsResponse,
    GetEventRequest,
    GetEventResponse,
)
from typing import Any, Unpack


def clean(query):
    clean_query: dict[str, Any] = {k: v for k, v in query.items() if v is not None}
    return clean_query


class Metadata:
    BASE: URL = URL("https://api.elections.kalshi.com/trade-api/v2/events")

    def __init__(self, client: AsyncClient):
        self.client: AsyncClient = client

    async def list(
        self, id: str, **query: Unpack[GetEventMetadataRequest]
    ) -> GetEventMetadataResponse:
        response = await self.client.get(
            str(self.BASE / id / "metadata"), params=clean(query)
        )
        return GetEventMetadataResponse(**response.json())


class Events:
    BASE: URL = URL("https://api.elections.kalshi.com/trade-api/v2/events")

    def __init__(self, client: AsyncClient):
        self.client: AsyncClient = client
        self.metadata: Metadata = Metadata(client)

    async def list(self, **query: Unpack[GetEventsRequest]) -> GetEventsResponse:
        response = await self.client.get(str(self.BASE), params=clean(query))
        return GetEventsResponse(**response.json())

    async def get(self, id: str, **query: Unpack[GetEventRequest]) -> GetEventResponse:
        response = await self.client.get(str(self.BASE / id), params=clean(query))
        return GetEventResponse(**response.json())
