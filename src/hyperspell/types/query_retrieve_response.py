# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "QueryRetrieveResponse",
    "Document",
    "DocumentSection",
    "DocumentSectionElement",
    "DocumentSectionElementMetadata",
    "DocumentSectionScores",
]


class DocumentSectionElementMetadata(BaseModel):
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


class DocumentSectionElement(BaseModel):
    text: str

    type: Literal["text", "markdown", "image", "table", "title", "query"]

    id: Optional[str] = None

    metadata: Optional[DocumentSectionElementMetadata] = None

    summary: Optional[str] = None


class DocumentSectionScores(BaseModel):
    full_text_search: Optional[float] = None
    """How relevant the section is based on full text search"""

    semantic_search: Optional[float] = None
    """How relevant the section is based on vector search"""

    weighted: Optional[float] = None
    """The final weighted score of the section"""


class DocumentSection(BaseModel):
    document_id: int

    id: Optional[int] = None

    elements: Optional[List[DocumentSectionElement]] = None

    embedding_e5_large: Optional[List[float]] = None

    embedding_ts: Optional[str] = None

    metadata: Optional[object] = None

    scores: Optional[DocumentSectionScores] = None

    text: Optional[str] = None


class Document(BaseModel):
    id: Optional[int] = None

    collection: str

    created_at: Optional[datetime] = None

    ingested_at: Optional[datetime] = None

    metadata: object

    resource_id: str

    title: Optional[str] = None

    sections: Optional[List[DocumentSection]] = None

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


class QueryRetrieveResponse(BaseModel):
    documents: List[Document]

    total_sections: int
