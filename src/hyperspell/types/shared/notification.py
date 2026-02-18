# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Notification"]


class Notification(BaseModel):
    message: str

    type: Literal["error", "warning", "info", "success"]

    time: Optional[datetime] = None
