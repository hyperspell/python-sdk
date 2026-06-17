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
        "github",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
        "microsoft_teams",
        "gmail_actions",
        "granola",
        "fathom",
        "fireflies",
        "linear",
        "hubspot",
        "salesforce",
        "coda",
        "lightfield",
        "gong",
    ]
    """The connection's provider"""

    selected_count: Optional[int] = None
    """
    Count of items in user_options.channels (Teams: workspaces selected; 0 means
    nothing is being indexed for integrations that require selection).
    """


class ConnectionListResponse(BaseModel):
    connections: List[Connection]
