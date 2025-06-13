# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import document_add_params, document_list_params, document_upload_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.document import Document
from ..types.document_status import DocumentStatus
from ..types.document_status_response import DocumentStatusResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        collection: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        source: Optional[
            Literal[
                "collections",
                "web_crawler",
                "notion",
                "slack",
                "google_calendar",
                "reddit",
                "box",
                "google_drive",
                "airtable",
                "algolia",
                "amplitude",
                "asana",
                "ashby",
                "bamboohr",
                "basecamp",
                "bubbles",
                "calendly",
                "confluence",
                "clickup",
                "datadog",
                "deel",
                "discord",
                "dropbox",
                "exa",
                "facebook",
                "front",
                "github",
                "gitlab",
                "google_docs",
                "google_mail",
                "google_sheet",
                "hubspot",
                "jira",
                "linear",
                "microsoft_teams",
                "mixpanel",
                "monday",
                "outlook",
                "perplexity",
                "rippling",
                "salesforce",
                "segment",
                "todoist",
                "twitter",
                "zoom",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Document]:
        """This endpoint allows you to paginate through all documents in the index.

        You can
        filter the documents by title, date, metadata, etc.

        Args:
          collection: Filter documents by collection.

          source: Filter documents by source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/documents/list",
            page=SyncCursorPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection": collection,
                        "cursor": cursor,
                        "size": size,
                        "source": source,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=Document,
        )

    def add(
        self,
        *,
        text: str,
        collection: Optional[str] | NotGiven = NOT_GIVEN,
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        resource_id: str | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentStatus:
        """Adds an arbitrary document to the index.

        This can be any text, email, call
        transcript, etc. The document will be processed and made available for querying
        once the processing is complete.

        Args:
          text: Full text of the document.

          collection: The collection to add the document to for easier retrieval.

          date: Date of the document. Depending on the document, this could be the creation date
              or date the document was last updated (eg. for a chat transcript, this would be
              the date of the last message). This helps the ranking algorithm and allows you
              to filter by date range.

          resource_id: The resource ID to add the document to. If not provided, a new resource ID will
              be generated. If provided, the document will be updated if it already exists.

          title: Title of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents/add",
            body=maybe_transform(
                {
                    "text": text,
                    "collection": collection,
                    "date": date,
                    "resource_id": resource_id,
                    "title": title,
                },
                document_add_params.DocumentAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentStatus,
        )

    def get(
        self,
        resource_id: str,
        *,
        source: Literal[
            "collections",
            "web_crawler",
            "notion",
            "slack",
            "google_calendar",
            "reddit",
            "box",
            "google_drive",
            "airtable",
            "algolia",
            "amplitude",
            "asana",
            "ashby",
            "bamboohr",
            "basecamp",
            "bubbles",
            "calendly",
            "confluence",
            "clickup",
            "datadog",
            "deel",
            "discord",
            "dropbox",
            "exa",
            "facebook",
            "front",
            "github",
            "gitlab",
            "google_docs",
            "google_mail",
            "google_sheet",
            "hubspot",
            "jira",
            "linear",
            "microsoft_teams",
            "mixpanel",
            "monday",
            "outlook",
            "perplexity",
            "rippling",
            "salesforce",
            "segment",
            "todoist",
            "twitter",
            "zoom",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Retrieves a document by provider and resource_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._get(
            f"/documents/get/{source}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentStatusResponse:
        """
        This endpoint shows the indexing progress of documents, both by provider and
        total.
        """
        return self._get(
            "/documents/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentStatusResponse,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        collection: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentStatus:
        """This endpoint will upload a file to the index and return a document ID.

        The file
        will be processed in the background and the document will be available for
        querying once the processing is complete. You can use the `document_id` to query
        the document later, and check the status of the document.

        Args:
          file: The file to ingest.

          collection: The collection to add the document to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "collection": collection,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/documents/upload",
            body=maybe_transform(body, document_upload_params.DocumentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentStatus,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        collection: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        source: Optional[
            Literal[
                "collections",
                "web_crawler",
                "notion",
                "slack",
                "google_calendar",
                "reddit",
                "box",
                "google_drive",
                "airtable",
                "algolia",
                "amplitude",
                "asana",
                "ashby",
                "bamboohr",
                "basecamp",
                "bubbles",
                "calendly",
                "confluence",
                "clickup",
                "datadog",
                "deel",
                "discord",
                "dropbox",
                "exa",
                "facebook",
                "front",
                "github",
                "gitlab",
                "google_docs",
                "google_mail",
                "google_sheet",
                "hubspot",
                "jira",
                "linear",
                "microsoft_teams",
                "mixpanel",
                "monday",
                "outlook",
                "perplexity",
                "rippling",
                "salesforce",
                "segment",
                "todoist",
                "twitter",
                "zoom",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Document, AsyncCursorPage[Document]]:
        """This endpoint allows you to paginate through all documents in the index.

        You can
        filter the documents by title, date, metadata, etc.

        Args:
          collection: Filter documents by collection.

          source: Filter documents by source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/documents/list",
            page=AsyncCursorPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection": collection,
                        "cursor": cursor,
                        "size": size,
                        "source": source,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=Document,
        )

    async def add(
        self,
        *,
        text: str,
        collection: Optional[str] | NotGiven = NOT_GIVEN,
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        resource_id: str | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentStatus:
        """Adds an arbitrary document to the index.

        This can be any text, email, call
        transcript, etc. The document will be processed and made available for querying
        once the processing is complete.

        Args:
          text: Full text of the document.

          collection: The collection to add the document to for easier retrieval.

          date: Date of the document. Depending on the document, this could be the creation date
              or date the document was last updated (eg. for a chat transcript, this would be
              the date of the last message). This helps the ranking algorithm and allows you
              to filter by date range.

          resource_id: The resource ID to add the document to. If not provided, a new resource ID will
              be generated. If provided, the document will be updated if it already exists.

          title: Title of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents/add",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "collection": collection,
                    "date": date,
                    "resource_id": resource_id,
                    "title": title,
                },
                document_add_params.DocumentAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentStatus,
        )

    async def get(
        self,
        resource_id: str,
        *,
        source: Literal[
            "collections",
            "web_crawler",
            "notion",
            "slack",
            "google_calendar",
            "reddit",
            "box",
            "google_drive",
            "airtable",
            "algolia",
            "amplitude",
            "asana",
            "ashby",
            "bamboohr",
            "basecamp",
            "bubbles",
            "calendly",
            "confluence",
            "clickup",
            "datadog",
            "deel",
            "discord",
            "dropbox",
            "exa",
            "facebook",
            "front",
            "github",
            "gitlab",
            "google_docs",
            "google_mail",
            "google_sheet",
            "hubspot",
            "jira",
            "linear",
            "microsoft_teams",
            "mixpanel",
            "monday",
            "outlook",
            "perplexity",
            "rippling",
            "salesforce",
            "segment",
            "todoist",
            "twitter",
            "zoom",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Retrieves a document by provider and resource_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._get(
            f"/documents/get/{source}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    async def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentStatusResponse:
        """
        This endpoint shows the indexing progress of documents, both by provider and
        total.
        """
        return await self._get(
            "/documents/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentStatusResponse,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        collection: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentStatus:
        """This endpoint will upload a file to the index and return a document ID.

        The file
        will be processed in the background and the document will be available for
        querying once the processing is complete. You can use the `document_id` to query
        the document later, and check the status of the document.

        Args:
          file: The file to ingest.

          collection: The collection to add the document to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "collection": collection,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/documents/upload",
            body=await async_maybe_transform(body, document_upload_params.DocumentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentStatus,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.list = to_raw_response_wrapper(
            documents.list,
        )
        self.add = to_raw_response_wrapper(
            documents.add,
        )
        self.get = to_raw_response_wrapper(
            documents.get,
        )
        self.status = to_raw_response_wrapper(
            documents.status,
        )
        self.upload = to_raw_response_wrapper(
            documents.upload,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.list = async_to_raw_response_wrapper(
            documents.list,
        )
        self.add = async_to_raw_response_wrapper(
            documents.add,
        )
        self.get = async_to_raw_response_wrapper(
            documents.get,
        )
        self.status = async_to_raw_response_wrapper(
            documents.status,
        )
        self.upload = async_to_raw_response_wrapper(
            documents.upload,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.list = to_streamed_response_wrapper(
            documents.list,
        )
        self.add = to_streamed_response_wrapper(
            documents.add,
        )
        self.get = to_streamed_response_wrapper(
            documents.get,
        )
        self.status = to_streamed_response_wrapper(
            documents.status,
        )
        self.upload = to_streamed_response_wrapper(
            documents.upload,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.list = async_to_streamed_response_wrapper(
            documents.list,
        )
        self.add = async_to_streamed_response_wrapper(
            documents.add,
        )
        self.get = async_to_streamed_response_wrapper(
            documents.get,
        )
        self.status = async_to_streamed_response_wrapper(
            documents.status,
        )
        self.upload = async_to_streamed_response_wrapper(
            documents.upload,
        )
