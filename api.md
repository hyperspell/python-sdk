# Documents

Types:

```python
from hyperspell.types import Document, DocumentStatus, DocumentListResponse
```

Methods:

- <code title="get /documents/list">client.documents.<a href="./src/hyperspell/resources/documents.py">list</a>(\*\*<a href="src/hyperspell/types/document_list_params.py">params</a>) -> <a href="./src/hyperspell/types/document_list_response.py">SyncCursorPage[DocumentListResponse]</a></code>
- <code title="post /documents/add">client.documents.<a href="./src/hyperspell/resources/documents.py">add</a>(\*\*<a href="src/hyperspell/types/document_add_params.py">params</a>) -> <a href="./src/hyperspell/types/document_status.py">DocumentStatus</a></code>
- <code title="post /documents/scrape">client.documents.<a href="./src/hyperspell/resources/documents.py">add_url</a>(\*\*<a href="src/hyperspell/types/document_add_url_params.py">params</a>) -> <a href="./src/hyperspell/types/document_status.py">DocumentStatus</a></code>
- <code title="get /documents/get/{document_id}">client.documents.<a href="./src/hyperspell/resources/documents.py">get</a>(document_id) -> <a href="./src/hyperspell/types/document.py">Document</a></code>
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
from hyperspell.types import Token
```

Methods:

- <code title="post /auth/user_token">client.auth.<a href="./src/hyperspell/resources/auth.py">user_token</a>(\*\*<a href="src/hyperspell/types/auth_user_token_params.py">params</a>) -> <a href="./src/hyperspell/types/token.py">Token</a></code>
