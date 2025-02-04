# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import (
    Document,
    DocumentStatus,
    DocumentListResponse,
)
from hyperspell._utils import parse_datetime
from hyperspell.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        document = client.documents.list(
            collection="collection",
        )
        assert_matches_type(SyncCursorPage[DocumentListResponse], document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hyperspell) -> None:
        document = client.documents.list(
            collection="collection",
            cursor="cursor",
            size=0,
        )
        assert_matches_type(SyncCursorPage[DocumentListResponse], document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.list(
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(SyncCursorPage[DocumentListResponse], document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.list(
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(SyncCursorPage[DocumentListResponse], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add(self, client: Hyperspell) -> None:
        document = client.documents.add(
            collection="collection",
            text="text",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Hyperspell) -> None:
        document = client.documents.add(
            collection="collection",
            text="text",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="generic",
            title="title",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.add(
            collection="collection",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.add(
            collection="collection",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentStatus, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_url(self, client: Hyperspell) -> None:
        document = client.documents.add_url(
            collection="collection",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_method_add_url_with_all_params(self, client: Hyperspell) -> None:
        document = client.documents.add_url(
            collection="collection",
            url="url",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_raw_response_add_url(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.add_url(
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_streaming_response_add_url(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.add_url(
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentStatus, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Hyperspell) -> None:
        document = client.documents.get(
            0,
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: Hyperspell) -> None:
        document = client.documents.upload(
            collection="collection",
            file=b"raw file contents",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.upload(
            collection="collection",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.upload(
            collection="collection",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentStatus, document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.list(
            collection="collection",
        )
        assert_matches_type(AsyncCursorPage[DocumentListResponse], document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.list(
            collection="collection",
            cursor="cursor",
            size=0,
        )
        assert_matches_type(AsyncCursorPage[DocumentListResponse], document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.list(
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(AsyncCursorPage[DocumentListResponse], document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.list(
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(AsyncCursorPage[DocumentListResponse], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.add(
            collection="collection",
            text="text",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.add(
            collection="collection",
            text="text",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="generic",
            title="title",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.add(
            collection="collection",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.add(
            collection="collection",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentStatus, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_url(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.add_url(
            collection="collection",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_method_add_url_with_all_params(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.add_url(
            collection="collection",
            url="url",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_raw_response_add_url(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.add_url(
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_streaming_response_add_url(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.add_url(
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentStatus, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.get(
            0,
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.upload(
            collection="collection",
            file=b"raw file contents",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.upload(
            collection="collection",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.upload(
            collection="collection",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentStatus, document, path=["response"])

        assert cast(Any, response.is_closed) is True
