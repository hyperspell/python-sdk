# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AuthUserTokenParams"]


class AuthUserTokenParams(TypedDict, total=False):
    user_id: Required[str]

    expires_in: Optional[str]
    """Token lifetime, e.g., '30m', '2h', '1d'. Defaults to 24 hours if not provided."""

    origin: Optional[str]
    """Origin of the request, used for CSRF protection.

    If set, the token will only be valid for requests originating from this origin.
    """
