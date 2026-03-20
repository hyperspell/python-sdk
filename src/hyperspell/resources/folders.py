# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import folder_list_params, folder_set_policies_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.folder_list_response import FolderListResponse
from ..types.folder_set_policies_response import FolderSetPoliciesResponse
from ..types.folder_delete_policy_response import FolderDeletePolicyResponse
from ..types.folder_list_policies_response import FolderListPoliciesResponse

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)

    def list(
        self,
        connection_id: str,
        *,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """
        List one level of folders from the user's connected source.

        Returns folders decorated with their explicit folder policy (if any). Use
        parent_id to drill into subfolders.

        Args:
          parent_id: Parent folder ID. Omit for root-level folders.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            path_template("/connections/{connection_id}/folders", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"parent_id": parent_id}, folder_list_params.FolderListParams),
            ),
            cast_to=FolderListResponse,
        )

    def delete_policy(
        self,
        policy_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeletePolicyResponse:
        """
        Delete a folder policy for a specific connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._delete(
            path_template(
                "/connections/{connection_id}/folder-policies/{policy_id}",
                connection_id=connection_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeletePolicyResponse,
        )

    def list_policies(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListPoliciesResponse:
        """
        List all folder policies for a specific connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            path_template("/connections/{connection_id}/folder-policies", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderListPoliciesResponse,
        )

    def set_policies(
        self,
        connection_id: str,
        *,
        provider_folder_id: str,
        sync_mode: Literal["sync", "skip", "manual"],
        folder_name: Optional[str] | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        parent_folder_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderSetPoliciesResponse:
        """
        Create or update a folder policy for a specific connection.

        Args:
          provider_folder_id: Folder ID from the source provider

          sync_mode: Sync mode for this folder

          folder_name: Display name of the folder

          folder_path: Display path of the folder

          parent_folder_id: Parent folder's provider ID for inheritance resolution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            path_template("/connections/{connection_id}/folder-policies", connection_id=connection_id),
            body=maybe_transform(
                {
                    "provider_folder_id": provider_folder_id,
                    "sync_mode": sync_mode,
                    "folder_name": folder_name,
                    "folder_path": folder_path,
                    "parent_folder_id": parent_folder_id,
                },
                folder_set_policies_params.FolderSetPoliciesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderSetPoliciesResponse,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hyperspell/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hyperspell/python-sdk#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def list(
        self,
        connection_id: str,
        *,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """
        List one level of folders from the user's connected source.

        Returns folders decorated with their explicit folder policy (if any). Use
        parent_id to drill into subfolders.

        Args:
          parent_id: Parent folder ID. Omit for root-level folders.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            path_template("/connections/{connection_id}/folders", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"parent_id": parent_id}, folder_list_params.FolderListParams),
            ),
            cast_to=FolderListResponse,
        )

    async def delete_policy(
        self,
        policy_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeletePolicyResponse:
        """
        Delete a folder policy for a specific connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._delete(
            path_template(
                "/connections/{connection_id}/folder-policies/{policy_id}",
                connection_id=connection_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeletePolicyResponse,
        )

    async def list_policies(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListPoliciesResponse:
        """
        List all folder policies for a specific connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            path_template("/connections/{connection_id}/folder-policies", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderListPoliciesResponse,
        )

    async def set_policies(
        self,
        connection_id: str,
        *,
        provider_folder_id: str,
        sync_mode: Literal["sync", "skip", "manual"],
        folder_name: Optional[str] | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        parent_folder_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderSetPoliciesResponse:
        """
        Create or update a folder policy for a specific connection.

        Args:
          provider_folder_id: Folder ID from the source provider

          sync_mode: Sync mode for this folder

          folder_name: Display name of the folder

          folder_path: Display path of the folder

          parent_folder_id: Parent folder's provider ID for inheritance resolution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            path_template("/connections/{connection_id}/folder-policies", connection_id=connection_id),
            body=await async_maybe_transform(
                {
                    "provider_folder_id": provider_folder_id,
                    "sync_mode": sync_mode,
                    "folder_name": folder_name,
                    "folder_path": folder_path,
                    "parent_folder_id": parent_folder_id,
                },
                folder_set_policies_params.FolderSetPoliciesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderSetPoliciesResponse,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.list = to_raw_response_wrapper(
            folders.list,
        )
        self.delete_policy = to_raw_response_wrapper(
            folders.delete_policy,
        )
        self.list_policies = to_raw_response_wrapper(
            folders.list_policies,
        )
        self.set_policies = to_raw_response_wrapper(
            folders.set_policies,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.list = async_to_raw_response_wrapper(
            folders.list,
        )
        self.delete_policy = async_to_raw_response_wrapper(
            folders.delete_policy,
        )
        self.list_policies = async_to_raw_response_wrapper(
            folders.list_policies,
        )
        self.set_policies = async_to_raw_response_wrapper(
            folders.set_policies,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.list = to_streamed_response_wrapper(
            folders.list,
        )
        self.delete_policy = to_streamed_response_wrapper(
            folders.delete_policy,
        )
        self.list_policies = to_streamed_response_wrapper(
            folders.list_policies,
        )
        self.set_policies = to_streamed_response_wrapper(
            folders.set_policies,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.list = async_to_streamed_response_wrapper(
            folders.list,
        )
        self.delete_policy = async_to_streamed_response_wrapper(
            folders.delete_policy,
        )
        self.list_policies = async_to_streamed_response_wrapper(
            folders.list_policies,
        )
        self.set_policies = async_to_streamed_response_wrapper(
            folders.set_policies,
        )
