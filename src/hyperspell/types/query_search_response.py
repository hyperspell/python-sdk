# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .document import Document

__all__ = ["QuerySearchResponse"]


class QuerySearchResponse(BaseModel):
    documents: List[Document]

    total_sections: int
