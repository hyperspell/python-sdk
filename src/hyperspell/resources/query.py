# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import query_search_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.query_search_response import QuerySearchResponse

__all__ = ["QueryResource", "AsyncQueryResource"]


class QueryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return QueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return QueryResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        query: str,
        answer: bool | NotGiven = NOT_GIVEN,
        filter: Optional[query_search_params.Filter] | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        options: query_search_params.Options | NotGiven = NOT_GIVEN,
        sources: List[
            Literal["collections", "notion", "slack", "hubspot", "google_calendar", "reddit", "web_crawler", "box"]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuerySearchResponse:
        """
        Retrieves documents matching the query.

        Args:
          query: Query to run.

          answer: If true, the query will be answered along with matching source documents.

          filter: DEPRECATED: Use options instead. This field will be removed in a future version.

          max_results: Maximum number of results to return.

          options: Search options for the query.

          sources: Only query documents from these sources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/query",
            body=maybe_transform(
                {
                    "query": query,
                    "answer": answer,
                    "filter": filter,
                    "max_results": max_results,
                    "options": options,
                    "sources": sources,
                },
                query_search_params.QuerySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuerySearchResponse,
        )


class AsyncQueryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncQueryResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        query: str,
        answer: bool | NotGiven = NOT_GIVEN,
        filter: Optional[query_search_params.Filter] | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        options: query_search_params.Options | NotGiven = NOT_GIVEN,
        sources: List[
            Literal["collections", "notion", "slack", "hubspot", "google_calendar", "reddit", "web_crawler", "box"]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuerySearchResponse:
        """
        Retrieves documents matching the query.

        Args:
          query: Query to run.

          answer: If true, the query will be answered along with matching source documents.

          filter: DEPRECATED: Use options instead. This field will be removed in a future version.

          max_results: Maximum number of results to return.

          options: Search options for the query.

          sources: Only query documents from these sources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/query",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "answer": answer,
                    "filter": filter,
                    "max_results": max_results,
                    "options": options,
                    "sources": sources,
                },
                query_search_params.QuerySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuerySearchResponse,
        )


class QueryResourceWithRawResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.search = to_raw_response_wrapper(
            query.search,
        )


class AsyncQueryResourceWithRawResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.search = async_to_raw_response_wrapper(
            query.search,
        )


class QueryResourceWithStreamingResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.search = to_streamed_response_wrapper(
            query.search,
        )


class AsyncQueryResourceWithStreamingResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.search = async_to_streamed_response_wrapper(
            query.search,
        )
