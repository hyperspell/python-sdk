# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["IngestFileParams", "Data"]


class IngestFileParams(TypedDict, total=False):
    data: Required[Data]

    file: Required[FileTypes]


class Data(TypedDict, total=False):
    date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Date of the document.

    Depending on the document, this could be the creation date or date the document
    was last updated (eg. for a chat transcript, this would be the date of the last
    message). This helps the ranking algorithm and allows you to filter by date
    range.
    """

    metadata: Dict[str, Union[str, float, bool, List[str], Iterable[int], Iterable[float], Iterable[bool]]]
    """Metadata to attach to the document.

    This can be used to store additional information about the document.
    """

    namespace: Optional[str]
    """Namespace to assign this document to.

    This can be for example a specific conversation that it is scoped to
    """

    org_id: Optional[str]
    """Organization ID to assign this document to."""

    text: Optional[str]
    """Full text of the document."""

    title: Optional[str]
    """Title of the document."""

    type: Literal["chat", "email", "generic", "transcript", "legal"]
    """Type of the document. This is optional, but helps with parsing the document."""

    url: Optional[str]
    """Source URL of the document.

    If text is not provided and URL is publicly accessible, Hyperspell will retrieve
    the document from this URL.
    """

    user_id: Optional[str]
    """User ID to assign this document to."""

    visibility: Literal["user", "org", "app", "system"]
    """Visibility of the document.

    If visibility is set to USER, then `user_id` must be present, and the document
    will only be visible to this user. If visibility is set to `org`, then `org_id`
    must be present and the document will be visible to all users in the same
    organization.
    """
