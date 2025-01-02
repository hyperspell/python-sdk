# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document", "Section"]


class Section(BaseModel):
    content: str

    type: Literal["text", "markdown", "table", "image", "messages", "message"]

    children_ids: Optional[List[str]] = None

    document_id: Optional[str] = None

    metadata: Optional[object] = None

    parent_id: Optional[str] = None


class Document(BaseModel):
    collection: str

    resource_id: str
    """Along with service, uniquely identifies the source document"""

    created_at: Optional[datetime] = None

    ingested_at: Optional[datetime] = None

    metadata: Optional[object] = None

    sections: Optional[List[Section]] = None

    service: Optional[Literal["slack", "s3", "gmail", "notion", "google_docs", "api"]] = None

    title: Optional[str] = None

    type: Optional[Literal["chat", "email", "generic", "transcript", "legal"]] = None
