# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QueryResult", "Document", "DocumentMetadata", "DocumentMetadataEvent"]


class DocumentMetadataEvent(BaseModel):
    message: str

    type: Literal["error", "warning", "info", "success"]

    time: Optional[datetime] = None


class DocumentMetadata(BaseModel):
    created_at: Optional[datetime] = None

    events: Optional[List[DocumentMetadataEvent]] = None

    indexed_at: Optional[datetime] = None

    last_modified: Optional[datetime] = None

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None

    url: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Document(BaseModel):
    resource_id: str

    source: Literal[
        "collections",
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
    ]

    metadata: Optional[DocumentMetadata] = None

    score: Optional[float] = None
    """The relevance of the resource to the query"""

    title: Optional[str] = None


class QueryResult(BaseModel):
    documents: List[Document]

    answer: Optional[str] = None
    """The answer to the query, if the request was set to answer."""

    errors: Optional[List[Dict[str, str]]] = None
    """Errors that occurred during the query.

    These are meant to help the developer debug the query, and are not meant to be
    shown to the user.
    """

    query_id: Optional[str] = None
    """The ID of the query.

    This can be used to retrieve the query later, or add feedback to it. If the
    query failed, this will be None.
    """

    score: Optional[float] = None
    """The average score of the query feedback, if any."""
