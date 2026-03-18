# Shared Types

```python
from hyperspell.types import Metadata, Notification, QueryResult, Resource
```

# Connections

Types:

```python
from hyperspell.types import ConnectionListResponse, ConnectionRevokeResponse
```

Methods:

- <code title="get /connections/list">client.connections.<a href="./src/hyperspell/resources/connections.py">list</a>() -> <a href="./src/hyperspell/types/connection_list_response.py">ConnectionListResponse</a></code>
- <code title="delete /connections/{connection_id}/revoke">client.connections.<a href="./src/hyperspell/resources/connections.py">revoke</a>(connection_id) -> <a href="./src/hyperspell/types/connection_revoke_response.py">ConnectionRevokeResponse</a></code>

# Folders

Types:

```python
from hyperspell.types import (
    FolderListResponse,
    FolderDeletePolicyResponse,
    FolderListPoliciesResponse,
    FolderSetPoliciesResponse,
)
```

Methods:

- <code title="get /connections/{connection_id}/folders">client.folders.<a href="./src/hyperspell/resources/folders.py">list</a>(connection_id, \*\*<a href="src/hyperspell/types/folder_list_params.py">params</a>) -> <a href="./src/hyperspell/types/folder_list_response.py">FolderListResponse</a></code>
- <code title="delete /connections/{connection_id}/folder-policies/{policy_id}">client.folders.<a href="./src/hyperspell/resources/folders.py">delete_policy</a>(policy_id, \*, connection_id) -> <a href="./src/hyperspell/types/folder_delete_policy_response.py">FolderDeletePolicyResponse</a></code>
- <code title="get /connections/{connection_id}/folder-policies">client.folders.<a href="./src/hyperspell/resources/folders.py">list_policies</a>(connection_id) -> <a href="./src/hyperspell/types/folder_list_policies_response.py">FolderListPoliciesResponse</a></code>
- <code title="post /connections/{connection_id}/folder-policies">client.folders.<a href="./src/hyperspell/resources/folders.py">set_policies</a>(connection_id, \*\*<a href="src/hyperspell/types/folder_set_policies_params.py">params</a>) -> <a href="./src/hyperspell/types/folder_set_policies_response.py">FolderSetPoliciesResponse</a></code>

# Integrations

Types:

```python
from hyperspell.types import IntegrationListResponse, IntegrationConnectResponse
```

Methods:

- <code title="get /integrations/list">client.integrations.<a href="./src/hyperspell/resources/integrations/integrations.py">list</a>() -> <a href="./src/hyperspell/types/integration_list_response.py">IntegrationListResponse</a></code>
- <code title="get /integrations/{integration_id}/connect">client.integrations.<a href="./src/hyperspell/resources/integrations/integrations.py">connect</a>(integration_id, \*\*<a href="src/hyperspell/types/integration_connect_params.py">params</a>) -> <a href="./src/hyperspell/types/integration_connect_response.py">IntegrationConnectResponse</a></code>

## GoogleCalendar

Types:

```python
from hyperspell.types.integrations import Calendar
```

Methods:

- <code title="get /integrations/google_calendar/list">client.integrations.google_calendar.<a href="./src/hyperspell/resources/integrations/google_calendar.py">list</a>() -> <a href="./src/hyperspell/types/integrations/calendar.py">Calendar</a></code>

## WebCrawler

Types:

```python
from hyperspell.types.integrations import WebCrawlerIndexResponse
```

Methods:

- <code title="get /integrations/web_crawler/index">client.integrations.web_crawler.<a href="./src/hyperspell/resources/integrations/web_crawler.py">index</a>(\*\*<a href="src/hyperspell/types/integrations/web_crawler_index_params.py">params</a>) -> <a href="./src/hyperspell/types/integrations/web_crawler_index_response.py">WebCrawlerIndexResponse</a></code>

## Slack

Methods:

- <code title="get /integrations/slack/list">client.integrations.slack.<a href="./src/hyperspell/resources/integrations/slack.py">list</a>(\*\*<a href="src/hyperspell/types/integrations/slack_list_params.py">params</a>) -> object</code>

# Memories

Types:

```python
from hyperspell.types import (
    Memory,
    MemoryStatus,
    MemoryDeleteResponse,
    MemoryAddBulkResponse,
    MemoryStatusResponse,
)
```

Methods:

- <code title="post /memories/update/{source}/{resource_id}">client.memories.<a href="./src/hyperspell/resources/memories.py">update</a>(resource_id, \*, source, \*\*<a href="src/hyperspell/types/memory_update_params.py">params</a>) -> <a href="./src/hyperspell/types/memory_status.py">MemoryStatus</a></code>
- <code title="get /memories/list">client.memories.<a href="./src/hyperspell/resources/memories.py">list</a>(\*\*<a href="src/hyperspell/types/memory_list_params.py">params</a>) -> <a href="./src/hyperspell/types/shared/resource.py">SyncCursorPage[Resource]</a></code>
- <code title="delete /memories/delete/{source}/{resource_id}">client.memories.<a href="./src/hyperspell/resources/memories.py">delete</a>(resource_id, \*, source) -> <a href="./src/hyperspell/types/memory_delete_response.py">MemoryDeleteResponse</a></code>
- <code title="post /memories/add">client.memories.<a href="./src/hyperspell/resources/memories.py">add</a>(\*\*<a href="src/hyperspell/types/memory_add_params.py">params</a>) -> <a href="./src/hyperspell/types/memory_status.py">MemoryStatus</a></code>
- <code title="post /memories/add/bulk">client.memories.<a href="./src/hyperspell/resources/memories.py">add_bulk</a>(\*\*<a href="src/hyperspell/types/memory_add_bulk_params.py">params</a>) -> <a href="./src/hyperspell/types/memory_add_bulk_response.py">MemoryAddBulkResponse</a></code>
- <code title="get /memories/get/{source}/{resource_id}">client.memories.<a href="./src/hyperspell/resources/memories.py">get</a>(resource_id, \*, source) -> <a href="./src/hyperspell/types/memory.py">Memory</a></code>
- <code title="post /memories/query">client.memories.<a href="./src/hyperspell/resources/memories.py">search</a>(\*\*<a href="src/hyperspell/types/memory_search_params.py">params</a>) -> <a href="./src/hyperspell/types/shared/query_result.py">QueryResult</a></code>
- <code title="get /memories/status">client.memories.<a href="./src/hyperspell/resources/memories.py">status</a>() -> <a href="./src/hyperspell/types/memory_status_response.py">MemoryStatusResponse</a></code>
- <code title="post /memories/upload">client.memories.<a href="./src/hyperspell/resources/memories.py">upload</a>(\*\*<a href="src/hyperspell/types/memory_upload_params.py">params</a>) -> <a href="./src/hyperspell/types/memory_status.py">MemoryStatus</a></code>

# Evaluate

Types:

```python
from hyperspell.types import EvaluateScoreHighlightResponse, EvaluateScoreQueryResponse
```

Methods:

- <code title="get /evaluate/query/{query_id}">client.evaluate.<a href="./src/hyperspell/resources/evaluate.py">get_query</a>(query_id) -> <a href="./src/hyperspell/types/shared/query_result.py">QueryResult</a></code>
- <code title="post /evaluate/highlight/{highlight_id}">client.evaluate.<a href="./src/hyperspell/resources/evaluate.py">score_highlight</a>(highlight_id, \*\*<a href="src/hyperspell/types/evaluate_score_highlight_params.py">params</a>) -> <a href="./src/hyperspell/types/evaluate_score_highlight_response.py">EvaluateScoreHighlightResponse</a></code>
- <code title="post /evaluate/query/{query_id}">client.evaluate.<a href="./src/hyperspell/resources/evaluate.py">score_query</a>(query_id, \*\*<a href="src/hyperspell/types/evaluate_score_query_params.py">params</a>) -> <a href="./src/hyperspell/types/evaluate_score_query_response.py">EvaluateScoreQueryResponse</a></code>

# Actions

Types:

```python
from hyperspell.types import ActionAddReactionResponse, ActionSendMessageResponse
```

Methods:

- <code title="post /actions/add_reaction">client.actions.<a href="./src/hyperspell/resources/actions.py">add_reaction</a>(\*\*<a href="src/hyperspell/types/action_add_reaction_params.py">params</a>) -> <a href="./src/hyperspell/types/action_add_reaction_response.py">ActionAddReactionResponse</a></code>
- <code title="post /actions/send_message">client.actions.<a href="./src/hyperspell/resources/actions.py">send_message</a>(\*\*<a href="src/hyperspell/types/action_send_message_params.py">params</a>) -> <a href="./src/hyperspell/types/action_send_message_response.py">ActionSendMessageResponse</a></code>

# Sessions

Methods:

- <code title="post /trace/add">client.sessions.<a href="./src/hyperspell/resources/sessions.py">add</a>(\*\*<a href="src/hyperspell/types/session_add_params.py">params</a>) -> <a href="./src/hyperspell/types/memory_status.py">MemoryStatus</a></code>

# Vaults

Types:

```python
from hyperspell.types import VaultListResponse
```

Methods:

- <code title="get /vault/list">client.vaults.<a href="./src/hyperspell/resources/vaults.py">list</a>(\*\*<a href="src/hyperspell/types/vault_list_params.py">params</a>) -> <a href="./src/hyperspell/types/vault_list_response.py">SyncCursorPage[VaultListResponse]</a></code>

# Auth

Types:

```python
from hyperspell.types import Token, AuthDeleteUserResponse, AuthMeResponse
```

Methods:

- <code title="delete /auth/delete">client.auth.<a href="./src/hyperspell/resources/auth.py">delete_user</a>() -> <a href="./src/hyperspell/types/auth_delete_user_response.py">AuthDeleteUserResponse</a></code>
- <code title="get /auth/me">client.auth.<a href="./src/hyperspell/resources/auth.py">me</a>() -> <a href="./src/hyperspell/types/auth_me_response.py">AuthMeResponse</a></code>
- <code title="post /auth/user_token">client.auth.<a href="./src/hyperspell/resources/auth.py">user_token</a>(\*\*<a href="src/hyperspell/types/auth_user_token_params.py">params</a>) -> <a href="./src/hyperspell/types/token.py">Token</a></code>
