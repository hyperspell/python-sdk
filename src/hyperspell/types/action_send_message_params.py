# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionSendMessageParams"]


class ActionSendMessageParams(TypedDict, total=False):
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

    text: Required[str]
    """Message text"""

    channel: Optional[str]
    """Channel ID (required for Slack)"""

    connection: Optional[str]
    """Connection ID. If omitted, auto-resolved from provider + user."""

    parent: Optional[str]
    """Parent message ID for threading (thread_ts for Slack)"""
