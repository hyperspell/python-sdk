# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from .metadata import Metadata
from ..._models import BaseModel
from .tool_call import ToolCall
from .tool_result import ToolResult
from .trace_message import TraceMessage

__all__ = ["Trace", "Child"]

Child: TypeAlias = Annotated[Union[TraceMessage, ToolCall, ToolResult], PropertyInfo(discriminator="type")]


class Trace(BaseModel):
    """An agent trace/transcript containing a sequence of steps.

    Steps can be TraceMessage (user/assistant messages or thinking),
    ToolCall (function calls), or ToolResult (tool responses).
    """

    id: Optional[str] = None

    children: Optional[List[Child]] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["trace"]] = None
