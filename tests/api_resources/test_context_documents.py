# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import (
    ContextDocumentGetResponse,
    ContextDocumentListResponse,
    ContextDocumentGenerateResponse,
)
from hyperspell.pagination import SyncContextDocumentsCursorPage, AsyncContextDocumentsCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContextDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        context_document = client.context_documents.list()
        assert_matches_type(
            SyncContextDocumentsCursorPage[ContextDocumentListResponse], context_document, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Hyperspell) -> None:
        context_document = client.context_documents.list(
            cursor="cursor",
            limit=0,
            status="processing",
        )
        assert_matches_type(
            SyncContextDocumentsCursorPage[ContextDocumentListResponse], context_document, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.context_documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context_document = response.parse()
        assert_matches_type(
            SyncContextDocumentsCursorPage[ContextDocumentListResponse], context_document, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.context_documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context_document = response.parse()
            assert_matches_type(
                SyncContextDocumentsCursorPage[ContextDocumentListResponse], context_document, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate(self, client: Hyperspell) -> None:
        context_document = client.context_documents.generate()
        assert_matches_type(ContextDocumentGenerateResponse, context_document, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Hyperspell) -> None:
        context_document = client.context_documents.generate(
            model="model",
            prompt="prompt",
            sources=["string"],
            user_id="user_id",
        )
        assert_matches_type(ContextDocumentGenerateResponse, context_document, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Hyperspell) -> None:
        response = client.context_documents.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context_document = response.parse()
        assert_matches_type(ContextDocumentGenerateResponse, context_document, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Hyperspell) -> None:
        with client.context_documents.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context_document = response.parse()
            assert_matches_type(ContextDocumentGenerateResponse, context_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Hyperspell) -> None:
        context_document = client.context_documents.get(
            "document_id",
        )
        assert_matches_type(ContextDocumentGetResponse, context_document, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Hyperspell) -> None:
        response = client.context_documents.with_raw_response.get(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context_document = response.parse()
        assert_matches_type(ContextDocumentGetResponse, context_document, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Hyperspell) -> None:
        with client.context_documents.with_streaming_response.get(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context_document = response.parse()
            assert_matches_type(ContextDocumentGetResponse, context_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.context_documents.with_raw_response.get(
                "",
            )


class TestAsyncContextDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncHyperspell) -> None:
        context_document = await async_client.context_documents.list()
        assert_matches_type(
            AsyncContextDocumentsCursorPage[ContextDocumentListResponse], context_document, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHyperspell) -> None:
        context_document = await async_client.context_documents.list(
            cursor="cursor",
            limit=0,
            status="processing",
        )
        assert_matches_type(
            AsyncContextDocumentsCursorPage[ContextDocumentListResponse], context_document, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context_document = await response.parse()
        assert_matches_type(
            AsyncContextDocumentsCursorPage[ContextDocumentListResponse], context_document, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context_document = await response.parse()
            assert_matches_type(
                AsyncContextDocumentsCursorPage[ContextDocumentListResponse], context_document, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate(self, async_client: AsyncHyperspell) -> None:
        context_document = await async_client.context_documents.generate()
        assert_matches_type(ContextDocumentGenerateResponse, context_document, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncHyperspell) -> None:
        context_document = await async_client.context_documents.generate(
            model="model",
            prompt="prompt",
            sources=["string"],
            user_id="user_id",
        )
        assert_matches_type(ContextDocumentGenerateResponse, context_document, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context_document = await response.parse()
        assert_matches_type(ContextDocumentGenerateResponse, context_document, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context_document = await response.parse()
            assert_matches_type(ContextDocumentGenerateResponse, context_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncHyperspell) -> None:
        context_document = await async_client.context_documents.get(
            "document_id",
        )
        assert_matches_type(ContextDocumentGetResponse, context_document, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.with_raw_response.get(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context_document = await response.parse()
        assert_matches_type(ContextDocumentGetResponse, context_document, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.with_streaming_response.get(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context_document = await response.parse()
            assert_matches_type(ContextDocumentGetResponse, context_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.context_documents.with_raw_response.get(
                "",
            )
