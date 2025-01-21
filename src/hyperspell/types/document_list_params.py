# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentListParams", "Filter"]


class DocumentListParams(TypedDict, total=False):
    collections: Required[Iterable[int]]
    """The collections to filter documents by."""

    filter: Filter
    """Filter the query results."""

    limit: int
    """Number of documents to return per page."""

    page: int
    """Page number to return."""


class Filter(TypedDict, total=False):
    chunk_type: List[Literal["text", "markdown", "table", "image", "messages", "message"]]
    """Only query chunks of these types."""

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents before this date."""

    source: List[
        Literal[
            "generic",
            "generic_chat",
            "generic_email",
            "generic_transcript",
            "generic_legal",
            "website",
            "slack",
            "s3",
            "gmail",
            "notion",
            "google_docs",
        ]
    ]
    """Only query documents of these types."""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents on or after this date."""
