# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["QuerySearchResponse", "Document"]


class Document(BaseModel):
    resource_id: str

    source: Literal[
        "generic", "mcp", "slack", "s3", "gmail", "notion", "google_docs", "hubspot", "reddit", "google-calendar"
    ]

    extra: Optional[object] = None


class QuerySearchResponse(BaseModel):
    documents: List[Document]
