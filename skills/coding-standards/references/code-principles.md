## General Code Principles Guidelines

Follow the rules below to ensure that the code follows the same core principles across the codebase.

---

### Type Hints & Typing

#### Use NamedTuples for complex function signatures
When a function uses or returns an object type that is complex (e.g., multiple nested structures), use NamedTuples or other relevant structures to clarify the typing and simplify function input types/return values.

**DO:**
```python
from typing import NamedTuple

class ProcessingResult(NamedTuple):
    filtered_paragraphs: list[dict[str, Any]]
    metadata: dict[str, int]
    confidence_scores: list[float]

def process_document(text: str) -> ProcessingResult:
    # Clear return type
    return ProcessingResult(
        filtered_paragraphs=[...],
        metadata={'total': 10},
        confidence_scores=[0.9, 0.8]
    )
```

**DON'T:**
```python
# Bad: Unclear nested structure
def process_document(text: str) -> tuple[list[dict[str, Any]], dict[str, int], list[float]]:
    return ([...], {'total': 10}, [0.9, 0.8])

# Bad: Using generic dict without structure
def process_document(text: str) -> dict:
    return {
        'filtered_paragraphs': [...],
        'metadata': {'total': 10},
        'confidence_scores': [0.9, 0.8]
    }

# Bad: Nested dictionaries without clear types
def get_stats(data: dict[str, dict[str, list[int]]]) -> dict[str, dict[str, float]]:
    pass
```

#### Declare class member types at the beginning
For custom classes, give the member variables typing at the beginning of the class definition. This applies to all classes (regular classes, dataclasses, etc.).

**DO:**
```python
import numpy as np

class EmbeddingClassifier:
    """Classifier using embeddings."""
    settings: ClassifierSettings
    _model: SentenceTransformer | None = None
    _category_embeddings: np.ndarray | None = None
    cache_dir: str = "./cache"
    
    def __init__(self, settings: ClassifierSettings):
        self.settings = settings
```

```python
from dataclasses import dataclass

@dataclass
class ProcessorConfig:
    """Processor configuration."""
    model_name: str
    batch_size: int = 32
    device: str = "cpu"
```

**DON'T:**
```python
# Bad: No type hints
class EmbeddingClassifier:
    def __init__(self, settings):
        self.settings = settings
        self._model = None
        self._category_embeddings = None

# Bad: Types only in __init__, not at class level
class EmbeddingClassifier:
    def __init__(self, settings: ClassifierSettings):
        self.settings: ClassifierSettings = settings
        self._model: SentenceTransformer | None = None

# Bad: Inconsistent typing
class EmbeddingClassifier:
    settings: ClassifierSettings
    
    def __init__(self, settings):
        self.settings = settings
        self._model = None  # Type not declared at class level
```

#### Avoid `from __future__ import annotations` by default
Do not use `from __future__ import annotations` unless really required. It should not be a default import.

**DO:**
```python
# Modern Python 3.10+ with native type hints
class MyClass:
    settings: dict[str, Any]
    items: list[str]
```

**DON'T:**
```python
# Bad: Unnecessary future import for simple cases
from __future__ import annotations

class MyClass:
    settings: dict[str, Any]
    items: list[str]
```

**EXCEPTION (when it IS needed):**
```python
# OK: When you have forward references or circular dependencies
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .other_module import SomeClass

class MyClass:
    def process(self, obj: SomeClass) -> SomeClass:  # Forward reference needed
        pass
```

---

### Code Structure & Design

#### In-place modification functions should not return values
For clarity, functions that modify an input variable in-place (by reference) should NOT have any return value. If such a function needs a return value, modify the object by copy.

**DO:**
```python
def normalize_image(image: np.ndarray) -> None:
    """Normalize image in-place."""
    image[:] = (image - image.mean()) / image.std()

# Or if you need a return value, work on a copy:
def normalize_image(image: np.ndarray) -> np.ndarray:
    """Return normalized copy of image."""
    normalized = image.copy()
    normalized = (normalized - normalized.mean()) / normalized.std()
    return normalized
```

**DON'T:**
```python
# Bad: Modifies in-place AND returns
def normalize_image(image: np.ndarray) -> np.ndarray:
    image[:] = (image - image.mean()) / image.std()
    return image  # Confusing: modifies input AND returns it

# Bad: Unclear whether it modifies in-place or returns copy
def process_data(data: list[int]) -> list[int]:
    data.sort()  # In-place modification
    return data  # Returns same object

# Bad: Mixed behavior
def update_config(config: dict) -> dict:
    config['updated'] = True  # Modifies in-place
    return config  # Also returns it
```

#### Prefer objects over indices and dictionary access
Use objects directly rather than indices and list/dictionary access when possible.

**DO:**
```python
for paragraph in paragraphs:
    process_paragraph(paragraph)

for user in users:
    send_email(user.email, user.name)
```

**DON'T:**
```python
# Bad: Using indices unnecessarily
for i in range(len(paragraphs)):
    process_paragraph(paragraphs[i])

# Bad: Dictionary access when object attributes exist
user_dict = {'email': '...', 'name': '...'}
send_email(user_dict['email'], user_dict['name'])
```

#### Prefer classes over dictionaries for reusable structures
Use classes (dataclass, enums, StrEnums, etc.) over dictionaries when it makes sense (for instance, when object structures are re-used).

**DO:**
```python
from dataclasses import dataclass
from enum import StrEnum

class ParagraphType(StrEnum):
    HEADER = "header"
    BODY = "body"
    FOOTER = "footer"

@dataclass
class Paragraph:
    text: str
    type: ParagraphType
    confidence: float
```

**DON'T:**
```python
# Bad: Re-using the same dictionary structure everywhere
paragraph = {
    'text': '...',
    'type': 'header',
    'confidence': 0.9
}
```

#### Each module should have a single responsibility
Each module/file should have a well-defined, single responsibility.

#### Favor composition over inheritance
Develop reusable functions and classes, favoring composition over inheritance.

#### Modular design with appropriate granularity
Encourage modular design principles to improve code maintainability and reusability. However, avoid unnecessary classes and one-line functions.

**DON'T:**
```python
# Bad: Unnecessary one-liner
def add_one(x: int) -> int:
    return x + 1

# Bad: Over-engineered class for simple operation
class Adder:
    def add_one(self, x: int) -> int:
        return x + 1
```

#### Ensure version compatibility
Ensure suggested changes are compatible with the project's specified language or framework versions.

#### Replace hardcoded values with named constants
**DO:**
```python
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

def fetch_data():
    for attempt in range(MAX_RETRIES):
        ...
```

**DON'T:**
```python
def fetch_data():
    for attempt in range(3):  # What does 3 mean?
        ...
```

#### Simple return values over complex dictionaries
When writing return values for functions, avoid returning a dictionary with stats when it isn't necessary. Prioritize returning simple objects.

**DO:**
```python
def process_text(text: str) -> list[str]:
    return text.split()

# If you need metadata, use NamedTuple:
class ProcessResult(NamedTuple):
    tokens: list[str]
    count: int

def process_text(text: str) -> ProcessResult:
    tokens = text.split()
    return ProcessResult(tokens, len(tokens))
```

**DON'T:**
```python
# Bad: Unnecessary dict wrapping
def process_text(text: str) -> dict:
    return {'tokens': text.split()}

# Bad: Stats dict when not needed
def process_text(text: str) -> dict:
    tokens = text.split()
    return {'result': tokens, 'count': len(tokens), 'status': 'ok'}
```

#### Direct dictionary access over `.get()`
When accessing dictionary items, avoid using the "get" method like `mydict.get(0, [])`. Instead, prefer the use of simple brackets `mydict[0]`.

**DO:**
```python
value = mydict[key]

# Or with try-except if key might not exist:
try:
    value = mydict[key]
except KeyError:
    value = default_value
```

**DON'T:**
```python
value = mydict.get(key, default_value)
```

---

### Performance

#### Prefer vectorized operations over explicit loops
Use vectorized operations for better performance when working with numerical data.

**DO:**
```python
import numpy as np

# Vectorized operation
result = array * 2 + 5
normalized = (array - array.mean()) / array.std()
```

**DON'T:**
```python
# Bad: Explicit loop for vectorizable operation
result = np.zeros_like(array)
for i in range(len(array)):
    result[i] = array[i] * 2 + 5
```

---

### Error Handling

#### Implement robust error handling and logging
Implement robust error handling and logging where necessary.

#### Use assertions to validate assumptions
Include assertions wherever possible to validate assumptions and catch potential errors early.

**DO:**
```python
def process_batch(items: list[str]) -> list[str]:
    assert len(items) > 0, "Batch cannot be empty"
    assert all(isinstance(item, str) for item in items), "All items must be strings"
    return [item.upper() for item in items]
```

---

### Logging

#### Use the logging module, not print statements
Use Python's `logging` module for all diagnostic output.

**DO:**
```python
import logging

logger = logging.getLogger(__name__)

def process_data(data: list[str]) -> None:
    logger.debug("Processing %d items", len(data))
    logger.info("Processing complete")
```

**DON'T:**
```python
def process_data(data: list[str]) -> None:
    print(f"Processing {len(data)} items")  # Bad: use logging
    print("Processing complete")
```

---

### Preferred Libraries

#### Use OpenCV for image processing
When working with images, use OpenCV (cv2) rather than PIL. You can also work with numpy if required.

**DO:**
```python
import cv2
import numpy as np

image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

**DON'T:**
```python
from PIL import Image

image = Image.open('image.jpg')
gray = image.convert('L')
```

#### Use defaultdict to avoid manual key checking
Use defaultdict when necessary rather than checking key existence and assigning empty values manually.

**DO:**
```python
from collections import defaultdict

counts = defaultdict(int)
counts[key] += 1

groups = defaultdict(list)
groups[category].append(item)
```

**DON'T:**
```python
# Bad: Manual key checking
counts = {}
if key not in counts:
    counts[key] = 0
counts[key] += 1

# Bad: Using .get() with mutable default
groups = {}
groups.setdefault(category, []).append(item)
```

---

### General Philosophy

#### Prioritize simplicity and maintainability
Do not over-engineer solutions. Strive for simplicity and maintainability while still being efficient.

#### Balance modularity appropriately
Favor modularity, but avoid over-modularization.

#### Choose modern, efficient libraries wisely
Use the most modern and efficient libraries when appropriate, but justify their use and ensure they don't add unnecessary complexity.

#### Leverage Python 3.10+ features
Prioritize new features in Python 3.10+ (e.g., `|` for Union types, match/case, improved error messages).

#### Ask clarifying questions when needed
If a request is unclear or lacks sufficient information, ask clarifying questions before proceeding.
