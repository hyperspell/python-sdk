# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EvaluateScoreQueryResponse"]


class EvaluateScoreQueryResponse(BaseModel):
    message: str
    """A message describing the result."""

    success: bool
    """Whether the feedback was successfully saved."""
