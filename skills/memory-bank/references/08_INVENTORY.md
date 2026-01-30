# codeInventory Reference

## Purpose

The `codeInventory.md` file maintains an inventory of classes, interfaces, and functions in the codebase. It provides a quick reference for understanding the code structure without reading source files, enabling faster navigation and reducing redundant code creation.

## When to Update

Update codeInventory.md when:
- **Adding** new classes, interfaces, or functions
- **Removing** existing classes, interfaces, or functions
- **Renaming** classes, interfaces, or functions
- **At the end of major implementation phases** (review for accuracy)

**Do NOT update for:**
- Internal implementation changes (logic changes within methods)
- Private helper functions that are implementation details
- Minor refactoring that doesn't change signatures

## Format Specification

### Classes

```markdown
### ClassName
- **File:** `path/to/file.ext`
- **Purpose:** [Brief description of what this class does]
- **Methods:**
  - `publicMethod(param1: Type, param2: Type) -> ReturnType` - [Description]
  - `anotherPublic(param: Type)` - [Description]
  - `_privateMethod(param: Type)` - [Description]
```

### Interfaces

```markdown
### InterfaceName
- **File:** `path/to/file.ext`
- **Purpose:** [Brief description of what this interface defines]
- **Methods:**
  - `requiredMethod(param: Type) -> ReturnType`
  - `optionalMethod?(param: Type) -> ReturnType`
```

### Standalone Functions

```markdown
### functionName
- **File:** `path/to/file.ext`
- **Signature:** `functionName(param1: Type, param2: Type) -> ReturnType`
- **Purpose:** [Brief description of what this function does]
```

## Method Signature Conventions

### Python

```markdown
- `process_data(data: list[dict], options: dict | None = None) -> ProcessResult`
- `_validate_input(value: str) -> bool`
- `__init__(self, config: Config)`
```

### TypeScript/JavaScript

```markdown
- `processData(data: Record<string, unknown>[], options?: Options): ProcessResult`
- `private validateInput(value: string): boolean`
- `constructor(config: Config)`
```

### Go

```markdown
- `ProcessData(data []map[string]interface{}, options *Options) (*ProcessResult, error)`
- `validateInput(value string) bool`
- `NewProcessor(config *Config) *Processor`
```

### Rust

```markdown
- `process_data(data: Vec<HashMap<String, Value>>, options: Option<Options>) -> Result<ProcessResult, Error>`
- `fn validate_input(&self, value: &str) -> bool`
- `pub fn new(config: Config) -> Self`
```

## Examples

### Python Example

```markdown
## Classes

### UserAuthenticator
- **File:** `src/auth/authenticator.py`
- **Purpose:** Handles user authentication and session management
- **Methods:**
  - `authenticate(username: str, password: str) -> AuthResult` - Validates credentials
  - `create_session(user: User) -> Session` - Creates new session
  - `validate_token(token: str) -> bool` - Validates JWT token
  - `_hash_password(password: str) -> str` - Hashes password with salt
  - `_generate_token(user: User) -> str` - Generates JWT token

### SessionManager
- **File:** `src/auth/session.py`
- **Purpose:** Manages active user sessions
- **Methods:**
  - `get_session(session_id: str) -> Session | None` - Retrieves session
  - `invalidate_session(session_id: str)` - Ends session
  - `_cleanup_expired()` - Removes expired sessions

## Interfaces

### AuthProvider
- **File:** `src/auth/interfaces.py`
- **Purpose:** Interface for authentication providers
- **Methods:**
  - `authenticate(credentials: Credentials) -> AuthResult`
  - `refresh_token(token: str) -> str`

## Functions

### hash_password
- **File:** `src/auth/utils.py`
- **Signature:** `hash_password(password: str, salt: bytes | None = None) -> tuple[str, bytes]`
- **Purpose:** Securely hashes a password with optional salt

### verify_password
- **File:** `src/auth/utils.py`
- **Signature:** `verify_password(password: str, hashed: str, salt: bytes) -> bool`
- **Purpose:** Verifies a password against its hash
```

### TypeScript Example

```markdown
## Classes

### ApiClient
- **File:** `src/api/client.ts`
- **Purpose:** HTTP client for API communication
- **Methods:**
  - `get<T>(endpoint: string, options?: RequestOptions): Promise<T>` - GET request
  - `post<T>(endpoint: string, data: unknown, options?: RequestOptions): Promise<T>` - POST request
  - `private handleError(error: Error): never` - Error handler

## Interfaces

### RequestOptions
- **File:** `src/api/types.ts`
- **Purpose:** Configuration options for API requests
- **Methods:**
  - `headers?: Record<string, string>`
  - `timeout?: number`
  - `retries?: number`

## Functions

### formatApiError
- **File:** `src/api/utils.ts`
- **Signature:** `formatApiError(error: unknown): ApiError`
- **Purpose:** Converts unknown errors to structured ApiError objects
```

## Organization

Keep the codeInventory organized by:

1. **Group by category** - Classes, Interfaces, Functions
2. **Alphabetize within categories** - Makes finding entries easier
3. **Group related items** - Keep related classes/functions near each other
4. **Update timestamp** - Always update "Last Updated" when modifying

## Best Practices

1. **Include private methods** - They help understand class internals
2. **Keep descriptions brief** - One line per method is usually sufficient
3. **Use consistent signature format** - Follow language conventions
4. **Remove deleted items** - Don't leave stale entries
5. **Review periodically** - Check accuracy at end of implementation phases
