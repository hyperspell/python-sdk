# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LiveListSourcesResponse", "Source"]


class Source(BaseModel):
    auth_provider: Literal["nango", "unified", "whitelabel"]

    capabilities: List[
        Literal["list_resources", "fetch_resource", "search_live", "passthrough", "resolve", "query_structured"]
    ]

    source: Union[
        Literal[
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
        ],
        str,
    ]


class LiveListSourcesResponse(BaseModel):
    sources: List[Source]
