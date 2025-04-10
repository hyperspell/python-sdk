# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentAddParams"]


class DocumentAddParams(TypedDict, total=False):
    text: Required[str]
    """Full text of the document."""

    collection: Optional[str]
    """Name of the collection to add the document to.

    If the collection does not exist, it will be created. If not given, the document
    will be added to the user's default collection.
    """

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date of the document.

    Depending on the document, this could be the creation date or date the document
    was last updated (eg. for a chat transcript, this would be the date of the last
    message). This helps the ranking algorithm and allows you to filter by date
    range.
    """

    title: Optional[str]
    """Title of the document."""
