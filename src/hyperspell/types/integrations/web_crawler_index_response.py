# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebCrawlerIndexResponse"]


class WebCrawlerIndexResponse(BaseModel):
    resource_id: str

    source: Literal["collections", "notion", "slack", "hubspot", "google_calendar", "reddit", "web_crawler", "box"]

    status: Literal["pending", "processing", "completed", "failed"]
