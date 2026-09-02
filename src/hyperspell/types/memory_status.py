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
        "imap",
        "google_meet",
        "box",
        "dropbox",
        "github",
        "gitlab",
        "google_drive",
        "vault",
        "web_crawler",
        "trace",
        "microsoft_outlook",
        "microsoft_teams",
        "granola",
        "fathom",
        "fireflies",
        "figma",
        "linear",
        "hubspot",
        "salesforce",
        "coda",
        "confluence",
        "jira",
        "metabase",
        "gong",
        "clickup",
        "lightfield",
        "pylon",
        "fellow",
        "odoo",
        "external_mcp",
    ]

    status: Literal[
        "pending", "processing", "completed", "failed", "pending_review", "skipped", "filtered", "cancelled"
    ]
