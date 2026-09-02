# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["TreeGenerateResponse"]


class TreeGenerateResponse(BaseModel):
    created_at: datetime

    status: str

    tree_id: str
