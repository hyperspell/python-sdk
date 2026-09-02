# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ContextDocumentGenerateResponse"]


class ContextDocumentGenerateResponse(BaseModel):
    created_at: datetime

    document_id: str

    status: str
