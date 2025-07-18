# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["MemoryUploadParams"]


class MemoryUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to ingest."""

    collection: Optional[str]
    """The collection to add the document to."""
