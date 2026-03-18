# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FolderListResponse", "Folder", "FolderPolicy"]


class FolderPolicy(BaseModel):
    """Explicit policy on this folder, or null if inheriting/default"""

    id: str
    """Policy UUID"""

    sync_mode: Literal["sync", "skip", "manual"]
    """Sync mode set on this folder"""


class Folder(BaseModel):
    has_children: bool
    """Whether this folder may have subfolders"""

    name: str
    """Display name of the folder"""

    provider_folder_id: str
    """Folder ID from the source provider"""

    parent_folder_id: Optional[str] = None
    """Parent folder's provider ID"""

    policy: Optional[FolderPolicy] = None
    """Explicit policy on this folder, or null if inheriting/default"""


class FolderListResponse(BaseModel):
    folders: List[Folder]
    """Folders at this level"""
