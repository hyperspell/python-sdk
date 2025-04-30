# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "QuerySearchParams",
    "Filter",
    "FilterCollections",
    "FilterGoogleCalendar",
    "FilterNotion",
    "FilterReddit",
    "FilterSlack",
    "FilterWebCrawler",
    "Options",
    "OptionsCollections",
    "OptionsGoogleCalendar",
    "OptionsNotion",
    "OptionsReddit",
    "OptionsSlack",
    "OptionsWebCrawler",
]


class QuerySearchParams(TypedDict, total=False):
    query: Required[str]
    """Query to run."""

    answer: bool
    """If true, the query will be answered along with matching source documents."""

    filter: Optional[Filter]
    """DEPRECATED: Use options instead.

    This field will be removed in a future version.
    """

    max_results: int
    """Maximum number of results to return."""

    options: Options
    """Search options for the query."""

    sources: List[
        Literal["collections", "notion", "slack", "hubspot", "google_calendar", "reddit", "web_crawler", "box"]
    ]
    """Only query documents from these sources."""


class FilterCollections(TypedDict, total=False):
    collections: Optional[List[str]]
    """List of collections to search.

    If not provided, only the user's default collection will be searched.
    """


class FilterGoogleCalendar(TypedDict, total=False):
    calendar_id: Optional[str]
    """The ID of the calendar to search.

    If not provided, it will use the ID of the default calendar. You can get the
    list of calendars with the `/integrations/google_calendar/list` endpoint.
    """


class FilterNotion(TypedDict, total=False):
    notion_page_ids: List[str]
    """List of Notion page IDs to search.

    If not provided, all pages in the workspace will be searched.
    """


class FilterReddit(TypedDict, total=False):
    period: Literal["hour", "day", "week", "month", "year", "all"]
    """The time period to search. Defaults to 'month'."""

    sort: Literal["relevance", "new", "hot", "top", "comments"]
    """The sort order of the posts. Defaults to 'relevance'."""

    subreddit: Optional[str]
    """The subreddit to search.

    If not provided, the query will be searched for in all subreddits.
    """


class FilterSlack(TypedDict, total=False):
    channels: List[str]
    """List of Slack channels to search.

    If not provided, all channels in the workspace will be searched.
    """


class FilterWebCrawler(TypedDict, total=False):
    max_depth: int
    """Maximum depth to crawl from the starting URL"""

    url: Union[str, object]
    """The URL to crawl"""


class Filter(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    box: object
    """Search options for Box"""

    collections: FilterCollections
    """Search options for Collections"""

    google_calendar: FilterGoogleCalendar
    """Search options for Google Calendar"""

    notion: FilterNotion
    """Search options for Notion"""

    reddit: FilterReddit
    """Search options for Reddit"""

    slack: FilterSlack
    """Search options for Slack"""

    web_crawler: FilterWebCrawler
    """Search options for Web Crawler"""


class OptionsCollections(TypedDict, total=False):
    collections: Optional[List[str]]
    """List of collections to search.

    If not provided, only the user's default collection will be searched.
    """


class OptionsGoogleCalendar(TypedDict, total=False):
    calendar_id: Optional[str]
    """The ID of the calendar to search.

    If not provided, it will use the ID of the default calendar. You can get the
    list of calendars with the `/integrations/google_calendar/list` endpoint.
    """


class OptionsNotion(TypedDict, total=False):
    notion_page_ids: List[str]
    """List of Notion page IDs to search.

    If not provided, all pages in the workspace will be searched.
    """


class OptionsReddit(TypedDict, total=False):
    period: Literal["hour", "day", "week", "month", "year", "all"]
    """The time period to search. Defaults to 'month'."""

    sort: Literal["relevance", "new", "hot", "top", "comments"]
    """The sort order of the posts. Defaults to 'relevance'."""

    subreddit: Optional[str]
    """The subreddit to search.

    If not provided, the query will be searched for in all subreddits.
    """


class OptionsSlack(TypedDict, total=False):
    channels: List[str]
    """List of Slack channels to search.

    If not provided, all channels in the workspace will be searched.
    """


class OptionsWebCrawler(TypedDict, total=False):
    max_depth: int
    """Maximum depth to crawl from the starting URL"""

    url: Union[str, object]
    """The URL to crawl"""


class Options(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created on or after this date."""

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only query documents created before this date."""

    box: object
    """Search options for Box"""

    collections: OptionsCollections
    """Search options for Collections"""

    google_calendar: OptionsGoogleCalendar
    """Search options for Google Calendar"""

    notion: OptionsNotion
    """Search options for Notion"""

    reddit: OptionsReddit
    """Search options for Reddit"""

    slack: OptionsSlack
    """Search options for Slack"""

    web_crawler: OptionsWebCrawler
    """Search options for Web Crawler"""
