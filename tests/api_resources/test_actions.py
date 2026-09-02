# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import (
    ActionAddReactionResponse,
    ActionSendMessageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_reaction(self, client: Hyperspell) -> None:
        action = client.actions.add_reaction(
            channel="channel",
            name="name",
            provider="slack",
            timestamp="timestamp",
        )
        assert_matches_type(ActionAddReactionResponse, action, path=["response"])

    @parametrize
    def test_method_add_reaction_with_all_params(self, client: Hyperspell) -> None:
        action = client.actions.add_reaction(
            channel="channel",
            name="name",
            provider="slack",
            timestamp="timestamp",
            connection="connection",
        )
        assert_matches_type(ActionAddReactionResponse, action, path=["response"])

    @parametrize
    def test_raw_response_add_reaction(self, client: Hyperspell) -> None:
        response = client.actions.with_raw_response.add_reaction(
            channel="channel",
            name="name",
            provider="slack",
            timestamp="timestamp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionAddReactionResponse, action, path=["response"])

    @parametrize
    def test_streaming_response_add_reaction(self, client: Hyperspell) -> None:
        with client.actions.with_streaming_response.add_reaction(
            channel="channel",
            name="name",
            provider="slack",
            timestamp="timestamp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionAddReactionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_message(self, client: Hyperspell) -> None:
        action = client.actions.send_message(
            provider="slack",
            text="text",
        )
        assert_matches_type(ActionSendMessageResponse, action, path=["response"])

    @parametrize
    def test_method_send_message_with_all_params(self, client: Hyperspell) -> None:
        action = client.actions.send_message(
            provider="slack",
            text="text",
            channel="channel",
            connection="connection",
            parent="parent",
        )
        assert_matches_type(ActionSendMessageResponse, action, path=["response"])

    @parametrize
    def test_raw_response_send_message(self, client: Hyperspell) -> None:
        response = client.actions.with_raw_response.send_message(
            provider="slack",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionSendMessageResponse, action, path=["response"])

    @parametrize
    def test_streaming_response_send_message(self, client: Hyperspell) -> None:
        with client.actions.with_streaming_response.send_message(
            provider="slack",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionSendMessageResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add_reaction(self, async_client: AsyncHyperspell) -> None:
        action = await async_client.actions.add_reaction(
            channel="channel",
            name="name",
            provider="slack",
            timestamp="timestamp",
        )
        assert_matches_type(ActionAddReactionResponse, action, path=["response"])

    @parametrize
    async def test_method_add_reaction_with_all_params(self, async_client: AsyncHyperspell) -> None:
        action = await async_client.actions.add_reaction(
            channel="channel",
            name="name",
            provider="slack",
            timestamp="timestamp",
            connection="connection",
        )
        assert_matches_type(ActionAddReactionResponse, action, path=["response"])

    @parametrize
    async def test_raw_response_add_reaction(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.actions.with_raw_response.add_reaction(
            channel="channel",
            name="name",
            provider="slack",
            timestamp="timestamp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionAddReactionResponse, action, path=["response"])

    @parametrize
    async def test_streaming_response_add_reaction(self, async_client: AsyncHyperspell) -> None:
        async with async_client.actions.with_streaming_response.add_reaction(
            channel="channel",
            name="name",
            provider="slack",
            timestamp="timestamp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionAddReactionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_message(self, async_client: AsyncHyperspell) -> None:
        action = await async_client.actions.send_message(
            provider="slack",
            text="text",
        )
        assert_matches_type(ActionSendMessageResponse, action, path=["response"])

    @parametrize
    async def test_method_send_message_with_all_params(self, async_client: AsyncHyperspell) -> None:
        action = await async_client.actions.send_message(
            provider="slack",
            text="text",
            channel="channel",
            connection="connection",
            parent="parent",
        )
        assert_matches_type(ActionSendMessageResponse, action, path=["response"])

    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.actions.with_raw_response.send_message(
            provider="slack",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionSendMessageResponse, action, path=["response"])

    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncHyperspell) -> None:
        async with async_client.actions.with_streaming_response.send_message(
            provider="slack",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionSendMessageResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True
