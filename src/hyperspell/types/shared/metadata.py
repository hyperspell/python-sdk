# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Metadata", "Source"]


class Source(BaseModel):
    """A reference to source content that supports a block.

    ``chunk_id`` identifies the supporting content. ``resource_id`` and
    ``source`` identify its document, and ``score`` optionally records relevance.
    """

    chunk_id: str

    resource_id: Optional[str] = None

    score: Optional[float] = None

    source: Optional[str] = None


class Metadata(BaseModel):
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is
    omitted from serialized responses.
    """

    edited_by: Optional[str] = None

    sources: Optional[List[Source]] = None
