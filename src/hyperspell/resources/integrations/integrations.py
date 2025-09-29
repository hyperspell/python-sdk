# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .slack import (
    SlackResource,
    AsyncSlackResource,
    SlackResourceWithRawResponse,
    AsyncSlackResourceWithRawResponse,
    SlackResourceWithStreamingResponse,
    AsyncSlackResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .web_crawler import (
    WebCrawlerResource,
    AsyncWebCrawlerResource,
    WebCrawlerResourceWithRawResponse,
    AsyncWebCrawlerResourceWithRawResponse,
    WebCrawlerResourceWithStreamingResponse,
    AsyncWebCrawlerResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .google_calendar import (
    GoogleCalendarResource,
    AsyncGoogleCalendarResource,
    GoogleCalendarResourceWithRawResponse,
    AsyncGoogleCalendarResourceWithRawResponse,
    GoogleCalendarResourceWithStreamingResponse,
    AsyncGoogleCalendarResourceWithStreamingResponse,
)
from ...types.integration_revoke_response import IntegrationRevokeResponse

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def google_calendar(self) -> GoogleCalendarResource:
        return GoogleCalendarResource(self._client)

    @cached_property
    def web_crawler(self) -> WebCrawlerResource:
        return WebCrawlerResource(self._client)

    @cached_property
    def slack(self) -> SlackResource:
        return SlackResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return IntegrationsResourceWithStreamingResponse(self)

    def revoke(
        self,
        provider: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationRevokeResponse:
        """
        Revokes Hyperspell's access the given provider and deletes all stored
        credentials and indexed data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._get(
            f"/integrations/{provider}/revoke",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationRevokeResponse,
        )


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def google_calendar(self) -> AsyncGoogleCalendarResource:
        return AsyncGoogleCalendarResource(self._client)

    @cached_property
    def web_crawler(self) -> AsyncWebCrawlerResource:
        return AsyncWebCrawlerResource(self._client)

    @cached_property
    def slack(self) -> AsyncSlackResource:
        return AsyncSlackResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def revoke(
        self,
        provider: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationRevokeResponse:
        """
        Revokes Hyperspell's access the given provider and deletes all stored
        credentials and indexed data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._get(
            f"/integrations/{provider}/revoke",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationRevokeResponse,
        )


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.revoke = to_raw_response_wrapper(
            integrations.revoke,
        )

    @cached_property
    def google_calendar(self) -> GoogleCalendarResourceWithRawResponse:
        return GoogleCalendarResourceWithRawResponse(self._integrations.google_calendar)

    @cached_property
    def web_crawler(self) -> WebCrawlerResourceWithRawResponse:
        return WebCrawlerResourceWithRawResponse(self._integrations.web_crawler)

    @cached_property
    def slack(self) -> SlackResourceWithRawResponse:
        return SlackResourceWithRawResponse(self._integrations.slack)


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.revoke = async_to_raw_response_wrapper(
            integrations.revoke,
        )

    @cached_property
    def google_calendar(self) -> AsyncGoogleCalendarResourceWithRawResponse:
        return AsyncGoogleCalendarResourceWithRawResponse(self._integrations.google_calendar)

    @cached_property
    def web_crawler(self) -> AsyncWebCrawlerResourceWithRawResponse:
        return AsyncWebCrawlerResourceWithRawResponse(self._integrations.web_crawler)

    @cached_property
    def slack(self) -> AsyncSlackResourceWithRawResponse:
        return AsyncSlackResourceWithRawResponse(self._integrations.slack)


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.revoke = to_streamed_response_wrapper(
            integrations.revoke,
        )

    @cached_property
    def google_calendar(self) -> GoogleCalendarResourceWithStreamingResponse:
        return GoogleCalendarResourceWithStreamingResponse(self._integrations.google_calendar)

    @cached_property
    def web_crawler(self) -> WebCrawlerResourceWithStreamingResponse:
        return WebCrawlerResourceWithStreamingResponse(self._integrations.web_crawler)

    @cached_property
    def slack(self) -> SlackResourceWithStreamingResponse:
        return SlackResourceWithStreamingResponse(self._integrations.slack)


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.revoke = async_to_streamed_response_wrapper(
            integrations.revoke,
        )

    @cached_property
    def google_calendar(self) -> AsyncGoogleCalendarResourceWithStreamingResponse:
        return AsyncGoogleCalendarResourceWithStreamingResponse(self._integrations.google_calendar)

    @cached_property
    def web_crawler(self) -> AsyncWebCrawlerResourceWithStreamingResponse:
        return AsyncWebCrawlerResourceWithStreamingResponse(self._integrations.web_crawler)

    @cached_property
    def slack(self) -> AsyncSlackResourceWithStreamingResponse:
        return AsyncSlackResourceWithStreamingResponse(self._integrations.slack)
