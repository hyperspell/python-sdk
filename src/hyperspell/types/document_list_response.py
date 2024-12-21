# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .document import Document

__all__ = ["DocumentListResponse"]


class DocumentListResponse(BaseModel):
    count: int

    documents: List[Document]

    has_more: bool

    page: int
