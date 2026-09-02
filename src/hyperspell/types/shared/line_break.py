# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["LineBreak"]


class LineBreak(BaseModel):
    id: Optional[str] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    type: Optional[Literal["line_break"]] = None
