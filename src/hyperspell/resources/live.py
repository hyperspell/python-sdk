# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import live_search_params, live_get_resource_params, live_list_resources_params
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
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.live_search_response import LiveSearchResponse
from ..types.live_get_resource_response import LiveGetResourceResponse
from ..types.live_list_sources_response import LiveListSourcesResponse
from ..types.live_list_resources_response import LiveListResourcesResponse

__all__ = ["LiveResource", "AsyncLiveResource"]


class LiveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return LiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return LiveResourceWithStreamingResponse(self)

    def get_resource(
        self,
        resource_id: str,
        *,
        source: Literal[
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
        connection_id: Optional[str] | Omit = omit,
        index: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveGetResourceResponse:
        """Fetch one resource live by id.

        A single fetch may fan out into several resources
        (e.g. a thread → its messages); all are returned.

        Args:
          connection_id: Specific connection id.

          index: Also queue this resource for indexing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._get(
            path_template("/live/{source}/resources/{resource_id}", source=source, resource_id=resource_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "index": index,
                    },
                    live_get_resource_params.LiveGetResourceParams,
                ),
            ),
            cast_to=LiveGetResourceResponse,
        )

    def list_resources(
        self,
        source: Literal[
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
        *,
        connection_id: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[LiveListResourcesResponse]:
        """
        Page through a source's resources live (no indexing side effect).

        The cursor is opaque and integration-defined — pass back the `next_cursor` from
        the previous page verbatim.

        Args:
          connection_id: Specific connection id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        return self._get_api_list(
            path_template("/live/{source}/resources", source=source),
            page=SyncCursorPage[LiveListResourcesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "cursor": cursor,
                        "size": size,
                    },
                    live_list_resources_params.LiveListResourcesParams,
                ),
            ),
            model=LiveListResourcesResponse,
        )

    def list_sources(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveListSourcesResponse:
        """List the user's connected sources and the live capabilities each supports."""
        return self._get(
            "/live/sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveListSourcesResponse,
        )

    def search(
        self,
        source: Literal[
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
        *,
        query: str,
        connection_id: Optional[str] | Omit = omit,
        index: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveSearchResponse:
        """Search a source live for content that may not be indexed yet.

        With `index=true`,
        each hit is queued for indexing (no-op for live-only sources like Google
        Calendar — see `notes` in the response).

        Args:
          query: Live search query.

          connection_id: Specific connection id when the user has multiple for this source.

          index: If true, queue each hit for indexing so it's on-hand next time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        return self._post(
            path_template("/live/{source}/search", source=source),
            body=maybe_transform(
                {
                    "query": query,
                    "connection_id": connection_id,
                    "index": index,
                },
                live_search_params.LiveSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveSearchResponse,
        )


class AsyncLiveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncLiveResourceWithStreamingResponse(self)

    async def get_resource(
        self,
        resource_id: str,
        *,
        source: Literal[
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
        connection_id: Optional[str] | Omit = omit,
        index: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveGetResourceResponse:
        """Fetch one resource live by id.

        A single fetch may fan out into several resources
        (e.g. a thread → its messages); all are returned.

        Args:
          connection_id: Specific connection id.

          index: Also queue this resource for indexing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._get(
            path_template("/live/{source}/resources/{resource_id}", source=source, resource_id=resource_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connection_id": connection_id,
                        "index": index,
                    },
                    live_get_resource_params.LiveGetResourceParams,
                ),
            ),
            cast_to=LiveGetResourceResponse,
        )

    def list_resources(
        self,
        source: Literal[
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
        *,
        connection_id: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LiveListResourcesResponse, AsyncCursorPage[LiveListResourcesResponse]]:
        """
        Page through a source's resources live (no indexing side effect).

        The cursor is opaque and integration-defined — pass back the `next_cursor` from
        the previous page verbatim.

        Args:
          connection_id: Specific connection id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        return self._get_api_list(
            path_template("/live/{source}/resources", source=source),
            page=AsyncCursorPage[LiveListResourcesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "cursor": cursor,
                        "size": size,
                    },
                    live_list_resources_params.LiveListResourcesParams,
                ),
            ),
            model=LiveListResourcesResponse,
        )

    async def list_sources(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveListSourcesResponse:
        """List the user's connected sources and the live capabilities each supports."""
        return await self._get(
            "/live/sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveListSourcesResponse,
        )

    async def search(
        self,
        source: Literal[
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
        *,
        query: str,
        connection_id: Optional[str] | Omit = omit,
        index: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveSearchResponse:
        """Search a source live for content that may not be indexed yet.

        With `index=true`,
        each hit is queued for indexing (no-op for live-only sources like Google
        Calendar — see `notes` in the response).

        Args:
          query: Live search query.

          connection_id: Specific connection id when the user has multiple for this source.

          index: If true, queue each hit for indexing so it's on-hand next time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        return await self._post(
            path_template("/live/{source}/search", source=source),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "connection_id": connection_id,
                    "index": index,
                },
                live_search_params.LiveSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveSearchResponse,
        )


class LiveResourceWithRawResponse:
    def __init__(self, live: LiveResource) -> None:
        self._live = live

        self.get_resource = to_raw_response_wrapper(
            live.get_resource,
        )
        self.list_resources = to_raw_response_wrapper(
            live.list_resources,
        )
        self.list_sources = to_raw_response_wrapper(
            live.list_sources,
        )
        self.search = to_raw_response_wrapper(
            live.search,
        )


class AsyncLiveResourceWithRawResponse:
    def __init__(self, live: AsyncLiveResource) -> None:
        self._live = live

        self.get_resource = async_to_raw_response_wrapper(
            live.get_resource,
        )
        self.list_resources = async_to_raw_response_wrapper(
            live.list_resources,
        )
        self.list_sources = async_to_raw_response_wrapper(
            live.list_sources,
        )
        self.search = async_to_raw_response_wrapper(
            live.search,
        )


class LiveResourceWithStreamingResponse:
    def __init__(self, live: LiveResource) -> None:
        self._live = live

        self.get_resource = to_streamed_response_wrapper(
            live.get_resource,
        )
        self.list_resources = to_streamed_response_wrapper(
            live.list_resources,
        )
        self.list_sources = to_streamed_response_wrapper(
            live.list_sources,
        )
        self.search = to_streamed_response_wrapper(
            live.search,
        )


class AsyncLiveResourceWithStreamingResponse:
    def __init__(self, live: AsyncLiveResource) -> None:
        self._live = live

        self.get_resource = async_to_streamed_response_wrapper(
            live.get_resource,
        )
        self.list_resources = async_to_streamed_response_wrapper(
            live.list_resources,
        )
        self.list_sources = async_to_streamed_response_wrapper(
            live.list_sources,
        )
        self.search = async_to_streamed_response_wrapper(
            live.search,
        )
