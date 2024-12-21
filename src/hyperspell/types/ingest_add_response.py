# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IngestAddResponse"]


class IngestAddResponse(BaseModel):
    document_id: str

    status: Literal["processing", "done"]
