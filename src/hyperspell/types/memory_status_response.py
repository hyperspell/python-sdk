# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MemoryStatusResponse"]


class MemoryStatusResponse(BaseModel):
    providers: Dict[str, Dict[str, int]]

    total: Dict[str, int]
