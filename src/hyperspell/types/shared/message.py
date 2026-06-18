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

__all__ = ["Message", "Child"]

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


class Message(BaseModel):
    date: datetime

    sender: "Person"

    id: Optional[str] = None

    channel: Optional[str] = None
    """
    The channel or platform where the message was posted, if this Message is not
    explicitly part of a conversation
    """

    children: Optional[TypingList[Child]] = None

    external_id: Optional[str] = None
    """Provider message id (e.g. Slack ts, Gmail message id) — merge-dedup key"""

    is_self: Optional[bool] = None

    mentioned_users: Optional[TypingList["Person"]] = None

    metadata: Optional[Metadata] = None
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    num_replies: Optional[int] = None

    replies: Optional[TypingList["Message"]] = None
    """The replies or comments to the message"""

    text: Optional[str] = None

    thread_id: Optional[str] = None

    title: Optional[str] = None
    """The subject or title of the message"""

    type: Optional[Literal["message"]] = None

    updated_at: Optional[datetime] = None

    upvotes: Optional[int] = None
    """The number of upvotes, likes, or reactions on the message"""


from .list import List as ListList
from .chunk import Chunk
from .quote import Quote
from .table import Table
from .to_do import ToDo
from .person import Person
from .callout import Callout
from .heading import Heading
from .equation import Equation
from .footnote import Footnote
from .list_item import ListItem
from .paragraph import Paragraph
from .table_row import TableRow
from .utterance import Utterance
from .table_cell import TableCell
