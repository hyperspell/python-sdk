# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CollectionCreateParams"]


class CollectionCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the collection."""

    owner: Optional[str]
    """The owner of the collection.

    If the request is made using a user token, this will be set to the user ID.
    """
