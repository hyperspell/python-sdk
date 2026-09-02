# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List as TypingList, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .blob import Blob
from .code import Code
from .link import Link
from .text import Text
from .image import Image
from .trace import Trace
from .comment import Comment
from .divider import Divider
from ..._utils import PropertyInfo
from .metadata import Metadata
from ..._models import BaseModel
from .tool_call import ToolCall
from .line_break import LineBreak
from .tool_result import ToolResult
from .trace_message import TraceMessage

__all__ = ["ScoredDocumentResponse", "Document", "DocumentInvoice", "DocumentInvoiceChild", "Chunk"]

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
        "ListList",
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


class ScoredDocumentResponse(BaseModel):
    """
    A document response with its relevance score, matched highlights, and
    a summary of those highlights.
    """

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

    highlights: Optional[TypingList[object]] = None
    """The matched chunks that made this document a hit, with per-chunk scores."""

    ingested_at: Optional[datetime] = None
    """When Hyperspell first indexed the document."""

    last_modified_at: Optional[datetime] = None
    """When the source document was last modified, if supplied by the source."""

    metadata: Optional[Dict[str, object]] = None
    """Filterable custom metadata attached to the document."""

    score: Optional[float] = None
    """Relevance of the document to the query."""

    status: Optional[
        Literal["pending", "processing", "completed", "failed", "pending_review", "skipped", "filtered", "cancelled"]
    ] = None
    """Indexing status of the document."""

    summary: Optional[str] = None
    """Concatenated text of the matched highlights."""

    title: Optional[str] = None
    """Human-readable document title."""


from . import chunk, document
from .deal import Deal
from .file import File
from .list import List as ListList
from .page import Page
from .task import Task
from .event import Event
from .quote import Quote
from .table import Table
from .to_do import ToDo
from .person import Person
from .callout import Callout
from .company import Company
from .heading import Heading
from .message import Message
from .website import Website
from .equation import Equation
from .footnote import Footnote
from .list_item import ListItem
from .paragraph import Paragraph
from .table_row import TableRow
from .utterance import Utterance
from .table_cell import TableCell
from .transcript import Transcript
from .conversation import Conversation
