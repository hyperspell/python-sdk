# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentAddURLParams"]


class DocumentAddURLParams(TypedDict, total=False):
    collection: Required[str]
    """Name of the collection to add the document to.

    If the collection does not exist, it will be created.
    """

    url: Required[str]
    """Source URL of the document."""
