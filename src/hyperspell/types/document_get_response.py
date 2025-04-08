# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentGetResponse", "Event", "Metadata"]


class Event(BaseModel):
    message: str

    type: Literal["error", "warning", "info"]

    time: Optional[datetime] = None


class Metadata(BaseModel):
    created_at: Optional[datetime] = None

    last_modified: Optional[datetime] = None

    url: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class DocumentGetResponse(BaseModel):
    resource_id: str

    source: Literal[
        "collections", "mcp", "slack", "s3", "gmail", "notion", "google_docs", "hubspot", "reddit", "google-calendar"
    ]

    id: Optional[int] = None

    collection: Optional[str] = None

    data: Optional[List[object]] = None

    events: Optional[List[Event]] = None

    highlights: Optional[List[object]] = None

    metadata: Optional[Metadata] = None

    summary: Optional[str] = None

    title: Optional[str] = None
