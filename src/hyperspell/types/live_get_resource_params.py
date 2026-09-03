# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LiveGetResourceParams"]


class LiveGetResourceParams(TypedDict, total=False):
    source: Required[
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

    connection_id: Optional[str]
    """Specific connection id."""

    index: bool
    """Also queue this resource for indexing."""
