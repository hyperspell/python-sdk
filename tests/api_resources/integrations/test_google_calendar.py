# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types.integrations import Calendar

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGoogleCalendar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        google_calendar = client.integrations.google_calendar.list()
        assert_matches_type(Calendar, google_calendar, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.integrations.google_calendar.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        google_calendar = response.parse()
        assert_matches_type(Calendar, google_calendar, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.integrations.google_calendar.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            google_calendar = response.parse()
            assert_matches_type(Calendar, google_calendar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGoogleCalendar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncHyperspell) -> None:
        google_calendar = await async_client.integrations.google_calendar.list()
        assert_matches_type(Calendar, google_calendar, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.integrations.google_calendar.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        google_calendar = await response.parse()
        assert_matches_type(Calendar, google_calendar, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.integrations.google_calendar.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            google_calendar = await response.parse()
            assert_matches_type(Calendar, google_calendar, path=["response"])

        assert cast(Any, response.is_closed) is True
