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

# Documents

Types:

```python
from hyperspell.types import Document, DocumentStatus, DocumentListResponse, DocumentGetResponse
```

Methods:

- <code title="get /documents/list">client.documents.<a href="./src/hyperspell/resources/documents.py">list</a>(\*\*<a href="src/hyperspell/types/document_list_params.py">params</a>) -> <a href="./src/hyperspell/types/document_list_response.py">SyncCursorPage[DocumentListResponse]</a></code>
- <code title="post /documents/add">client.documents.<a href="./src/hyperspell/resources/documents.py">add</a>(\*\*<a href="src/hyperspell/types/document_add_params.py">params</a>) -> <a href="./src/hyperspell/types/document_status.py">DocumentStatus</a></code>
- <code title="post /documents/scrape">client.documents.<a href="./src/hyperspell/resources/documents.py">add_url</a>(\*\*<a href="src/hyperspell/types/document_add_url_params.py">params</a>) -> <a href="./src/hyperspell/types/document_status.py">DocumentStatus</a></code>
- <code title="get /documents/get/{document_id}">client.documents.<a href="./src/hyperspell/resources/documents.py">get</a>(document_id) -> <a href="./src/hyperspell/types/document_get_response.py">object</a></code>
- <code title="post /documents/upload">client.documents.<a href="./src/hyperspell/resources/documents.py">upload</a>(\*\*<a href="src/hyperspell/types/document_upload_params.py">params</a>) -> <a href="./src/hyperspell/types/document_status.py">DocumentStatus</a></code>

# Collections

Types:

```python
from hyperspell.types import Collection, CollectionListResponse
```

Methods:

- <code title="post /collections/add">client.collections.<a href="./src/hyperspell/resources/collections.py">create</a>(\*\*<a href="src/hyperspell/types/collection_create_params.py">params</a>) -> <a href="./src/hyperspell/types/collection.py">Collection</a></code>
- <code title="get /collections/list">client.collections.<a href="./src/hyperspell/resources/collections.py">list</a>(\*\*<a href="src/hyperspell/types/collection_list_params.py">params</a>) -> <a href="./src/hyperspell/types/collection_list_response.py">SyncCursorPage[CollectionListResponse]</a></code>
- <code title="get /collections/get/{name}">client.collections.<a href="./src/hyperspell/resources/collections.py">get</a>(name) -> <a href="./src/hyperspell/types/collection.py">Collection</a></code>

# Query

Types:

```python
from hyperspell.types import QuerySearchResponse
```

Methods:

- <code title="post /query">client.query.<a href="./src/hyperspell/resources/query.py">search</a>(\*\*<a href="src/hyperspell/types/query_search_params.py">params</a>) -> <a href="./src/hyperspell/types/query_search_response.py">QuerySearchResponse</a></code>

# Auth

Types:

```python
from hyperspell.types import Token, AuthMeResponse
```

Methods:

- <code title="get /auth/me">client.auth.<a href="./src/hyperspell/resources/auth.py">me</a>() -> <a href="./src/hyperspell/types/auth_me_response.py">AuthMeResponse</a></code>
- <code title="post /auth/user_token">client.auth.<a href="./src/hyperspell/resources/auth.py">user_token</a>(\*\*<a href="src/hyperspell/types/auth_user_token_params.py">params</a>) -> <a href="./src/hyperspell/types/token.py">Token</a></code>
