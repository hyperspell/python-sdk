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
        "vault",
        "web_crawler",
        "notion",
        "slack",
        "google_calendar",
        "reddit",
        "box",
        "google_drive",
        "airtable",
        "algolia",
        "amplitude",
        "asana",
        "ashby",
        "bamboohr",
        "basecamp",
        "bubbles",
        "calendly",
        "confluence",
        "clickup",
        "datadog",
        "deel",
        "discord",
        "dropbox",
        "exa",
        "facebook",
        "front",
        "github",
        "gitlab",
        "google_docs",
        "google_mail",
        "google_sheet",
        "hubspot",
        "jira",
        "linear",
        "microsoft_teams",
        "mixpanel",
        "monday",
        "outlook",
        "perplexity",
        "rippling",
        "salesforce",
        "segment",
        "todoist",
        "twitter",
        "zoom",
    ]

    success: bool
