# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TreeGetResponse", "File", "Generating"]


class File(BaseModel):
    content: str

    path: str

    team: Optional[str] = None

    tier: str

    updated_at: str

    error: Optional[str] = None

    provenance: Optional[Dict[str, object]] = None

    status: Optional[str] = None


class Generating(BaseModel):
    """Status of a newer generation that is processing or recently failed.

    This can accompany the last ready tree so clients can report progress while
    continuing to use ready content.
    """

    created_at: datetime

    status: Literal["processing", "failed"]

    tree_id: str

    error: Optional[str] = None

    progress: Optional[Dict[str, object]] = None


class TreeGetResponse(BaseModel):
    completed_at: Optional[datetime] = None

    created_at: datetime

    error: Optional[str] = None

    files: Optional[List[File]] = None

    meta: Dict[str, object]

    status: str

    tree_id: str

    version: int

    generating: Optional[Generating] = None
    """Status of a newer generation that is processing or recently failed.

    This can accompany the last ready tree so clients can report progress while
    continuing to use ready content.
    """
