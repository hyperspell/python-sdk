# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import session_add_params
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
from ..types.memory_status import MemoryStatus

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def add(
        self,
        *,
        history: str,
        date: Union[str, datetime] | Omit = omit,
        extract: List[Literal["procedure", "memory", "mood"]] | Omit = omit,
        format: Optional[Literal["vercel", "hyperdoc", "openclaw"]] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        session_id: str | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatus:
        """
        Add an agent trace/transcript to the index.

        Accepts traces as a string in Hyperdoc format (native), Vercel AI SDK format, or
        OpenClaw JSONL format. The format is auto-detected if not specified.

        **Hyperdoc format** (JSON array, snake_case with type discriminators):

        ```json
        {
          "history": "[{\"type\": \"trace_message\", \"role\": \"user\", \"text\": \"Hello\"}]"
        }
        ```

        **Vercel AI SDK format** (JSON array, camelCase):

        ```json
        { "history": "[{\"role\": \"user\", \"content\": \"Hello\"}]" }
        ```

        **OpenClaw JSONL format** (newline-delimited JSON):

        ```json
        {
          "history": "{\"type\":\"session\",\"id\":\"abc\"}\n{\"type\":\"message\",\"message\":{\"role\":\"user\",...}}"
        }
        ```

        Args:
          history: The trace history as a string. Can be a JSON array of Hyperdoc steps, a JSON
              array of Vercel AI SDK steps, or OpenClaw JSONL.

          date: Date of the trace

          extract: What kind of memories to extract from the trace

          format: Trace format: 'vercel', 'hyperdoc', or 'openclaw'. Auto-detected if not set.

          metadata: Custom metadata for filtering. Keys must be alphanumeric with underscores, max
              64 chars.

          session_id: Resource identifier for the trace.

          title: Title of the trace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/trace/add",
            body=maybe_transform(
                {
                    "history": history,
                    "date": date,
                    "extract": extract,
                    "format": format,
                    "metadata": metadata,
                    "session_id": session_id,
                    "title": title,
                },
                session_add_params.SessionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatus,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def add(
        self,
        *,
        history: str,
        date: Union[str, datetime] | Omit = omit,
        extract: List[Literal["procedure", "memory", "mood"]] | Omit = omit,
        format: Optional[Literal["vercel", "hyperdoc", "openclaw"]] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        session_id: str | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatus:
        """
        Add an agent trace/transcript to the index.

        Accepts traces as a string in Hyperdoc format (native), Vercel AI SDK format, or
        OpenClaw JSONL format. The format is auto-detected if not specified.

        **Hyperdoc format** (JSON array, snake_case with type discriminators):

        ```json
        {
          "history": "[{\"type\": \"trace_message\", \"role\": \"user\", \"text\": \"Hello\"}]"
        }
        ```

        **Vercel AI SDK format** (JSON array, camelCase):

        ```json
        { "history": "[{\"role\": \"user\", \"content\": \"Hello\"}]" }
        ```

        **OpenClaw JSONL format** (newline-delimited JSON):

        ```json
        {
          "history": "{\"type\":\"session\",\"id\":\"abc\"}\n{\"type\":\"message\",\"message\":{\"role\":\"user\",...}}"
        }
        ```

        Args:
          history: The trace history as a string. Can be a JSON array of Hyperdoc steps, a JSON
              array of Vercel AI SDK steps, or OpenClaw JSONL.

          date: Date of the trace

          extract: What kind of memories to extract from the trace

          format: Trace format: 'vercel', 'hyperdoc', or 'openclaw'. Auto-detected if not set.

          metadata: Custom metadata for filtering. Keys must be alphanumeric with underscores, max
              64 chars.

          session_id: Resource identifier for the trace.

          title: Title of the trace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/trace/add",
            body=await async_maybe_transform(
                {
                    "history": history,
                    "date": date,
                    "extract": extract,
                    "format": format,
                    "metadata": metadata,
                    "session_id": session_id,
                    "title": title,
                },
                session_add_params.SessionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatus,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.add = to_raw_response_wrapper(
            sessions.add,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.add = async_to_raw_response_wrapper(
            sessions.add,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.add = to_streamed_response_wrapper(
            sessions.add,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.add = async_to_streamed_response_wrapper(
            sessions.add,
        )
