# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentStatus"]


class DocumentStatus(BaseModel):
    id: int
    """Deprecated: refer to documents by source and resource_id instead"""

    resource_id: str

    source: Literal[
        "collections", "notion", "slack", "hubspot", "google_calendar", "reddit", "web_crawler", "box", "google_drive"
    ]

    status: Literal["pending", "processing", "completed", "failed"]
