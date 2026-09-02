# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ContextDocumentGetResponse"]


class ContextDocumentGetResponse(BaseModel):
    completed_at: Optional[datetime] = None

    content: Optional[str] = None

    created_at: datetime

    document_id: str

    error: Optional[str] = None

    metadata: Dict[str, object]

    model: str

    prompt: Optional[str] = None

    sources: List[str]

    status: str

    token_usage: Optional[Dict[str, object]] = None

    user_id: Optional[str] = None
