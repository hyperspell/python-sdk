# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["TreeGenerateParams"]


class TreeGenerateParams(TypedDict, total=False):
    sources: Optional[SequenceNotStr[str]]
    """Integration sources to include (e.g., ['gmail', 'slack']). Defaults to all."""

    user_id: Optional[str]
    """User ID for personal tier scoping.

    When set, personal/context.md is generated from this user's data only. Company
    and workstream tiers still use all data.
    """

    workstream_name: Optional[str]
    """Generate docs for this workstream only (skip auto-detection)."""
