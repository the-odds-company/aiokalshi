from pydantic import BaseModel
import datetime
from typing import TypedDict, Literal

Status = Literal["unopened", "open", "closed", "settled"]


class OrderBook(BaseModel):
    no: list[tuple[int, int]]
    yes: list[tuple[int, int]]
    no_dollars: list[tuple[float, float]]
    yes_dollars: list[tuple[float, float]]


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
    limit: int
    cursor: str
    event_ticker: str
    series_ticker: str
    max_close_ts: int
    min_close_ts: int
    status: Status
    tickers: str


class GetMarketsResponse(BaseModel):
    cursor: str
    markets: list[Market]


class GetTradesRequest(TypedDict, total=False):
    limit: int
    cursor: str
    ticker: str
    min_ts: int
    max_ts: int


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
