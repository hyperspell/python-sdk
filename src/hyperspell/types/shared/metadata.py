# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Metadata", "Source"]


class Source(BaseModel):
    """A reference to a memory/chunk that a block's content is grounded in (ENG-1390).

    Chunks are the unit persisted to the DB — extracted memories become chunks when
    indexed — so `chunk_id` is the stable pointer back to the source. `resource_id`
    and `source` locate the originating document; `score` carries optional retrieval
    relevance. Kept deliberately self-contained (plain `str` for `source` rather than
    the `DocumentProviders` enum) so the hyperdoc format stays free of app-layer imports.
    """

    chunk_id: str

    resource_id: Optional[str] = None

    score: Optional[float] = None

    source: Optional[str] = None


class Metadata(BaseModel):
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    edited_by: Optional[str] = None

    sources: Optional[List[Source]] = None
