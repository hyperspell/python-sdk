# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ProvenanceEntity"]


class ProvenanceEntity(BaseModel):
    """A canonical entity referenced by the answer's source documents."""

    id: str

    name: str

    type: str
