# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import (
    shared,
    memory_get_response,
    live_search_response,
    memory_list_response,
    live_get_resource_response,
    live_list_resources_response,
)
from .. import _compat
from .token import Token as Token
from .shared import (
    Blob as Blob,
    Code as Code,
    Deal as Deal,
    File as File,
    Link as Link,
    List as List,
    Page as Page,
    Task as Task,
    Text as Text,
    ToDo as ToDo,
    Chunk as Chunk,
    Event as Event,
    Image as Image,
    Quote as Quote,
    Table as Table,
    Trace as Trace,
    Person as Person,
    Callout as Callout,
    Comment as Comment,
    Company as Company,
    Divider as Divider,
    Heading as Heading,
    Message as Message,
    Website as Website,
    Document as Document,
    Equation as Equation,
    Footnote as Footnote,
    ListItem as ListItem,
    Metadata as Metadata,
    TableRow as TableRow,
    ToolCall as ToolCall,
    LineBreak as LineBreak,
    Paragraph as Paragraph,
    TableCell as TableCell,
    Utterance as Utterance,
    Provenance as Provenance,
    ToolResult as ToolResult,
    Transcript as Transcript,
    QueryResult as QueryResult,
    Conversation as Conversation,
    TraceMessage as TraceMessage,
    ProvenanceStep as ProvenanceStep,
    ProvenanceEntity as ProvenanceEntity,
    ProvenanceSource as ProvenanceSource,
    ScoredDocumentResponse as ScoredDocumentResponse,
)
from .memory_status import MemoryStatus as MemoryStatus
from .auth_me_response import AuthMeResponse as AuthMeResponse
from .memory_add_params import MemoryAddParams as MemoryAddParams
from .memory_get_params import MemoryGetParams as MemoryGetParams
from .vault_list_params import VaultListParams as VaultListParams
from .entity_list_params import EntityListParams as EntityListParams
from .folder_list_params import FolderListParams as FolderListParams
from .live_search_params import LiveSearchParams as LiveSearchParams
from .memory_list_params import MemoryListParams as MemoryListParams
from .session_add_params import SessionAddParams as SessionAddParams
from .entity_get_response import EntityGetResponse as EntityGetResponse
from .memory_get_response import MemoryGetResponse as MemoryGetResponse
from .vault_list_response import VaultListResponse as VaultListResponse
from .entity_list_response import EntityListResponse as EntityListResponse
from .entity_search_params import EntitySearchParams as EntitySearchParams
from .folder_list_response import FolderListResponse as FolderListResponse
from .live_search_response import LiveSearchResponse as LiveSearchResponse
from .memory_list_response import MemoryListResponse as MemoryListResponse
from .memory_search_params import MemorySearchParams as MemorySearchParams
from .memory_update_params import MemoryUpdateParams as MemoryUpdateParams
from .memory_upload_params import MemoryUploadParams as MemoryUploadParams
from .auth_user_token_params import AuthUserTokenParams as AuthUserTokenParams
from .entity_search_response import EntitySearchResponse as EntitySearchResponse
from .memory_add_bulk_params import MemoryAddBulkParams as MemoryAddBulkParams
from .memory_delete_response import MemoryDeleteResponse as MemoryDeleteResponse
from .memory_status_response import MemoryStatusResponse as MemoryStatusResponse
from .connection_list_response import ConnectionListResponse as ConnectionListResponse
from .live_get_resource_params import LiveGetResourceParams as LiveGetResourceParams
from .memory_add_bulk_response import MemoryAddBulkResponse as MemoryAddBulkResponse
from .auth_delete_user_response import AuthDeleteUserResponse as AuthDeleteUserResponse
from .integration_list_response import IntegrationListResponse as IntegrationListResponse
from .action_add_reaction_params import ActionAddReactionParams as ActionAddReactionParams
from .action_send_message_params import ActionSendMessageParams as ActionSendMessageParams
from .connection_revoke_response import ConnectionRevokeResponse as ConnectionRevokeResponse
from .folder_set_policies_params import FolderSetPoliciesParams as FolderSetPoliciesParams
from .integration_connect_params import IntegrationConnectParams as IntegrationConnectParams
from .live_get_resource_response import LiveGetResourceResponse as LiveGetResourceResponse
from .live_list_resources_params import LiveListResourcesParams as LiveListResourcesParams
from .live_list_sources_response import LiveListSourcesResponse as LiveListSourcesResponse
from .evaluate_score_query_params import EvaluateScoreQueryParams as EvaluateScoreQueryParams
from .action_add_reaction_response import ActionAddReactionResponse as ActionAddReactionResponse
from .action_send_message_response import ActionSendMessageResponse as ActionSendMessageResponse
from .evaluate_list_queries_params import EvaluateListQueriesParams as EvaluateListQueriesParams
from .folder_set_policies_response import FolderSetPoliciesResponse as FolderSetPoliciesResponse
from .integration_connect_response import IntegrationConnectResponse as IntegrationConnectResponse
from .live_list_resources_response import LiveListResourcesResponse as LiveListResourcesResponse
from .evaluate_score_query_response import EvaluateScoreQueryResponse as EvaluateScoreQueryResponse
from .folder_delete_policy_response import FolderDeletePolicyResponse as FolderDeletePolicyResponse
from .folder_list_policies_response import FolderListPoliciesResponse as FolderListPoliciesResponse
from .evaluate_list_queries_response import EvaluateListQueriesResponse as EvaluateListQueriesResponse
from .evaluate_score_highlight_params import EvaluateScoreHighlightParams as EvaluateScoreHighlightParams
from .evaluate_score_highlight_response import EvaluateScoreHighlightResponse as EvaluateScoreHighlightResponse

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    live_get_resource_response.DocumentDocumentInvoice.update_forward_refs()  # type: ignore
    live_get_resource_response.DocumentChunk.update_forward_refs()  # type: ignore
    live_get_resource_response.Document.update_forward_refs()  # type: ignore
    live_get_resource_response.LiveGetResourceResponse.update_forward_refs()  # type: ignore
    live_list_resources_response.DocumentInvoice.update_forward_refs()  # type: ignore
    live_list_resources_response.Chunk.update_forward_refs()  # type: ignore
    live_list_resources_response.LiveListResourcesResponse.update_forward_refs()  # type: ignore
    live_search_response.DocumentDocumentInvoice.update_forward_refs()  # type: ignore
    live_search_response.DocumentChunk.update_forward_refs()  # type: ignore
    live_search_response.Document.update_forward_refs()  # type: ignore
    live_search_response.LiveSearchResponse.update_forward_refs()  # type: ignore
    memory_list_response.DocumentInvoice.update_forward_refs()  # type: ignore
    memory_list_response.Chunk.update_forward_refs()  # type: ignore
    memory_list_response.MemoryListResponse.update_forward_refs()  # type: ignore
    memory_get_response.DocumentInvoice.update_forward_refs()  # type: ignore
    memory_get_response.Chunk.update_forward_refs()  # type: ignore
    memory_get_response.MemoryGetResponse.update_forward_refs()  # type: ignore
    shared.callout.Callout.update_forward_refs()  # type: ignore
    shared.chunk.Chunk.update_forward_refs()  # type: ignore
    shared.company.Company.update_forward_refs()  # type: ignore
    shared.conversation.Conversation.update_forward_refs()  # type: ignore
    shared.deal.Deal.update_forward_refs()  # type: ignore
    shared.document.Document.update_forward_refs()  # type: ignore
    shared.equation.Equation.update_forward_refs()  # type: ignore
    shared.event.Event.update_forward_refs()  # type: ignore
    shared.file.File.update_forward_refs()  # type: ignore
    shared.footnote.Footnote.update_forward_refs()  # type: ignore
    shared.heading.Heading.update_forward_refs()  # type: ignore
    shared.list.List.update_forward_refs()  # type: ignore
    shared.list_item.ListItem.update_forward_refs()  # type: ignore
    shared.message.Message.update_forward_refs()  # type: ignore
    shared.page.Page.update_forward_refs()  # type: ignore
    shared.paragraph.Paragraph.update_forward_refs()  # type: ignore
    shared.person.Person.update_forward_refs()  # type: ignore
    shared.query_result.QueryResult.update_forward_refs()  # type: ignore
    shared.quote.Quote.update_forward_refs()  # type: ignore
    shared.scored_document_response.DocumentInvoice.update_forward_refs()  # type: ignore
    shared.scored_document_response.Chunk.update_forward_refs()  # type: ignore
    shared.scored_document_response.ScoredDocumentResponse.update_forward_refs()  # type: ignore
    shared.table.Table.update_forward_refs()  # type: ignore
    shared.table_cell.TableCell.update_forward_refs()  # type: ignore
    shared.table_row.TableRow.update_forward_refs()  # type: ignore
    shared.task.Task.update_forward_refs()  # type: ignore
    shared.to_do.ToDo.update_forward_refs()  # type: ignore
    shared.transcript.Transcript.update_forward_refs()  # type: ignore
    shared.utterance.Utterance.update_forward_refs()  # type: ignore
    shared.website.Website.update_forward_refs()  # type: ignore
else:
    live_get_resource_response.DocumentDocumentInvoice.model_rebuild(_parent_namespace_depth=0)
    live_get_resource_response.DocumentChunk.model_rebuild(_parent_namespace_depth=0)
    live_get_resource_response.Document.model_rebuild(_parent_namespace_depth=0)
    live_get_resource_response.LiveGetResourceResponse.model_rebuild(_parent_namespace_depth=0)
    live_list_resources_response.DocumentInvoice.model_rebuild(_parent_namespace_depth=0)
    live_list_resources_response.Chunk.model_rebuild(_parent_namespace_depth=0)
    live_list_resources_response.LiveListResourcesResponse.model_rebuild(_parent_namespace_depth=0)
    live_search_response.DocumentDocumentInvoice.model_rebuild(_parent_namespace_depth=0)
    live_search_response.DocumentChunk.model_rebuild(_parent_namespace_depth=0)
    live_search_response.Document.model_rebuild(_parent_namespace_depth=0)
    live_search_response.LiveSearchResponse.model_rebuild(_parent_namespace_depth=0)
    memory_list_response.DocumentInvoice.model_rebuild(_parent_namespace_depth=0)
    memory_list_response.Chunk.model_rebuild(_parent_namespace_depth=0)
    memory_list_response.MemoryListResponse.model_rebuild(_parent_namespace_depth=0)
    memory_get_response.DocumentInvoice.model_rebuild(_parent_namespace_depth=0)
    memory_get_response.Chunk.model_rebuild(_parent_namespace_depth=0)
    memory_get_response.MemoryGetResponse.model_rebuild(_parent_namespace_depth=0)
    shared.callout.Callout.model_rebuild(_parent_namespace_depth=0)
    shared.chunk.Chunk.model_rebuild(_parent_namespace_depth=0)
    shared.company.Company.model_rebuild(_parent_namespace_depth=0)
    shared.conversation.Conversation.model_rebuild(_parent_namespace_depth=0)
    shared.deal.Deal.model_rebuild(_parent_namespace_depth=0)
    shared.document.Document.model_rebuild(_parent_namespace_depth=0)
    shared.equation.Equation.model_rebuild(_parent_namespace_depth=0)
    shared.event.Event.model_rebuild(_parent_namespace_depth=0)
    shared.file.File.model_rebuild(_parent_namespace_depth=0)
    shared.footnote.Footnote.model_rebuild(_parent_namespace_depth=0)
    shared.heading.Heading.model_rebuild(_parent_namespace_depth=0)
    shared.list.List.model_rebuild(_parent_namespace_depth=0)
    shared.list_item.ListItem.model_rebuild(_parent_namespace_depth=0)
    shared.message.Message.model_rebuild(_parent_namespace_depth=0)
    shared.page.Page.model_rebuild(_parent_namespace_depth=0)
    shared.paragraph.Paragraph.model_rebuild(_parent_namespace_depth=0)
    shared.person.Person.model_rebuild(_parent_namespace_depth=0)
    shared.query_result.QueryResult.model_rebuild(_parent_namespace_depth=0)
    shared.quote.Quote.model_rebuild(_parent_namespace_depth=0)
    shared.scored_document_response.DocumentInvoice.model_rebuild(_parent_namespace_depth=0)
    shared.scored_document_response.Chunk.model_rebuild(_parent_namespace_depth=0)
    shared.scored_document_response.ScoredDocumentResponse.model_rebuild(_parent_namespace_depth=0)
    shared.table.Table.model_rebuild(_parent_namespace_depth=0)
    shared.table_cell.TableCell.model_rebuild(_parent_namespace_depth=0)
    shared.table_row.TableRow.model_rebuild(_parent_namespace_depth=0)
    shared.task.Task.model_rebuild(_parent_namespace_depth=0)
    shared.to_do.ToDo.model_rebuild(_parent_namespace_depth=0)
    shared.transcript.Transcript.model_rebuild(_parent_namespace_depth=0)
    shared.utterance.Utterance.model_rebuild(_parent_namespace_depth=0)
    shared.website.Website.model_rebuild(_parent_namespace_depth=0)
