# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types.context_documents import (
    TreeGetResponse,
    TreeGenerateResponse,
    TreeProgressResponse,
    TreeGetLatestResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate(self, client: Hyperspell) -> None:
        tree = client.context_documents.trees.generate()
        assert_matches_type(TreeGenerateResponse, tree, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Hyperspell) -> None:
        tree = client.context_documents.trees.generate(
            sources=["string"],
            user_id="user_id",
            workstream_name="workstream_name",
        )
        assert_matches_type(TreeGenerateResponse, tree, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Hyperspell) -> None:
        response = client.context_documents.trees.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tree = response.parse()
        assert_matches_type(TreeGenerateResponse, tree, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Hyperspell) -> None:
        with client.context_documents.trees.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tree = response.parse()
            assert_matches_type(TreeGenerateResponse, tree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Hyperspell) -> None:
        tree = client.context_documents.trees.get(
            "tree_id",
        )
        assert_matches_type(TreeGetResponse, tree, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Hyperspell) -> None:
        response = client.context_documents.trees.with_raw_response.get(
            "tree_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tree = response.parse()
        assert_matches_type(TreeGetResponse, tree, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Hyperspell) -> None:
        with client.context_documents.trees.with_streaming_response.get(
            "tree_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tree = response.parse()
            assert_matches_type(TreeGetResponse, tree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tree_id` but received ''"):
            client.context_documents.trees.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_latest(self, client: Hyperspell) -> None:
        tree = client.context_documents.trees.get_latest()
        assert_matches_type(TreeGetLatestResponse, tree, path=["response"])

    @parametrize
    def test_method_get_latest_with_all_params(self, client: Hyperspell) -> None:
        tree = client.context_documents.trees.get_latest(
            status="status",
        )
        assert_matches_type(TreeGetLatestResponse, tree, path=["response"])

    @parametrize
    def test_raw_response_get_latest(self, client: Hyperspell) -> None:
        response = client.context_documents.trees.with_raw_response.get_latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tree = response.parse()
        assert_matches_type(TreeGetLatestResponse, tree, path=["response"])

    @parametrize
    def test_streaming_response_get_latest(self, client: Hyperspell) -> None:
        with client.context_documents.trees.with_streaming_response.get_latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tree = response.parse()
            assert_matches_type(TreeGetLatestResponse, tree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_progress(self, client: Hyperspell) -> None:
        tree = client.context_documents.trees.progress(
            "tree_id",
        )
        assert_matches_type(TreeProgressResponse, tree, path=["response"])

    @parametrize
    def test_raw_response_progress(self, client: Hyperspell) -> None:
        response = client.context_documents.trees.with_raw_response.progress(
            "tree_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tree = response.parse()
        assert_matches_type(TreeProgressResponse, tree, path=["response"])

    @parametrize
    def test_streaming_response_progress(self, client: Hyperspell) -> None:
        with client.context_documents.trees.with_streaming_response.progress(
            "tree_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tree = response.parse()
            assert_matches_type(TreeProgressResponse, tree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_progress(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tree_id` but received ''"):
            client.context_documents.trees.with_raw_response.progress(
                "",
            )


class TestAsyncTrees:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_generate(self, async_client: AsyncHyperspell) -> None:
        tree = await async_client.context_documents.trees.generate()
        assert_matches_type(TreeGenerateResponse, tree, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncHyperspell) -> None:
        tree = await async_client.context_documents.trees.generate(
            sources=["string"],
            user_id="user_id",
            workstream_name="workstream_name",
        )
        assert_matches_type(TreeGenerateResponse, tree, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.trees.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tree = await response.parse()
        assert_matches_type(TreeGenerateResponse, tree, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.trees.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tree = await response.parse()
            assert_matches_type(TreeGenerateResponse, tree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncHyperspell) -> None:
        tree = await async_client.context_documents.trees.get(
            "tree_id",
        )
        assert_matches_type(TreeGetResponse, tree, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.trees.with_raw_response.get(
            "tree_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tree = await response.parse()
        assert_matches_type(TreeGetResponse, tree, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.trees.with_streaming_response.get(
            "tree_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tree = await response.parse()
            assert_matches_type(TreeGetResponse, tree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tree_id` but received ''"):
            await async_client.context_documents.trees.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_latest(self, async_client: AsyncHyperspell) -> None:
        tree = await async_client.context_documents.trees.get_latest()
        assert_matches_type(TreeGetLatestResponse, tree, path=["response"])

    @parametrize
    async def test_method_get_latest_with_all_params(self, async_client: AsyncHyperspell) -> None:
        tree = await async_client.context_documents.trees.get_latest(
            status="status",
        )
        assert_matches_type(TreeGetLatestResponse, tree, path=["response"])

    @parametrize
    async def test_raw_response_get_latest(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.trees.with_raw_response.get_latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tree = await response.parse()
        assert_matches_type(TreeGetLatestResponse, tree, path=["response"])

    @parametrize
    async def test_streaming_response_get_latest(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.trees.with_streaming_response.get_latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tree = await response.parse()
            assert_matches_type(TreeGetLatestResponse, tree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_progress(self, async_client: AsyncHyperspell) -> None:
        tree = await async_client.context_documents.trees.progress(
            "tree_id",
        )
        assert_matches_type(TreeProgressResponse, tree, path=["response"])

    @parametrize
    async def test_raw_response_progress(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.trees.with_raw_response.progress(
            "tree_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tree = await response.parse()
        assert_matches_type(TreeProgressResponse, tree, path=["response"])

    @parametrize
    async def test_streaming_response_progress(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.trees.with_streaming_response.progress(
            "tree_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tree = await response.parse()
            assert_matches_type(TreeProgressResponse, tree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_progress(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tree_id` but received ''"):
            await async_client.context_documents.trees.with_raw_response.progress(
                "",
            )
