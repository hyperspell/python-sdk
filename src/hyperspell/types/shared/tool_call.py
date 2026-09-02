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
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    type: Optional[Literal["tool_call"]] = None
