# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing
from typing_extensions import Literal, Annotated, TypeAlias, TypeAliasType

from ..._utils import PropertyInfo
from .metadata import Metadata
from ..._compat import PYDANTIC_V1
from ..._models import BaseModel

__all__ = ["List", "Child"]

if typing.TYPE_CHECKING or not PYDANTIC_V1:
    Child = TypeAliasType("Child", Annotated[typing.Union["ListItem", "ToDo"], PropertyInfo(discriminator="type")])
else:
    Child: TypeAlias = Annotated[typing.Union["ListItem", "ToDo"], PropertyInfo(discriminator="type")]


class List(BaseModel):
    id: typing.Optional[str] = None

    children: typing.Optional[typing.List[Child]] = None

    metadata: typing.Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    ordered: typing.Optional[bool] = None

    text: typing.Optional[str] = None

    type: typing.Optional[Literal["list"]] = None


from .to_do import ToDo
from .list_item import ListItem
