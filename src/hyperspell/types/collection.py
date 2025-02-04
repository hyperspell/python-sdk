# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Collection"]


class Collection(BaseModel):
    created_at: datetime

    name: str

    owner: Optional[str] = None
