# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..scores import Scores
from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["Collection", "Document", "DocumentEvent", "DocumentSection"]


class DocumentEvent(BaseModel):
    message: str

    type: Literal["error", "warning", "info"]

    time: Optional[datetime] = None


class DocumentSection(BaseModel):
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


class Document(BaseModel):
    collection_id: int

    data: Union[List[object], object]
    """Structured representation of the document"""

    summary: str
    """Summary of the document"""

    id: Optional[int] = None

    collection: Optional[str] = None

    created_at: Optional[datetime] = None

    events: Optional[List[DocumentEvent]] = None

    ingested_at: Optional[datetime] = None

    metadata: Optional[Dict[str, object]] = None

    resource_id: Optional[str] = None
    """Along with service, uniquely identifies the source document"""

    sections: Optional[List[DocumentSection]] = None

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


class Collection(BaseModel):
    app_id: int

    name: str

    id: Optional[int] = None

    app: Optional["App"] = None
    """Apps Base Schema."""

    created_at: Optional[datetime] = None

    documents: Optional[List[Document]] = None

    documents_count: Optional[int] = None

    owner: Optional[str] = None


from .app import App

if PYDANTIC_V2:
    Collection.model_rebuild()
    Document.model_rebuild()
    DocumentEvent.model_rebuild()
    DocumentSection.model_rebuild()
else:
    Collection.update_forward_refs()  # type: ignore
    Document.update_forward_refs()  # type: ignore
    DocumentEvent.update_forward_refs()  # type: ignore
    DocumentSection.update_forward_refs()  # type: ignore
