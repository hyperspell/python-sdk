# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectionListResponse", "Connection"]


class Connection(BaseModel):
    id: str
    """The connection's id"""

    integration_id: str
    """The connection's integration id"""

    label: Optional[str] = None
    """The connection's label"""

    provider: Literal[
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "box",
        "dropbox",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
    ]
    """The connection's provider"""


class ConnectionListResponse(BaseModel):
    connections: List[Connection]
