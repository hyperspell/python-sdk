# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import MemoryStatus
from hyperspell._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add(self, client: Hyperspell) -> None:
        session = client.sessions.add(
            history="history",
        )
        assert_matches_type(MemoryStatus, session, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Hyperspell) -> None:
        session = client.sessions.add(
            history="history",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            extract=["procedure"],
            format="vercel",
            metadata={"foo": "string"},
            session_id="session_id",
            title="title",
        )
        assert_matches_type(MemoryStatus, session, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Hyperspell) -> None:
        response = client.sessions.with_raw_response.add(
            history="history",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(MemoryStatus, session, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Hyperspell) -> None:
        with client.sessions.with_streaming_response.add(
            history="history",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(MemoryStatus, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add(self, async_client: AsyncHyperspell) -> None:
        session = await async_client.sessions.add(
            history="history",
        )
        assert_matches_type(MemoryStatus, session, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncHyperspell) -> None:
        session = await async_client.sessions.add(
            history="history",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            extract=["procedure"],
            format="vercel",
            metadata={"foo": "string"},
            session_id="session_id",
            title="title",
        )
        assert_matches_type(MemoryStatus, session, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.sessions.with_raw_response.add(
            history="history",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(MemoryStatus, session, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHyperspell) -> None:
        async with async_client.sessions.with_streaming_response.add(
            history="history",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(MemoryStatus, session, path=["response"])

        assert cast(Any, response.is_closed) is True
