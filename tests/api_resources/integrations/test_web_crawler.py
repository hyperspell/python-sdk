# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types.integrations import WebCrawlerIndexResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebCrawler:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_index(self, client: Hyperspell) -> None:
        web_crawler = client.integrations.web_crawler.index(
            url="url",
        )
        assert_matches_type(WebCrawlerIndexResponse, web_crawler, path=["response"])

    @parametrize
    def test_method_index_with_all_params(self, client: Hyperspell) -> None:
        web_crawler = client.integrations.web_crawler.index(
            url="url",
            limit=1,
            max_depth=0,
        )
        assert_matches_type(WebCrawlerIndexResponse, web_crawler, path=["response"])

    @parametrize
    def test_raw_response_index(self, client: Hyperspell) -> None:
        response = client.integrations.web_crawler.with_raw_response.index(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web_crawler = response.parse()
        assert_matches_type(WebCrawlerIndexResponse, web_crawler, path=["response"])

    @parametrize
    def test_streaming_response_index(self, client: Hyperspell) -> None:
        with client.integrations.web_crawler.with_streaming_response.index(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web_crawler = response.parse()
            assert_matches_type(WebCrawlerIndexResponse, web_crawler, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebCrawler:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_index(self, async_client: AsyncHyperspell) -> None:
        web_crawler = await async_client.integrations.web_crawler.index(
            url="url",
        )
        assert_matches_type(WebCrawlerIndexResponse, web_crawler, path=["response"])

    @parametrize
    async def test_method_index_with_all_params(self, async_client: AsyncHyperspell) -> None:
        web_crawler = await async_client.integrations.web_crawler.index(
            url="url",
            limit=1,
            max_depth=0,
        )
        assert_matches_type(WebCrawlerIndexResponse, web_crawler, path=["response"])

    @parametrize
    async def test_raw_response_index(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.integrations.web_crawler.with_raw_response.index(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web_crawler = await response.parse()
        assert_matches_type(WebCrawlerIndexResponse, web_crawler, path=["response"])

    @parametrize
    async def test_streaming_response_index(self, async_client: AsyncHyperspell) -> None:
        async with async_client.integrations.web_crawler.with_streaming_response.index(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web_crawler = await response.parse()
            assert_matches_type(WebCrawlerIndexResponse, web_crawler, path=["response"])

        assert cast(Any, response.is_closed) is True
