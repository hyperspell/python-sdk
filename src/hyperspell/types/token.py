# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Token"]


class Token(BaseModel):
    token: str

    expires_at: datetime
