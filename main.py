from aiokalshi import Kalshi
from httpx import AsyncClient
import asyncio


async def main():
    async with AsyncClient() as c:
        kalshi = Kalshi(c)

        markets = await kalshi.markets.list()
        events = await kalshi.events.list()
        orderbook = await kalshi.markets.orderbook.get(markets.markets[0].ticker)

        print(orderbook)


asyncio.run(main())
