# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LiveListResourcesParams"]


class LiveListResourcesParams(TypedDict, total=False):
    connection_id: Optional[str]
    """Specific connection id."""

    cursor: Optional[str]

    size: int
