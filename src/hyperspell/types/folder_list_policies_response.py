# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FolderListPoliciesResponse", "Policy"]


class Policy(BaseModel):
    id: str
    """Unique policy ID"""

    provider_folder_id: str
    """Folder ID from the source provider"""

    sync_mode: Literal["sync", "skip", "manual"]
    """Sync mode for this folder"""

    connection_id: Optional[str] = None
    """Connection ID (null for integration defaults)"""

    folder_name: Optional[str] = None
    """Display name of the folder"""

    folder_path: Optional[str] = None
    """Display path of the folder"""

    parent_folder_id: Optional[str] = None
    """Parent folder's provider ID"""


class FolderListPoliciesResponse(BaseModel):
    policies: List[Policy]
    """List of folder policies"""
