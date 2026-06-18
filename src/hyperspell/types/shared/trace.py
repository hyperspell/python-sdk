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

    type: Optional[Literal["trace"]] = None
