# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .metadata import Metadata
from ..._compat import PYDANTIC_V1
from ..._models import BaseModel

__all__ = ["List", "Child"]

if typing.TYPE_CHECKING or not PYDANTIC_V1:
    Child = TypeAliasType("Child", typing.Union["ListItem", "ToDo"])
else:
    Child: TypeAlias = typing.Union["ListItem", "ToDo"]


class List(BaseModel):
    id: typing.Optional[str] = None

    children: typing.Optional[typing.List[Child]] = None

    metadata: typing.Optional[Metadata] = None
    """Per-block annotations carried by any Hyperdoc node (ENG-1390).

    Out-of-band annotations that travel with a block but aren't part of its content:
    provenance (`sources`) and human edit attribution (`edited_by`). New annotation
    types get added here as typed fields as the need arises.

    Empty by default. Because `Node.model_dump` forces `exclude_none=True`, an unset
    `metadata` (None) is dropped from serialization entirely, and within a populated
    `Metadata` only the set keys survive.
    """

    ordered: typing.Optional[bool] = None

    text: typing.Optional[str] = None

    type: typing.Optional[Literal["list"]] = None


from .to_do import ToDo
from .list_item import ListItem
