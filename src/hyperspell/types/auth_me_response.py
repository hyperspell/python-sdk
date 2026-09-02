# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthMeResponse", "App"]


class App(BaseModel):
    """The Hyperspell app's id this user belongs to"""

    id: str
    """The Hyperspell app's id this user belongs to"""

    icon_url: Optional[str] = None
    """The app's icon"""

    name: str
    """The app's name"""

    redirect_url: Optional[str] = None
    """The app's redirect URL"""


class AuthMeResponse(BaseModel):
    id: str
    """The user's id"""

    app: App
    """The Hyperspell app's id this user belongs to"""

    available_integrations: List[
        Literal[
            "reddit",
            "notion",
            "slack",
            "google_calendar",
            "google_mail",
            "imap",
            "google_meet",
            "box",
            "dropbox",
            "github",
            "gitlab",
            "google_drive",
            "vault",
            "web_crawler",
            "trace",
            "microsoft_outlook",
            "microsoft_teams",
            "granola",
            "fathom",
            "fireflies",
            "figma",
            "linear",
            "hubspot",
            "salesforce",
            "coda",
            "confluence",
            "jira",
            "metabase",
            "gong",
            "clickup",
            "lightfield",
            "pylon",
            "fellow",
            "odoo",
            "external_mcp",
        ]
    ]
    """All integrations available for the app"""

    installed_integrations: List[
        Literal[
            "reddit",
            "notion",
            "slack",
            "google_calendar",
            "google_mail",
            "imap",
            "google_meet",
            "box",
            "dropbox",
            "github",
            "gitlab",
            "google_drive",
            "vault",
            "web_crawler",
            "trace",
            "microsoft_outlook",
            "microsoft_teams",
            "granola",
            "fathom",
            "fireflies",
            "figma",
            "linear",
            "hubspot",
            "salesforce",
            "coda",
            "confluence",
            "jira",
            "metabase",
            "gong",
            "clickup",
            "lightfield",
            "pylon",
            "fellow",
            "odoo",
            "external_mcp",
        ]
    ]
    """All integrations installed for the user"""

    token_expiration: Optional[datetime] = None
    """The expiration time of the user token used to make the request"""
