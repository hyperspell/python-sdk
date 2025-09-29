# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import evaluate_score_query_params, evaluate_score_highlight_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.shared.query_result import QueryResult
from ..types.evaluate_score_query_response import EvaluateScoreQueryResponse
from ..types.evaluate_score_highlight_response import EvaluateScoreHighlightResponse

__all__ = ["EvaluateResource", "AsyncEvaluateResource"]


class EvaluateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return EvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return EvaluateResourceWithStreamingResponse(self)

    def get_query(
        self,
        query_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryResult:
        """
        Retrieve the result of a previous query.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not query_id:
            raise ValueError(f"Expected a non-empty value for `query_id` but received {query_id!r}")
        return self._get(
            f"/evaluate/query/{query_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryResult,
        )

    def score_highlight(
        self,
        highlight_id: str,
        *,
        comment: Optional[str] | Omit = omit,
        score: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateScoreHighlightResponse:
        """
        Score an individual highlight.

        Args:
          comment: Comment on the chunk

          score: Rating of the chunk from -1 (bad) to +1 (good).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not highlight_id:
            raise ValueError(f"Expected a non-empty value for `highlight_id` but received {highlight_id!r}")
        return self._post(
            f"/evaluate/highlight/{highlight_id}",
            body=maybe_transform(
                {
                    "comment": comment,
                    "score": score,
                },
                evaluate_score_highlight_params.EvaluateScoreHighlightParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateScoreHighlightResponse,
        )

    def score_query(
        self,
        query_id: str,
        *,
        score: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateScoreQueryResponse:
        """
        Score the result of a query.

        Args:
          score: Rating of the query result from -1 (bad) to +1 (good).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not query_id:
            raise ValueError(f"Expected a non-empty value for `query_id` but received {query_id!r}")
        return self._post(
            f"/evaluate/query/{query_id}",
            body=maybe_transform({"score": score}, evaluate_score_query_params.EvaluateScoreQueryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateScoreQueryResponse,
        )


class AsyncEvaluateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncEvaluateResourceWithStreamingResponse(self)

    async def get_query(
        self,
        query_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryResult:
        """
        Retrieve the result of a previous query.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not query_id:
            raise ValueError(f"Expected a non-empty value for `query_id` but received {query_id!r}")
        return await self._get(
            f"/evaluate/query/{query_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryResult,
        )

    async def score_highlight(
        self,
        highlight_id: str,
        *,
        comment: Optional[str] | Omit = omit,
        score: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateScoreHighlightResponse:
        """
        Score an individual highlight.

        Args:
          comment: Comment on the chunk

          score: Rating of the chunk from -1 (bad) to +1 (good).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not highlight_id:
            raise ValueError(f"Expected a non-empty value for `highlight_id` but received {highlight_id!r}")
        return await self._post(
            f"/evaluate/highlight/{highlight_id}",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "score": score,
                },
                evaluate_score_highlight_params.EvaluateScoreHighlightParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateScoreHighlightResponse,
        )

    async def score_query(
        self,
        query_id: str,
        *,
        score: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateScoreQueryResponse:
        """
        Score the result of a query.

        Args:
          score: Rating of the query result from -1 (bad) to +1 (good).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not query_id:
            raise ValueError(f"Expected a non-empty value for `query_id` but received {query_id!r}")
        return await self._post(
            f"/evaluate/query/{query_id}",
            body=await async_maybe_transform({"score": score}, evaluate_score_query_params.EvaluateScoreQueryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateScoreQueryResponse,
        )


class EvaluateResourceWithRawResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.get_query = to_raw_response_wrapper(
            evaluate.get_query,
        )
        self.score_highlight = to_raw_response_wrapper(
            evaluate.score_highlight,
        )
        self.score_query = to_raw_response_wrapper(
            evaluate.score_query,
        )


class AsyncEvaluateResourceWithRawResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.get_query = async_to_raw_response_wrapper(
            evaluate.get_query,
        )
        self.score_highlight = async_to_raw_response_wrapper(
            evaluate.score_highlight,
        )
        self.score_query = async_to_raw_response_wrapper(
            evaluate.score_query,
        )


class EvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.get_query = to_streamed_response_wrapper(
            evaluate.get_query,
        )
        self.score_highlight = to_streamed_response_wrapper(
            evaluate.score_highlight,
        )
        self.score_query = to_streamed_response_wrapper(
            evaluate.score_query,
        )


class AsyncEvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.get_query = async_to_streamed_response_wrapper(
            evaluate.get_query,
        )
        self.score_highlight = async_to_streamed_response_wrapper(
            evaluate.score_highlight,
        )
        self.score_query = async_to_streamed_response_wrapper(
            evaluate.score_query,
        )
