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

    answer: bool
    """If true, the query will be answered along with matching source documents."""

    filter: Filter
    """Filter the query results."""

    max_results: int
    """Maximum number of results to return."""

    sources: List[
        Literal[
            "collections",
            "mcp",
            "slack",
            "s3",
            "gmail",
            "notion",
            "google_docs",
            "hubspot",
            "reddit",
            "google-calendar",
        ]
    ]
    """Only query documents from these sources."""


class Filter(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents before this date."""

    collections: Union[str, List[str], None]
    """If querying collections: Only query documents in these collections.

    If not given, will query the user's default collection
    """
