---
trigger: always_on
---

## General Code Style Guidelines

Follow the rules below to ensure consistency, clarity, and maintainability across the codebase.

---

### 1. Comments

- Minimize comments.
- Use **clear names** and **logical structure** instead of explanatory remarks.
- Avoid docstrings and function headers explaining what the function does, except when the logic is particularly complex.
- Avoid stating the obvious or repeating what the code already makes clear.
- Never use filler comments like `# this is where the change happens`.

#### Example of what **not** to do:

```python
# Get list of message files sorted by timestamp (oldest first)
message_files = sorted(queue_dir.glob("*.json"))
if not message_files:
    raise EmptyQueue(f"Queue '{queue_name}' is empty")

# Process the oldest message
oldest_message_file = message_files[0]
try:
    # Read and parse message
    with open(oldest_message_file) as f:
        message_data = json.load(f)

    # Create Message object
    message = Message.model_validate(message_data)

    # Process message using callback
    await callback(message)

    # Remove processed message file
    oldest_message_file.unlink()
except Exception as e:
    # In case of error, don't remove the message file
    raise RuntimeError(f"Error processing message: {e}") from e
```

#### Example of what **to do**:

```python
message_files = sorted(queue_dir.glob("*.json"))
if not message_files:
    raise EmptyQueue(f"Queue '{queue_name}' is empty")

oldest_message_file = message_files[0]
try:
    with open(oldest_message_file) as f:
        message_data = json.load(f)

    message = Message.model_validate(message_data)

    await callback(message)

    oldest_message_file.unlink()
except Exception as e:
    raise RuntimeError(f"Error processing message: {e}") from e
```

---

### 2. Type Hints

- Use **type hints everywhere** — no exceptions.
- Prefer **native Python syntax**:
  - Use `list[str]` instead of `List[str]`
  - Use `str | None` instead of `Optional[str]`
- All function arguments and return values must be annotated.
- The linter is strict, so make sure that the types are verified.

---

### 3. Code Formatting

- Use `ruff` to format all `.py` files.
- `ruff` may not auto-correct long strings — handle those manually for clarity.
- Prefer the use of double quotes (") to single quotes (').

#### Example Fix

**Before** (too long, unhandled by `ruff`):

```python
logger.warning(
    "This is a long string and ruff can't really decide the how to split it. A llm however should be able to make a decision."
)
```

**After** (split for clarity):

```python
logger.warning(
    "This is a long string and ruff can't really decide the how to split it."
    "A llm however should be able to make a decision."
)
```

---

### 4. Import Organization

- Group imports in this order: standard library, third-party, local
- Separate each group with a blank line
- Sort alphabetically within each group
- Use absolute imports, not relative imports (except within a package)

**DO:**
```python
import json
import logging
from pathlib import Path

import numpy as np
from pydantic import BaseModel

from faisop.ai_processors.base import BaseProcessor
from faisop.models import Document
```

**DON'T:**
```python
from faisop.models import Document
import json
import numpy as np
from pathlib import Path
from pydantic import BaseModel
import logging
from faisop.ai_processors.base import BaseProcessor
```

---

### 5. Naming Conventions

- **Classes**: PascalCase (`DocumentProcessor`, `EmbeddingClassifier`)
- **Functions/methods**: snake_case (`process_document`, `get_embeddings`)
- **Variables**: snake_case (`document_count`, `processed_items`)
- **Constants**: UPPER_SNAKE_CASE (`MAX_RETRIES`, `DEFAULT_TIMEOUT`)
- **Private members**: prefix with underscore (`_internal_cache`, `_process_batch`)
- **Boolean variables**: use `is_`, `has_`, `can_` prefixes (`is_valid`, `has_errors`)

---

### 6. Line Length and Wrapping

- Maximum line length: 100 characters (ruff default)
- For long function signatures, put each parameter on its own line
- For long strings, split into multiple concatenated strings

**DO:**
```python
def process_document(
    document: Document,
    config: ProcessorConfig,
    cache_dir: Path | None = None,
) -> ProcessingResult:
    pass
```

---

## Summary

Write **intentional**, readable code. Let naming and structure replace commentary. Be strict with **type hints** and consistent with **`ruff` formatting**.
