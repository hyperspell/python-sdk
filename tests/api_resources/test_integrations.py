# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import IntegrationListResponse, IntegrationConnectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        integration = client.integrations.list()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.integrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.integrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationListResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_connect(self, client: Hyperspell) -> None:
        integration = client.integrations.connect(
            integration_id="integration_id",
        )
        assert_matches_type(IntegrationConnectResponse, integration, path=["response"])

    @parametrize
    def test_method_connect_with_all_params(self, client: Hyperspell) -> None:
        integration = client.integrations.connect(
            integration_id="integration_id",
            redirect_url="redirect_url",
        )
        assert_matches_type(IntegrationConnectResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_connect(self, client: Hyperspell) -> None:
        response = client.integrations.with_raw_response.connect(
            integration_id="integration_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationConnectResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_connect(self, client: Hyperspell) -> None:
        with client.integrations.with_streaming_response.connect(
            integration_id="integration_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationConnectResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_connect(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integrations.with_raw_response.connect(
                integration_id="",
            )


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncHyperspell) -> None:
        integration = await async_client.integrations.list()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.integrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.integrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationListResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_connect(self, async_client: AsyncHyperspell) -> None:
        integration = await async_client.integrations.connect(
            integration_id="integration_id",
        )
        assert_matches_type(IntegrationConnectResponse, integration, path=["response"])

    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncHyperspell) -> None:
        integration = await async_client.integrations.connect(
            integration_id="integration_id",
            redirect_url="redirect_url",
        )
        assert_matches_type(IntegrationConnectResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.integrations.with_raw_response.connect(
            integration_id="integration_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationConnectResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncHyperspell) -> None:
        async with async_client.integrations.with_streaming_response.connect(
            integration_id="integration_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationConnectResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_connect(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integrations.with_raw_response.connect(
                integration_id="",
            )
