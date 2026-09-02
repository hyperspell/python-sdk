# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "MemorySearchParams",
    "Options",
    "OptionsGoogleDrive",
    "OptionsGoogleMail",
    "OptionsNotion",
    "OptionsSlack",
    "OptionsVault",
    "OptionsWebCrawler",
]


class MemorySearchParams(TypedDict, total=False):
    query: Required[str]
    """Query to run."""

    answer: bool
    """If true, the query will be answered along with matching source documents."""

    effort: Literal["minimal", "low", "medium", "high", "very_high"]
    """Controls retrieval thoroughness.

    'minimal' performs direct retrieval. 'low' improves the query and extracts date
    filters. 'medium' adds up to 3 refinement rounds; 'high' allows up to 6. Higher
    levels can improve recall but add latency and cost.
    """

    max_results: int
    """Maximum number of results to return."""

    options: Options
    """Search options for the query."""

    provenance: bool
    """
    If true (effort='very_high' only), attach a provenance record to the response:
    the source documents and entities the answer was grounded in, the agent's search
    trajectory, and any sources that failed. Intended for auditability and
    compliance use cases.
    """

    sources: List[
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
        ]
    ]
    """Only query documents from these sources.

    Names are case-insensitive and accept either separator, so `Google Drive`'s
    provider may be given as `google_drive`, `google-drive`, or `GOOGLE_DRIVE`.
    """


class OptionsGoogleDrive(TypedDict, total=False):
    """Search options for Google Drive"""

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsGoogleMail(TypedDict, total=False):
    """Search options for Gmail"""

    label_ids: SequenceNotStr[str]
    """List of label IDs to filter messages (e.g., ['INBOX', 'SENT', 'DRAFT']).

    Multiple labels are combined with OR logic - messages matching ANY specified
    label will be returned. If empty, no label filtering is applied (searches all
    accessible messages).
    """

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsNotion(TypedDict, total=False):
    """Search options for Notion"""

    notion_page_ids: SequenceNotStr[str]
    """List of Notion page IDs to search.

    If not provided, all pages in the workspace will be searched.
    """

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsSlack(TypedDict, total=False):
    """Search options for Slack"""

    channels: SequenceNotStr[str]
    """List of Slack channels to include (by id, name, or #name)."""

    exclude_archived: Optional[bool]
    """If set, pass 'exclude_archived' to Slack. If None, omit the param."""

    include_dms: bool
    """Include direct messages (im) when listing conversations."""

    include_group_dms: bool
    """Include group DMs (mpim) when listing conversations."""

    include_private: bool
    """Include private channels when constructing Slack 'types'.

    Defaults to False to preserve existing cassette query params.
    """

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsVault(TypedDict, total=False):
    """Search options for vault"""

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsWebCrawler(TypedDict, total=False):
    """Search options for Web Crawler"""

    max_depth: int
    """Maximum depth to crawl from the starting URL"""

    url: Optional[str]
    """The URL to crawl"""

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class Options(TypedDict, total=False):
    """Search options for the query."""

    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    answer_model: Literal[
        "llama-3.1",
        "gemma2",
        "qwen-qwq",
        "mistral-saba",
        "llama-4-scout",
        "deepseek-r1",
        "gpt-oss-20b",
        "gpt-oss-120b",
        "claude-sonnet-4-6",
        "claude-sonnet-5",
        "claude-opus-4-7",
        "claude-opus-4-8",
    ]
    """Model to use for answer generation when answer=True"""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    filter: Optional[Dict[str, object]]
    """Metadata filters using MongoDB-style operators.

    Example: {'status': 'published', 'priority': {'$gt': 3}}
    """

    google_drive: OptionsGoogleDrive
    """Search options for Google Drive"""

    google_mail: OptionsGoogleMail
    """Search options for Gmail"""

    max_results: int
    """Maximum number of results to return."""

    memory_types: List[Literal["procedure", "memory", "mood"]]
    """Filter by memory type.

    Defaults to generic memories only. Pass multiple types to include procedures,
    etc.
    """

    notion: OptionsNotion
    """Search options for Notion"""

    recency_half_life_days: Optional[float]
    """
    When set, multiplies each result's score by an exponential-decay factor based on
    the document's most recent activity timestamp (source-reported last_modified,
    falling back to document_date). A document one half-life old gets its score
    halved. Resources with no recency timestamp are passed through unchanged. Leave
    unset to disable.
    """

    resource_ids: Optional[SequenceNotStr[str]]
    """Only return results from these specific resource IDs.

    Useful for scoping searches to specific documents (e.g., a specific email thread
    or uploaded file).
    """

    slack: OptionsSlack
    """Search options for Slack"""

    timezone: str
    """IANA timezone used to interpret date-only bounds and relative calendar phrases.

    Defaults to UTC.
    """

    vault: OptionsVault
    """Search options for vault"""

    web_crawler: OptionsWebCrawler
    """Search options for Web Crawler"""
