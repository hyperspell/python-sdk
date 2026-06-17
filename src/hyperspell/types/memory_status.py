# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemoryStatus"]


class MemoryStatus(BaseModel):
    resource_id: str

    source: Literal[
        "reddit",
        "notion",
        "slack",
        "google_calendar",
        "google_mail",
        "box",
        "dropbox",
        "github",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
        "microsoft_teams",
        "gmail_actions",
        "granola",
        "fathom",
        "fireflies",
        "linear",
        "hubspot",
        "salesforce",
        "coda",
        "lightfield",
        "gong",
    ]

    status: Literal["pending", "processing", "completed", "failed", "pending_review", "skipped"]
