# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentListResponse", "Metadata"]


class Metadata(BaseModel):
    created_at: Optional[datetime] = None

    last_modified: Optional[datetime] = None

    url: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class DocumentListResponse(BaseModel):
    resource_id: str

    source: Literal[
        "collections", "notion", "slack", "hubspot", "google_calendar", "reddit", "web_crawler", "box", "google_drive"
    ]

    metadata: Optional[Metadata] = None

    score: Optional[float] = None
    """The relevance of the resource to the query"""
