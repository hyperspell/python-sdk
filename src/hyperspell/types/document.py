# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document", "Section"]


class Section(BaseModel):
    content: str

    type: Literal["text", "markdown", "table", "image", "messages", "message"]

    children_ids: Optional[List[int]] = None

    document_id: Optional[int] = None

    metadata: Optional[object] = None

    parent_id: Optional[int] = None


class Document(BaseModel):
    collection_id: int

    resource_id: int
    """Along with service, uniquely identifies the source document"""

    id: Optional[int] = None

    created_at: Optional[datetime] = None

    ingested_at: Optional[datetime] = None

    metadata: Optional[object] = None

    sections: Optional[List[Section]] = None

    service: Optional[Literal["slack", "s3", "gmail", "notion", "google_docs", "api"]] = None

    title: Optional[str] = None

    type: Optional[Literal["chat", "email", "generic", "transcript", "legal"]] = None
