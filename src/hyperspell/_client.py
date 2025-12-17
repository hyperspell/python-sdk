# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, HyperspellError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import auth, vaults, evaluate, memories, connections, integrations
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.vaults import VaultsResource, AsyncVaultsResource
    from .resources.evaluate import EvaluateResource, AsyncEvaluateResource
    from .resources.memories import MemoriesResource, AsyncMemoriesResource
    from .resources.connections import ConnectionsResource, AsyncConnectionsResource
    from .resources.integrations.integrations import IntegrationsResource, AsyncIntegrationsResource

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

        This automatically infers the `api_key` argument from the `HYPERSPELL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HYPERSPELL_API_KEY")
        if api_key is None:
            raise HyperspellError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HYPERSPELL_API_KEY environment variable"
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

    @cached_property
    def connections(self) -> ConnectionsResource:
        from .resources.connections import ConnectionsResource

        return ConnectionsResource(self)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        from .resources.integrations import IntegrationsResource

        return IntegrationsResource(self)

    @cached_property
    def memories(self) -> MemoriesResource:
        from .resources.memories import MemoriesResource

        return MemoriesResource(self)

    @cached_property
    def evaluate(self) -> EvaluateResource:
        from .resources.evaluate import EvaluateResource

        return EvaluateResource(self)

    @cached_property
    def vaults(self) -> VaultsResource:
        from .resources.vaults import VaultsResource

        return VaultsResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def with_raw_response(self) -> HyperspellWithRawResponse:
        return HyperspellWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HyperspellWithStreamedResponse:
        return HyperspellWithStreamedResponse(self)

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

        This automatically infers the `api_key` argument from the `HYPERSPELL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HYPERSPELL_API_KEY")
        if api_key is None:
            raise HyperspellError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HYPERSPELL_API_KEY environment variable"
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

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        from .resources.connections import AsyncConnectionsResource

        return AsyncConnectionsResource(self)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        from .resources.integrations import AsyncIntegrationsResource

        return AsyncIntegrationsResource(self)

    @cached_property
    def memories(self) -> AsyncMemoriesResource:
        from .resources.memories import AsyncMemoriesResource

        return AsyncMemoriesResource(self)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResource:
        from .resources.evaluate import AsyncEvaluateResource

        return AsyncEvaluateResource(self)

    @cached_property
    def vaults(self) -> AsyncVaultsResource:
        from .resources.vaults import AsyncVaultsResource

        return AsyncVaultsResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncHyperspellWithRawResponse:
        return AsyncHyperspellWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHyperspellWithStreamedResponse:
        return AsyncHyperspellWithStreamedResponse(self)

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
    _client: Hyperspell

    def __init__(self, client: Hyperspell) -> None:
        self._client = client

    @cached_property
    def connections(self) -> connections.ConnectionsResourceWithRawResponse:
        from .resources.connections import ConnectionsResourceWithRawResponse

        return ConnectionsResourceWithRawResponse(self._client.connections)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithRawResponse:
        from .resources.integrations import IntegrationsResourceWithRawResponse

        return IntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def memories(self) -> memories.MemoriesResourceWithRawResponse:
        from .resources.memories import MemoriesResourceWithRawResponse

        return MemoriesResourceWithRawResponse(self._client.memories)

    @cached_property
    def evaluate(self) -> evaluate.EvaluateResourceWithRawResponse:
        from .resources.evaluate import EvaluateResourceWithRawResponse

        return EvaluateResourceWithRawResponse(self._client.evaluate)

    @cached_property
    def vaults(self) -> vaults.VaultsResourceWithRawResponse:
        from .resources.vaults import VaultsResourceWithRawResponse

        return VaultsResourceWithRawResponse(self._client.vaults)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)


class AsyncHyperspellWithRawResponse:
    _client: AsyncHyperspell

    def __init__(self, client: AsyncHyperspell) -> None:
        self._client = client

    @cached_property
    def connections(self) -> connections.AsyncConnectionsResourceWithRawResponse:
        from .resources.connections import AsyncConnectionsResourceWithRawResponse

        return AsyncConnectionsResourceWithRawResponse(self._client.connections)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithRawResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithRawResponse

        return AsyncIntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def memories(self) -> memories.AsyncMemoriesResourceWithRawResponse:
        from .resources.memories import AsyncMemoriesResourceWithRawResponse

        return AsyncMemoriesResourceWithRawResponse(self._client.memories)

    @cached_property
    def evaluate(self) -> evaluate.AsyncEvaluateResourceWithRawResponse:
        from .resources.evaluate import AsyncEvaluateResourceWithRawResponse

        return AsyncEvaluateResourceWithRawResponse(self._client.evaluate)

    @cached_property
    def vaults(self) -> vaults.AsyncVaultsResourceWithRawResponse:
        from .resources.vaults import AsyncVaultsResourceWithRawResponse

        return AsyncVaultsResourceWithRawResponse(self._client.vaults)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)


class HyperspellWithStreamedResponse:
    _client: Hyperspell

    def __init__(self, client: Hyperspell) -> None:
        self._client = client

    @cached_property
    def connections(self) -> connections.ConnectionsResourceWithStreamingResponse:
        from .resources.connections import ConnectionsResourceWithStreamingResponse

        return ConnectionsResourceWithStreamingResponse(self._client.connections)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithStreamingResponse:
        from .resources.integrations import IntegrationsResourceWithStreamingResponse

        return IntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def memories(self) -> memories.MemoriesResourceWithStreamingResponse:
        from .resources.memories import MemoriesResourceWithStreamingResponse

        return MemoriesResourceWithStreamingResponse(self._client.memories)

    @cached_property
    def evaluate(self) -> evaluate.EvaluateResourceWithStreamingResponse:
        from .resources.evaluate import EvaluateResourceWithStreamingResponse

        return EvaluateResourceWithStreamingResponse(self._client.evaluate)

    @cached_property
    def vaults(self) -> vaults.VaultsResourceWithStreamingResponse:
        from .resources.vaults import VaultsResourceWithStreamingResponse

        return VaultsResourceWithStreamingResponse(self._client.vaults)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)


class AsyncHyperspellWithStreamedResponse:
    _client: AsyncHyperspell

    def __init__(self, client: AsyncHyperspell) -> None:
        self._client = client

    @cached_property
    def connections(self) -> connections.AsyncConnectionsResourceWithStreamingResponse:
        from .resources.connections import AsyncConnectionsResourceWithStreamingResponse

        return AsyncConnectionsResourceWithStreamingResponse(self._client.connections)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithStreamingResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithStreamingResponse

        return AsyncIntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def memories(self) -> memories.AsyncMemoriesResourceWithStreamingResponse:
        from .resources.memories import AsyncMemoriesResourceWithStreamingResponse

        return AsyncMemoriesResourceWithStreamingResponse(self._client.memories)

    @cached_property
    def evaluate(self) -> evaluate.AsyncEvaluateResourceWithStreamingResponse:
        from .resources.evaluate import AsyncEvaluateResourceWithStreamingResponse

        return AsyncEvaluateResourceWithStreamingResponse(self._client.evaluate)

    @cached_property
    def vaults(self) -> vaults.AsyncVaultsResourceWithStreamingResponse:
        from .resources.vaults import AsyncVaultsResourceWithStreamingResponse

        return AsyncVaultsResourceWithStreamingResponse(self._client.vaults)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)


Client = Hyperspell

AsyncClient = AsyncHyperspell
