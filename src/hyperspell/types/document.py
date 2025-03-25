# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document"]


class Document(BaseModel):
    collection: str

    data: Union[List[object], object]
    """Structured representation of the document"""

    summary: str
    """Summary of the document"""

    id: Optional[int] = None

    created_at: Optional[datetime] = None

    ingested_at: Optional[datetime] = None

    metadata: Optional[Dict[str, object]] = None

    resource_id: Optional[str] = None
    """Along with service, uniquely identifies the source document"""

    source: Optional[Literal["generic", "slack", "s3", "gmail", "notion", "google_docs", "hubspot"]] = None

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None

    title: Optional[str] = None

    type: Optional[
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
            "spreadsheet",
            "archive",
            "book",
            "video",
            "code",
            "calendar",
            "json",
            "presentation",
            "unsupported",
            "person",
            "company",
            "crm_contact",
        ]
    ] = None
