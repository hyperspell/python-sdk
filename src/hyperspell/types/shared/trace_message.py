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
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    role: Optional[Literal["user", "assistant"]] = None

    timestamp: Optional[datetime] = None

    type: Optional[Literal["trace_message"]] = None
