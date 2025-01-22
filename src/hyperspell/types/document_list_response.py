# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentListResponse", "Item"]


class Item(BaseModel):
    id: Optional[int] = None

    created_at: Optional[datetime] = None

    ingested_at: Optional[datetime] = None

    metadata: object

    resource_id: str

    sections_count: Optional[int] = None

    title: Optional[str] = None

    source: Optional[
        Literal[
            "generic",
            "generic_chat",
            "generic_email",
            "generic_transcript",
            "generic_legal",
            "website",
            "slack",
            "s3",
            "gmail",
            "notion",
            "google_docs",
        ]
    ] = None

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None


class DocumentListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = None
