# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Hyperspell) -> None:
        query = client.query.retrieve(
            query="query",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Hyperspell) -> None:
        query = client.query.retrieve(
            query="query",
            collections=["string"],
            filter={
                "chunk_type": ["text"],
                "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "source": ["generic"],
                "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            max_results=0,
            query_type="auto",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Hyperspell) -> None:
        response = client.query.with_raw_response.retrieve(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Hyperspell) -> None:
        with client.query.with_streaming_response.retrieve(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(object, query, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHyperspell) -> None:
        query = await async_client.query.retrieve(
            query="query",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHyperspell) -> None:
        query = await async_client.query.retrieve(
            query="query",
            collections=["string"],
            filter={
                "chunk_type": ["text"],
                "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "source": ["generic"],
                "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            max_results=0,
            query_type="auto",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.query.with_raw_response.retrieve(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHyperspell) -> None:
        async with async_client.query.with_streaming_response.retrieve(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(object, query, path=["response"])

        assert cast(Any, response.is_closed) is True
