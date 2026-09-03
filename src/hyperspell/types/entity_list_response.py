# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EntityListResponse"]


class EntityListResponse(BaseModel):
    id: str

    created_at: datetime

    name: str

    status: Literal["provisional", "confirmed"]
    """How strongly the entity's current identity has been established."""

    type: str

    updated_at: datetime

    attributes: Optional[Dict[str, object]] = None

    description: Optional[str] = None

    hard_linked_mention_count: Optional[int] = None

    prominence_calculated_at: Optional[datetime] = None

    prominence_version: Optional[str] = None

    record_count: Optional[int] = None

    supporting_document_count: Optional[int] = None

    supporting_scope_count: Optional[int] = None
