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
from hyperspell.types import Document, DocumentStatus
```

# Auth

Types:

```python
from hyperspell.types import Token, AuthMeResponse
```

Methods:

- <code title="get /auth/me">client.auth.<a href="./src/hyperspell/resources/auth.py">me</a>() -> <a href="./src/hyperspell/types/auth_me_response.py">AuthMeResponse</a></code>
- <code title="post /auth/user_token">client.auth.<a href="./src/hyperspell/resources/auth.py">user_token</a>(\*\*<a href="src/hyperspell/types/auth_user_token_params.py">params</a>) -> <a href="./src/hyperspell/types/token.py">Token</a></code>
