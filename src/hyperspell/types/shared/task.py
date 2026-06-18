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

__all__ = ["Task", "Child"]

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


class Task(BaseModel):
    id: Optional[str] = None

    children: Optional[TypingList[Child]] = None

    comments: Optional[TypingList["Message"]] = None

    due_at: Optional[datetime] = None

    metadata: Optional[Metadata] = None
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    priority: Optional[Literal["urgent", "high", "medium", "low"]] = None

    status: Optional[Literal["completed", "not_started", "in_progress", "cancelled"]] = None

    text: Optional[str] = None

    type: Optional[Literal["task"]] = None


from .list import List as ListList
from .chunk import Chunk
from .quote import Quote
from .table import Table
from .to_do import ToDo
from .callout import Callout
from .heading import Heading
from .message import Message
from .equation import Equation
from .footnote import Footnote
from .list_item import ListItem
from .paragraph import Paragraph
from .table_row import TableRow
from .utterance import Utterance
from .table_cell import TableCell
