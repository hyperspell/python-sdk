# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types.context_documents import (
    ConfigGetResponse,
    ConfigResetResponse,
    ConfigUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Hyperspell) -> None:
        config = client.context_documents.config.update()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hyperspell) -> None:
        config = client.context_documents.config.update(
            company_prompts={"foo": "string"},
            detection_prompt="detection_prompt",
            domain="domain",
            personal_prompt="personal_prompt",
            source_weights={"foo": "string"},
            structure={
                "company": [
                    {
                        "filename": "filename",
                        "key": "key",
                        "prompt": "prompt",
                        "search_queries": ["string"],
                    }
                ],
                "workstream": [
                    {
                        "filename": "filename",
                        "key": "key",
                        "prompt": "prompt",
                        "search_queries": ["string"],
                    }
                ],
            },
            workstream_prompts={"foo": "string"},
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Hyperspell) -> None:
        response = client.context_documents.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Hyperspell) -> None:
        with client.context_documents.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Hyperspell) -> None:
        config = client.context_documents.config.get()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Hyperspell) -> None:
        response = client.context_documents.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Hyperspell) -> None:
        with client.context_documents.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigGetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reset(self, client: Hyperspell) -> None:
        config = client.context_documents.config.reset()
        assert_matches_type(ConfigResetResponse, config, path=["response"])

    @parametrize
    def test_raw_response_reset(self, client: Hyperspell) -> None:
        response = client.context_documents.config.with_raw_response.reset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigResetResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_reset(self, client: Hyperspell) -> None:
        with client.context_documents.config.with_streaming_response.reset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigResetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncHyperspell) -> None:
        config = await async_client.context_documents.config.update()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHyperspell) -> None:
        config = await async_client.context_documents.config.update(
            company_prompts={"foo": "string"},
            detection_prompt="detection_prompt",
            domain="domain",
            personal_prompt="personal_prompt",
            source_weights={"foo": "string"},
            structure={
                "company": [
                    {
                        "filename": "filename",
                        "key": "key",
                        "prompt": "prompt",
                        "search_queries": ["string"],
                    }
                ],
                "workstream": [
                    {
                        "filename": "filename",
                        "key": "key",
                        "prompt": "prompt",
                        "search_queries": ["string"],
                    }
                ],
            },
            workstream_prompts={"foo": "string"},
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncHyperspell) -> None:
        config = await async_client.context_documents.config.get()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigGetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reset(self, async_client: AsyncHyperspell) -> None:
        config = await async_client.context_documents.config.reset()
        assert_matches_type(ConfigResetResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.context_documents.config.with_raw_response.reset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigResetResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncHyperspell) -> None:
        async with async_client.context_documents.config.with_streaming_response.reset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigResetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
