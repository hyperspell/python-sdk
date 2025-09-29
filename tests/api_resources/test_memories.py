# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import (
    Memory,
    MemoryStatus,
    MemoryDeleteResponse,
    MemoryStatusResponse,
)
from hyperspell._utils import parse_datetime
from hyperspell.pagination import SyncCursorPage, AsyncCursorPage
from hyperspell.types.shared import QueryResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        memory = client.memories.list()
        assert_matches_type(SyncCursorPage[Memory], memory, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hyperspell) -> None:
        memory = client.memories.list(
            collection="collection",
            cursor="cursor",
            size=0,
            source="collections",
        )
        assert_matches_type(SyncCursorPage[Memory], memory, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.memories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(SyncCursorPage[Memory], memory, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.memories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(SyncCursorPage[Memory], memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Hyperspell) -> None:
        memory = client.memories.delete(
            resource_id="resource_id",
            source="collections",
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Hyperspell) -> None:
        response = client.memories.with_raw_response.delete(
            resource_id="resource_id",
            source="collections",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Hyperspell) -> None:
        with client.memories.with_streaming_response.delete(
            resource_id="resource_id",
            source="collections",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            client.memories.with_raw_response.delete(
                resource_id="",
                source="collections",
            )

    @parametrize
    def test_method_add(self, client: Hyperspell) -> None:
        memory = client.memories.add(
            text="text",
        )
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Hyperspell) -> None:
        memory = client.memories.add(
            text="text",
            collection="collection",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            resource_id="resource_id",
            title="title",
        )
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Hyperspell) -> None:
        response = client.memories.with_raw_response.add(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Hyperspell) -> None:
        with client.memories.with_streaming_response.add(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryStatus, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Hyperspell) -> None:
        memory = client.memories.get(
            resource_id="resource_id",
            source="collections",
        )
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Hyperspell) -> None:
        response = client.memories.with_raw_response.get(
            resource_id="resource_id",
            source="collections",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Hyperspell) -> None:
        with client.memories.with_streaming_response.get(
            resource_id="resource_id",
            source="collections",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(Memory, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            client.memories.with_raw_response.get(
                resource_id="",
                source="collections",
            )

    @parametrize
    def test_method_search(self, client: Hyperspell) -> None:
        memory = client.memories.search(
            query="query",
        )
        assert_matches_type(QueryResult, memory, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Hyperspell) -> None:
        memory = client.memories.search(
            query="query",
            answer=True,
            max_results=0,
            options={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "answer_model": "llama-3.1",
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "box": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "weight": 0,
                },
                "collections": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "weight": 0,
                },
                "google_calendar": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "calendar_id": "calendar_id",
                    "weight": 0,
                },
                "google_drive": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "weight": 0,
                },
                "google_mail": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "label_ids": ["string"],
                    "weight": 0,
                },
                "max_results": 0,
                "notion": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "notion_page_ids": ["string"],
                    "weight": 0,
                },
                "reddit": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "period": "hour",
                    "sort": "relevance",
                    "subreddit": "subreddit",
                    "weight": 0,
                },
                "slack": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "channels": ["string"],
                    "exclude_archived": True,
                    "include_dms": True,
                    "include_group_dms": True,
                    "include_private": True,
                    "weight": 0,
                },
                "web_crawler": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "max_depth": 0,
                    "url": "string",
                    "weight": 0,
                },
            },
            sources=["collections"],
        )
        assert_matches_type(QueryResult, memory, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Hyperspell) -> None:
        response = client.memories.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(QueryResult, memory, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Hyperspell) -> None:
        with client.memories.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(QueryResult, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_status(self, client: Hyperspell) -> None:
        memory = client.memories.status()
        assert_matches_type(MemoryStatusResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Hyperspell) -> None:
        response = client.memories.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryStatusResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Hyperspell) -> None:
        with client.memories.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryStatusResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: Hyperspell) -> None:
        memory = client.memories.upload(
            file=b"raw file contents",
        )
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Hyperspell) -> None:
        memory = client.memories.upload(
            file=b"raw file contents",
            collection="collection",
        )
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Hyperspell) -> None:
        response = client.memories.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Hyperspell) -> None:
        with client.memories.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryStatus, memory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMemories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.list()
        assert_matches_type(AsyncCursorPage[Memory], memory, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.list(
            collection="collection",
            cursor="cursor",
            size=0,
            source="collections",
        )
        assert_matches_type(AsyncCursorPage[Memory], memory, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.memories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(AsyncCursorPage[Memory], memory, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.memories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(AsyncCursorPage[Memory], memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.delete(
            resource_id="resource_id",
            source="collections",
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.memories.with_raw_response.delete(
            resource_id="resource_id",
            source="collections",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHyperspell) -> None:
        async with async_client.memories.with_streaming_response.delete(
            resource_id="resource_id",
            source="collections",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            await async_client.memories.with_raw_response.delete(
                resource_id="",
                source="collections",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.add(
            text="text",
        )
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.add(
            text="text",
            collection="collection",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            resource_id="resource_id",
            title="title",
        )
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.memories.with_raw_response.add(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHyperspell) -> None:
        async with async_client.memories.with_streaming_response.add(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryStatus, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.get(
            resource_id="resource_id",
            source="collections",
        )
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.memories.with_raw_response.get(
            resource_id="resource_id",
            source="collections",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHyperspell) -> None:
        async with async_client.memories.with_streaming_response.get(
            resource_id="resource_id",
            source="collections",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(Memory, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            await async_client.memories.with_raw_response.get(
                resource_id="",
                source="collections",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.search(
            query="query",
        )
        assert_matches_type(QueryResult, memory, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.search(
            query="query",
            answer=True,
            max_results=0,
            options={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "answer_model": "llama-3.1",
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "box": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "weight": 0,
                },
                "collections": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "weight": 0,
                },
                "google_calendar": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "calendar_id": "calendar_id",
                    "weight": 0,
                },
                "google_drive": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "weight": 0,
                },
                "google_mail": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "label_ids": ["string"],
                    "weight": 0,
                },
                "max_results": 0,
                "notion": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "notion_page_ids": ["string"],
                    "weight": 0,
                },
                "reddit": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "period": "hour",
                    "sort": "relevance",
                    "subreddit": "subreddit",
                    "weight": 0,
                },
                "slack": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "channels": ["string"],
                    "exclude_archived": True,
                    "include_dms": True,
                    "include_group_dms": True,
                    "include_private": True,
                    "weight": 0,
                },
                "web_crawler": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "max_depth": 0,
                    "url": "string",
                    "weight": 0,
                },
            },
            sources=["collections"],
        )
        assert_matches_type(QueryResult, memory, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.memories.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(QueryResult, memory, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHyperspell) -> None:
        async with async_client.memories.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(QueryResult, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_status(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.status()
        assert_matches_type(MemoryStatusResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.memories.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryStatusResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncHyperspell) -> None:
        async with async_client.memories.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryStatusResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.upload(
            file=b"raw file contents",
        )
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncHyperspell) -> None:
        memory = await async_client.memories.upload(
            file=b"raw file contents",
            collection="collection",
        )
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.memories.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryStatus, memory, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncHyperspell) -> None:
        async with async_client.memories.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryStatus, memory, path=["response"])

        assert cast(Any, response.is_closed) is True
