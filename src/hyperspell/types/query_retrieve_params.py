# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QueryRetrieveParams"]


class QueryRetrieveParams(TypedDict, total=False):
    query: Required[str]
    """Query to run."""

    collections: List[str]
    """Only query documents in these collections."""

    max_results: int
    """Maximum number of results to return."""

    query_type: Literal["auto", "semantic", "keyword"]
    """Type of query to run."""
