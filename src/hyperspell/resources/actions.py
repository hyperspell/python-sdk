# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import action_add_reaction_params, action_send_message_params
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
from ..types.action_add_reaction_response import ActionAddReactionResponse
from ..types.action_send_message_response import ActionSendMessageResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def add_reaction(
        self,
        *,
        channel: str,
        name: str,
        provider: Literal["slack"],
        timestamp: str,
        connection: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAddReactionResponse:
        """
        Add an emoji reaction to a message on a connected integration.

        Args:
          channel: Channel ID containing the message

          name: Emoji name without colons (e.g., thumbsup)

          provider: Integration provider.

          timestamp: Message timestamp to react to

          connection: Connection ID. If omitted, auto-resolved from provider + user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/actions/add_reaction",
            body=maybe_transform(
                {
                    "channel": channel,
                    "name": name,
                    "provider": provider,
                    "timestamp": timestamp,
                    "connection": connection,
                },
                action_add_reaction_params.ActionAddReactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddReactionResponse,
        )

    def send_message(
        self,
        *,
        provider: Literal["slack"],
        text: str,
        channel: Optional[str] | Omit = omit,
        connection: Optional[str] | Omit = omit,
        parent: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionSendMessageResponse:
        """
        Send a message to a channel or conversation on a connected integration.

        Args:
          provider: Integration provider.

          text: Message text

          channel: Channel ID (required for Slack)

          connection: Connection ID. If omitted, auto-resolved from provider + user.

          parent: Parent message ID for threading (thread_ts for Slack)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/actions/send_message",
            body=maybe_transform(
                {
                    "provider": provider,
                    "text": text,
                    "channel": channel,
                    "connection": connection,
                    "parent": parent,
                },
                action_send_message_params.ActionSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSendMessageResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def add_reaction(
        self,
        *,
        channel: str,
        name: str,
        provider: Literal["slack"],
        timestamp: str,
        connection: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAddReactionResponse:
        """
        Add an emoji reaction to a message on a connected integration.

        Args:
          channel: Channel ID containing the message

          name: Emoji name without colons (e.g., thumbsup)

          provider: Integration provider.

          timestamp: Message timestamp to react to

          connection: Connection ID. If omitted, auto-resolved from provider + user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/actions/add_reaction",
            body=await async_maybe_transform(
                {
                    "channel": channel,
                    "name": name,
                    "provider": provider,
                    "timestamp": timestamp,
                    "connection": connection,
                },
                action_add_reaction_params.ActionAddReactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddReactionResponse,
        )

    async def send_message(
        self,
        *,
        provider: Literal["slack"],
        text: str,
        channel: Optional[str] | Omit = omit,
        connection: Optional[str] | Omit = omit,
        parent: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionSendMessageResponse:
        """
        Send a message to a channel or conversation on a connected integration.

        Args:
          provider: Integration provider.

          text: Message text

          channel: Channel ID (required for Slack)

          connection: Connection ID. If omitted, auto-resolved from provider + user.

          parent: Parent message ID for threading (thread_ts for Slack)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/actions/send_message",
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "text": text,
                    "channel": channel,
                    "connection": connection,
                    "parent": parent,
                },
                action_send_message_params.ActionSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSendMessageResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.add_reaction = to_raw_response_wrapper(
            actions.add_reaction,
        )
        self.send_message = to_raw_response_wrapper(
            actions.send_message,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.add_reaction = async_to_raw_response_wrapper(
            actions.add_reaction,
        )
        self.send_message = async_to_raw_response_wrapper(
            actions.send_message,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.add_reaction = to_streamed_response_wrapper(
            actions.add_reaction,
        )
        self.send_message = to_streamed_response_wrapper(
            actions.send_message,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.add_reaction = async_to_streamed_response_wrapper(
            actions.add_reaction,
        )
        self.send_message = async_to_streamed_response_wrapper(
            actions.send_message,
        )
