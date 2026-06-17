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

    size: int

    source: Optional[
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
    """Filter documents by source."""

    status: Optional[Literal["pending", "processing", "completed", "failed", "pending_review", "skipped"]]
    """Filter documents by status."""
