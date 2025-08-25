# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import Token, AuthMeResponse, AuthDeleteUserResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete_user(self, client: Hyperspell) -> None:
        auth = client.auth.delete_user()
        assert_matches_type(AuthDeleteUserResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_delete_user(self, client: Hyperspell) -> None:
        response = client.auth.with_raw_response.delete_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthDeleteUserResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_delete_user(self, client: Hyperspell) -> None:
        with client.auth.with_streaming_response.delete_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthDeleteUserResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_me(self, client: Hyperspell) -> None:
        auth = client.auth.me()
        assert_matches_type(AuthMeResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_me(self, client: Hyperspell) -> None:
        response = client.auth.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthMeResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_me(self, client: Hyperspell) -> None:
        with client.auth.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthMeResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_user_token(self, client: Hyperspell) -> None:
        auth = client.auth.user_token(
            user_id="user_id",
        )
        assert_matches_type(Token, auth, path=["response"])

    @parametrize
    def test_method_user_token_with_all_params(self, client: Hyperspell) -> None:
        auth = client.auth.user_token(
            user_id="user_id",
            expires_in="30m",
            origin="origin",
        )
        assert_matches_type(Token, auth, path=["response"])

    @parametrize
    def test_raw_response_user_token(self, client: Hyperspell) -> None:
        response = client.auth.with_raw_response.user_token(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(Token, auth, path=["response"])

    @parametrize
    def test_streaming_response_user_token(self, client: Hyperspell) -> None:
        with client.auth.with_streaming_response.user_token(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(Token, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete_user(self, async_client: AsyncHyperspell) -> None:
        auth = await async_client.auth.delete_user()
        assert_matches_type(AuthDeleteUserResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_delete_user(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.auth.with_raw_response.delete_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthDeleteUserResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_delete_user(self, async_client: AsyncHyperspell) -> None:
        async with async_client.auth.with_streaming_response.delete_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthDeleteUserResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_me(self, async_client: AsyncHyperspell) -> None:
        auth = await async_client.auth.me()
        assert_matches_type(AuthMeResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_me(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.auth.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthMeResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_me(self, async_client: AsyncHyperspell) -> None:
        async with async_client.auth.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthMeResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_user_token(self, async_client: AsyncHyperspell) -> None:
        auth = await async_client.auth.user_token(
            user_id="user_id",
        )
        assert_matches_type(Token, auth, path=["response"])

    @parametrize
    async def test_method_user_token_with_all_params(self, async_client: AsyncHyperspell) -> None:
        auth = await async_client.auth.user_token(
            user_id="user_id",
            expires_in="30m",
            origin="origin",
        )
        assert_matches_type(Token, auth, path=["response"])

    @parametrize
    async def test_raw_response_user_token(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.auth.with_raw_response.user_token(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(Token, auth, path=["response"])

    @parametrize
    async def test_streaming_response_user_token(self, async_client: AsyncHyperspell) -> None:
        async with async_client.auth.with_streaming_response.user_token(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(Token, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
