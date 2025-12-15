# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemoryUpdateParams"]


class MemoryUpdateParams(TypedDict, total=False):
    source: Required[
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

    collection: Union[str, object, None]
    """The collection to move the document to. Set to null to remove the collection."""

    metadata: Union[Dict[str, Union[str, float, bool]], object, None]
    """Custom metadata for filtering.

    Keys must be alphanumeric with underscores, max 64 chars. Values must be string,
    number, or boolean. Will be merged with existing metadata.
    """

    text: Union[str, object, None]
    """Full text of the document. If provided, the document will be re-indexed."""

    title: Union[str, object, None]
    """Title of the document."""
