# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["QuerySearchResponse", "Document", "DocumentMetadata"]


class DocumentMetadata(BaseModel):
    created_at: Optional[datetime] = None

    last_modified: Optional[datetime] = None

    url: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Document(BaseModel):
    resource_id: str

    source: Literal["collections", "notion", "slack", "hubspot", "google_calendar", "reddit", "web_crawler", "box"]

    metadata: Optional[DocumentMetadata] = None

    score: Optional[float] = None
    """The relevance of the resource to the query"""


class QuerySearchResponse(BaseModel):
    documents: List[Document]

    answer: Optional[str] = None
    """The answer to the query, if the request was set to answer."""

    errors: Optional[List[Dict[str, str]]] = None
    """Errors that occurred during the query.

    These are meant to help the developer debug the query, and are not meant to be
    shown to the user.
    """
