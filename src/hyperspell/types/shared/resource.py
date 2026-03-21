# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["Resource"]


class Resource(BaseModel):
    resource_id: str

    source: Literal[
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "box",
        "dropbox",
        "google_drive",
        "github",
        "vault",
        "web_crawler",
        "trace",
        "microsoft_teams",
        "gmail_actions",
    ]

    folder_id: Optional[str] = None
    """Provider folder ID this resource belongs to"""

    metadata: Optional[Metadata] = None

    parent_folder_id: Optional[str] = None
    """Parent folder ID for policy inheritance"""

    score: Optional[float] = None
    """The relevance of the resource to the query"""

    title: Optional[str] = None
