# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["Table"]


class Table(BaseModel):
    id: Optional[str] = None

    children: Optional[List["TableRow"]] = None

    has_header: Optional[bool] = None
    """Whether the first row should be treated as a header"""

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    text: Optional[str] = None

    type: Optional[Literal["table"]] = None


from .table_row import TableRow
