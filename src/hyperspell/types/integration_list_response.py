# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
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

    icon: str
    """Generate a display name from the provider by capitalizing each word."""

    name: str
    """Generate a display name from the provider by capitalizing each word."""

    provider: Literal[
        "collections",
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "box",
        "google_drive",
        "vault",
        "web_crawler",
    ]
    """The integration's provider"""


class IntegrationListResponse(BaseModel):
    integrations: List[Integration]
