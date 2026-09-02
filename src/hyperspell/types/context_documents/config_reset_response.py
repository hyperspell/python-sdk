# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["ConfigResetResponse"]


class ConfigResetResponse(BaseModel):
    """Brain-generation settings that customers can view and edit."""

    prompts: Dict[str, object]

    source_weights: Dict[str, str]

    structure: Dict[str, object]

    detected_domain: Optional[str] = None

    domain: Optional[str] = None
