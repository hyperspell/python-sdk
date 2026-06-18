# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryUpdateParams"]


class MemoryUpdateParams(TypedDict, total=False):
    source: Required[
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

    collection: Union[str, object, None]
    """
    The collection to move the document to — deprecated, set the collection using
    metadata instead.
    """

    date: Annotated[Union[Union[str, datetime], object, None], PropertyInfo(format="iso8601")]
    """Date of the document for ranking and filtering."""

    metadata: Union[Dict[str, Union[str, float, bool, None]], object, None]
    """Custom metadata for filtering.

    Keys must be alphanumeric with underscores, max 64 chars. Values must be string,
    number, boolean, or null. Will be merged with existing metadata.
    """

    text: Union[str, object, None]
    """Full text of the document. If provided, the document will be re-indexed."""

    title: Union[str, object, None]
    """Title of the document."""
