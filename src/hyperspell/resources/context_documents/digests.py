# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.context_documents import digest_list_params, digest_generate_params
from ...types.context_documents.digest_list_response import DigestListResponse
from ...types.context_documents.digest_generate_response import DigestGenerateResponse

__all__ = ["DigestsResource", "AsyncDigestsResource"]


class DigestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DigestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return DigestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DigestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return DigestsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        period: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DigestListResponse:
        """
        List recent digest summaries, newest first.

        Filter by cadence with `period=daily` or `period=weekly`. Fetch full content
        with `GET /context-documents/tree/by-id/{tree_id}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/context-documents/digest/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "period": period,
                    },
                    digest_list_params.DigestListParams,
                ),
            ),
            cast_to=DigestListResponse,
        )

    def generate(
        self,
        *,
        period: str | Omit = omit,
        sources: Optional[SequenceNotStr[str]] | Omit = omit,
        window_end: Union[str, datetime, None] | Omit = omit,
        window_start: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DigestGenerateResponse:
        """
        Generate a date-windowed "what the company did today" digest.

        Returns immediately with a tree ID. Poll
        `GET /context-documents/tree/{tree_id}/progress` for completion or fetch the
        result with `GET /context-documents/tree/by-id/{tree_id}`.

        Args:
          period: Digest cadence: 'daily' or 'weekly'. Sets the default window when none is given.

          sources: Integration sources to include (e.g., ['slack', 'github']). Defaults to all.

          window_end: Exclusive upper bound of the digest window. Defaults to now.

          window_start: Inclusive lower bound of the digest window. Defaults to midnight UTC today
              (paired with window_end=now) when omitted. Both bounds must be supplied
              together.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/context-documents/digest",
            body=maybe_transform(
                {
                    "period": period,
                    "sources": sources,
                    "window_end": window_end,
                    "window_start": window_start,
                },
                digest_generate_params.DigestGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigestGenerateResponse,
        )


class AsyncDigestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDigestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDigestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDigestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncDigestsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        period: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DigestListResponse:
        """
        List recent digest summaries, newest first.

        Filter by cadence with `period=daily` or `period=weekly`. Fetch full content
        with `GET /context-documents/tree/by-id/{tree_id}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/context-documents/digest/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "period": period,
                    },
                    digest_list_params.DigestListParams,
                ),
            ),
            cast_to=DigestListResponse,
        )

    async def generate(
        self,
        *,
        period: str | Omit = omit,
        sources: Optional[SequenceNotStr[str]] | Omit = omit,
        window_end: Union[str, datetime, None] | Omit = omit,
        window_start: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DigestGenerateResponse:
        """
        Generate a date-windowed "what the company did today" digest.

        Returns immediately with a tree ID. Poll
        `GET /context-documents/tree/{tree_id}/progress` for completion or fetch the
        result with `GET /context-documents/tree/by-id/{tree_id}`.

        Args:
          period: Digest cadence: 'daily' or 'weekly'. Sets the default window when none is given.

          sources: Integration sources to include (e.g., ['slack', 'github']). Defaults to all.

          window_end: Exclusive upper bound of the digest window. Defaults to now.

          window_start: Inclusive lower bound of the digest window. Defaults to midnight UTC today
              (paired with window_end=now) when omitted. Both bounds must be supplied
              together.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/context-documents/digest",
            body=await async_maybe_transform(
                {
                    "period": period,
                    "sources": sources,
                    "window_end": window_end,
                    "window_start": window_start,
                },
                digest_generate_params.DigestGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigestGenerateResponse,
        )


class DigestsResourceWithRawResponse:
    def __init__(self, digests: DigestsResource) -> None:
        self._digests = digests

        self.list = to_raw_response_wrapper(
            digests.list,
        )
        self.generate = to_raw_response_wrapper(
            digests.generate,
        )


class AsyncDigestsResourceWithRawResponse:
    def __init__(self, digests: AsyncDigestsResource) -> None:
        self._digests = digests

        self.list = async_to_raw_response_wrapper(
            digests.list,
        )
        self.generate = async_to_raw_response_wrapper(
            digests.generate,
        )


class DigestsResourceWithStreamingResponse:
    def __init__(self, digests: DigestsResource) -> None:
        self._digests = digests

        self.list = to_streamed_response_wrapper(
            digests.list,
        )
        self.generate = to_streamed_response_wrapper(
            digests.generate,
        )


class AsyncDigestsResourceWithStreamingResponse:
    def __init__(self, digests: AsyncDigestsResource) -> None:
        self._digests = digests

        self.list = async_to_streamed_response_wrapper(
            digests.list,
        )
        self.generate = async_to_streamed_response_wrapper(
            digests.generate,
        )
