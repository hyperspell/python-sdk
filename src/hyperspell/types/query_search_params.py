# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["QuerySearchParams", "Filter"]


class QuerySearchParams(TypedDict, total=False):
    query: Required[str]
    """Query to run."""

    collections: List[str]
    """Only query documents in these collections."""

    filter: Filter
    """Filter the query results."""

    include_elements: bool
    """Include the elements of a section in the results."""

    max_results: int
    """Maximum number of results to return."""

    query_type: Literal["auto", "semantic", "keyword"]
    """Type of query to run."""


class Filter(TypedDict, total=False):
    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents before this date."""

    source: List[
        Literal[
            "generic",
            "markdown",
            "chat",
            "email",
            "transcript",
            "legal",
            "website",
            "image",
            "pdf",
            "audio",
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
