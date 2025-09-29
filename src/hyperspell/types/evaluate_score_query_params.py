# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EvaluateScoreQueryParams"]


class EvaluateScoreQueryParams(TypedDict, total=False):
    score: float
    """Rating of the query result from -1 (bad) to +1 (good)."""
