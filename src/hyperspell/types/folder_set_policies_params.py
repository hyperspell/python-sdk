# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FolderSetPoliciesParams"]


class FolderSetPoliciesParams(TypedDict, total=False):
    provider_folder_id: Required[str]
    """Folder ID from the source provider"""

    sync_mode: Required[Literal["sync", "skip", "manual"]]
    """Sync mode for this folder"""

    folder_name: Optional[str]
    """Display name of the folder"""

    folder_path: Optional[str]
    """Display path of the folder"""

    parent_folder_id: Optional[str]
    """Parent folder's provider ID for inheritance resolution"""
