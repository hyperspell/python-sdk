# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntegrationListResponse", "Integration"]


class Integration(BaseModel):
    id: str
    """The integration's id"""

    allow_multiple_connections: bool
    """Whether the integration allows multiple connections"""

    auth_provider: Literal["nango", "unified", "whitelabel"]
    """The integration's auth provider"""

    icon: Optional[str] = None
    """URL to the integration's icon"""

    name: str
    """The integration's display name"""

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
    """The integration's provider"""

    actions_only: Optional[bool] = None
    """Whether this integration only supports write actions (no sync)"""

    requires_channel_selection: Optional[bool] = None
    """Whether the user must select channels before indexing starts"""


class IntegrationListResponse(BaseModel):
    integrations: List[Integration]
