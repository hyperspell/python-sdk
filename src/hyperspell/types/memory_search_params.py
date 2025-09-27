# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "MemorySearchParams",
    "Options",
    "OptionsBox",
    "OptionsCollections",
    "OptionsGoogleCalendar",
    "OptionsGoogleDrive",
    "OptionsGoogleMail",
    "OptionsNotion",
    "OptionsReddit",
    "OptionsSlack",
    "OptionsWebCrawler",
]


class MemorySearchParams(TypedDict, total=False):
    query: Required[str]
    """Query to run."""

    answer: bool
    """If true, the query will be answered along with matching source documents."""

    max_results: int
    """Maximum number of results to return."""

    options: Options
    """Search options for the query."""

    sources: List[
        Literal[
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
    ]
    """Only query documents from these sources."""


class OptionsBox(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsCollections(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsGoogleCalendar(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    calendar_id: Optional[str]
    """The ID of the calendar to search.

    If not provided, it will use the ID of the default calendar. You can get the
    list of calendars with the `/integrations/google_calendar/list` endpoint.
    """

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsGoogleDrive(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsGoogleMail(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

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
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

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


class OptionsReddit(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    period: Literal["hour", "day", "week", "month", "year", "all"]
    """The time period to search. Defaults to 'month'."""

    sort: Literal["relevance", "new", "hot", "top", "comments"]
    """The sort order of the posts. Defaults to 'relevance'."""

    subreddit: Optional[str]
    """The subreddit to search.

    If not provided, the query will be searched for in all subreddits.
    """

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class OptionsSlack(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

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


class OptionsWebCrawler(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    max_depth: int
    """Maximum depth to crawl from the starting URL"""

    url: Union[str, object]
    """The URL to crawl"""

    weight: float
    """Weight of results from this source.

    A weight greater than 1.0 means more results from this source will be returned,
    a weight less than 1.0 means fewer results will be returned. This will only
    affect results if multiple sources are queried at the same time.
    """


class Options(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    answer_model: Literal["llama-3.1", "gemma2", "qwen-qwq", "mistral-saba", "llama-4-scout", "deepseek-r1"]
    """Model to use for answer generation when answer=True"""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    box: OptionsBox
    """Search options for Box"""

    collections: OptionsCollections
    """Search options for vault"""

    google_calendar: OptionsGoogleCalendar
    """Search options for Google Calendar"""

    google_drive: OptionsGoogleDrive
    """Search options for Google Drive"""

    google_mail: OptionsGoogleMail
    """Search options for Gmail"""

    max_results: int
    """Maximum number of results to return."""

    notion: OptionsNotion
    """Search options for Notion"""

    reddit: OptionsReddit
    """Search options for Reddit"""

    slack: OptionsSlack
    """Search options for Slack"""

    web_crawler: OptionsWebCrawler
    """Search options for Web Crawler"""
