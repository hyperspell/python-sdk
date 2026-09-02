# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List as TypingList, Union, Optional
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

__all__ = ["Company", "Child"]

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


class Company(BaseModel):
    """A CRM company or account record."""

    id: Optional[str] = None

    address: Optional[str] = None

    children: Optional[TypingList[Child]] = None

    contact_ids: Optional[TypingList[str]] = None

    deal_ids: Optional[TypingList[str]] = None

    description: Optional[str] = None

    emails: Optional[TypingList[str]] = None

    employees: Optional[int] = None

    image_url: Optional[str] = None

    industry: Optional[str] = None

    is_active: Optional[bool] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    name: Optional[str] = None

    phone_numbers: Optional[TypingList[str]] = None

    tags: Optional[TypingList[str]] = None

    text: Optional[str] = None

    timezone: Optional[str] = None

    type: Optional[Literal["company"]] = None

    websites: Optional[TypingList[str]] = None


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
