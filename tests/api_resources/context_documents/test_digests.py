# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell._utils import parse_datetime
from hyperspell.types.context_documents import (
    DigestListResponse,
    DigestGenerateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDigests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        digest = client.context_documents.digests.list()
        assert_matches_type(DigestListResponse, digest, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hyperspell) -> None:
        digest = client.context_documents.digests.list(
            limit=0,
            period="period",
        )
        assert_matches_type(DigestListResponse, digest, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.context_documents.digests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digest = response.parse()
        assert_matches_type(DigestListResponse, digest, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.context_documents.digests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digest = response.parse()
            assert_matches_type(DigestListResponse, digest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate(self, client: Hyperspell) -> None:
        digest = client.context_documents.digests.generate()
        assert_matches_type(DigestGenerateResponse, digest, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Hyperspell) -> None:
        digest = client.context_documents.digests.generate(
            period="period",
            sources=["string"],
            window_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            window_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DigestGenerateResponse, digest, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Hyperspell) -> None:
        response = client.context_documents.digests.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digest = response.parse()
        assert_matches_type(DigestGenerateResponse, digest, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Hyperspell) -> None:
        with client.context_documents.digests.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digest = response.parse()
            assert_matches_type(DigestGenerateResponse, digest, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDigests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncHyperspell) -> None:
        digest = await async_client.context_documents.digests.list()
        assert_matches_type(DigestListResponse, digest, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHyperspell) -> None:
        digest = await async_client.context_documents.digests.list(
            limit=0,
            period="period",
        )
        assert_matches_type(DigestListResponse, digest, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.digests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digest = await response.parse()
        assert_matches_type(DigestListResponse, digest, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.digests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digest = await response.parse()
            assert_matches_type(DigestListResponse, digest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate(self, async_client: AsyncHyperspell) -> None:
        digest = await async_client.context_documents.digests.generate()
        assert_matches_type(DigestGenerateResponse, digest, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncHyperspell) -> None:
        digest = await async_client.context_documents.digests.generate(
            period="period",
            sources=["string"],
            window_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            window_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DigestGenerateResponse, digest, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.digests.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digest = await response.parse()
        assert_matches_type(DigestGenerateResponse, digest, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.digests.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digest = await response.parse()
            assert_matches_type(DigestGenerateResponse, digest, path=["response"])

        assert cast(Any, response.is_closed) is True
