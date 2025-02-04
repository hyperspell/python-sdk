# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentListResponse"]


class DocumentListResponse(BaseModel):
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
            "markdown",
            "chat",
            "email",
            "transcript",
            "legal",
            "website",
            "image",
            "pdf",
            "audio",
            "slack",
            "s3",
            "gmail",
            "notion",
            "google_docs",
        ]
    ] = None

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None
