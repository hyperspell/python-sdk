# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionAddParams"]


class SessionAddParams(TypedDict, total=False):
    history: Required[str]
    """The trace history as a string.

    Can be a JSON array of Hyperdoc steps, a JSON array of Vercel AI SDK steps, or
    OpenClaw JSONL.
    """

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date of the trace"""

    extract: List[Literal["procedure", "memory", "mood"]]
    """What kind of memories to extract from the trace"""

    format: Optional[Literal["vercel", "hyperdoc", "openclaw"]]
    """Trace format: 'vercel', 'hyperdoc', or 'openclaw'. Auto-detected if not set."""

    metadata: Optional[Dict[str, Union[str, float, bool]]]
    """Custom metadata for filtering.

    Keys must be alphanumeric with underscores, max 64 chars.
    """

    session_id: str
    """Resource identifier for the trace."""

    title: Optional[str]
    """Title of the trace"""
