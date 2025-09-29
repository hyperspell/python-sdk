# Shared Types

```python
from hyperspell.types import QueryResult
```

# Integrations

Types:

```python
from hyperspell.types import IntegrationRevokeResponse
```

Methods:

- <code title="get /integrations/{provider}/revoke">client.integrations.<a href="./src/hyperspell/resources/integrations/integrations.py">revoke</a>(provider) -> <a href="./src/hyperspell/types/integration_revoke_response.py">IntegrationRevokeResponse</a></code>

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
from hyperspell.types import Memory, MemoryStatus, MemoryDeleteResponse, MemoryStatusResponse
```

Methods:

- <code title="get /memories/list">client.memories.<a href="./src/hyperspell/resources/memories.py">list</a>(\*\*<a href="src/hyperspell/types/memory_list_params.py">params</a>) -> <a href="./src/hyperspell/types/memory.py">SyncCursorPage[Memory]</a></code>
- <code title="delete /memories/delete/{source}/{resource_id}">client.memories.<a href="./src/hyperspell/resources/memories.py">delete</a>(resource_id, \*, source) -> <a href="./src/hyperspell/types/memory_delete_response.py">MemoryDeleteResponse</a></code>
- <code title="post /memories/add">client.memories.<a href="./src/hyperspell/resources/memories.py">add</a>(\*\*<a href="src/hyperspell/types/memory_add_params.py">params</a>) -> <a href="./src/hyperspell/types/memory_status.py">MemoryStatus</a></code>
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
