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
    """The integration's provider"""

    actions_only: Optional[bool] = None
    """Whether this integration only supports write actions (no sync)"""

    channel_selection_required: Optional[bool] = None
    """Whether indexing waits until the user selects at least one channel."""

    connected_via_service_account: Optional[bool] = None
    """
    Whether this app already has a scope='app' (service-account/bot) connection for
    this integration. Informational only: a shared connection no longer blocks
    personal OAuth — shared and personal connections can coexist.
    """

    folder_selection_required: Optional[bool] = None
    """
    Whether a new personal connection waits for the user to select at least one
    folder before indexing begins. Shared service-account connections are exempt.
    """

    private_channels_included: Optional[bool] = None
    """
    Whether private channels are included by default when no explicit channel
    selection is provided.
    """

    public_channels_included: Optional[bool] = None
    """
    Whether public channels are included by default when no explicit channel
    selection is provided.
    """

    requires_channel_selection: Optional[bool] = None
    """Whether the user must select channels before indexing starts"""

    supports_channel_selection: Optional[bool] = None
    """Whether the integration allows users to choose specific channels to index.

    Unless selection is required, an empty selection indexes all channels.
    """

    supports_folder_selection: Optional[bool] = None
    """
    Whether the integration supports listing folders and configuring per-folder sync
    policies.
    """


class IntegrationListResponse(BaseModel):
    integrations: List[Integration]
