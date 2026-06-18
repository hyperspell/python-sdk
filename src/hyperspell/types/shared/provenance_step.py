# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProvenanceStep"]


class ProvenanceStep(BaseModel):
    """One tool invocation in the agent's search trajectory (audit trail)."""

    iteration: int

    status: str

    tool: str

    query: Optional[str] = None

    result_count: Optional[int] = None

    source: Optional[str] = None
