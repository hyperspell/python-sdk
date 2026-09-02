# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ConfigUpdateParams", "Structure", "StructureCompany", "StructureWorkstream"]


class ConfigUpdateParams(TypedDict, total=False):
    company_prompts: Optional[Dict[str, str]]

    detection_prompt: Optional[str]

    domain: Optional[str]

    personal_prompt: Optional[str]

    source_weights: Optional[Dict[str, str]]

    structure: Optional[Structure]
    """Per-tier document definitions for custom generation."""

    workstream_prompts: Optional[Dict[str, str]]


class StructureCompany(TypedDict, total=False):
    """
    One document in a context-tree tier: what to generate and how to retrieve for it.
    """

    filename: Required[str]

    key: Required[str]

    prompt: Required[str]

    search_queries: Required[SequenceNotStr[str]]


class StructureWorkstream(TypedDict, total=False):
    """
    One document in a context-tree tier: what to generate and how to retrieve for it.
    """

    filename: Required[str]

    key: Required[str]

    prompt: Required[str]

    search_queries: Required[SequenceNotStr[str]]


class Structure(TypedDict, total=False):
    """Per-tier document definitions for custom generation."""

    company: Optional[Iterable[StructureCompany]]

    workstream: Optional[Iterable[StructureWorkstream]]
