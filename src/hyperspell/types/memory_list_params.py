# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MemoryListParams"]


class MemoryListParams(TypedDict, total=False):
    collection: Optional[str]
    """Filter documents by collection."""

    cursor: Optional[str]

    filter: Optional[str]
    """Filter documents by metadata using MongoDB-style operators.

    Example: {"department": "engineering", "priority": {"$gt": 3}}
    """

    include_chunks: int
    """
    When > 0, include up to this many extracted memories (chunks with summaries) per
    document in each item's `chunks` field, in document order. 0 (default) omits
    them.
    """

    size: int

    source: Optional[
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
    """Filter documents by source."""

    status: Optional[
        Literal["pending", "processing", "completed", "failed", "pending_review", "skipped", "filtered", "cancelled"]
    ]
    """Filter documents by status."""
