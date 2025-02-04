# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentAddParams"]


class DocumentAddParams(TypedDict, total=False):
    collection: Required[str]
    """Name of the collection to add the document to.

    If the collection does not exist, it will be created.
    """

    text: Required[str]
    """Full text of the document."""

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date of the document.

    Depending on the document, this could be the creation date or date the document
    was last updated (eg. for a chat transcript, this would be the date of the last
    message). This helps the ranking algorithm and allows you to filter by date
    range.
    """

    source: Literal[
        "generic",
        "markdown",
        "chat",
        "email",
        "transcript",
        "legal",
        "website",
        "image",
        "pdf",
        "audio",
        "slack",
        "s3",
        "gmail",
        "notion",
        "google_docs",
    ]
    """Source of the document.

    This helps in parsing the document. Note that some sources require the document
    to be in a specific format.
    """

    title: Optional[str]
    """Title of the document."""
