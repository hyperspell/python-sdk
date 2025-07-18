# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VaultListResponse"]


class VaultListResponse(BaseModel):
    collection: Optional[str] = None

    document_count: int
