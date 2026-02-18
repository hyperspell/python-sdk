# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .memory_status import MemoryStatus

__all__ = ["MemoryAddBulkResponse"]


class MemoryAddBulkResponse(BaseModel):
    """Response schema for successful bulk ingestion."""

    count: int
    """Number of items successfully processed"""

    items: List[MemoryStatus]
    """Status of each ingested item"""

    success: Optional[bool] = None
