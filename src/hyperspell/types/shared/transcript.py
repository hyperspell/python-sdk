# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["Transcript"]


class Transcript(BaseModel):
    """A time-anchored, speaker-attributed transcript for a meeting or call.

    Utterance timestamps are relative offsets from `started_at`, which is the
    absolute wall-clock anchor.
    """

    id: Optional[str] = None

    children: Optional[List["Utterance"]] = None

    ended_at: Optional[datetime] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    participants: Optional[List["Person"]] = None

    started_at: Optional[datetime] = None

    text: Optional[str] = None

    title: Optional[str] = None

    type: Optional[Literal["transcript"]] = None


from .person import Person
from .utterance import Utterance
