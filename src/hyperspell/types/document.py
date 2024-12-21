# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document", "Chunk"]


class Chunk(BaseModel):
    score: float

    text: str

    type: Literal["text", "markdown", "table", "image", "messages", "message"]

    metadata: Optional[Dict[str, str]] = None


class Document(BaseModel):
    id: str

    chunk_count: int

    ingested_at: datetime

    chunk_ids: Optional[List[str]] = None

    chunks: Optional[List[Chunk]] = None

    date: Optional[datetime] = None

    metadata: Optional[Dict[str, str]] = None

    org_id: Optional[str] = None

    title: Optional[str] = None

    url: Optional[str] = None

    user_id: Optional[str] = None

    visibility: Optional[Literal["user", "org", "app", "system"]] = None
