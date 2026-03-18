# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FolderDeletePolicyResponse"]


class FolderDeletePolicyResponse(BaseModel):
    success: bool
    """Whether the deletion was successful"""
