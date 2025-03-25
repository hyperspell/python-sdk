# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .scores import Scores
from .._models import BaseModel

__all__ = ["DocumentListResponse", "Event", "Section"]


class Event(BaseModel):
    message: str

    type: Literal["error", "warning", "info"]

    time: Optional[datetime] = None


class Section(BaseModel):
    document_id: int

    text: str
    """Summary of the section"""

    id: Optional[int] = None

    content: Optional[str] = None

    elements: Optional[List[object]] = None

    embedding_e5_large: Optional[List[float]] = None

    embedding_ts: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    scores: Optional[Scores] = None


class DocumentListResponse(BaseModel):
    data: Union[List[object], object]
    """Structured representation of the document"""

    summary: str
    """Summary of the document"""

    id: Optional[int] = None

    collection: Optional[str] = None

    created_at: Optional[datetime] = None

    events: Optional[List[Event]] = None

    ingested_at: Optional[datetime] = None

    metadata: Optional[Dict[str, object]] = None

    resource_id: Optional[str] = None
    """Along with service, uniquely identifies the source document"""

    sections: Optional[List[Section]] = None

    sections_count: Optional[int] = None

    source: Optional[Literal["generic", "slack", "s3", "gmail", "notion", "google_docs", "hubspot"]] = None

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None

    title: Optional[str] = None

    type: Optional[
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
            "spreadsheet",
            "archive",
            "book",
            "video",
            "code",
            "calendar",
            "json",
            "presentation",
            "unsupported",
            "person",
            "company",
            "crm_contact",
        ]
    ] = None
