# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List as TypingList, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .blob import Blob
from .code import Code
from .link import Link
from .text import Text
from .image import Image
from .comment import Comment
from .divider import Divider
from ..._utils import PropertyInfo
from .metadata import Metadata
from ..._models import BaseModel
from .tool_call import ToolCall
from .line_break import LineBreak
from .tool_result import ToolResult
from .trace_message import TraceMessage

__all__ = ["Deal", "Child"]

Child: TypeAlias = Annotated[
    Union[
        Blob,
        "Callout",
        "Chunk",
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


class Deal(BaseModel):
    """A CRM deal or opportunity record."""

    id: Optional[str] = None

    amount: Optional[float] = None

    children: Optional[TypingList[Child]] = None

    closed_at: Optional[datetime] = None

    company_ids: Optional[TypingList[str]] = None

    contact_ids: Optional[TypingList[str]] = None

    currency: Optional[str] = None

    deal_source: Optional[str] = None

    lost_reason: Optional[str] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    name: Optional[str] = None

    pipeline: Optional[str] = None

    probability: Optional[float] = None

    stage: Optional[str] = None

    tags: Optional[TypingList[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["deal"]] = None

    won_reason: Optional[str] = None


from .list import List as ListList
from .page import Page
from .chunk import Chunk
from .quote import Quote
from .table import Table
from .to_do import ToDo
from .callout import Callout
from .heading import Heading
from .equation import Equation
from .footnote import Footnote
from .list_item import ListItem
from .paragraph import Paragraph
from .table_row import TableRow
from .utterance import Utterance
from .table_cell import TableCell
