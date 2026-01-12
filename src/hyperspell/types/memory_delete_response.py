# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemoryDeleteResponse"]


class MemoryDeleteResponse(BaseModel):
    chunks_deleted: int

    message: str

    resource_id: str

    source: Literal[
        "collections",
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "box",
        "google_drive",
        "vault",
        "web_crawler",
    ]

    success: bool
