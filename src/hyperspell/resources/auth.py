# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import auth_user_token_params
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
from ..types.token import Token
from .._base_client import make_request_options
from ..types.auth_me_response import AuthMeResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthMeResponse:
        """Endpoint to get basic user data."""
        return self._get(
            "/auth/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthMeResponse,
        )

    def user_token(
        self,
        *,
        user_id: str,
        expires_in: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Token:
        """Use this endpoint to create a user token for a specific user.

        This token can be
        safely passed to your user-facing front-end.

        Args:
          expires_in: Token lifetime, e.g., '30m', '2h', '1d'. Defaults to 24 hours if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/user_token",
            body=maybe_transform(
                {
                    "user_id": user_id,
                    "expires_in": expires_in,
                },
                auth_user_token_params.AuthUserTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Token,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthMeResponse:
        """Endpoint to get basic user data."""
        return await self._get(
            "/auth/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthMeResponse,
        )

    async def user_token(
        self,
        *,
        user_id: str,
        expires_in: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Token:
        """Use this endpoint to create a user token for a specific user.

        This token can be
        safely passed to your user-facing front-end.

        Args:
          expires_in: Token lifetime, e.g., '30m', '2h', '1d'. Defaults to 24 hours if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/user_token",
            body=await async_maybe_transform(
                {
                    "user_id": user_id,
                    "expires_in": expires_in,
                },
                auth_user_token_params.AuthUserTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Token,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.me = to_raw_response_wrapper(
            auth.me,
        )
        self.user_token = to_raw_response_wrapper(
            auth.user_token,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.me = async_to_raw_response_wrapper(
            auth.me,
        )
        self.user_token = async_to_raw_response_wrapper(
            auth.user_token,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.me = to_streamed_response_wrapper(
            auth.me,
        )
        self.user_token = to_streamed_response_wrapper(
            auth.user_token,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.me = async_to_streamed_response_wrapper(
            auth.me,
        )
        self.user_token = async_to_streamed_response_wrapper(
            auth.user_token,
        )
