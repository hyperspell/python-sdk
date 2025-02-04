# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CollectionListResponse"]


class CollectionListResponse(BaseModel):
    name: str

    id: Optional[int] = None

    created_at: Optional[datetime] = None

    documents_count: Optional[int] = None

    owner: Optional[str] = None
