# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["Conversation"]


class Conversation(BaseModel):
    id: Optional[str] = None

    channel: Optional[str] = None

    children: Optional[List["Message"]] = None

    metadata: Optional[Metadata] = None
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["conversation"]] = None


from .message import Message
