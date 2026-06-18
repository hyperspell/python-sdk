# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .trace import Trace
from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["ScoredDocumentResponse", "Document"]

Document: TypeAlias = Annotated[
    Union[
        "document.Document",
        "Website",
        "Task",
        "Person",
        "Message",
        "Event",
        "File",
        "Conversation",
        Trace,
        "Transcript",
        "Company",
        "Deal",
    ],
    PropertyInfo(discriminator="type"),
]


class ScoredDocumentResponse(BaseModel):
    """
    A `DocumentResponse` plus the query-path fields a `ScoredDocument` carries
    (ENG-2479): relevance score, matched highlights, and the concatenated
    summary of those highlights.
    """

    document: Document
    """The full hyperdoc tree.

    Switch on `type` for the document frame and recurse `children` for the body —
    see the `<Hyperdoc />` renderer.
    """

    resource_id: str

    source: Literal[
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "box",
        "dropbox",
        "github",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
        "microsoft_teams",
        "gmail_actions",
        "granola",
        "fathom",
        "fireflies",
        "linear",
        "hubspot",
        "salesforce",
        "coda",
        "lightfield",
        "gong",
    ]

    type: str
    """Hyperdoc document type discriminator (document, message, file, event, ...)."""

    collection: Optional[str] = None
    """The document's collection, if any."""

    document_date: Optional[datetime] = None
    """The document's own date (e.g. email sent date, event date)."""

    highlights: Optional[List[object]] = None
    """The matched chunks that made this document a hit, with per-chunk scores."""

    ingested_at: Optional[datetime] = None
    """When Hyperspell first indexed the document."""

    last_modified_at: Optional[datetime] = None
    """When the source document was last modified."""

    metadata: Optional[Dict[str, object]] = None
    """Filterable custom metadata attached to the document."""

    score: Optional[float] = None
    """Relevance of the document to the query."""

    status: Optional[Literal["pending", "processing", "completed", "failed", "pending_review", "skipped"]] = None
    """Indexing status of the document."""

    summary: Optional[str] = None
    """Concatenated text of the matched highlights."""

    title: Optional[str] = None
    """Human-readable document title."""


from . import document
from .deal import Deal
from .file import File
from .task import Task
from .event import Event
from .person import Person
from .company import Company
from .message import Message
from .website import Website
from .transcript import Transcript
from .conversation import Conversation
