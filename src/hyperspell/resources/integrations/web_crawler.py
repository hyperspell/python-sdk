# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.integrations import web_crawler_index_params
from ...types.integrations.web_crawler_index_response import WebCrawlerIndexResponse

__all__ = ["WebCrawlerResource", "AsyncWebCrawlerResource"]


class WebCrawlerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebCrawlerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return WebCrawlerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebCrawlerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return WebCrawlerResourceWithStreamingResponse(self)

    def index(
        self,
        *,
        url: str,
        limit: int | Omit = omit,
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebCrawlerIndexResponse:
        """
        Recursively crawl a website to make it available for indexed search.

        Args:
          url: The base URL of the website to crawl

          limit: Maximum number of pages to crawl in total

          max_depth: Maximum depth of links to follow during crawling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/integrations/web_crawler/index",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "limit": limit,
                        "max_depth": max_depth,
                    },
                    web_crawler_index_params.WebCrawlerIndexParams,
                ),
            ),
            cast_to=WebCrawlerIndexResponse,
        )


class AsyncWebCrawlerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebCrawlerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWebCrawlerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebCrawlerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncWebCrawlerResourceWithStreamingResponse(self)

    async def index(
        self,
        *,
        url: str,
        limit: int | Omit = omit,
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebCrawlerIndexResponse:
        """
        Recursively crawl a website to make it available for indexed search.

        Args:
          url: The base URL of the website to crawl

          limit: Maximum number of pages to crawl in total

          max_depth: Maximum depth of links to follow during crawling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/integrations/web_crawler/index",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "limit": limit,
                        "max_depth": max_depth,
                    },
                    web_crawler_index_params.WebCrawlerIndexParams,
                ),
            ),
            cast_to=WebCrawlerIndexResponse,
        )


class WebCrawlerResourceWithRawResponse:
    def __init__(self, web_crawler: WebCrawlerResource) -> None:
        self._web_crawler = web_crawler

        self.index = to_raw_response_wrapper(
            web_crawler.index,
        )


class AsyncWebCrawlerResourceWithRawResponse:
    def __init__(self, web_crawler: AsyncWebCrawlerResource) -> None:
        self._web_crawler = web_crawler

        self.index = async_to_raw_response_wrapper(
            web_crawler.index,
        )


class WebCrawlerResourceWithStreamingResponse:
    def __init__(self, web_crawler: WebCrawlerResource) -> None:
        self._web_crawler = web_crawler

        self.index = to_streamed_response_wrapper(
            web_crawler.index,
        )


class AsyncWebCrawlerResourceWithStreamingResponse:
    def __init__(self, web_crawler: AsyncWebCrawlerResource) -> None:
        self._web_crawler = web_crawler

        self.index = async_to_streamed_response_wrapper(
            web_crawler.index,
        )
