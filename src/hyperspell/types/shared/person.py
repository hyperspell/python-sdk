# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List as TypingList, Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypeAlias, TypeAliasType

from .blob import Blob
from .code import Code
from .link import Link
from .text import Text
from .image import Image
from .comment import Comment
from .divider import Divider
from ..._utils import PropertyInfo
from .metadata import Metadata
from ..._compat import PYDANTIC_V1
from ..._models import BaseModel
from .tool_call import ToolCall
from .line_break import LineBreak
from .tool_result import ToolResult
from .trace_message import TraceMessage

__all__ = ["Person", "Child"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Child = TypeAliasType(
        "Child",
        Annotated[
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
        ],
    )
else:
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


class Person(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    alt_names: Optional[TypingList[str]] = None

    children: Optional[TypingList[Child]] = None

    company: Optional[str] = None

    company_ids: Optional[TypingList[str]] = None

    date_of_birth: Optional[date] = None

    deal_ids: Optional[TypingList[str]] = None

    email: Optional[str] = None

    emails: Optional[TypingList[str]] = None
    """All known email addresses; `email` holds the primary one"""

    image_url: Optional[str] = None

    job_title: Optional[str] = None

    link_urls: Optional[TypingList[str]] = None

    metadata: Optional[Metadata] = None
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    name: Optional[str] = None

    phone_numbers: Optional[TypingList[str]] = None

    tags: Optional[TypingList[str]] = None

    text: Optional[str] = None

    type: Optional[Literal["person"]] = None

    username: Optional[str] = None


from .list import List as ListList
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
