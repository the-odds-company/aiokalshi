from aiokalshi.resources.events import Events
from aiokalshi.resources.markets import Markets
from httpx import AsyncClient


class Kalshi:
    def __init__(self, client: AsyncClient):
        self.markets: Markets = Markets(client)
        self.events: Events = Events(client)
