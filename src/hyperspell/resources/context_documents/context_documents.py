# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .trees import (
    TreesResource,
    AsyncTreesResource,
    TreesResourceWithRawResponse,
    AsyncTreesResourceWithRawResponse,
    TreesResourceWithStreamingResponse,
    AsyncTreesResourceWithStreamingResponse,
)
from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from ...types import context_document_list_params, context_document_generate_params
from .digests import (
    DigestsResource,
    AsyncDigestsResource,
    DigestsResourceWithRawResponse,
    AsyncDigestsResourceWithRawResponse,
    DigestsResourceWithStreamingResponse,
    AsyncDigestsResourceWithStreamingResponse,
)
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
from ...pagination import SyncContextDocumentsCursorPage, AsyncContextDocumentsCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.context_document_get_response import ContextDocumentGetResponse
from ...types.context_document_list_response import ContextDocumentListResponse
from ...types.context_document_generate_response import ContextDocumentGenerateResponse

__all__ = ["ContextDocumentsResource", "AsyncContextDocumentsResource"]


class ContextDocumentsResource(SyncAPIResource):
    @cached_property
    def trees(self) -> TreesResource:
        return TreesResource(self._client)

    @cached_property
    def digests(self) -> DigestsResource:
        return DigestsResource(self._client)

    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContextDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ContextDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return ContextDocumentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[Literal["processing", "completed", "failed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncContextDocumentsCursorPage[ContextDocumentListResponse]:
        """
        List context documents for the authenticated app, most recent first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/context-documents",
            page=SyncContextDocumentsCursorPage[ContextDocumentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    context_document_list_params.ContextDocumentListParams,
                ),
            ),
            model=ContextDocumentListResponse,
        )

    def generate(
        self,
        *,
        model: str | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        sources: Optional[SequenceNotStr[str]] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextDocumentGenerateResponse:
        """
        Generate an LLM-synthesized context document from the app's synced data.

        Generation runs asynchronously. The endpoint returns immediately with status
        `PROCESSING`; synthesis time depends on the amount of source data.

        Args:
          model: Model used for final synthesis.

          prompt: Custom prompt template. Replaces the standard summary prompt.

          sources: Integration sources to include (e.g., ['gmail', 'slack']). Defaults to all
              connected integrations.

          user_id: Scope generation to a specific user's data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/context-documents/generate",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "sources": sources,
                    "user_id": user_id,
                },
                context_document_generate_params.ContextDocumentGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextDocumentGenerateResponse,
        )

    def get(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextDocumentGetResponse:
        """
        Get a specific context document by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            path_template("/context-documents/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextDocumentGetResponse,
        )


class AsyncContextDocumentsResource(AsyncAPIResource):
    @cached_property
    def trees(self) -> AsyncTreesResource:
        return AsyncTreesResource(self._client)

    @cached_property
    def digests(self) -> AsyncDigestsResource:
        return AsyncDigestsResource(self._client)

    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContextDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncContextDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncContextDocumentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[Literal["processing", "completed", "failed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ContextDocumentListResponse, AsyncContextDocumentsCursorPage[ContextDocumentListResponse]]:
        """
        List context documents for the authenticated app, most recent first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/context-documents",
            page=AsyncContextDocumentsCursorPage[ContextDocumentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    context_document_list_params.ContextDocumentListParams,
                ),
            ),
            model=ContextDocumentListResponse,
        )

    async def generate(
        self,
        *,
        model: str | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        sources: Optional[SequenceNotStr[str]] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextDocumentGenerateResponse:
        """
        Generate an LLM-synthesized context document from the app's synced data.

        Generation runs asynchronously. The endpoint returns immediately with status
        `PROCESSING`; synthesis time depends on the amount of source data.

        Args:
          model: Model used for final synthesis.

          prompt: Custom prompt template. Replaces the standard summary prompt.

          sources: Integration sources to include (e.g., ['gmail', 'slack']). Defaults to all
              connected integrations.

          user_id: Scope generation to a specific user's data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/context-documents/generate",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "sources": sources,
                    "user_id": user_id,
                },
                context_document_generate_params.ContextDocumentGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextDocumentGenerateResponse,
        )

    async def get(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextDocumentGetResponse:
        """
        Get a specific context document by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            path_template("/context-documents/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextDocumentGetResponse,
        )


class ContextDocumentsResourceWithRawResponse:
    def __init__(self, context_documents: ContextDocumentsResource) -> None:
        self._context_documents = context_documents

        self.list = to_raw_response_wrapper(
            context_documents.list,
        )
        self.generate = to_raw_response_wrapper(
            context_documents.generate,
        )
        self.get = to_raw_response_wrapper(
            context_documents.get,
        )

    @cached_property
    def trees(self) -> TreesResourceWithRawResponse:
        return TreesResourceWithRawResponse(self._context_documents.trees)

    @cached_property
    def digests(self) -> DigestsResourceWithRawResponse:
        return DigestsResourceWithRawResponse(self._context_documents.digests)

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._context_documents.config)


class AsyncContextDocumentsResourceWithRawResponse:
    def __init__(self, context_documents: AsyncContextDocumentsResource) -> None:
        self._context_documents = context_documents

        self.list = async_to_raw_response_wrapper(
            context_documents.list,
        )
        self.generate = async_to_raw_response_wrapper(
            context_documents.generate,
        )
        self.get = async_to_raw_response_wrapper(
            context_documents.get,
        )

    @cached_property
    def trees(self) -> AsyncTreesResourceWithRawResponse:
        return AsyncTreesResourceWithRawResponse(self._context_documents.trees)

    @cached_property
    def digests(self) -> AsyncDigestsResourceWithRawResponse:
        return AsyncDigestsResourceWithRawResponse(self._context_documents.digests)

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._context_documents.config)


class ContextDocumentsResourceWithStreamingResponse:
    def __init__(self, context_documents: ContextDocumentsResource) -> None:
        self._context_documents = context_documents

        self.list = to_streamed_response_wrapper(
            context_documents.list,
        )
        self.generate = to_streamed_response_wrapper(
            context_documents.generate,
        )
        self.get = to_streamed_response_wrapper(
            context_documents.get,
        )

    @cached_property
    def trees(self) -> TreesResourceWithStreamingResponse:
        return TreesResourceWithStreamingResponse(self._context_documents.trees)

    @cached_property
    def digests(self) -> DigestsResourceWithStreamingResponse:
        return DigestsResourceWithStreamingResponse(self._context_documents.digests)

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._context_documents.config)


class AsyncContextDocumentsResourceWithStreamingResponse:
    def __init__(self, context_documents: AsyncContextDocumentsResource) -> None:
        self._context_documents = context_documents

        self.list = async_to_streamed_response_wrapper(
            context_documents.list,
        )
        self.generate = async_to_streamed_response_wrapper(
            context_documents.generate,
        )
        self.get = async_to_streamed_response_wrapper(
            context_documents.get,
        )

    @cached_property
    def trees(self) -> AsyncTreesResourceWithStreamingResponse:
        return AsyncTreesResourceWithStreamingResponse(self._context_documents.trees)

    @cached_property
    def digests(self) -> AsyncDigestsResourceWithStreamingResponse:
        return AsyncDigestsResourceWithStreamingResponse(self._context_documents.digests)

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._context_documents.config)
