# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["TableRow"]


class TableRow(BaseModel):
    id: Optional[str] = None

    children: Optional[List["TableCell"]] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    text: Optional[str] = None

    type: Optional[Literal["table_row"]] = None


from .table_cell import TableCell
