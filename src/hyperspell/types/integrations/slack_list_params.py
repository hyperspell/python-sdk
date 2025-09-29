# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["SlackListParams"]


class SlackListParams(TypedDict, total=False):
    channels: SequenceNotStr[str]
    """List of Slack channels to include (by id, name, or #name)."""

    exclude_archived: Optional[bool]
    """If set, pass 'exclude_archived' to Slack. If None, omit the param."""

    include_dms: bool
    """Include direct messages (im) when listing conversations."""

    include_group_dms: bool
    """Include group DMs (mpim) when listing conversations."""

    include_private: bool
    """Include private channels when constructing Slack 'types'."""
