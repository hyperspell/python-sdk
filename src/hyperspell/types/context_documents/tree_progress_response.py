# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TreeProgressResponse"]


class TreeProgressResponse(BaseModel):
    """Response shape for GET /context-documents/tree/{tree_id}/progress."""

    status: str

    tree_id: str

    completed_docs: Optional[int] = None

    failed_docs: Optional[int] = None

    failed_keys: Optional[List[str]] = None

    phase: Optional[str] = None
    """Generation phase.

    Values: discover, search, select, synthesize, finalize, personal, done. Null
    when detailed progress is unavailable.
    """

    total_docs: Optional[int] = None
