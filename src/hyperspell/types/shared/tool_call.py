# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["ToolCall"]


class ToolCall(BaseModel):
    """A tool/function call made by the assistant."""

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    args: Optional[Dict[str, object]] = None

    metadata: Optional[Metadata] = None
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    type: Optional[Literal["tool_call"]] = None
