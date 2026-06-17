# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionAddReactionParams"]


class ActionAddReactionParams(TypedDict, total=False):
    channel: Required[str]
    """Channel ID containing the message"""

    name: Required[str]
    """Emoji name without colons (e.g., thumbsup)"""

    provider: Required[
        Literal[
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
    ]
    """Integration provider (e.g., slack)"""

    timestamp: Required[str]
    """Message timestamp to react to"""

    connection: Optional[str]
    """Connection ID. If omitted, auto-resolved from provider + user."""
