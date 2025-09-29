# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EvaluateScoreQueryParams"]


class EvaluateScoreQueryParams(TypedDict, total=False):
    query_id: Required[str]
    """The ID of the query to provide feedback on."""

    score: float
    """Rating of the query result from -1 (bad) to +1 (good)."""
