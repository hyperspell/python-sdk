# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebCrawlerIndexResponse"]


class WebCrawlerIndexResponse(BaseModel):
    resource_id: str

    source: Literal[
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "box",
        "dropbox",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
    ]

    status: Literal["pending", "processing", "completed", "failed"]
