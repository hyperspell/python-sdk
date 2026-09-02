# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .memory_status import MemoryStatus

__all__ = ["MemoryAddBulkResponse", "Skipped"]


class Skipped(BaseModel):
    """A bulk item that was neither written nor indexed, with the reason.

    ``owned_by_another_user`` means the resource ID already belongs to another
    user in the app. The bulk endpoint skips that item without modifying the
    existing document. Single-item ``/memories/add`` returns 409 instead.
    """

    reason: str
    """Why the item was skipped (e.g. 'owned_by_another_user')"""

    resource_id: str
    """Resource ID of the skipped item"""


class MemoryAddBulkResponse(BaseModel):
    """Response schema for successful bulk ingestion."""

    count: int
    """Number of items successfully processed"""

    items: List[MemoryStatus]
    """Status of each ingested item"""

    skipped: Optional[List[Skipped]] = None
    """
    Items not ingested because their resource_id is already owned by another user on
    this app. Empty in the common case; a non-empty list is a partial success, not
    an error.
    """

    success: Optional[bool] = None
