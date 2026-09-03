# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["LiveSearchParams"]


class LiveSearchParams(TypedDict, total=False):
    query: Required[str]
    """Live search query."""

    connection_id: Optional[str]
    """Specific connection id when the user has multiple for this source."""

    index: bool
    """If true, queue each hit for indexing so it's on-hand next time."""
