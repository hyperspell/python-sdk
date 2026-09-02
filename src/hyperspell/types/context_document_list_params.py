# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ContextDocumentListParams"]


class ContextDocumentListParams(TypedDict, total=False):
    cursor: Optional[str]

    limit: int

    status: Optional[Literal["processing", "completed", "failed"]]
