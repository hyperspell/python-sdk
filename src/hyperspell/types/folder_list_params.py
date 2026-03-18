# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FolderListParams"]


class FolderListParams(TypedDict, total=False):
    parent_id: Optional[str]
    """Parent folder ID. Omit for root-level folders."""
