from aiokalshi import Kalshi
from httpx import AsyncClient
import asyncio


async def main():
    async with AsyncClient(follow_redirects=True) as c:
        kalshi = Kalshi(c)

        # Test markets
        print("Testing Markets API...")
        markets = await kalshi.markets.list(limit=5)
        print(f"Found {len(markets.markets)} markets")
        if markets.markets:
            categories = set(m.category for m in markets.markets)
            print(f"Categories found in markets: {categories}")

        # Test events
        print("\nTesting Events API...")
        events = await kalshi.events.list(limit=5)
        print(f"Found {len(events.events)} events")
        if events.events:
            event_categories = set(e.category for e in events.events)
            print(f"Categories found in events: {event_categories}")

        # Test series - use a real category from the events
        print("\nTesting Series API...")
        test_category = list(event_categories)[0] if event_categories else "World"
        print(f"Testing with category: {test_category}")
        try:
            series_list = await kalshi.series.list(category=test_category)
            series_count = len(series_list.series) if series_list.series else 0
            print(f"Found {series_count} series in {test_category} category")
            if series_list.series and len(series_list.series) > 0:
                print(f"First series: {series_list.series[0].ticker}")
        except Exception as e:
            print(f"Series test error: {e}")

        # Test orderbook - try to find a market with actual orders
        print("\nTesting Orderbook...")
        if markets.markets:
            for market in markets.markets:
                orderbook = await kalshi.markets.orderbook.get(market.ticker, depth=5)
                yes_levels = len(orderbook.orderbook.yes) if orderbook.orderbook.yes else 0
                no_levels = len(orderbook.orderbook.no) if orderbook.orderbook.no else 0
                if yes_levels > 0 or no_levels > 0:
                    print(f"Market {market.ticker}: {yes_levels} yes levels, {no_levels} no levels")
                    break
            else:
                print(f"Checked {len(markets.markets)} markets - none had active orders")

        # Test trades - get global trades instead of per-market
        print("\nTesting Trades...")
        try:
            trades = await kalshi.markets.trades.list(limit=5)
            print(f"Found {len(trades.trades)} recent trades across all markets")
            if trades.trades:
                print(f"Most recent trade: {trades.trades[0].ticker} at {trades.trades[0].yes_price}¢")
        except Exception as e:
            print(f"Trades test error: {e}")

        print("\nAll tests completed!")


asyncio.run(main())
