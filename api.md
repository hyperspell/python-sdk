# Ingest

Types:

```python
from hyperspell.types import IngestAddResponse, IngestFileResponse
```

Methods:

- <code title="post /ingest">client.ingest.<a href="./src/hyperspell/resources/ingest.py">add</a>(\*\*<a href="src/hyperspell/types/ingest_add_params.py">params</a>) -> <a href="./src/hyperspell/types/ingest_add_response.py">IngestAddResponse</a></code>
- <code title="post /ingest_file">client.ingest.<a href="./src/hyperspell/resources/ingest.py">file</a>(\*\*<a href="src/hyperspell/types/ingest_file_params.py">params</a>) -> <a href="./src/hyperspell/types/ingest_file_response.py">object</a></code>

# Query

Types:

```python
from hyperspell.types import QueryRetrieveResponse
```

Methods:

- <code title="post /query">client.query.<a href="./src/hyperspell/resources/query.py">retrieve</a>(\*\*<a href="src/hyperspell/types/query_retrieve_params.py">params</a>) -> <a href="./src/hyperspell/types/query_retrieve_response.py">object</a></code>

# Documents

Types:

```python
from hyperspell.types import Document, DocumentListResponse
```

Methods:

- <code title="get /documents/get/{document_id}">client.documents.<a href="./src/hyperspell/resources/documents.py">retrieve</a>(document_id) -> <a href="./src/hyperspell/types/document.py">Document</a></code>
- <code title="post /documents/list">client.documents.<a href="./src/hyperspell/resources/documents.py">list</a>(\*\*<a href="src/hyperspell/types/document_list_params.py">params</a>) -> <a href="./src/hyperspell/types/document_list_response.py">DocumentListResponse</a></code>
