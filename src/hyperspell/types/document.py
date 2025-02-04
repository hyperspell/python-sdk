# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "Document",
    "Section",
    "SectionSectionResult",
    "SectionSectionResultScores",
    "SectionSectionResultWithElements",
    "SectionSectionResultWithElementsElement",
    "SectionSectionResultWithElementsElementMetadata",
    "SectionSectionResultWithElementsScores",
]


class SectionSectionResultScores(BaseModel):
    full_text_search: Optional[float] = None
    """How relevant the section is based on full text search"""

    semantic_search: Optional[float] = None
    """How relevant the section is based on vector search"""

    weighted: Optional[float] = None
    """The final weighted score of the section"""


class SectionSectionResult(BaseModel):
    id: Optional[int] = None

    scores: Optional[SectionSectionResultScores] = None

    text: Optional[str] = None


class SectionSectionResultWithElementsElementMetadata(BaseModel):
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


class SectionSectionResultWithElementsElement(BaseModel):
    text: str

    type: Literal["text", "markdown", "image", "table", "title", "query"]

    id: Optional[str] = None

    metadata: Optional[SectionSectionResultWithElementsElementMetadata] = None

    summary: Optional[str] = None


class SectionSectionResultWithElementsScores(BaseModel):
    full_text_search: Optional[float] = None
    """How relevant the section is based on full text search"""

    semantic_search: Optional[float] = None
    """How relevant the section is based on vector search"""

    weighted: Optional[float] = None
    """The final weighted score of the section"""


class SectionSectionResultWithElements(BaseModel):
    id: Optional[int] = None

    elements: Optional[List[SectionSectionResultWithElementsElement]] = None

    scores: Optional[SectionSectionResultWithElementsScores] = None

    text: Optional[str] = None


Section: TypeAlias = Union[SectionSectionResult, SectionSectionResultWithElements]


class Document(BaseModel):
    id: Optional[int] = None

    collection: str

    created_at: Optional[datetime] = None

    ingested_at: Optional[datetime] = None

    metadata: object

    resource_id: str

    title: Optional[str] = None

    sections: Optional[List[Section]] = None

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
