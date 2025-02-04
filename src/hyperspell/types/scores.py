# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Scores"]


class Scores(BaseModel):
    full_text_search: Optional[float] = None
    """How relevant the section is based on full text search"""

    semantic_search: Optional[float] = None
    """How relevant the section is based on vector search"""

    weighted: Optional[float] = None
    """The final weighted score of the section"""
