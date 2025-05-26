# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import collection_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.collection_list_response import CollectionListResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[CollectionListResponse]:
        """
        This endpoint lists all collections, and how many documents are in each
        collection. All documents that do not have a collection assigned are in the
        `null` collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/collections/list",
            page=SyncCursorPage[CollectionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "size": size,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            model=CollectionListResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CollectionListResponse, AsyncCursorPage[CollectionListResponse]]:
        """
        This endpoint lists all collections, and how many documents are in each
        collection. All documents that do not have a collection assigned are in the
        `null` collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/collections/list",
            page=AsyncCursorPage[CollectionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "size": size,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            model=CollectionListResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.list = to_raw_response_wrapper(
            collections.list,
        )


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.list = async_to_raw_response_wrapper(
            collections.list,
        )


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.list = to_streamed_response_wrapper(
            collections.list,
        )


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
