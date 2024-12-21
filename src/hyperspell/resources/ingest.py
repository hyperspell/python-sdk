# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Mapping, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import ingest_add_params, ingest_file_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.ingest_add_response import IngestAddResponse

__all__ = ["IngestResource", "AsyncIngestResource"]


class IngestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IngestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return IngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IngestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return IngestResourceWithStreamingResponse(self)

    def add(
        self,
        *,
        date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, Union[str, float, bool, List[str], Iterable[int], Iterable[float], Iterable[bool]]]
        | NotGiven = NOT_GIVEN,
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        org_id: Optional[str] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["chat", "email", "generic", "transcript", "legal"] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        visibility: Literal["user", "org", "app", "system"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IngestAddResponse:
        """Add a document to the index.

        Args:
          date: Date of the document.

        Depending on the document, this could be the creation date
              or date the document was last updated (eg. for a chat transcript, this would be
              the date of the last message). This helps the ranking algorithm and allows you
              to filter by date range.

          metadata: Metadata to attach to the document. This can be used to store additional
              information about the document.

          namespace: Namespace to assign this document to. This can be for example a specific
              conversation that it is scoped to

          org_id: Organization ID to assign this document to.

          text: Full text of the document.

          title: Title of the document.

          type: Type of the document. This is optional, but helps with parsing the document.

          url: Source URL of the document. If text is not provided and URL is publicly
              accessible, Hyperspell will retrieve the document from this URL.

          user_id: User ID to assign this document to.

          visibility: Visibility of the document. If visibility is set to USER, then `user_id` must be
              present, and the document will only be visible to this user. If visibility is
              set to `org`, then `org_id` must be present and the document will be visible to
              all users in the same organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ingest",
            body=maybe_transform(
                {
                    "date": date,
                    "metadata": metadata,
                    "namespace": namespace,
                    "org_id": org_id,
                    "text": text,
                    "title": title,
                    "type": type,
                    "url": url,
                    "user_id": user_id,
                    "visibility": visibility,
                },
                ingest_add_params.IngestAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestAddResponse,
        )

    def file(
        self,
        *,
        data: ingest_file_params.Data,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Ingest File

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "data": data,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/ingest_file",
            body=maybe_transform(body, ingest_file_params.IngestFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncIngestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIngestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIngestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncIngestResourceWithStreamingResponse(self)

    async def add(
        self,
        *,
        date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, Union[str, float, bool, List[str], Iterable[int], Iterable[float], Iterable[bool]]]
        | NotGiven = NOT_GIVEN,
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        org_id: Optional[str] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["chat", "email", "generic", "transcript", "legal"] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        visibility: Literal["user", "org", "app", "system"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IngestAddResponse:
        """Add a document to the index.

        Args:
          date: Date of the document.

        Depending on the document, this could be the creation date
              or date the document was last updated (eg. for a chat transcript, this would be
              the date of the last message). This helps the ranking algorithm and allows you
              to filter by date range.

          metadata: Metadata to attach to the document. This can be used to store additional
              information about the document.

          namespace: Namespace to assign this document to. This can be for example a specific
              conversation that it is scoped to

          org_id: Organization ID to assign this document to.

          text: Full text of the document.

          title: Title of the document.

          type: Type of the document. This is optional, but helps with parsing the document.

          url: Source URL of the document. If text is not provided and URL is publicly
              accessible, Hyperspell will retrieve the document from this URL.

          user_id: User ID to assign this document to.

          visibility: Visibility of the document. If visibility is set to USER, then `user_id` must be
              present, and the document will only be visible to this user. If visibility is
              set to `org`, then `org_id` must be present and the document will be visible to
              all users in the same organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ingest",
            body=await async_maybe_transform(
                {
                    "date": date,
                    "metadata": metadata,
                    "namespace": namespace,
                    "org_id": org_id,
                    "text": text,
                    "title": title,
                    "type": type,
                    "url": url,
                    "user_id": user_id,
                    "visibility": visibility,
                },
                ingest_add_params.IngestAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestAddResponse,
        )

    async def file(
        self,
        *,
        data: ingest_file_params.Data,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Ingest File

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "data": data,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/ingest_file",
            body=await async_maybe_transform(body, ingest_file_params.IngestFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class IngestResourceWithRawResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

        self.add = to_raw_response_wrapper(
            ingest.add,
        )
        self.file = to_raw_response_wrapper(
            ingest.file,
        )


class AsyncIngestResourceWithRawResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

        self.add = async_to_raw_response_wrapper(
            ingest.add,
        )
        self.file = async_to_raw_response_wrapper(
            ingest.file,
        )


class IngestResourceWithStreamingResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

        self.add = to_streamed_response_wrapper(
            ingest.add,
        )
        self.file = to_streamed_response_wrapper(
            ingest.file,
        )


class AsyncIngestResourceWithStreamingResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

        self.add = async_to_streamed_response_wrapper(
            ingest.add,
        )
        self.file = async_to_streamed_response_wrapper(
            ingest.file,
        )
