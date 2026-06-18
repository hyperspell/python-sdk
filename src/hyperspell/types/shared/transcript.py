# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["Transcript"]


class Transcript(BaseModel):
    """
    A time-anchored, speaker-attributed transcript — meetings, calls
    (ENG-2476/D10; mirrors the Trace+TraceStep precedent).

    Utterance timestamps are relative offsets from `started_at`, which is the
    absolute wall-clock anchor.
    """

    id: Optional[str] = None

    children: Optional[List["Utterance"]] = None

    ended_at: Optional[datetime] = None

    metadata: Optional[Metadata] = None
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    participants: Optional[List["Person"]] = None

    started_at: Optional[datetime] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["transcript"]] = None


from .person import Person
from .utterance import Utterance
