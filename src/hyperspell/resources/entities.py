# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import entity_list_params, entity_search_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncEntityCursorPage, AsyncEntityCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.entity_get_response import EntityGetResponse
from ..types.entity_list_response import EntityListResponse
from ..types.entity_search_response import EntitySearchResponse

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        min_supporting_documents: Optional[int] | Omit = omit,
        name_prefix: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        sort_by: Literal["id", "name", "type", "prominence"] | Omit = omit,
        sort_dir: Literal["asc", "desc"] | Omit = omit,
        status: Optional[Literal["provisional", "confirmed"]] | Omit = omit,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntityCursorPage[EntityListResponse]:
        """
        List entities available to the current app.

        Results can be filtered by type, status, name, and supporting-document count.
        Use the returned cursor to retrieve the next page.

        Args:
          status: How strongly the entity's current identity has been established.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entities",
            page=SyncEntityCursorPage[EntityListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "min_supporting_documents": min_supporting_documents,
                        "name_prefix": name_prefix,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_dir": sort_dir,
                        "status": status,
                        "type": type,
                    },
                    entity_list_params.EntityListParams,
                ),
            ),
            model=EntityListResponse,
        )

    def get(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityGetResponse:
        """
        Fetch a single entity belonging to the current app.

        Returns 404 when the entity does not exist or is not visible to the app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            path_template("/entities/{entity_id}", entity_id=entity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityGetResponse,
        )

    def search(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitySearchResponse:
        """
        Search the current app's entities by meaning.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entities/search",
            body=maybe_transform(
                {
                    "query": query,
                    "limit": limit,
                    "type": type,
                },
                entity_search_params.EntitySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitySearchResponse,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        min_supporting_documents: Optional[int] | Omit = omit,
        name_prefix: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        sort_by: Literal["id", "name", "type", "prominence"] | Omit = omit,
        sort_dir: Literal["asc", "desc"] | Omit = omit,
        status: Optional[Literal["provisional", "confirmed"]] | Omit = omit,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EntityListResponse, AsyncEntityCursorPage[EntityListResponse]]:
        """
        List entities available to the current app.

        Results can be filtered by type, status, name, and supporting-document count.
        Use the returned cursor to retrieve the next page.

        Args:
          status: How strongly the entity's current identity has been established.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entities",
            page=AsyncEntityCursorPage[EntityListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "min_supporting_documents": min_supporting_documents,
                        "name_prefix": name_prefix,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_dir": sort_dir,
                        "status": status,
                        "type": type,
                    },
                    entity_list_params.EntityListParams,
                ),
            ),
            model=EntityListResponse,
        )

    async def get(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityGetResponse:
        """
        Fetch a single entity belonging to the current app.

        Returns 404 when the entity does not exist or is not visible to the app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            path_template("/entities/{entity_id}", entity_id=entity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityGetResponse,
        )

    async def search(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitySearchResponse:
        """
        Search the current app's entities by meaning.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entities/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "limit": limit,
                    "type": type,
                },
                entity_search_params.EntitySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitySearchResponse,
        )


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.list = to_raw_response_wrapper(
            entities.list,
        )
        self.get = to_raw_response_wrapper(
            entities.get,
        )
        self.search = to_raw_response_wrapper(
            entities.search,
        )


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.list = async_to_raw_response_wrapper(
            entities.list,
        )
        self.get = async_to_raw_response_wrapper(
            entities.get,
        )
        self.search = async_to_raw_response_wrapper(
            entities.search,
        )


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.list = to_streamed_response_wrapper(
            entities.list,
        )
        self.get = to_streamed_response_wrapper(
            entities.get,
        )
        self.search = to_streamed_response_wrapper(
            entities.search,
        )


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.list = async_to_streamed_response_wrapper(
            entities.list,
        )
        self.get = async_to_streamed_response_wrapper(
            entities.get,
        )
        self.search = async_to_streamed_response_wrapper(
            entities.search,
        )
