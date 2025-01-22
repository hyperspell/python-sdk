# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document", "Section"]


class Section(BaseModel):
    content: str

    document_id: int

    id: Optional[int] = None

    embedding_e5_large: Optional[List[float]] = None

    fts: Optional[List[float]] = None

    metadata: Optional[object] = None

    type: Optional[Literal["text", "markdown", "table", "image", "messages", "message"]] = None
    """Type of the section"""


class Document(BaseModel):
    collection_id: int

    resource_id: str
    """Along with service, uniquely identifies the source document"""

    id: Optional[int] = None

    created_at: Optional[datetime] = None

    ingested_at: Optional[datetime] = None

    metadata: Optional[object] = None

    sections: Optional[List[Section]] = None

    source: Optional[
        Literal[
            "generic",
            "generic_chat",
            "generic_email",
            "generic_transcript",
            "generic_legal",
            "website",
            "slack",
            "s3",
            "gmail",
            "notion",
            "google_docs",
        ]
    ] = None

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None

    title: Optional[str] = None
