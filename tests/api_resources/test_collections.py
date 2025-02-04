# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import Collection, CollectionListResponse
from hyperspell.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Hyperspell) -> None:
        collection = client.collections.create(
            name="name",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hyperspell) -> None:
        collection = client.collections.create(
            name="name",
            owner="owner",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Hyperspell) -> None:
        response = client.collections.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Hyperspell) -> None:
        with client.collections.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        collection = client.collections.list()
        assert_matches_type(SyncCursorPage[CollectionListResponse], collection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hyperspell) -> None:
        collection = client.collections.list(
            cursor="cursor",
            size=0,
        )
        assert_matches_type(SyncCursorPage[CollectionListResponse], collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(SyncCursorPage[CollectionListResponse], collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(SyncCursorPage[CollectionListResponse], collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Hyperspell) -> None:
        collection = client.collections.get(
            "name",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Hyperspell) -> None:
        response = client.collections.with_raw_response.get(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Hyperspell) -> None:
        with client.collections.with_streaming_response.get(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.collections.with_raw_response.get(
                "",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHyperspell) -> None:
        collection = await async_client.collections.create(
            name="name",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHyperspell) -> None:
        collection = await async_client.collections.create(
            name="name",
            owner="owner",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.collections.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHyperspell) -> None:
        async with async_client.collections.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncHyperspell) -> None:
        collection = await async_client.collections.list()
        assert_matches_type(AsyncCursorPage[CollectionListResponse], collection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHyperspell) -> None:
        collection = await async_client.collections.list(
            cursor="cursor",
            size=0,
        )
        assert_matches_type(AsyncCursorPage[CollectionListResponse], collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(AsyncCursorPage[CollectionListResponse], collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(AsyncCursorPage[CollectionListResponse], collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncHyperspell) -> None:
        collection = await async_client.collections.get(
            "name",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.collections.with_raw_response.get(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHyperspell) -> None:
        async with async_client.collections.with_streaming_response.get(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.collections.with_raw_response.get(
                "",
            )
