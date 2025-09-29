# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.integrations import slack_list_params

__all__ = ["SlackResource", "AsyncSlackResource"]


class SlackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SlackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return SlackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SlackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return SlackResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        channels: SequenceNotStr[str] | Omit = omit,
        exclude_archived: Optional[bool] | Omit = omit,
        include_dms: bool | Omit = omit,
        include_group_dms: bool | Omit = omit,
        include_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        List Slack conversations accessible to the user via the live Nango connection.

        Returns minimal channel metadata suitable for selection UIs. If required scopes
        are missing, Slack's error is propagated with details.

        Supports filtering by channels, including/excluding private channels, DMs, group
        DMs, and archived channels based on the provided search options.

        Args:
          channels: List of Slack channels to include (by id, name, or #name).

          exclude_archived: If set, pass 'exclude_archived' to Slack. If None, omit the param.

          include_dms: Include direct messages (im) when listing conversations.

          include_group_dms: Include group DMs (mpim) when listing conversations.

          include_private: Include private channels when constructing Slack 'types'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/integrations/slack/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channels": channels,
                        "exclude_archived": exclude_archived,
                        "include_dms": include_dms,
                        "include_group_dms": include_group_dms,
                        "include_private": include_private,
                    },
                    slack_list_params.SlackListParams,
                ),
            ),
            cast_to=object,
        )


class AsyncSlackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSlackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSlackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSlackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncSlackResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        channels: SequenceNotStr[str] | Omit = omit,
        exclude_archived: Optional[bool] | Omit = omit,
        include_dms: bool | Omit = omit,
        include_group_dms: bool | Omit = omit,
        include_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        List Slack conversations accessible to the user via the live Nango connection.

        Returns minimal channel metadata suitable for selection UIs. If required scopes
        are missing, Slack's error is propagated with details.

        Supports filtering by channels, including/excluding private channels, DMs, group
        DMs, and archived channels based on the provided search options.

        Args:
          channels: List of Slack channels to include (by id, name, or #name).

          exclude_archived: If set, pass 'exclude_archived' to Slack. If None, omit the param.

          include_dms: Include direct messages (im) when listing conversations.

          include_group_dms: Include group DMs (mpim) when listing conversations.

          include_private: Include private channels when constructing Slack 'types'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/integrations/slack/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channels": channels,
                        "exclude_archived": exclude_archived,
                        "include_dms": include_dms,
                        "include_group_dms": include_group_dms,
                        "include_private": include_private,
                    },
                    slack_list_params.SlackListParams,
                ),
            ),
            cast_to=object,
        )


class SlackResourceWithRawResponse:
    def __init__(self, slack: SlackResource) -> None:
        self._slack = slack

        self.list = to_raw_response_wrapper(
            slack.list,
        )


class AsyncSlackResourceWithRawResponse:
    def __init__(self, slack: AsyncSlackResource) -> None:
        self._slack = slack

        self.list = async_to_raw_response_wrapper(
            slack.list,
        )


class SlackResourceWithStreamingResponse:
    def __init__(self, slack: SlackResource) -> None:
        self._slack = slack

        self.list = to_streamed_response_wrapper(
            slack.list,
        )


class AsyncSlackResourceWithStreamingResponse:
    def __init__(self, slack: AsyncSlackResource) -> None:
        self._slack = slack

        self.list = async_to_streamed_response_wrapper(
            slack.list,
        )
