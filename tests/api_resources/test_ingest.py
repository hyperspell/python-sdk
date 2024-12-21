# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import IngestAddResponse
from hyperspell._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIngest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add(self, client: Hyperspell) -> None:
        ingest = client.ingest.add()
        assert_matches_type(IngestAddResponse, ingest, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Hyperspell) -> None:
        ingest = client.ingest.add(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
            namespace="namespace",
            org_id="org_id",
            text="text",
            title="title",
            type="chat",
            url="url",
            user_id="user_id",
            visibility="user",
        )
        assert_matches_type(IngestAddResponse, ingest, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Hyperspell) -> None:
        response = client.ingest.with_raw_response.add()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = response.parse()
        assert_matches_type(IngestAddResponse, ingest, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Hyperspell) -> None:
        with client.ingest.with_streaming_response.add() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = response.parse()
            assert_matches_type(IngestAddResponse, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_file(self, client: Hyperspell) -> None:
        ingest = client.ingest.file(
            data={},
            file=b"raw file contents",
        )
        assert_matches_type(object, ingest, path=["response"])

    @parametrize
    def test_method_file_with_all_params(self, client: Hyperspell) -> None:
        ingest = client.ingest.file(
            data={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "metadata": {"foo": "string"},
                "namespace": "chat-8213",
                "org_id": "org_id",
                "text": "text",
                "title": "title",
                "type": "chat",
                "url": "url",
                "user_id": "user-1231",
                "visibility": "user",
            },
            file=b"raw file contents",
        )
        assert_matches_type(object, ingest, path=["response"])

    @parametrize
    def test_raw_response_file(self, client: Hyperspell) -> None:
        response = client.ingest.with_raw_response.file(
            data={},
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = response.parse()
        assert_matches_type(object, ingest, path=["response"])

    @parametrize
    def test_streaming_response_file(self, client: Hyperspell) -> None:
        with client.ingest.with_streaming_response.file(
            data={},
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = response.parse()
            assert_matches_type(object, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIngest:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_add(self, async_client: AsyncHyperspell) -> None:
        ingest = await async_client.ingest.add()
        assert_matches_type(IngestAddResponse, ingest, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncHyperspell) -> None:
        ingest = await async_client.ingest.add(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
            namespace="namespace",
            org_id="org_id",
            text="text",
            title="title",
            type="chat",
            url="url",
            user_id="user_id",
            visibility="user",
        )
        assert_matches_type(IngestAddResponse, ingest, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.ingest.with_raw_response.add()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = await response.parse()
        assert_matches_type(IngestAddResponse, ingest, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHyperspell) -> None:
        async with async_client.ingest.with_streaming_response.add() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = await response.parse()
            assert_matches_type(IngestAddResponse, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_file(self, async_client: AsyncHyperspell) -> None:
        ingest = await async_client.ingest.file(
            data={},
            file=b"raw file contents",
        )
        assert_matches_type(object, ingest, path=["response"])

    @parametrize
    async def test_method_file_with_all_params(self, async_client: AsyncHyperspell) -> None:
        ingest = await async_client.ingest.file(
            data={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "metadata": {"foo": "string"},
                "namespace": "chat-8213",
                "org_id": "org_id",
                "text": "text",
                "title": "title",
                "type": "chat",
                "url": "url",
                "user_id": "user-1231",
                "visibility": "user",
            },
            file=b"raw file contents",
        )
        assert_matches_type(object, ingest, path=["response"])

    @parametrize
    async def test_raw_response_file(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.ingest.with_raw_response.file(
            data={},
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = await response.parse()
        assert_matches_type(object, ingest, path=["response"])

    @parametrize
    async def test_streaming_response_file(self, async_client: AsyncHyperspell) -> None:
        async with async_client.ingest.with_streaming_response.file(
            data={},
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = await response.parse()
            assert_matches_type(object, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True
