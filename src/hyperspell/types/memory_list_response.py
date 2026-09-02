# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List as TypingList, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.blob import Blob
from .shared.code import Code
from .shared.link import Link
from .shared.text import Text
from .shared.image import Image
from .shared.trace import Trace
from .shared.comment import Comment
from .shared.divider import Divider
from .shared.metadata import Metadata
from .shared.tool_call import ToolCall
from .shared.line_break import LineBreak
from .shared.tool_result import ToolResult
from .shared.trace_message import TraceMessage

__all__ = ["MemoryListResponse", "Document", "DocumentInvoice", "DocumentInvoiceChild", "Chunk"]

DocumentInvoiceChild: TypeAlias = Annotated[
    Union[
        Blob,
        "Callout",
        "chunk.Chunk",
        Code,
        Comment,
        Divider,
        "Equation",
        "Footnote",
        "Heading",
        Image,
        Link,
        LineBreak,
        "SharedList",
        "ListItem",
        "Page",
        "Paragraph",
        "Quote",
        "Table",
        "TableCell",
        "TableRow",
        Text,
        "ToDo",
        ToolCall,
        ToolResult,
        TraceMessage,
        "Utterance",
    ],
    PropertyInfo(discriminator="type"),
]


class DocumentInvoice(BaseModel):
    """A customer invoice, vendor bill, or credit memo.

    Line items are included in ``children``.
    """

    id: Optional[str] = None

    attachment_names: Optional[TypingList[str]] = None

    balance_amount: Optional[float] = None

    cancelled_at: Optional[datetime] = None

    children: Optional[TypingList[DocumentInvoiceChild]] = None

    contact_id: Optional[str] = None

    contact_name: Optional[str] = None

    currency: Optional[str] = None

    due_at: Optional[datetime] = None

    invoice_type: Optional[str] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    notes: Optional[str] = None

    number: Optional[str] = None

    organization_id: Optional[str] = None

    paid_amount: Optional[float] = None

    paid_at: Optional[datetime] = None

    posted_at: Optional[datetime] = None

    reference: Optional[str] = None

    refund_amount: Optional[float] = None

    refund_reason: Optional[str] = None

    refunded_at: Optional[datetime] = None

    status: Optional[str] = None

    tax_amount: Optional[float] = None

    text: Optional[str] = None

    total_amount: Optional[float] = None

    type: Optional[Literal["invoice"]] = None


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
        DocumentInvoice,
    ],
    PropertyInfo(discriminator="type"),
]


class Chunk(BaseModel):
    """A searchable chunk extracted from a document during ingestion.

    `summary` is null when no summary was generated for the chunk.
    """

    chunk_id: str
    """Stable identifier of the chunk."""

    summary: Optional[str] = None
    """LLM-generated summary of the chunk, if one was produced."""


class MemoryListResponse(BaseModel):
    """A document-shaped API response containing the hyperdoc tree."""

    document: Document
    """The full hyperdoc tree.

    Switch on `type` for the document frame and recurse through `children` for the
    body.
    """

    resource_id: str

    source: Literal[
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "imap",
        "google_meet",
        "box",
        "dropbox",
        "github",
        "gitlab",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
        "microsoft_outlook",
        "microsoft_teams",
        "granola",
        "fathom",
        "fireflies",
        "figma",
        "linear",
        "hubspot",
        "salesforce",
        "coda",
        "confluence",
        "jira",
        "metabase",
        "gong",
        "clickup",
        "lightfield",
        "pylon",
        "fellow",
        "odoo",
        "external_mcp",
    ]

    type: str
    """Hyperdoc document type discriminator (document, message, file, event, ...)."""

    chunks: Optional[TypingList[Chunk]] = None
    """Extracted memories (chunks with summaries) for this document, in document order.

    Present only when explicitly requested via `include_chunks`; omitted otherwise.
    """

    collection: Optional[str] = None
    """The document's collection, if any."""

    document_date: Optional[datetime] = None
    """The document's own date (e.g. email sent date, event date)."""

    ingested_at: Optional[datetime] = None
    """When Hyperspell first indexed the document."""

    last_modified_at: Optional[datetime] = None
    """When the source document was last modified, if supplied by the source."""

    metadata: Optional[Dict[str, object]] = None
    """Filterable custom metadata attached to the document."""

    status: Optional[
        Literal["pending", "processing", "completed", "failed", "pending_review", "skipped", "filtered", "cancelled"]
    ] = None
    """Indexing status of the document."""

    title: Optional[str] = None
    """Human-readable document title."""


from .shared import chunk, document
from .shared.deal import Deal
from .shared.file import File
from .shared.list import List as SharedList
from .shared.page import Page
from .shared.task import Task
from .shared.event import Event
from .shared.quote import Quote
from .shared.table import Table
from .shared.to_do import ToDo
from .shared.person import Person
from .shared.callout import Callout
from .shared.company import Company
from .shared.heading import Heading
from .shared.message import Message
from .shared.website import Website
from .shared.equation import Equation
from .shared.footnote import Footnote
from .shared.list_item import ListItem
from .shared.paragraph import Paragraph
from .shared.table_row import TableRow
from .shared.utterance import Utterance
from .shared.table_cell import TableCell
from .shared.transcript import Transcript
from .shared.conversation import Conversation
