# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    app_id: int

    scopes: List[Literal["all", "ingest", "query"]]

    secret: str

    id: Optional[int] = None

    app: Optional["App"] = None
    """Apps Base Schema."""

    created_at: Optional[datetime] = None

    label: Optional[str] = None

    revoked_at: Optional[datetime] = None


from .app import App

if PYDANTIC_V2:
    APIKey.model_rebuild()
else:
    APIKey.update_forward_refs()  # type: ignore
