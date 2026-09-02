# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ContextDocumentListResponse"]


class ContextDocumentListResponse(BaseModel):
    completed_at: Optional[datetime] = None

    created_at: datetime

    document_id: str

    model: str

    sources: List[str]

    status: str

    token_count: Optional[int] = None

    error: Optional[str] = None
