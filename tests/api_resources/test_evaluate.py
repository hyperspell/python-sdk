# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import (
    EvaluateScoreQueryResponse,
    EvaluateScoreHighlightResponse,
)
from hyperspell.types.shared import QueryResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_query(self, client: Hyperspell) -> None:
        evaluate = client.evaluate.get_query(
            "query_id",
        )
        assert_matches_type(QueryResult, evaluate, path=["response"])

    @parametrize
    def test_raw_response_get_query(self, client: Hyperspell) -> None:
        response = client.evaluate.with_raw_response.get_query(
            "query_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(QueryResult, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_get_query(self, client: Hyperspell) -> None:
        with client.evaluate.with_streaming_response.get_query(
            "query_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(QueryResult, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_query(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `query_id` but received ''"):
            client.evaluate.with_raw_response.get_query(
                "",
            )

    @parametrize
    def test_method_score_highlight(self, client: Hyperspell) -> None:
        evaluate = client.evaluate.score_highlight(
            highlight_id="highlight_id",
        )
        assert_matches_type(EvaluateScoreHighlightResponse, evaluate, path=["response"])

    @parametrize
    def test_method_score_highlight_with_all_params(self, client: Hyperspell) -> None:
        evaluate = client.evaluate.score_highlight(
            highlight_id="highlight_id",
            comment="comment",
            score=-1,
        )
        assert_matches_type(EvaluateScoreHighlightResponse, evaluate, path=["response"])

    @parametrize
    def test_raw_response_score_highlight(self, client: Hyperspell) -> None:
        response = client.evaluate.with_raw_response.score_highlight(
            highlight_id="highlight_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(EvaluateScoreHighlightResponse, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_score_highlight(self, client: Hyperspell) -> None:
        with client.evaluate.with_streaming_response.score_highlight(
            highlight_id="highlight_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(EvaluateScoreHighlightResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_score_highlight(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `highlight_id` but received ''"):
            client.evaluate.with_raw_response.score_highlight(
                highlight_id="",
            )

    @parametrize
    def test_method_score_query(self, client: Hyperspell) -> None:
        evaluate = client.evaluate.score_query(
            query_id="query_id",
        )
        assert_matches_type(EvaluateScoreQueryResponse, evaluate, path=["response"])

    @parametrize
    def test_method_score_query_with_all_params(self, client: Hyperspell) -> None:
        evaluate = client.evaluate.score_query(
            query_id="query_id",
            score=-1,
        )
        assert_matches_type(EvaluateScoreQueryResponse, evaluate, path=["response"])

    @parametrize
    def test_raw_response_score_query(self, client: Hyperspell) -> None:
        response = client.evaluate.with_raw_response.score_query(
            query_id="query_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(EvaluateScoreQueryResponse, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_score_query(self, client: Hyperspell) -> None:
        with client.evaluate.with_streaming_response.score_query(
            query_id="query_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(EvaluateScoreQueryResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_score_query(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `query_id` but received ''"):
            client.evaluate.with_raw_response.score_query(
                query_id="",
            )


class TestAsyncEvaluate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_query(self, async_client: AsyncHyperspell) -> None:
        evaluate = await async_client.evaluate.get_query(
            "query_id",
        )
        assert_matches_type(QueryResult, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_get_query(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.evaluate.with_raw_response.get_query(
            "query_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(QueryResult, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_get_query(self, async_client: AsyncHyperspell) -> None:
        async with async_client.evaluate.with_streaming_response.get_query(
            "query_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(QueryResult, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_query(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `query_id` but received ''"):
            await async_client.evaluate.with_raw_response.get_query(
                "",
            )

    @parametrize
    async def test_method_score_highlight(self, async_client: AsyncHyperspell) -> None:
        evaluate = await async_client.evaluate.score_highlight(
            highlight_id="highlight_id",
        )
        assert_matches_type(EvaluateScoreHighlightResponse, evaluate, path=["response"])

    @parametrize
    async def test_method_score_highlight_with_all_params(self, async_client: AsyncHyperspell) -> None:
        evaluate = await async_client.evaluate.score_highlight(
            highlight_id="highlight_id",
            comment="comment",
            score=-1,
        )
        assert_matches_type(EvaluateScoreHighlightResponse, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_score_highlight(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.evaluate.with_raw_response.score_highlight(
            highlight_id="highlight_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(EvaluateScoreHighlightResponse, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_score_highlight(self, async_client: AsyncHyperspell) -> None:
        async with async_client.evaluate.with_streaming_response.score_highlight(
            highlight_id="highlight_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(EvaluateScoreHighlightResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_score_highlight(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `highlight_id` but received ''"):
            await async_client.evaluate.with_raw_response.score_highlight(
                highlight_id="",
            )

    @parametrize
    async def test_method_score_query(self, async_client: AsyncHyperspell) -> None:
        evaluate = await async_client.evaluate.score_query(
            query_id="query_id",
        )
        assert_matches_type(EvaluateScoreQueryResponse, evaluate, path=["response"])

    @parametrize
    async def test_method_score_query_with_all_params(self, async_client: AsyncHyperspell) -> None:
        evaluate = await async_client.evaluate.score_query(
            query_id="query_id",
            score=-1,
        )
        assert_matches_type(EvaluateScoreQueryResponse, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_score_query(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.evaluate.with_raw_response.score_query(
            query_id="query_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(EvaluateScoreQueryResponse, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_score_query(self, async_client: AsyncHyperspell) -> None:
        async with async_client.evaluate.with_streaming_response.score_query(
            query_id="query_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(EvaluateScoreQueryResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_score_query(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `query_id` but received ''"):
            await async_client.evaluate.with_raw_response.score_query(
                query_id="",
            )
