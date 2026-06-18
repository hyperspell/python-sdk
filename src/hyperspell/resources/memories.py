# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Mapping, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    memory_add_params,
    memory_list_params,
    memory_search_params,
    memory_update_params,
    memory_upload_params,
    memory_add_bulk_params,
)
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
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
from ..types.memory_status import MemoryStatus
from ..types.memory_get_response import MemoryGetResponse
from ..types.shared.query_result import QueryResult
from ..types.memory_list_response import MemoryListResponse
from ..types.memory_delete_response import MemoryDeleteResponse
from ..types.memory_status_response import MemoryStatusResponse
from ..types.memory_add_bulk_response import MemoryAddBulkResponse

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

    def update(
        self,
        resource_id: str,
        *,
        source: Literal[
            "reddit",
            "notion",
            "slack",
            "google_calendar",
            "google_mail",
            "box",
            "dropbox",
            "github",
            "google_drive",
            "vault",
            "web_crawler",
            "trace",
            "microsoft_teams",
            "gmail_actions",
            "granola",
            "fathom",
            "fireflies",
            "linear",
            "hubspot",
            "salesforce",
            "coda",
            "lightfield",
            "gong",
        ],
        collection: Union[str, object, None] | Omit = omit,
        date: Union[Union[str, datetime], object, None] | Omit = omit,
        metadata: Union[Dict[str, Union[str, float, bool, None]], object, None] | Omit = omit,
        text: Union[str, object, None] | Omit = omit,
        title: Union[str, object, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatus:
        """Updates an existing document in the index.

        You can update the text, collection,
        title, and metadata. The document must already exist or a 404 will be returned.
        This works for documents from any source (vault, slack, gmail, etc.).

        To remove a collection, set it to null explicitly.

        Args:
          collection: The collection to move the document to — deprecated, set the collection using
              metadata instead.

          date: Date of the document for ranking and filtering.

          metadata: Custom metadata for filtering. Keys must be alphanumeric with underscores, max
              64 chars. Values must be string, number, boolean, or null. Will be merged with
              existing metadata.

          text: Full text of the document. If provided, the document will be re-indexed.

          title: Title of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._post(
            path_template("/memories/update/{source}/{resource_id}", source=source, resource_id=resource_id),
            body=maybe_transform(
                {
                    "collection": collection,
                    "date": date,
                    "metadata": metadata,
                    "text": text,
                    "title": title,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatus,
        )

    def list(
        self,
        *,
        collection: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        size: int | Omit = omit,
        source: Optional[
            Literal[
                "reddit",
                "notion",
                "slack",
                "google_calendar",
                "google_mail",
                "box",
                "dropbox",
                "github",
                "google_drive",
                "vault",
                "web_crawler",
                "trace",
                "microsoft_teams",
                "gmail_actions",
                "granola",
                "fathom",
                "fireflies",
                "linear",
                "hubspot",
                "salesforce",
                "coda",
                "lightfield",
                "gong",
            ]
        ]
        | Omit = omit,
        status: Optional[Literal["pending", "processing", "completed", "failed", "pending_review", "skipped"]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[MemoryListResponse]:
        """This endpoint allows you to paginate through all documents in the index.

        You can
        filter the documents by title, date, metadata, etc.

        Args:
          collection: Filter documents by collection.

          filter:
              Filter documents by metadata using MongoDB-style operators. Example:
              {"department": "engineering", "priority": {"$gt": 3}}

          source: Filter documents by source.

          status: Filter documents by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/memories/list",
            page=SyncCursorPage[MemoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection": collection,
                        "cursor": cursor,
                        "filter": filter,
                        "size": size,
                        "source": source,
                        "status": status,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            model=MemoryListResponse,
        )

    def delete(
        self,
        resource_id: str,
        *,
        source: Literal[
            "reddit",
            "notion",
            "slack",
            "google_calendar",
            "google_mail",
            "box",
            "dropbox",
            "github",
            "google_drive",
            "vault",
            "web_crawler",
            "trace",
            "microsoft_teams",
            "gmail_actions",
            "granola",
            "fathom",
            "fireflies",
            "linear",
            "hubspot",
            "salesforce",
            "coda",
            "lightfield",
            "gong",
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
        2. The documents row AND any legacy resources rows sharing the identity —
           leaving either one behind would resurrect the memory through the double-read
           path (ENG-2477).

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
            path_template("/memories/delete/{source}/{resource_id}", source=source, resource_id=resource_id),
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
        metadata: Optional[Dict[str, Union[str, float, bool, None]]] | Omit = omit,
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

          collection: The collection to add the document to — deprecated, set the collection using
              metadata instead.

          date: Date of the document. Depending on the document, this could be the creation date
              or date the document was last updated (eg. for a chat transcript, this would be
              the date of the last message). This helps the ranking algorithm and allows you
              to filter by date range.

          metadata: Custom metadata for filtering. Keys must be alphanumeric with underscores, max
              64 chars. Values must be string, number, boolean, or null.

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
                    "metadata": metadata,
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

    def add_bulk(
        self,
        *,
        items: Iterable[memory_add_bulk_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryAddBulkResponse:
        """
        Adds multiple documents to the index in a single request.

        All items are validated before any database operations occur. If any item fails
        validation, the entire batch is rejected with a 422 error detailing which items
        failed and why.

        Maximum 100 items per request. Each item follows the same schema as the
        single-item /memories/add endpoint.

        Args:
          items: List of memories to ingest. Maximum 100 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/memories/add/bulk",
            body=maybe_transform({"items": items}, memory_add_bulk_params.MemoryAddBulkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryAddBulkResponse,
        )

    def get(
        self,
        resource_id: str,
        *,
        source: Literal[
            "reddit",
            "notion",
            "slack",
            "google_calendar",
            "google_mail",
            "box",
            "dropbox",
            "github",
            "google_drive",
            "vault",
            "web_crawler",
            "trace",
            "microsoft_teams",
            "gmail_actions",
            "granola",
            "fathom",
            "fireflies",
            "linear",
            "hubspot",
            "salesforce",
            "coda",
            "lightfield",
            "gong",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryGetResponse:
        """
        Retrieves a document by provider and resource_id, as a document-shaped response
        carrying the full hyperdoc tree (ENG-2479 Phase 4).

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
            path_template("/memories/get/{source}/{resource_id}", source=source, resource_id=resource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryGetResponse,
        )

    def search(
        self,
        *,
        query: str,
        answer: bool | Omit = omit,
        effort: Literal["minimal", "low", "medium", "high", "very_high"] | Omit = omit,
        max_results: int | Omit = omit,
        options: memory_search_params.Options | Omit = omit,
        provenance: bool | Omit = omit,
        sources: List[
            Literal[
                "reddit",
                "notion",
                "slack",
                "google_calendar",
                "google_mail",
                "box",
                "dropbox",
                "github",
                "google_drive",
                "vault",
                "web_crawler",
                "trace",
                "microsoft_teams",
                "gmail_actions",
                "granola",
                "fathom",
                "fireflies",
                "linear",
                "hubspot",
                "salesforce",
                "coda",
                "lightfield",
                "gong",
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

          effort: How much compute to spend on retrieval. Mirrors the dial popularized by
              frontier-model APIs (OpenAI reasoning_effort, etc.). 'minimal' = verbatim
              single-shot retrieval (fastest). 'low' = LLM rewrites the query for better
              retrieval and extracts date filters. 'medium' = rewrite + agentic refinement
              loop (the answer LLM may request additional retrieval rounds, up to 3). 'high' =
              rewrite + extended refinement (up to 6 rounds). Higher = better recall, more
              latency, more cost.

          max_results: Maximum number of results to return.

          options: Search options for the query.

          provenance:
              If true (effort='very_high' only), attach a provenance record to the response:
              the source documents and entities the answer was grounded in, the agent's search
              trajectory, and any sources that failed. Adds one indexed lookup; intended for
              auditability / compliance use cases.

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
                    "effort": effort,
                    "max_results": max_results,
                    "options": options,
                    "provenance": provenance,
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
        metadata: Optional[str] | Omit = omit,
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

          collection: The collection to add the document to — deprecated, set the collection using
              metadata instead.

          metadata: Custom metadata as JSON string for filtering. Keys must be alphanumeric with
              underscores, max 64 chars. Values must be string, number, or boolean.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "collection": collection,
                "metadata": metadata,
            },
            [["file"]],
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

    async def update(
        self,
        resource_id: str,
        *,
        source: Literal[
            "reddit",
            "notion",
            "slack",
            "google_calendar",
            "google_mail",
            "box",
            "dropbox",
            "github",
            "google_drive",
            "vault",
            "web_crawler",
            "trace",
            "microsoft_teams",
            "gmail_actions",
            "granola",
            "fathom",
            "fireflies",
            "linear",
            "hubspot",
            "salesforce",
            "coda",
            "lightfield",
            "gong",
        ],
        collection: Union[str, object, None] | Omit = omit,
        date: Union[Union[str, datetime], object, None] | Omit = omit,
        metadata: Union[Dict[str, Union[str, float, bool, None]], object, None] | Omit = omit,
        text: Union[str, object, None] | Omit = omit,
        title: Union[str, object, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStatus:
        """Updates an existing document in the index.

        You can update the text, collection,
        title, and metadata. The document must already exist or a 404 will be returned.
        This works for documents from any source (vault, slack, gmail, etc.).

        To remove a collection, set it to null explicitly.

        Args:
          collection: The collection to move the document to — deprecated, set the collection using
              metadata instead.

          date: Date of the document for ranking and filtering.

          metadata: Custom metadata for filtering. Keys must be alphanumeric with underscores, max
              64 chars. Values must be string, number, boolean, or null. Will be merged with
              existing metadata.

          text: Full text of the document. If provided, the document will be re-indexed.

          title: Title of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source:
            raise ValueError(f"Expected a non-empty value for `source` but received {source!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._post(
            path_template("/memories/update/{source}/{resource_id}", source=source, resource_id=resource_id),
            body=await async_maybe_transform(
                {
                    "collection": collection,
                    "date": date,
                    "metadata": metadata,
                    "text": text,
                    "title": title,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStatus,
        )

    def list(
        self,
        *,
        collection: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        size: int | Omit = omit,
        source: Optional[
            Literal[
                "reddit",
                "notion",
                "slack",
                "google_calendar",
                "google_mail",
                "box",
                "dropbox",
                "github",
                "google_drive",
                "vault",
                "web_crawler",
                "trace",
                "microsoft_teams",
                "gmail_actions",
                "granola",
                "fathom",
                "fireflies",
                "linear",
                "hubspot",
                "salesforce",
                "coda",
                "lightfield",
                "gong",
            ]
        ]
        | Omit = omit,
        status: Optional[Literal["pending", "processing", "completed", "failed", "pending_review", "skipped"]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MemoryListResponse, AsyncCursorPage[MemoryListResponse]]:
        """This endpoint allows you to paginate through all documents in the index.

        You can
        filter the documents by title, date, metadata, etc.

        Args:
          collection: Filter documents by collection.

          filter:
              Filter documents by metadata using MongoDB-style operators. Example:
              {"department": "engineering", "priority": {"$gt": 3}}

          source: Filter documents by source.

          status: Filter documents by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/memories/list",
            page=AsyncCursorPage[MemoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection": collection,
                        "cursor": cursor,
                        "filter": filter,
                        "size": size,
                        "source": source,
                        "status": status,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            model=MemoryListResponse,
        )

    async def delete(
        self,
        resource_id: str,
        *,
        source: Literal[
            "reddit",
            "notion",
            "slack",
            "google_calendar",
            "google_mail",
            "box",
            "dropbox",
            "github",
            "google_drive",
            "vault",
            "web_crawler",
            "trace",
            "microsoft_teams",
            "gmail_actions",
            "granola",
            "fathom",
            "fireflies",
            "linear",
            "hubspot",
            "salesforce",
            "coda",
            "lightfield",
            "gong",
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
        2. The documents row AND any legacy resources rows sharing the identity —
           leaving either one behind would resurrect the memory through the double-read
           path (ENG-2477).

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
            path_template("/memories/delete/{source}/{resource_id}", source=source, resource_id=resource_id),
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
        metadata: Optional[Dict[str, Union[str, float, bool, None]]] | Omit = omit,
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

          collection: The collection to add the document to — deprecated, set the collection using
              metadata instead.

          date: Date of the document. Depending on the document, this could be the creation date
              or date the document was last updated (eg. for a chat transcript, this would be
              the date of the last message). This helps the ranking algorithm and allows you
              to filter by date range.

          metadata: Custom metadata for filtering. Keys must be alphanumeric with underscores, max
              64 chars. Values must be string, number, boolean, or null.

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
                    "metadata": metadata,
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

    async def add_bulk(
        self,
        *,
        items: Iterable[memory_add_bulk_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryAddBulkResponse:
        """
        Adds multiple documents to the index in a single request.

        All items are validated before any database operations occur. If any item fails
        validation, the entire batch is rejected with a 422 error detailing which items
        failed and why.

        Maximum 100 items per request. Each item follows the same schema as the
        single-item /memories/add endpoint.

        Args:
          items: List of memories to ingest. Maximum 100 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/memories/add/bulk",
            body=await async_maybe_transform({"items": items}, memory_add_bulk_params.MemoryAddBulkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryAddBulkResponse,
        )

    async def get(
        self,
        resource_id: str,
        *,
        source: Literal[
            "reddit",
            "notion",
            "slack",
            "google_calendar",
            "google_mail",
            "box",
            "dropbox",
            "github",
            "google_drive",
            "vault",
            "web_crawler",
            "trace",
            "microsoft_teams",
            "gmail_actions",
            "granola",
            "fathom",
            "fireflies",
            "linear",
            "hubspot",
            "salesforce",
            "coda",
            "lightfield",
            "gong",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryGetResponse:
        """
        Retrieves a document by provider and resource_id, as a document-shaped response
        carrying the full hyperdoc tree (ENG-2479 Phase 4).

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
            path_template("/memories/get/{source}/{resource_id}", source=source, resource_id=resource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryGetResponse,
        )

    async def search(
        self,
        *,
        query: str,
        answer: bool | Omit = omit,
        effort: Literal["minimal", "low", "medium", "high", "very_high"] | Omit = omit,
        max_results: int | Omit = omit,
        options: memory_search_params.Options | Omit = omit,
        provenance: bool | Omit = omit,
        sources: List[
            Literal[
                "reddit",
                "notion",
                "slack",
                "google_calendar",
                "google_mail",
                "box",
                "dropbox",
                "github",
                "google_drive",
                "vault",
                "web_crawler",
                "trace",
                "microsoft_teams",
                "gmail_actions",
                "granola",
                "fathom",
                "fireflies",
                "linear",
                "hubspot",
                "salesforce",
                "coda",
                "lightfield",
                "gong",
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

          effort: How much compute to spend on retrieval. Mirrors the dial popularized by
              frontier-model APIs (OpenAI reasoning_effort, etc.). 'minimal' = verbatim
              single-shot retrieval (fastest). 'low' = LLM rewrites the query for better
              retrieval and extracts date filters. 'medium' = rewrite + agentic refinement
              loop (the answer LLM may request additional retrieval rounds, up to 3). 'high' =
              rewrite + extended refinement (up to 6 rounds). Higher = better recall, more
              latency, more cost.

          max_results: Maximum number of results to return.

          options: Search options for the query.

          provenance:
              If true (effort='very_high' only), attach a provenance record to the response:
              the source documents and entities the answer was grounded in, the agent's search
              trajectory, and any sources that failed. Adds one indexed lookup; intended for
              auditability / compliance use cases.

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
                    "effort": effort,
                    "max_results": max_results,
                    "options": options,
                    "provenance": provenance,
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
        metadata: Optional[str] | Omit = omit,
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

          collection: The collection to add the document to — deprecated, set the collection using
              metadata instead.

          metadata: Custom metadata as JSON string for filtering. Keys must be alphanumeric with
              underscores, max 64 chars. Values must be string, number, or boolean.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "collection": collection,
                "metadata": metadata,
            },
            [["file"]],
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

        self.update = to_raw_response_wrapper(
            memories.update,
        )
        self.list = to_raw_response_wrapper(
            memories.list,
        )
        self.delete = to_raw_response_wrapper(
            memories.delete,
        )
        self.add = to_raw_response_wrapper(
            memories.add,
        )
        self.add_bulk = to_raw_response_wrapper(
            memories.add_bulk,
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

        self.update = async_to_raw_response_wrapper(
            memories.update,
        )
        self.list = async_to_raw_response_wrapper(
            memories.list,
        )
        self.delete = async_to_raw_response_wrapper(
            memories.delete,
        )
        self.add = async_to_raw_response_wrapper(
            memories.add,
        )
        self.add_bulk = async_to_raw_response_wrapper(
            memories.add_bulk,
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

        self.update = to_streamed_response_wrapper(
            memories.update,
        )
        self.list = to_streamed_response_wrapper(
            memories.list,
        )
        self.delete = to_streamed_response_wrapper(
            memories.delete,
        )
        self.add = to_streamed_response_wrapper(
            memories.add,
        )
        self.add_bulk = to_streamed_response_wrapper(
            memories.add_bulk,
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

        self.update = async_to_streamed_response_wrapper(
            memories.update,
        )
        self.list = async_to_streamed_response_wrapper(
            memories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            memories.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            memories.add,
        )
        self.add_bulk = async_to_streamed_response_wrapper(
            memories.add_bulk,
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
