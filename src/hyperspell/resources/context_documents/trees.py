# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.context_documents import tree_generate_params, tree_get_latest_params
from ...types.context_documents.tree_get_response import TreeGetResponse
from ...types.context_documents.tree_generate_response import TreeGenerateResponse
from ...types.context_documents.tree_progress_response import TreeProgressResponse
from ...types.context_documents.tree_get_latest_response import TreeGetLatestResponse

__all__ = ["TreesResource", "AsyncTreesResource"]


class TreesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TreesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TreesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TreesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return TreesResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        sources: Optional[SequenceNotStr[str]] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        workstream_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreeGenerateResponse:
        """
        Generate a three-tier context document tree for local push delivery.

        Creates company, workstream, and personal context documents from the app's
        synced data. Returns immediately with a tree ID; use
        `GET /context-documents/tree/latest` to retrieve the result.

        Args:
          sources: Integration sources to include (e.g., ['gmail', 'slack']). Defaults to all.

          user_id: User ID for personal tier scoping. When set, personal/context.md is generated
              from this user's data only. Company and workstream tiers still use all data.

          workstream_name: Generate docs for this workstream only (skip auto-detection).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/context-documents/tree",
            body=maybe_transform(
                {
                    "sources": sources,
                    "user_id": user_id,
                    "workstream_name": workstream_name,
                },
                tree_generate_params.TreeGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreeGenerateResponse,
        )

    def get(
        self,
        tree_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreeGetResponse:
        """
        Fetch a specific tree by its tree ID instead of selecting the latest one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tree_id:
            raise ValueError(f"Expected a non-empty value for `tree_id` but received {tree_id!r}")
        return self._get(
            path_template("/context-documents/tree/by-id/{tree_id}", tree_id=tree_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreeGetResponse,
        )

    def get_latest(
        self,
        *,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreeGetLatestResponse:
        """
        Get the most recent context document tree for the authenticated app.

        By default, the endpoint returns the latest ready tree. Readiness depends on
        whether the app has `require_review` enabled:

        - `require_review=False` (default): return the latest completed tree.
        - `require_review=True`: return the latest published tree.

        `status` filters to a specific status (case-insensitive). When no ready tree
        exists yet, the endpoint returns the newest available generation state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/context-documents/tree/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, tree_get_latest_params.TreeGetLatestParams),
            ),
            cast_to=TreeGetLatestResponse,
        )

    def progress(
        self,
        tree_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreeProgressResponse:
        """
        Return the generation progress for a single tree.

        Active generations include phase and counter data. Completed generations, and
        generations without detailed progress data, return status only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tree_id:
            raise ValueError(f"Expected a non-empty value for `tree_id` but received {tree_id!r}")
        return self._get(
            path_template("/context-documents/tree/{tree_id}/progress", tree_id=tree_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreeProgressResponse,
        )


class AsyncTreesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTreesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTreesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTreesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncTreesResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        sources: Optional[SequenceNotStr[str]] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        workstream_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreeGenerateResponse:
        """
        Generate a three-tier context document tree for local push delivery.

        Creates company, workstream, and personal context documents from the app's
        synced data. Returns immediately with a tree ID; use
        `GET /context-documents/tree/latest` to retrieve the result.

        Args:
          sources: Integration sources to include (e.g., ['gmail', 'slack']). Defaults to all.

          user_id: User ID for personal tier scoping. When set, personal/context.md is generated
              from this user's data only. Company and workstream tiers still use all data.

          workstream_name: Generate docs for this workstream only (skip auto-detection).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/context-documents/tree",
            body=await async_maybe_transform(
                {
                    "sources": sources,
                    "user_id": user_id,
                    "workstream_name": workstream_name,
                },
                tree_generate_params.TreeGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreeGenerateResponse,
        )

    async def get(
        self,
        tree_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreeGetResponse:
        """
        Fetch a specific tree by its tree ID instead of selecting the latest one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tree_id:
            raise ValueError(f"Expected a non-empty value for `tree_id` but received {tree_id!r}")
        return await self._get(
            path_template("/context-documents/tree/by-id/{tree_id}", tree_id=tree_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreeGetResponse,
        )

    async def get_latest(
        self,
        *,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreeGetLatestResponse:
        """
        Get the most recent context document tree for the authenticated app.

        By default, the endpoint returns the latest ready tree. Readiness depends on
        whether the app has `require_review` enabled:

        - `require_review=False` (default): return the latest completed tree.
        - `require_review=True`: return the latest published tree.

        `status` filters to a specific status (case-insensitive). When no ready tree
        exists yet, the endpoint returns the newest available generation state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/context-documents/tree/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, tree_get_latest_params.TreeGetLatestParams),
            ),
            cast_to=TreeGetLatestResponse,
        )

    async def progress(
        self,
        tree_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreeProgressResponse:
        """
        Return the generation progress for a single tree.

        Active generations include phase and counter data. Completed generations, and
        generations without detailed progress data, return status only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tree_id:
            raise ValueError(f"Expected a non-empty value for `tree_id` but received {tree_id!r}")
        return await self._get(
            path_template("/context-documents/tree/{tree_id}/progress", tree_id=tree_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreeProgressResponse,
        )


class TreesResourceWithRawResponse:
    def __init__(self, trees: TreesResource) -> None:
        self._trees = trees

        self.generate = to_raw_response_wrapper(
            trees.generate,
        )
        self.get = to_raw_response_wrapper(
            trees.get,
        )
        self.get_latest = to_raw_response_wrapper(
            trees.get_latest,
        )
        self.progress = to_raw_response_wrapper(
            trees.progress,
        )


class AsyncTreesResourceWithRawResponse:
    def __init__(self, trees: AsyncTreesResource) -> None:
        self._trees = trees

        self.generate = async_to_raw_response_wrapper(
            trees.generate,
        )
        self.get = async_to_raw_response_wrapper(
            trees.get,
        )
        self.get_latest = async_to_raw_response_wrapper(
            trees.get_latest,
        )
        self.progress = async_to_raw_response_wrapper(
            trees.progress,
        )


class TreesResourceWithStreamingResponse:
    def __init__(self, trees: TreesResource) -> None:
        self._trees = trees

        self.generate = to_streamed_response_wrapper(
            trees.generate,
        )
        self.get = to_streamed_response_wrapper(
            trees.get,
        )
        self.get_latest = to_streamed_response_wrapper(
            trees.get_latest,
        )
        self.progress = to_streamed_response_wrapper(
            trees.progress,
        )


class AsyncTreesResourceWithStreamingResponse:
    def __init__(self, trees: AsyncTreesResource) -> None:
        self._trees = trees

        self.generate = async_to_streamed_response_wrapper(
            trees.generate,
        )
        self.get = async_to_streamed_response_wrapper(
            trees.get,
        )
        self.get_latest = async_to_streamed_response_wrapper(
            trees.get_latest,
        )
        self.progress = async_to_streamed_response_wrapper(
            trees.progress,
        )
