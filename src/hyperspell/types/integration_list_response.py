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

    auth_provider: Literal["nango", "hyperspell", "composio", "whitelabel", "unified"]
    """The integration's auth provider"""

    icon: str
    """Generate a display name from the provider by capitalizing each word."""

    name: str
    """Generate a display name from the provider by capitalizing each word."""

    provider: Literal[
        "collections",
        "vault",
        "web_crawler",
        "notion",
        "slack",
        "google_calendar",
        "reddit",
        "box",
        "google_drive",
        "airtable",
        "algolia",
        "amplitude",
        "asana",
        "ashby",
        "bamboohr",
        "basecamp",
        "bubbles",
        "calendly",
        "confluence",
        "clickup",
        "datadog",
        "deel",
        "discord",
        "dropbox",
        "exa",
        "facebook",
        "front",
        "github",
        "gitlab",
        "google_docs",
        "google_mail",
        "google_sheet",
        "hubspot",
        "jira",
        "linear",
        "microsoft_teams",
        "mixpanel",
        "monday",
        "outlook",
        "perplexity",
        "rippling",
        "salesforce",
        "segment",
        "todoist",
        "twitter",
        "zoom",
    ]
    """The integration's provider"""


class IntegrationListResponse(BaseModel):
    integrations: List[Integration]
