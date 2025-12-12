# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..memory import Memory
from ..._models import BaseModel

__all__ = ["QueryResult"]


class QueryResult(BaseModel):
    documents: List[Memory]

    answer: Optional[str] = None
    """The answer to the query, if the request was set to answer."""

    errors: Optional[List[Dict[str, str]]] = None
    """Errors that occurred during the query.

    These are meant to help the developer debug the query, and are not meant to be
    shown to the user.
    """

    query_id: Optional[str] = None
    """The ID of the query.

    This can be used to retrieve the query later, or add feedback to it. If the
    query failed, this will be None.
    """

    score: Optional[float] = None
    """The average score of the query feedback, if any."""
