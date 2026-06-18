# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["Utterance"]


class Utterance(BaseModel):
    """A speaker-attributed segment of a transcript (ENG-2476/D10).

    "Utterance" is the standard name for this across transcription providers
    (AssemblyAI, Deepgram, Rev). Timestamps are relative offsets in seconds —
    provider-native; absolute times derive from `Transcript.started_at`.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    metadata: Optional[Metadata] = None
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    speaker: Optional["Person"] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


from .person import Person
