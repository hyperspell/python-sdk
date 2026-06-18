# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["EvaluateListQueriesParams"]


class EvaluateListQueriesParams(TypedDict, total=False):
    cursor: Optional[str]

    size: int

    user_id: Optional[str]
    """Filter queries by the user that issued them."""
