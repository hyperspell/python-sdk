# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemoryStatus"]


class MemoryStatus(BaseModel):
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

    status: Literal["pending", "processing", "completed", "failed"]
