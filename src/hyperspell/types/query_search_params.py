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

    collections: Union[str, List[str], None]
    """Only query documents in these collections.

    If not given, will query the user's default collection
    """

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

    source: List[Literal["generic", "slack", "s3", "gmail", "notion", "google_docs", "hubspot"]]
    """Only query documents from these sources."""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents on or after this date."""

    types: List[
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
            "spreadsheet",
            "archive",
            "book",
            "video",
            "code",
            "calendar",
            "json",
            "presentation",
            "unsupported",
            "person",
            "company",
            "crm_contact",
        ]
    ]
    """Only query documents of these types."""
