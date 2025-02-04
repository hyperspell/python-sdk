# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentAddResponse"]


class DocumentAddResponse(BaseModel):
    id: int

    status: Literal["pending", "processing", "completed", "failed"]
