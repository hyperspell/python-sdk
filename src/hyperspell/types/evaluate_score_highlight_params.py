# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluateScoreHighlightParams"]


class EvaluateScoreHighlightParams(TypedDict, total=False):
    highlight_id: Required[str]
    """The ID of the chunk to provide feedback on."""

    comment: Optional[str]
    """Comment on the chunk"""

    score: float
    """Rating of the chunk from -1 (bad) to +1 (good)."""
