# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CollectionListResponse"]


class CollectionListResponse(BaseModel):
    created_at: datetime

    documents_count: Optional[int] = None

    name: str

    owner: Optional[str] = None
