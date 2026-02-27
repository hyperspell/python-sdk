# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["QueryResult", "Document"]


class Document(BaseModel):
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
        "github",
        "vault",
        "web_crawler",
        "trace",
    ]

    metadata: Optional[Metadata] = None

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
