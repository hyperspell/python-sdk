# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["Utterance"]


class Utterance(BaseModel):
    """A speaker-attributed segment of a transcript.

    Start and end times are offsets in seconds from the beginning of the transcript.
    """

    text: str

    id: Optional[str] = None

    end: Optional[float] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    speaker: Optional["Person"] = None

    start: Optional[float] = None

    type: Optional[Literal["utterance"]] = None


from .person import Person
