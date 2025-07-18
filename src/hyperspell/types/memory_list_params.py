# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MemoryListParams"]


class MemoryListParams(TypedDict, total=False):
    collection: Optional[str]
    """Filter documents by collection."""

    cursor: Optional[str]

    size: int

    source: Optional[
        Literal[
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
    ]
    """Filter documents by source."""
