# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentListResponse", "Section", "SectionElement", "SectionElementMetadata", "SectionScores"]


class SectionElementMetadata(BaseModel):
    author: Optional[str] = None

    continued_from: Optional[str] = None
    """
    The id of the element that this element is continued from if it had to be split
    during chunking
    """

    filename: Optional[str] = None

    languages: Optional[List[str]] = None

    links: Optional[List[str]] = None

    page_number: Optional[int] = None

    title_level: Optional[int] = None


class SectionElement(BaseModel):
    text: str

    type: Literal["text", "markdown", "image", "table", "title", "query"]

    id: Optional[str] = None

    metadata: Optional[SectionElementMetadata] = None

    summary: Optional[str] = None


class SectionScores(BaseModel):
    full_text_search: Optional[float] = None
    """How relevant the section is based on full text search"""

    semantic_search: Optional[float] = None
    """How relevant the section is based on vector search"""

    weighted: Optional[float] = None
    """The final weighted score of the section"""


class Section(BaseModel):
    document_id: int

    id: Optional[int] = None

    elements: Optional[List[SectionElement]] = None

    embedding_e5_large: Optional[List[float]] = None

    embedding_ts: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    scores: Optional[SectionScores] = None

    text: Optional[str] = None


class DocumentListResponse(BaseModel):
    id: Optional[int] = None

    collection: Optional[str] = None

    created_at: Optional[datetime] = None

    ingested_at: Optional[datetime] = None

    metadata: Optional[Dict[str, object]] = None

    resource_id: Optional[str] = None
    """Along with service, uniquely identifies the source document"""

    sections: Optional[List[Section]] = None

    sections_count: Optional[int] = None

    source: Optional[
        Literal[
            "generic",
            "markdown",
            "chat",
            "email",
            "transcript",
            "legal",
            "website",
            "image",
            "pdf",
            "audio",
            "slack",
            "s3",
            "gmail",
            "notion",
            "google_docs",
        ]
    ] = None

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None

    title: Optional[str] = None
