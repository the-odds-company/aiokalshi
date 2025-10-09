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
    async with AsyncClient(follow_redirects=True) as client:
        # Make a client
        kalshi = Kalshi(client)

        # Get markets
        # Convention: list for grabbing paginated things, get for grabbing one-off queries
        markets = await kalshi.markets.list()
        markets_one = await kalshi.markets.list(limit=1)

        # Get one market
        market = await kalshi.markets.get(markets_one.markets[0].ticker)

        # Get the orderbook for a market
        orderbook = await kalshi.markets.orderbook.get(market.ticker, depth=5)

        # Get trades for a market
        trades = await kalshi.markets.trades.list(market.ticker, limit=10)

        # Get candlestick data for a market
        candlesticks = await kalshi.markets.candlesticks.get(
            series_ticker="SERIES-TICKER",
            market_ticker=market.ticker,
            start_ts=1700000000,
            end_ts=1700086400,
            period_interval=60  # 1 hour intervals
        )

        # Get events
        events = await kalshi.events.list(status="open", limit=10)

        # Get a specific event
        event = await kalshi.events.get(events.events[0].event_ticker)

        # Get event metadata
        metadata = await kalshi.events.metadata.list(event.event.event_ticker)

        # Get series by category
        series_list = await kalshi.series.list(category="Science and Technology")

        # Get a specific series
        if series_list.series:
            series = await kalshi.series.get(series_list.series[0].ticker)
```

## Status
This project is under rapid development. Expect breaking changes.
