# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document", "Metadata"]


class Metadata(BaseModel):
    created_at: Optional[datetime] = None

    last_modified: Optional[datetime] = None

    url: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Document(BaseModel):
    resource_id: str

    source: Literal[
        "collections",
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

    metadata: Optional[Metadata] = None

    score: Optional[float] = None
    """The relevance of the resource to the query"""
