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
    """The connection's provider"""

    backfill_state: Optional[Literal["backfilling", "quiesced", "completed", "unknown"]] = None
    """
    State of the historical backfill for providers that deliver history
    asynchronously: 'backfilling' while history is still streaming in, 'quiesced'
    once no backfill batch has arrived for a while (drained or stalled), 'completed'
    if the provider confirmed completion, and 'unknown' when the provider has not
    reported a backfill state.
    """

    scope: Optional[Literal["user", "app"]] = None
    """
    'user' for a personal connection; 'app' for an org-wide (app-level) connection
    installed once by an app admin and shared with every user of the app.
    """

    selected_count: Optional[int] = None
    """Number of items selected for this connection.

    For integrations that require selection, 0 means nothing is being indexed.
    """


class ConnectionListResponse(BaseModel):
    connections: List[Connection]
