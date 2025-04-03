# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentGetResponse", "Event"]


class Event(BaseModel):
    message: str

    type: Literal["error", "warning", "info"]

    time: Optional[datetime] = None


class DocumentGetResponse(BaseModel):
    collection: str

    resource_id: str

    source: Literal[
        "generic", "mcp", "slack", "s3", "gmail", "notion", "google_docs", "hubspot", "reddit", "google-calendar"
    ]

    id: Optional[int] = None

    data: Optional[List[object]] = None

    events: Optional[List[Event]] = None

    extra: Optional[object] = None

    highlights: Optional[List[object]] = None

    summary: Optional[str] = None

    title: Optional[str] = None
