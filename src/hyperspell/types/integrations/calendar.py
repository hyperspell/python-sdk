# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Calendar", "Item"]


class Item(BaseModel):
    id: str
    """The ID of the calendar"""

    name: str
    """The name of the calendar"""

    primary: bool
    """Whether the calendar is the primary calendar of the user"""

    timezone: Optional[str] = None
    """Default timezone of the calendar"""


class Calendar(BaseModel):
    items: List[Item]
