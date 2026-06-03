# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .resource import Resource
from ..._models import BaseModel

__all__ = ["QueryResult", "Provenance", "ProvenanceEntity", "ProvenanceSource", "ProvenanceStep"]


class ProvenanceEntity(BaseModel):
    """A canonical entity referenced by the answer's source documents."""

    id: str

    name: str

    type: str


class ProvenanceSource(BaseModel):
    """A source document that informed the final answer (the post-rank result set)."""

    resource_id: str

    source: Literal[
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "box",
        "dropbox",
        "github",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
        "microsoft_teams",
        "gmail_actions",
        "granola",
        "fathom",
        "fireflies",
        "linear",
        "hubspot",
        "salesforce",
        "coda",
        "lightfield",
    ]

    score: Optional[float] = None

    title: Optional[str] = None


class ProvenanceStep(BaseModel):
    """One tool invocation in the agent's search trajectory (audit trail)."""

    iteration: int

    status: str

    tool: str

    query: Optional[str] = None

    result_count: Optional[int] = None

    source: Optional[str] = None


class Provenance(BaseModel):
    """Auditability record attached to an agentic answer.

    Gated behind ``provenance=true`` on the request: the cheap parts (sources,
    steps, failed_sources) are derived from in-memory loop state, but ``entities``
    costs one indexed DB lookup, so the whole record is only built on request.
    """

    entities: Optional[List[ProvenanceEntity]] = None

    failed_sources: Optional[List[str]] = None

    sources: Optional[List[ProvenanceSource]] = None

    steps: Optional[List[ProvenanceStep]] = None


class QueryResult(BaseModel):
    documents: List[Resource]

    answer: Optional[str] = None
    """The answer to the query, if the request was set to answer."""

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

    query_id: Optional[str] = None
    """The ID of the query.

    This can be used to retrieve the query later, or add feedback to it. If the
    query failed, this will be None.
    """

    score: Optional[float] = None
    """The average score of the query feedback, if any."""
