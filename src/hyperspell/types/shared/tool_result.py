# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["ToolResult"]


class ToolResult(BaseModel):
    """The result of a tool call."""

    output: Union[str, Dict[str, object], List[object]]

    tool_call_id: str

    tool_name: str

    id: Optional[str] = None

    is_error: Optional[bool] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    type: Optional[Literal["tool_result"]] = None
