# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebCrawlerIndexParams"]


class WebCrawlerIndexParams(TypedDict, total=False):
    url: Required[str]
    """The base URL of the website to crawl"""

    limit: int
    """Maximum number of pages to crawl in total"""

    max_depth: int
    """Maximum depth of links to follow during crawling"""
