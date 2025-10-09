from pydantic import BaseModel
import datetime
from typing import TypedDict, Literal, Optional

Status = Literal["unopened", "open", "closed", "settled"]


class BidAskDistribution(BaseModel):
    """OHLC data for bid/ask prices"""

    open: int | None = None
    high: int | None = None
    low: int | None = None
    close: int | None = None


class PriceDistribution(BaseModel):
    """OHLC and volume data for trade prices"""

    open: int | None = None
    high: int | None = None
    low: int | None = None
    close: int | None = None


class MarketCandlestick(BaseModel):
    """Candlestick data for a market over a specific time period"""

    end_period_ts: int
    open_interest: int | None = None
    price: PriceDistribution | None = None
    volume: int | None = None
    yes_ask: BidAskDistribution | None = None
    yes_bid: BidAskDistribution | None = None


class OrderBook(BaseModel):
    no: list[tuple[int, int]] | None = None
    yes: list[tuple[int, int]] | None = None
    no_dollars: list[tuple[float, float]] | None = None
    yes_dollars: list[tuple[float, float]] | None = None


class Trade(BaseModel):
    count: int
    created_time: datetime.datetime
    no_price: int
    taker_side: str
    ticker: str
    trade_id: str
    yes_price: int


class Market(BaseModel):
    ticker: str
    event_ticker: str
    market_type: str
    subtitle: str
    yes_sub_title: str
    no_sub_title: str
    open_time: datetime.datetime
    close_time: datetime.datetime
    expiration_time: datetime.datetime
    latest_expiration_time: datetime.datetime
    settlement_timer_seconds: int
    status: str
    response_price_units: str
    notional_value: int
    tick_size: int
    yes_bid: int
    yes_ask: int
    no_bid: int
    no_ask: int
    last_price: int
    previous_yes_bid: int
    previous_yes_ask: int
    previous_price: int
    volume: int
    volume_24h: int
    liquidity: int
    open_interest: int
    result: str
    can_close_early: bool
    expiration_value: str
    category: str
    risk_limit_cents: int
    rules_primary: str
    rules_secondary: str

    title: str | None = None
    notional_value_dollars: str | None = None
    yes_bid_dollars: str | None = None
    yes_ask_dollars: str | None = None
    no_bid_dollars: str | None = None
    no_ask_dollars: str | None = None
    last_price_dollars: str | None = None
    previous_yes_bid_dollars: str | None = None
    previous_yes_ask_dollars: str | None = None
    previous_price_dollars: str | None = None
    liquidity_dollars: str | None = None
    settlement_value: int | None = None
    settlement_value_dollars: str | None = None


class GetMarketsRequest(TypedDict, total=False):
    """Query parameters for the Get Markets endpoint"""

    limit: int | None  # Number of results per page (max 1000, default 100)
    cursor: str | None  # Pagination cursor
    event_ticker: str | None  # Filter by event ticker
    series_ticker: str | None  # Filter by series ticker
    max_close_ts: int | None  # Filter by maximum close timestamp
    min_close_ts: int | None  # Filter by minimum close timestamp
    status: Status | None  # Filter by market status
    tickers: str | None  # Comma-separated list of market tickers


class GetMarketsResponse(BaseModel):
    cursor: str
    markets: list[Market]


class GetTradesRequest(TypedDict, total=False):
    """Query parameters for the Get Trades endpoint"""

    limit: int | None  # Number of results per page (max 1000, default 100)
    cursor: str | None  # Pagination cursor
    ticker: str | None  # Filter by market ticker
    min_ts: int | None  # Filter by minimum timestamp
    max_ts: int | None  # Filter by maximum timestamp


class GetTradesResponse(BaseModel):
    cursor: str
    trades: list[Trade]


class GetMarketRequest(TypedDict, total=False): ...


class GetMarketResponse(BaseModel):
    market: Market


class GetMarketOrderBookRequest(TypedDict, total=False):
    depth: int


class GetMarketorderBookResponse(BaseModel):
    orderbook: OrderBook


class GetMarketCandlesticksRequest(TypedDict, total=False):
    """Query parameters for the Get Market Candlesticks endpoint"""

    start_ts: int  # Required - Start timestamp (Unix)
    end_ts: int  # Required - End timestamp (Unix)
    period_interval: int  # Required - 1 (1 min), 60 (1 hour), or 1440 (1 day)


class GetMarketCandlesticksResponse(BaseModel):
    """Response from the Get Market Candlesticks endpoint"""

    candlesticks: list[MarketCandlestick]
    ticker: str
