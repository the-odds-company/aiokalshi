from pydantic import BaseModel
import datetime
from .markets import Market
from typing import Literal, TypedDict, Optional


# Main models
class Event(BaseModel):
    """Event used in the Kalshi API. Can be thought of as a question. For instance: "What will be Taylor Swift's First Week Album Sales?" """

    available_on_brokers: bool
    category: str
    collateral_return_type: str
    event_ticker: str
    markets: list[Market] | None = None
    mutually_exclusive: bool
    price_level_structure: str
    series_ticker: str
    strike_date: datetime.datetime | None = None
    strike_period: str | None = None
    sub_title: str
    title: str


Status = Literal["open", "closed", "settled"]


class GetEventsRequest(TypedDict, total=False):
    """The query params to the `Get Events` endpoint"""

    limit: int | None
    cursor: str | None
    with_nested_markets: bool | None
    status: Status | None
    series_ticker: str | None
    min_close_ts: int | None


class GetEventsResponse(BaseModel):
    """The response of the `Get Events` endpoint"""

    cursor: str | None = None
    events: list[Event]


class GetEventRequest(TypedDict, total=False):
    """The query params of the `Get Event` endpoint"""

    with_nested_markets: bool | None


class GetEventResponse(BaseModel):
    """The response of the `Get Event` endpoint"""

    event: Event
    markets: list[Market] | None = None


class GetEventMetadataRequest(TypedDict, total=False):
    """The query params (empty!) for the get metadata requeest gbro im getting so tired of writing these"""

    ...


class GetEventMetadataResponse(BaseModel):
    """The response format of get metadata request"""

    competition: str
    competition_scope: str
    image_url: str

    class SettlementSource(BaseModel):
        name: str
        url: str

    settlement_sources: list[SettlementSource]
