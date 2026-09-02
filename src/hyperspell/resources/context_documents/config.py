# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.context_documents import config_update_params
from ...types.context_documents.config_get_response import ConfigGetResponse
from ...types.context_documents.config_reset_response import ConfigResetResponse
from ...types.context_documents.config_update_response import ConfigUpdateResponse

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        company_prompts: Optional[Dict[str, str]] | Omit = omit,
        detection_prompt: Optional[str] | Omit = omit,
        domain: Optional[str] | Omit = omit,
        personal_prompt: Optional[str] | Omit = omit,
        source_weights: Optional[Dict[str, str]] | Omit = omit,
        structure: Optional[config_update_params.Structure] | Omit = omit,
        workstream_prompts: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateResponse:
        """Update the supplied generation settings.

        Changes apply to the next generation.

        This endpoint does not start a generation
        or modify existing context documents.

        Args:
          structure: Per-tier document definitions for custom generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/context-documents/config",
            body=maybe_transform(
                {
                    "company_prompts": company_prompts,
                    "detection_prompt": detection_prompt,
                    "domain": domain,
                    "personal_prompt": personal_prompt,
                    "source_weights": source_weights,
                    "structure": structure,
                    "workstream_prompts": workstream_prompts,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigGetResponse:
        """Read the customer-editable generation config for the authenticated app."""
        return self._get(
            "/context-documents/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigGetResponse,
        )

    def reset(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigResetResponse:
        """
        Reset customer-editable generation settings to their defaults.

        Existing context documents remain unchanged. `detected_domain` is retained and
        used for future generations unless a new domain override is set.
        """
        return self._post(
            "/context-documents/config/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigResetResponse,
        )


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        company_prompts: Optional[Dict[str, str]] | Omit = omit,
        detection_prompt: Optional[str] | Omit = omit,
        domain: Optional[str] | Omit = omit,
        personal_prompt: Optional[str] | Omit = omit,
        source_weights: Optional[Dict[str, str]] | Omit = omit,
        structure: Optional[config_update_params.Structure] | Omit = omit,
        workstream_prompts: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateResponse:
        """Update the supplied generation settings.

        Changes apply to the next generation.

        This endpoint does not start a generation
        or modify existing context documents.

        Args:
          structure: Per-tier document definitions for custom generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/context-documents/config",
            body=await async_maybe_transform(
                {
                    "company_prompts": company_prompts,
                    "detection_prompt": detection_prompt,
                    "domain": domain,
                    "personal_prompt": personal_prompt,
                    "source_weights": source_weights,
                    "structure": structure,
                    "workstream_prompts": workstream_prompts,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigGetResponse:
        """Read the customer-editable generation config for the authenticated app."""
        return await self._get(
            "/context-documents/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigGetResponse,
        )

    async def reset(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigResetResponse:
        """
        Reset customer-editable generation settings to their defaults.

        Existing context documents remain unchanged. `detected_domain` is retained and
        used for future generations unless a new domain override is set.
        """
        return await self._post(
            "/context-documents/config/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigResetResponse,
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.update = to_raw_response_wrapper(
            config.update,
        )
        self.get = to_raw_response_wrapper(
            config.get,
        )
        self.reset = to_raw_response_wrapper(
            config.reset,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.update = async_to_raw_response_wrapper(
            config.update,
        )
        self.get = async_to_raw_response_wrapper(
            config.get,
        )
        self.reset = async_to_raw_response_wrapper(
            config.reset,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.update = to_streamed_response_wrapper(
            config.update,
        )
        self.get = to_streamed_response_wrapper(
            config.get,
        )
        self.reset = to_streamed_response_wrapper(
            config.reset,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
        self.get = async_to_streamed_response_wrapper(
            config.get,
        )
        self.reset = async_to_streamed_response_wrapper(
            config.reset,
        )
