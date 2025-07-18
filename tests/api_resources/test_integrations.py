# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import IntegrationRevokeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_revoke(self, client: Hyperspell) -> None:
        integration = client.integrations.revoke(
            "provider",
        )
        assert_matches_type(IntegrationRevokeResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_revoke(self, client: Hyperspell) -> None:
        response = client.integrations.with_raw_response.revoke(
            "provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationRevokeResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_revoke(self, client: Hyperspell) -> None:
        with client.integrations.with_streaming_response.revoke(
            "provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationRevokeResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.integrations.with_raw_response.revoke(
                "",
            )


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_revoke(self, async_client: AsyncHyperspell) -> None:
        integration = await async_client.integrations.revoke(
            "provider",
        )
        assert_matches_type(IntegrationRevokeResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.integrations.with_raw_response.revoke(
            "provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationRevokeResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncHyperspell) -> None:
        async with async_client.integrations.with_streaming_response.revoke(
            "provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationRevokeResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.integrations.with_raw_response.revoke(
                "",
            )
