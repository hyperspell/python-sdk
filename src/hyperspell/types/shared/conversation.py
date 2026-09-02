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
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    participants: Optional[List["Person"]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["conversation"]] = None


from .person import Person
from .message import Message
