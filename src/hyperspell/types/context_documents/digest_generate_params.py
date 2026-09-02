# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["DigestGenerateParams"]


class DigestGenerateParams(TypedDict, total=False):
    period: str
    """Digest cadence: 'daily' or 'weekly'.

    Sets the default window when none is given.
    """

    sources: Optional[SequenceNotStr[str]]
    """Integration sources to include (e.g., ['slack', 'github']). Defaults to all."""

    window_end: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Exclusive upper bound of the digest window. Defaults to now."""

    window_start: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Inclusive lower bound of the digest window.

    Defaults to midnight UTC today (paired with window_end=now) when omitted. Both
    bounds must be supplied together.
    """
