# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["App"]


class App(BaseModel):
    name: str

    slug: str

    user_id: str

    id: Optional[int] = None

    created_at: Optional[datetime] = None

    integrations: Optional[List[object]] = None

    optional_integrations: Optional[List[object]] = None

    settings: Optional[Dict[str, object]] = None
