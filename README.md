# An async-native, fully type-hinted Python client for Kalshi

`aiokalshi` provides a friendly interface into Kalshi's REST API (websocket support is in development). The library offers the benefits of asynchronous code, editor autocomplete, and parity with Kalshi's API while being easy to use and not requiring authentication.

## Installation
```bash
uv add aiokalshi
```
```bash
pip install aiokalshi
```

## Usage
`aiokalshi` uses the same structure as Kalshi's documented RESTful API. Every query parameter available is provided in a typed fashion, meaning you get autocomplete when customizing your queries.

Every response includes all of the available data and makes use of Pydantic.

```python
from httpx import AsyncClient
from aiokalshi import Kalshi

async def main():
    async with AsyncClient() as client:
        kalshi = Kalshi(client)
        markets = await kalshi.markets.list()
        markets_one = await kalshi.markets.list(limit=1)
        market = await kalshi.markets.get(markets_one.markets[0].ticker)
        orderbook = await kalshi.markets.orderbook.get(market.ticker, depth=5)
```

## Status
This project is under rapid development. Expect breaking changes.
