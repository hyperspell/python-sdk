# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EvaluateListQueriesResponse"]


class EvaluateListQueriesResponse(BaseModel):
    query: str
    """The query string that was issued."""

    query_id: str
    """The ID of the query."""

    time: datetime
    """When the query was issued."""

    user_id: Optional[str] = None
    """The ID of the user that issued the query, if any."""
