# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Memory", "Metadata", "MetadataEvent"]


class MetadataEvent(BaseModel):
    message: str

    type: Literal["error", "warning", "info", "success"]

    time: Optional[datetime] = None


class Metadata(BaseModel):
    created_at: Optional[datetime] = None

    events: Optional[List[MetadataEvent]] = None

    indexed_at: Optional[datetime] = None

    last_modified: Optional[datetime] = None

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None

    url: Optional[str] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Memory(BaseModel):
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

    metadata: Optional[Metadata] = None

    score: Optional[float] = None
    """The relevance of the resource to the query"""
