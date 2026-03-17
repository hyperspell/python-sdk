# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ActionSendMessageResponse"]


class ActionSendMessageResponse(BaseModel):
    """Result from executing an integration action."""

    success: bool

    error: Optional[str] = None

    provider_response: Optional[Dict[str, object]] = None
