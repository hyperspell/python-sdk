# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["QueryRetrieveParams", "Filter"]


class QueryRetrieveParams(TypedDict, total=False):
    query: Required[str]
    """Query to run."""

    collections: List[str]
    """Only query documents in these collections."""

    filter: Filter
    """Filter the query results."""

    max_results: int
    """Maximum number of results to return."""

    query_type: Literal["auto", "semantic", "keyword"]
    """Type of query to run."""


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
