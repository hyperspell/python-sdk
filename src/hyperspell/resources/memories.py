# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Mapping, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import memory_add_params, memory_list_params, memory_search_params, memory_upload_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
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
from ..types.memory import Memory
from ..types.memory_status import MemoryStatus
from ..types.shared.query_result import QueryResult
from ..types.memory_delete_response import MemoryDeleteResponse
from ..types.memory_status_response import MemoryStatusResponse

__all__ = ["MemoriesResource", "AsyncMemoriesResource"]


class MemoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return MemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return MemoriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        collection: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        size: int | Omit = omit,
        source: Optional[
            Literal[
                "collections",
                "vault",
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
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Memory]:
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
            "/memories/list",
            page=SyncCursorPage[Memory],
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
                    memory_list_params.MemoryListParams,
                ),
            ),
            model=Memory,
        )

    def delete(
        self,
        resource_id: str,
        *,
        source: Literal[
            "collections",
            "vault",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteResponse:
        """
        Delete a memory and its associated chunks from the index.

        This removes the memory completely from the vector index and database. The
        operation deletes:

        1. All chunks associated with the resource (including embeddings)
        2. The resource record itself

        Args: source: The document provider (e.g., gmail, notion, vault) resource_id:
        The unique identifier of the resource to delete api_token: Authentication token

        Returns: MemoryDeletionResponse with deletion details

        Raises: DocumentNotFound: If the resource doesn't exist or user doesn't have
        access

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
        return self._delete(
            f"/memories/delete/{source}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryDeleteResponse,
        )

    def add(
        self,
        *,
        text: str,
        collection: Optional[str] | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        resource_id: str | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatus:
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
            "/memories/add",
            body=maybe_transform(
                {
                    "text": text,
                    "collection": collection,
                    "date": date,
                    "resource_id": resource_id,
                    "title": title,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatus,
        )

    def get(
        self,
        resource_id: str,
        *,
        source: Literal[
            "collections",
            "vault",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Memory:
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
            f"/memories/get/{source}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )

    def search(
        self,
        *,
        query: str,
        answer: bool | Omit = omit,
        max_results: int | Omit = omit,
        options: memory_search_params.Options | Omit = omit,
        sources: List[
            Literal[
                "collections",
                "vault",
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
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryResult:
        """
        Retrieves documents matching the query.

        Args:
          query: Query to run.

          answer: If true, the query will be answered along with matching source documents.

          max_results: Maximum number of results to return.

          options: Search options for the query.

          sources: Only query documents from these sources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/memories/query",
            body=maybe_transform(
                {
                    "query": query,
                    "answer": answer,
                    "max_results": max_results,
                    "options": options,
                    "sources": sources,
                },
                memory_search_params.MemorySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryResult,
        )

    def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatusResponse:
        """
        This endpoint shows the indexing progress of documents, both by provider and
        total.
        """
        return self._get(
            "/memories/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatusResponse,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        collection: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatus:
        """This endpoint will upload a file to the index and return a resource_id.

        The file
        will be processed in the background and the memory will be available for
        querying once the processing is complete. You can use the `resource_id` to query
        the memory later, and check the status of the memory.

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
            "/memories/upload",
            body=maybe_transform(body, memory_upload_params.MemoryUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatus,
        )


class AsyncMemoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncMemoriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        collection: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        size: int | Omit = omit,
        source: Optional[
            Literal[
                "collections",
                "vault",
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
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Memory, AsyncCursorPage[Memory]]:
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
            "/memories/list",
            page=AsyncCursorPage[Memory],
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
                    memory_list_params.MemoryListParams,
                ),
            ),
            model=Memory,
        )

    async def delete(
        self,
        resource_id: str,
        *,
        source: Literal[
            "collections",
            "vault",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteResponse:
        """
        Delete a memory and its associated chunks from the index.

        This removes the memory completely from the vector index and database. The
        operation deletes:

        1. All chunks associated with the resource (including embeddings)
        2. The resource record itself

        Args: source: The document provider (e.g., gmail, notion, vault) resource_id:
        The unique identifier of the resource to delete api_token: Authentication token

        Returns: MemoryDeletionResponse with deletion details

        Raises: DocumentNotFound: If the resource doesn't exist or user doesn't have
        access

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
        return await self._delete(
            f"/memories/delete/{source}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryDeleteResponse,
        )

    async def add(
        self,
        *,
        text: str,
        collection: Optional[str] | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        resource_id: str | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatus:
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
            "/memories/add",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "collection": collection,
                    "date": date,
                    "resource_id": resource_id,
                    "title": title,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatus,
        )

    async def get(
        self,
        resource_id: str,
        *,
        source: Literal[
            "collections",
            "vault",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Memory:
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
            f"/memories/get/{source}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )

    async def search(
        self,
        *,
        query: str,
        answer: bool | Omit = omit,
        max_results: int | Omit = omit,
        options: memory_search_params.Options | Omit = omit,
        sources: List[
            Literal[
                "collections",
                "vault",
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
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryResult:
        """
        Retrieves documents matching the query.

        Args:
          query: Query to run.

          answer: If true, the query will be answered along with matching source documents.

          max_results: Maximum number of results to return.

          options: Search options for the query.

          sources: Only query documents from these sources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/memories/query",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "answer": answer,
                    "max_results": max_results,
                    "options": options,
                    "sources": sources,
                },
                memory_search_params.MemorySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryResult,
        )

    async def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatusResponse:
        """
        This endpoint shows the indexing progress of documents, both by provider and
        total.
        """
        return await self._get(
            "/memories/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatusResponse,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        collection: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatus:
        """This endpoint will upload a file to the index and return a resource_id.

        The file
        will be processed in the background and the memory will be available for
        querying once the processing is complete. You can use the `resource_id` to query
        the memory later, and check the status of the memory.

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
            "/memories/upload",
            body=await async_maybe_transform(body, memory_upload_params.MemoryUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatus,
        )


class MemoriesResourceWithRawResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.list = to_raw_response_wrapper(
            memories.list,
        )
        self.delete = to_raw_response_wrapper(
            memories.delete,
        )
        self.add = to_raw_response_wrapper(
            memories.add,
        )
        self.get = to_raw_response_wrapper(
            memories.get,
        )
        self.search = to_raw_response_wrapper(
            memories.search,
        )
        self.status = to_raw_response_wrapper(
            memories.status,
        )
        self.upload = to_raw_response_wrapper(
            memories.upload,
        )


class AsyncMemoriesResourceWithRawResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.list = async_to_raw_response_wrapper(
            memories.list,
        )
        self.delete = async_to_raw_response_wrapper(
            memories.delete,
        )
        self.add = async_to_raw_response_wrapper(
            memories.add,
        )
        self.get = async_to_raw_response_wrapper(
            memories.get,
        )
        self.search = async_to_raw_response_wrapper(
            memories.search,
        )
        self.status = async_to_raw_response_wrapper(
            memories.status,
        )
        self.upload = async_to_raw_response_wrapper(
            memories.upload,
        )


class MemoriesResourceWithStreamingResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.list = to_streamed_response_wrapper(
            memories.list,
        )
        self.delete = to_streamed_response_wrapper(
            memories.delete,
        )
        self.add = to_streamed_response_wrapper(
            memories.add,
        )
        self.get = to_streamed_response_wrapper(
            memories.get,
        )
        self.search = to_streamed_response_wrapper(
            memories.search,
        )
        self.status = to_streamed_response_wrapper(
            memories.status,
        )
        self.upload = to_streamed_response_wrapper(
            memories.upload,
        )


class AsyncMemoriesResourceWithStreamingResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.list = async_to_streamed_response_wrapper(
            memories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            memories.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            memories.add,
        )
        self.get = async_to_streamed_response_wrapper(
            memories.get,
        )
        self.search = async_to_streamed_response_wrapper(
            memories.search,
        )
        self.status = async_to_streamed_response_wrapper(
            memories.status,
        )
        self.upload = async_to_streamed_response_wrapper(
            memories.upload,
        )
