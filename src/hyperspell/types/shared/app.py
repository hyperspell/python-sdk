# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["App"]


class App(BaseModel):
    name: str

    slug: str

    user_id: str

    id: Optional[int] = None

    api_keys: Optional[List["APIKey"]] = None

    collections: Optional[List[object]] = None

    created_at: Optional[datetime] = None

    integrations: Optional[List[object]] = None

    jwt_secret: Optional[str] = None

    optional_integrations: Optional[List[object]] = None

    public_key: Optional[str] = None

    settings: Optional[object] = None


from .api_key import APIKey

if PYDANTIC_V2:
    App.model_rebuild()
else:
    App.update_forward_refs()  # type: ignore
