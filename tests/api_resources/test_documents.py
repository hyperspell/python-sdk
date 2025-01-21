# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import Document, DocumentListResponse
from hyperspell._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Hyperspell) -> None:
        document = client.documents.retrieve(
            0,
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        document = client.documents.list(
            collections=[0],
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hyperspell) -> None:
        document = client.documents.list(
            collections=[0],
            filter={
                "chunk_type": ["text"],
                "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "source": ["generic"],
                "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=0,
            page=2,
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.list(
            collections=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.list(
            collections=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.retrieve(
            0,
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.list(
            collections=[0],
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.list(
            collections=[0],
            filter={
                "chunk_type": ["text"],
                "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "source": ["generic"],
                "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=0,
            page=2,
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.list(
            collections=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.list(
            collections=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True
