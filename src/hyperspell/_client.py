# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import auth, vaults, evaluate, memories
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, HyperspellError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.integrations import integrations

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Hyperspell",
    "AsyncHyperspell",
    "Client",
    "AsyncClient",
]


class Hyperspell(SyncAPIClient):
    integrations: integrations.IntegrationsResource
    memories: memories.MemoriesResource
    evaluate: evaluate.EvaluateResource
    vaults: vaults.VaultsResource
    auth: auth.AuthResource
    with_raw_response: HyperspellWithRawResponse
    with_streaming_response: HyperspellWithStreamedResponse

    # client options
    api_key: str
    user_id: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        user_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Hyperspell client instance.

        This automatically infers the `api_key` argument from the `HYPERSPELL_TOKEN` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HYPERSPELL_TOKEN")
        if api_key is None:
            raise HyperspellError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HYPERSPELL_TOKEN environment variable"
            )
        self.api_key = api_key

        self.user_id = user_id

        if base_url is None:
            base_url = os.environ.get("HYPERSPELL_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hyperspell.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.integrations = integrations.IntegrationsResource(self)
        self.memories = memories.MemoriesResource(self)
        self.evaluate = evaluate.EvaluateResource(self)
        self.vaults = vaults.VaultsResource(self)
        self.auth = auth.AuthResource(self)
        self.with_raw_response = HyperspellWithRawResponse(self)
        self.with_streaming_response = HyperspellWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._as_user}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _as_user(self) -> dict[str, str]:
        user_id = self.user_id
        if user_id is None:
            return {}
        return {"X-As-User": user_id}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        user_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            user_id=user_id or self.user_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHyperspell(AsyncAPIClient):
    integrations: integrations.AsyncIntegrationsResource
    memories: memories.AsyncMemoriesResource
    evaluate: evaluate.AsyncEvaluateResource
    vaults: vaults.AsyncVaultsResource
    auth: auth.AsyncAuthResource
    with_raw_response: AsyncHyperspellWithRawResponse
    with_streaming_response: AsyncHyperspellWithStreamedResponse

    # client options
    api_key: str
    user_id: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        user_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncHyperspell client instance.

        This automatically infers the `api_key` argument from the `HYPERSPELL_TOKEN` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HYPERSPELL_TOKEN")
        if api_key is None:
            raise HyperspellError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HYPERSPELL_TOKEN environment variable"
            )
        self.api_key = api_key

        self.user_id = user_id

        if base_url is None:
            base_url = os.environ.get("HYPERSPELL_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hyperspell.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.integrations = integrations.AsyncIntegrationsResource(self)
        self.memories = memories.AsyncMemoriesResource(self)
        self.evaluate = evaluate.AsyncEvaluateResource(self)
        self.vaults = vaults.AsyncVaultsResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.with_raw_response = AsyncHyperspellWithRawResponse(self)
        self.with_streaming_response = AsyncHyperspellWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._as_user}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _as_user(self) -> dict[str, str]:
        user_id = self.user_id
        if user_id is None:
            return {}
        return {"X-As-User": user_id}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        user_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            user_id=user_id or self.user_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HyperspellWithRawResponse:
    def __init__(self, client: Hyperspell) -> None:
        self.integrations = integrations.IntegrationsResourceWithRawResponse(client.integrations)
        self.memories = memories.MemoriesResourceWithRawResponse(client.memories)
        self.evaluate = evaluate.EvaluateResourceWithRawResponse(client.evaluate)
        self.vaults = vaults.VaultsResourceWithRawResponse(client.vaults)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)


class AsyncHyperspellWithRawResponse:
    def __init__(self, client: AsyncHyperspell) -> None:
        self.integrations = integrations.AsyncIntegrationsResourceWithRawResponse(client.integrations)
        self.memories = memories.AsyncMemoriesResourceWithRawResponse(client.memories)
        self.evaluate = evaluate.AsyncEvaluateResourceWithRawResponse(client.evaluate)
        self.vaults = vaults.AsyncVaultsResourceWithRawResponse(client.vaults)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)


class HyperspellWithStreamedResponse:
    def __init__(self, client: Hyperspell) -> None:
        self.integrations = integrations.IntegrationsResourceWithStreamingResponse(client.integrations)
        self.memories = memories.MemoriesResourceWithStreamingResponse(client.memories)
        self.evaluate = evaluate.EvaluateResourceWithStreamingResponse(client.evaluate)
        self.vaults = vaults.VaultsResourceWithStreamingResponse(client.vaults)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)


class AsyncHyperspellWithStreamedResponse:
    def __init__(self, client: AsyncHyperspell) -> None:
        self.integrations = integrations.AsyncIntegrationsResourceWithStreamingResponse(client.integrations)
        self.memories = memories.AsyncMemoriesResourceWithStreamingResponse(client.memories)
        self.evaluate = evaluate.AsyncEvaluateResourceWithStreamingResponse(client.evaluate)
        self.vaults = vaults.AsyncVaultsResourceWithStreamingResponse(client.vaults)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)


Client = Hyperspell

AsyncClient = AsyncHyperspell
