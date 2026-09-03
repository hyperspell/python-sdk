# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import (
    LiveSearchResponse,
    LiveGetResourceResponse,
    LiveListSourcesResponse,
    LiveListResourcesResponse,
)
from hyperspell.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLive:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_resource(self, client: Hyperspell) -> None:
        live = client.live.get_resource(
            resource_id="resource_id",
            source="reddit",
        )
        assert_matches_type(LiveGetResourceResponse, live, path=["response"])

    @parametrize
    def test_method_get_resource_with_all_params(self, client: Hyperspell) -> None:
        live = client.live.get_resource(
            resource_id="resource_id",
            source="reddit",
            connection_id="connection_id",
            index=True,
        )
        assert_matches_type(LiveGetResourceResponse, live, path=["response"])

    @parametrize
    def test_raw_response_get_resource(self, client: Hyperspell) -> None:
        response = client.live.with_raw_response.get_resource(
            resource_id="resource_id",
            source="reddit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = response.parse()
        assert_matches_type(LiveGetResourceResponse, live, path=["response"])

    @parametrize
    def test_streaming_response_get_resource(self, client: Hyperspell) -> None:
        with client.live.with_streaming_response.get_resource(
            resource_id="resource_id",
            source="reddit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = response.parse()
            assert_matches_type(LiveGetResourceResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_resource(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            client.live.with_raw_response.get_resource(
                resource_id="",
                source="reddit",
            )

    @parametrize
    def test_method_list_resources(self, client: Hyperspell) -> None:
        live = client.live.list_resources(
            source="reddit",
        )
        assert_matches_type(SyncCursorPage[LiveListResourcesResponse], live, path=["response"])

    @parametrize
    def test_method_list_resources_with_all_params(self, client: Hyperspell) -> None:
        live = client.live.list_resources(
            source="reddit",
            connection_id="connection_id",
            cursor="cursor",
            size=0,
        )
        assert_matches_type(SyncCursorPage[LiveListResourcesResponse], live, path=["response"])

    @parametrize
    def test_raw_response_list_resources(self, client: Hyperspell) -> None:
        response = client.live.with_raw_response.list_resources(
            source="reddit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = response.parse()
        assert_matches_type(SyncCursorPage[LiveListResourcesResponse], live, path=["response"])

    @parametrize
    def test_streaming_response_list_resources(self, client: Hyperspell) -> None:
        with client.live.with_streaming_response.list_resources(
            source="reddit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = response.parse()
            assert_matches_type(SyncCursorPage[LiveListResourcesResponse], live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_sources(self, client: Hyperspell) -> None:
        live = client.live.list_sources()
        assert_matches_type(LiveListSourcesResponse, live, path=["response"])

    @parametrize
    def test_raw_response_list_sources(self, client: Hyperspell) -> None:
        response = client.live.with_raw_response.list_sources()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = response.parse()
        assert_matches_type(LiveListSourcesResponse, live, path=["response"])

    @parametrize
    def test_streaming_response_list_sources(self, client: Hyperspell) -> None:
        with client.live.with_streaming_response.list_sources() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = response.parse()
            assert_matches_type(LiveListSourcesResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Hyperspell) -> None:
        live = client.live.search(
            source="reddit",
            query="query",
        )
        assert_matches_type(LiveSearchResponse, live, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Hyperspell) -> None:
        live = client.live.search(
            source="reddit",
            query="query",
            connection_id="connection_id",
            index=True,
        )
        assert_matches_type(LiveSearchResponse, live, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Hyperspell) -> None:
        response = client.live.with_raw_response.search(
            source="reddit",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = response.parse()
        assert_matches_type(LiveSearchResponse, live, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Hyperspell) -> None:
        with client.live.with_streaming_response.search(
            source="reddit",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = response.parse()
            assert_matches_type(LiveSearchResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLive:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_resource(self, async_client: AsyncHyperspell) -> None:
        live = await async_client.live.get_resource(
            resource_id="resource_id",
            source="reddit",
        )
        assert_matches_type(LiveGetResourceResponse, live, path=["response"])

    @parametrize
    async def test_method_get_resource_with_all_params(self, async_client: AsyncHyperspell) -> None:
        live = await async_client.live.get_resource(
            resource_id="resource_id",
            source="reddit",
            connection_id="connection_id",
            index=True,
        )
        assert_matches_type(LiveGetResourceResponse, live, path=["response"])

    @parametrize
    async def test_raw_response_get_resource(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.live.with_raw_response.get_resource(
            resource_id="resource_id",
            source="reddit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = await response.parse()
        assert_matches_type(LiveGetResourceResponse, live, path=["response"])

    @parametrize
    async def test_streaming_response_get_resource(self, async_client: AsyncHyperspell) -> None:
        async with async_client.live.with_streaming_response.get_resource(
            resource_id="resource_id",
            source="reddit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = await response.parse()
            assert_matches_type(LiveGetResourceResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_resource(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            await async_client.live.with_raw_response.get_resource(
                resource_id="",
                source="reddit",
            )

    @parametrize
    async def test_method_list_resources(self, async_client: AsyncHyperspell) -> None:
        live = await async_client.live.list_resources(
            source="reddit",
        )
        assert_matches_type(AsyncCursorPage[LiveListResourcesResponse], live, path=["response"])

    @parametrize
    async def test_method_list_resources_with_all_params(self, async_client: AsyncHyperspell) -> None:
        live = await async_client.live.list_resources(
            source="reddit",
            connection_id="connection_id",
            cursor="cursor",
            size=0,
        )
        assert_matches_type(AsyncCursorPage[LiveListResourcesResponse], live, path=["response"])

    @parametrize
    async def test_raw_response_list_resources(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.live.with_raw_response.list_resources(
            source="reddit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = await response.parse()
        assert_matches_type(AsyncCursorPage[LiveListResourcesResponse], live, path=["response"])

    @parametrize
    async def test_streaming_response_list_resources(self, async_client: AsyncHyperspell) -> None:
        async with async_client.live.with_streaming_response.list_resources(
            source="reddit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = await response.parse()
            assert_matches_type(AsyncCursorPage[LiveListResourcesResponse], live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_sources(self, async_client: AsyncHyperspell) -> None:
        live = await async_client.live.list_sources()
        assert_matches_type(LiveListSourcesResponse, live, path=["response"])

    @parametrize
    async def test_raw_response_list_sources(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.live.with_raw_response.list_sources()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = await response.parse()
        assert_matches_type(LiveListSourcesResponse, live, path=["response"])

    @parametrize
    async def test_streaming_response_list_sources(self, async_client: AsyncHyperspell) -> None:
        async with async_client.live.with_streaming_response.list_sources() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = await response.parse()
            assert_matches_type(LiveListSourcesResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncHyperspell) -> None:
        live = await async_client.live.search(
            source="reddit",
            query="query",
        )
        assert_matches_type(LiveSearchResponse, live, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHyperspell) -> None:
        live = await async_client.live.search(
            source="reddit",
            query="query",
            connection_id="connection_id",
            index=True,
        )
        assert_matches_type(LiveSearchResponse, live, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.live.with_raw_response.search(
            source="reddit",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = await response.parse()
        assert_matches_type(LiveSearchResponse, live, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHyperspell) -> None:
        async with async_client.live.with_streaming_response.search(
            source="reddit",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = await response.parse()
            assert_matches_type(LiveSearchResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True
