# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hyperspell import Hyperspell, AsyncHyperspell
from tests.utils import assert_matches_type
from hyperspell.types import (
    FolderListResponse,
    FolderSetPoliciesResponse,
    FolderDeletePolicyResponse,
    FolderListPoliciesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Hyperspell) -> None:
        folder = client.folders.list(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hyperspell) -> None:
        folder = client.folders.list(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_id="parent_id",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hyperspell) -> None:
        response = client.folders.with_raw_response.list(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hyperspell) -> None:
        with client.folders.with_streaming_response.list(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.folders.with_raw_response.list(
                connection_id="",
            )

    @parametrize
    def test_method_delete_policy(self, client: Hyperspell) -> None:
        folder = client.folders.delete_policy(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FolderDeletePolicyResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_delete_policy(self, client: Hyperspell) -> None:
        response = client.folders.with_raw_response.delete_policy(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderDeletePolicyResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_delete_policy(self, client: Hyperspell) -> None:
        with client.folders.with_streaming_response.delete_policy(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderDeletePolicyResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_policy(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.folders.with_raw_response.delete_policy(
                policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.folders.with_raw_response.delete_policy(
                policy_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list_policies(self, client: Hyperspell) -> None:
        folder = client.folders.list_policies(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FolderListPoliciesResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_list_policies(self, client: Hyperspell) -> None:
        response = client.folders.with_raw_response.list_policies(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListPoliciesResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_list_policies(self, client: Hyperspell) -> None:
        with client.folders.with_streaming_response.list_policies(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListPoliciesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_policies(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.folders.with_raw_response.list_policies(
                "",
            )

    @parametrize
    def test_method_set_policies(self, client: Hyperspell) -> None:
        folder = client.folders.set_policies(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_folder_id="provider_folder_id",
            sync_mode="sync",
        )
        assert_matches_type(FolderSetPoliciesResponse, folder, path=["response"])

    @parametrize
    def test_method_set_policies_with_all_params(self, client: Hyperspell) -> None:
        folder = client.folders.set_policies(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_folder_id="provider_folder_id",
            sync_mode="sync",
            folder_name="folder_name",
            folder_path="folder_path",
            parent_folder_id="parent_folder_id",
        )
        assert_matches_type(FolderSetPoliciesResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_set_policies(self, client: Hyperspell) -> None:
        response = client.folders.with_raw_response.set_policies(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_folder_id="provider_folder_id",
            sync_mode="sync",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderSetPoliciesResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_set_policies(self, client: Hyperspell) -> None:
        with client.folders.with_streaming_response.set_policies(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_folder_id="provider_folder_id",
            sync_mode="sync",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderSetPoliciesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_policies(self, client: Hyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.folders.with_raw_response.set_policies(
                connection_id="",
                provider_folder_id="provider_folder_id",
                sync_mode="sync",
            )


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncHyperspell) -> None:
        folder = await async_client.folders.list(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHyperspell) -> None:
        folder = await async_client.folders.list(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_id="parent_id",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.folders.with_raw_response.list(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHyperspell) -> None:
        async with async_client.folders.with_streaming_response.list(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.folders.with_raw_response.list(
                connection_id="",
            )

    @parametrize
    async def test_method_delete_policy(self, async_client: AsyncHyperspell) -> None:
        folder = await async_client.folders.delete_policy(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FolderDeletePolicyResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_delete_policy(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.folders.with_raw_response.delete_policy(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderDeletePolicyResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_delete_policy(self, async_client: AsyncHyperspell) -> None:
        async with async_client.folders.with_streaming_response.delete_policy(
            policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderDeletePolicyResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_policy(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.folders.with_raw_response.delete_policy(
                policy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.folders.with_raw_response.delete_policy(
                policy_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list_policies(self, async_client: AsyncHyperspell) -> None:
        folder = await async_client.folders.list_policies(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FolderListPoliciesResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_list_policies(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.folders.with_raw_response.list_policies(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListPoliciesResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_list_policies(self, async_client: AsyncHyperspell) -> None:
        async with async_client.folders.with_streaming_response.list_policies(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListPoliciesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_policies(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.folders.with_raw_response.list_policies(
                "",
            )

    @parametrize
    async def test_method_set_policies(self, async_client: AsyncHyperspell) -> None:
        folder = await async_client.folders.set_policies(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_folder_id="provider_folder_id",
            sync_mode="sync",
        )
        assert_matches_type(FolderSetPoliciesResponse, folder, path=["response"])

    @parametrize
    async def test_method_set_policies_with_all_params(self, async_client: AsyncHyperspell) -> None:
        folder = await async_client.folders.set_policies(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_folder_id="provider_folder_id",
            sync_mode="sync",
            folder_name="folder_name",
            folder_path="folder_path",
            parent_folder_id="parent_folder_id",
        )
        assert_matches_type(FolderSetPoliciesResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_set_policies(self, async_client: AsyncHyperspell) -> None:
        response = await async_client.folders.with_raw_response.set_policies(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_folder_id="provider_folder_id",
            sync_mode="sync",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderSetPoliciesResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_set_policies(self, async_client: AsyncHyperspell) -> None:
        async with async_client.folders.with_streaming_response.set_policies(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_folder_id="provider_folder_id",
            sync_mode="sync",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderSetPoliciesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_policies(self, async_client: AsyncHyperspell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.folders.with_raw_response.set_policies(
                connection_id="",
                provider_folder_id="provider_folder_id",
                sync_mode="sync",
            )
