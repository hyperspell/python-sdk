# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from ..._models import BaseModel
from .provenance import Provenance

__all__ = ["QueryResult"]


class QueryResult(BaseModel):
    answer: Optional[str] = None
    """The answer to the query, if the request was set to answer."""

    documents: Optional[List["ScoredDocumentResponse"]] = None
    """
    The matching documents, each carrying its hyperdoc tree plus query-path
    score/highlights/summary (ENG-2479 Phase 4).
    """

    errors: Optional[List[Dict[str, str]]] = None
    """Errors that occurred during the query.

    These are meant to help the developer debug the query, and are not meant to be
    shown to the user.
    """

    provenance: Optional[Provenance] = None
    """Auditability record attached to an agentic answer.

    Gated behind `provenance=true` on the request: the cheap parts (sources, steps,
    failed_sources) are derived from in-memory loop state, but `entities` costs one
    indexed DB lookup, so the whole record is only built on request.
    """

    query: Optional[str] = None
    """The query string that was issued."""

    query_id: Optional[str] = None
    """The ID of the query.

    This can be used to retrieve the query later, or add feedback to it. If the
    query failed, this will be None.
    """

    score: Optional[float] = None
    """The average score of the query feedback, if any."""


from .scored_document_response import ScoredDocumentResponse
