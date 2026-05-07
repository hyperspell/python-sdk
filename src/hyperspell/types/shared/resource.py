# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
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
        "github",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
        "microsoft_teams",
        "gmail_actions",
        "granola",
        "fathom",
        "linear",
    ]

    folder_ancestors: Optional[List[str]] = None
    """
    Ordered list of provider folder IDs from immediate parent up to (but not
    including) provider root. Used by resolve_sync_mode to walk the actual folder
    tree without depending on intermediate policy records. Empty = resource lives at
    provider root.
    """

    folder_id: Optional[str] = None
    """Provider folder ID this resource belongs to"""

    metadata: Optional[Metadata] = None

    parent_folder_id: Optional[str] = None
    """Parent folder ID for policy inheritance"""

    score: Optional[float] = None
    """The relevance of the resource to the query"""

    title: Optional[str] = None
