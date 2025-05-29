# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["DocumentStatusResponse"]


class DocumentStatusResponse(BaseModel):
    providers: Dict[str, Dict[str, int]]

    total: Dict[str, int]
