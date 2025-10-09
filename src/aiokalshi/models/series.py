from pydantic import BaseModel
from typing import TypedDict, Literal, Optional


FeeType = Literal["quadratic", "quadratic_with_maker_fees", "flat"]


class ProductMetadata(BaseModel):
    """Product metadata for a series"""

    pass  # The exact fields weren't fully detailed in the OpenAPI spec


class Series(BaseModel):
    """Series used in the Kalshi API. A series represents a template for recurring events."""

    additional_prohibitions: list[str] | None = None
    category: str | None = None
    contract_terms_url: str | None = None
    contract_url: str | None = None
    fee_multiplier: float | None = None
    fee_type: FeeType | None = None
    frequency: str
    product_metadata: ProductMetadata | None = None
    ticker: str  # API returns 'ticker', not 'series_ticker'
    tags: list[str] | None = None
    title: str


class GetSeriesListRequest(TypedDict, total=False):
    """The query params to the Get Series List endpoint"""

    category: str  # Required
    include_product_metadata: bool | None
    tags: str | None  # Comma separated list


class GetSeriesListResponse(BaseModel):
    """The response of the Get Series List endpoint"""

    series: list[Series] | None = None


class GetSeriesRequest(TypedDict, total=False):
    """The query params of the Get Series endpoint (none)"""

    ...


class GetSeriesResponse(BaseModel):
    """The response of the Get Series endpoint"""

    series: Series
