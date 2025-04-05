# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["QuerySearchResponse", "Document", "Error"]


class Document(BaseModel):
    resource_id: str

    source: Literal[
        "collections", "mcp", "slack", "s3", "gmail", "notion", "google_docs", "hubspot", "reddit", "google-calendar"
    ]

    extra: Optional[object] = None


class Error(BaseModel):
    error: str

    message: str


class QuerySearchResponse(BaseModel):
    documents: List[Document]

    errors: Optional[List[Error]] = None
    """Errors that occurred during the query.

    These are meant to help the developer debug the query, and are not meant to be
    shown to the user.
    """
