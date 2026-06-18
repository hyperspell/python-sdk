# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.trace import Trace

__all__ = ["MemoryListResponse", "Document"]

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


class MemoryListResponse(BaseModel):
    """A document-shaped API response carrying the hyperdoc tree (ENG-2479/D12)."""

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

    ingested_at: Optional[datetime] = None
    """When Hyperspell first indexed the document."""

    last_modified_at: Optional[datetime] = None
    """When the source document was last modified."""

    metadata: Optional[Dict[str, object]] = None
    """Filterable custom metadata attached to the document."""

    status: Optional[Literal["pending", "processing", "completed", "failed", "pending_review", "skipped"]] = None
    """Indexing status of the document."""

    title: Optional[str] = None
    """Human-readable document title."""


from .shared import document
from .shared.deal import Deal
from .shared.file import File
from .shared.task import Task
from .shared.event import Event
from .shared.person import Person
from .shared.company import Company
from .shared.message import Message
from .shared.website import Website
from .shared.transcript import Transcript
from .shared.conversation import Conversation
