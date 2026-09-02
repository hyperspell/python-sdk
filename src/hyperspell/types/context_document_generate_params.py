# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ContextDocumentGenerateParams"]


class ContextDocumentGenerateParams(TypedDict, total=False):
    model: str
    """Model used for final synthesis."""

    prompt: Optional[str]
    """Custom prompt template. Replaces the standard summary prompt."""

    sources: Optional[SequenceNotStr[str]]
    """Integration sources to include (e.g., ['gmail', 'slack']).

    Defaults to all connected integrations.
    """

    user_id: Optional[str]
    """Scope generation to a specific user's data."""
