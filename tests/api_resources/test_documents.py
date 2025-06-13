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
    DocumentStatusResponse,
)
from hyperspell._utils import parse_datetime
from hyperspell.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        document = client.documents.list()
        assert_matches_type(SyncCursorPage[Document], document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hyperspell) -> None:
        document = client.documents.list(
            collection="collection",
            cursor="cursor",
            size=0,
            source="collections",
        )
        assert_matches_type(SyncCursorPage[Document], document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(SyncCursorPage[Document], document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(SyncCursorPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add(self, client: Hyperspell) -> None:
        document = client.documents.add(
            text="text",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Hyperspell) -> None:
        document = client.documents.add(
            text="text",
            collection="collection",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            resource_id="resource_id",
            title="title",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.add(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.add(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentStatus, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Hyperspell) -> None:
        document = client.documents.get(
            resource_id="resource_id",
            source="collections",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.get(
            resource_id="resource_id",
            source="collections",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.get(
            resource_id="resource_id",
            source="collections",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            client.documents.with_raw_response.get(
                resource_id="",
                source="collections",
            )

    @parametrize
    def test_method_status(self, client: Hyperspell) -> None:
        document = client.documents.status()
        assert_matches_type(DocumentStatusResponse, document, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentStatusResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentStatusResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: Hyperspell) -> None:
        document = client.documents.upload(
            file=b"raw file contents",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Hyperspell) -> None:
        document = client.documents.upload(
            file=b"raw file contents",
            collection="collection",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Hyperspell) -> None:
        response = client.documents.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Hyperspell) -> None:
        with client.documents.with_streaming_response.upload(
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
        document = await async_client.documents.list()
        assert_matches_type(AsyncCursorPage[Document], document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.list(
            collection="collection",
            cursor="cursor",
            size=0,
            source="collections",
        )
        assert_matches_type(AsyncCursorPage[Document], document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(AsyncCursorPage[Document], document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(AsyncCursorPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.add(
            text="text",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.add(
            text="text",
            collection="collection",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            resource_id="resource_id",
            title="title",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.add(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.add(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentStatus, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.get(
            resource_id="resource_id",
            source="collections",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.get(
            resource_id="resource_id",
            source="collections",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.get(
            resource_id="resource_id",
            source="collections",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            await async_client.documents.with_raw_response.get(
                resource_id="",
                source="collections",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.status()
        assert_matches_type(DocumentStatusResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentStatusResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentStatusResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.upload(
            file=b"raw file contents",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncHyperspell) -> None:
        document = await async_client.documents.upload(
            file=b"raw file contents",
            collection="collection",
        )
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.documents.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentStatus, document, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncHyperspell) -> None:
        async with async_client.documents.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentStatus, document, path=["response"])

        assert cast(Any, response.is_closed) is True
