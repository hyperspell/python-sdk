# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .provenance_step import ProvenanceStep
from .provenance_entity import ProvenanceEntity
from .provenance_source import ProvenanceSource

__all__ = ["Provenance"]


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
