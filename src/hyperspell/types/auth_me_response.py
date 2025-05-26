# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthMeResponse"]


class AuthMeResponse(BaseModel):
    id: str
    """The user's id"""

    app: str
    """The Hyperspell app's id this user belongs to"""

    available_integrations: List[
        Literal[
            "collections",
            "notion",
            "slack",
            "hubspot",
            "google_calendar",
            "reddit",
            "web_crawler",
            "box",
            "google_drive",
        ]
    ]
    """All integrations available for the app"""

    installed_integrations: List[
        Literal[
            "collections",
            "notion",
            "slack",
            "hubspot",
            "google_calendar",
            "reddit",
            "web_crawler",
            "box",
            "google_drive",
        ]
    ]
    """All integrations installed for the user"""

    token_expiration: Optional[datetime] = None
    """The expiration time of the user token used to make the request"""
