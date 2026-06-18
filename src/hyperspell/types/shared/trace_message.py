# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["TraceMessage"]


class TraceMessage(BaseModel):
    """A message in an agent trace (user message, assistant message, or thinking)."""

    text: str

    id: Optional[str] = None

    message_type: Optional[Literal["message", "thinking"]] = None

    metadata: Optional[Metadata] = None
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None
