# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "MemoryStatusResponse",
    "Integration",
    "IntegrationConnection",
    "IntegrationConnectionError",
    "IntegrationError",
]


class IntegrationConnectionError(BaseModel):
    """The current error for a connection.

    ``detail`` contains a sanitized summary suitable for display.
    """

    at: datetime

    detail: Optional[str] = None

    kind: Literal["auth", "rate_limited", "provider", "internal"]
    """Classification of the most recent synchronization or indexing failure."""

    origin: Optional[str] = None

    retry_at: Optional[datetime] = None


class IntegrationConnection(BaseModel):
    """The current health of one connection."""

    id: str

    error: Optional[IntegrationConnectionError] = None
    """The current error for a connection.

    `detail` contains a sanitized summary suitable for display.
    """

    label: Optional[str] = None

    last_activity_at: Optional[datetime] = None

    last_synced_at: Optional[datetime] = None

    status: Literal[
        "broken", "stalled", "error", "rate_limited", "syncing", "connected", "live", "never_synced", "not_connected"
    ]
    """Current health status of a connection or integration."""


class IntegrationError(BaseModel):
    """The current error for a connection.

    ``detail`` contains a sanitized summary suitable for display.
    """

    at: datetime

    detail: Optional[str] = None

    kind: Literal["auth", "rate_limited", "provider", "internal"]
    """Classification of the most recent synchronization or indexing failure."""

    origin: Optional[str] = None

    retry_at: Optional[datetime] = None


class Integration(BaseModel):
    """Health summary for a configured integration.

    ``provider`` uses lowercase snake_case naming (e.g. ``google_drive``).
    """

    connections: List[IntegrationConnection]

    error: Optional[IntegrationError] = None
    """The current error for a connection.

    `detail` contains a sanitized summary suitable for display.
    """

    integration_id: str

    last_synced_at: Optional[datetime] = None

    provider: str

    status: Literal[
        "broken", "stalled", "error", "rate_limited", "syncing", "connected", "live", "never_synced", "not_connected"
    ]
    """Current health status of a connection or integration."""


class MemoryStatusResponse(BaseModel):
    providers: Dict[str, Dict[str, int]]

    total: Dict[str, int]

    integrations: Optional[List[Integration]] = None
