# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DigestListResponse", "Digest"]


class Digest(BaseModel):
    """A digest summary. Fetch the full content through the tree-by-ID endpoint."""

    completed_at: Optional[datetime] = None

    created_at: datetime

    period: Optional[str] = None

    status: str

    tree_id: str

    window_end: Optional[datetime] = None

    window_start: Optional[datetime] = None


class DigestListResponse(BaseModel):
    digests: List[Digest]
