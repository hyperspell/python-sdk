# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .provenance_step import ProvenanceStep
from .provenance_entity import ProvenanceEntity
from .provenance_source import ProvenanceSource

__all__ = ["Provenance"]


class Provenance(BaseModel):
    """Auditability record returned when requested for a supported query."""

    entities: Optional[List[ProvenanceEntity]] = None

    failed_sources: Optional[List[str]] = None

    sources: Optional[List[ProvenanceSource]] = None

    steps: Optional[List[ProvenanceStep]] = None
