# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["Blob"]


class Blob(BaseModel):
    """Represents embedded binary data using data URI scheme.

    Format: data:[<media type>][;base64],<data>
    Example: data:text/html;base64,PGh0bWw+...
    """

    data: str

    mimetype: str

    id: Optional[str] = None

    metadata: Optional[Metadata] = None
    """Optional annotations carried by a hyperdoc node.

    Includes source provenance and human edit attribution. Unset metadata is omitted
    from serialized responses.
    """

    type: Optional[Literal["blob"]] = None
