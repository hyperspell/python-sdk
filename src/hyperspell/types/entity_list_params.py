# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EntityListParams"]


class EntityListParams(TypedDict, total=False):
    cursor: Optional[str]

    limit: int

    min_supporting_documents: Optional[int]

    name_prefix: Optional[str]

    search: Optional[str]

    sort_by: Literal["id", "name", "type", "prominence"]

    sort_dir: Literal["asc", "desc"]

    status: Optional[Literal["provisional", "confirmed"]]
    """How strongly the entity's current identity has been established."""

    type: Optional[str]
