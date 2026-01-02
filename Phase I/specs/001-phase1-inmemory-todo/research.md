# Research: Phase I - In-Memory Todo Console Application

## Decision: Python dataclass for Task entity

**Choice**: Use Python's `@dataclass` decorator for the Task model

**Rationale**:
- No external dependencies required
- Built-in type hints support
- Auto-generated `__init__`, `__repr__`, `__eq__`
- Simple, readable, minimal boilerplate

**Alternatives considered**:
- Namedtuple: Less mutable, harder to modify later
- Pydantic: External dependency, overkill for in-memory only
- Custom class: More boilerplate, no additional value

---

## Decision: Dictionary-based storage for TaskService

**Choice**: Use `dict[int, Task]` for in-memory task storage

**Rationale**:
- O(1) lookup by ID (required for update/delete/mark operations)
- Simple iteration for "view all" operations
- Native Python, no external dependencies
- Easy to extend if needed later

**Alternatives considered**:
- List: O(n) lookup by ID, would require linear search
- Set: Doesn't support duplicate fields (description can repeat)

---

## Decision: Sequential ID generation

**Choice**: Auto-incrementing integer IDs starting from 1

**Rationale**:
- Simple and predictable
- Matches user expectations for numbered lists
- Never reuses IDs (deleted tasks leave gaps)
- Easy to understand and display

**Alternatives considered**:
- UUID: Overkill, harder to read for users
- Timestamp-based: Unnecessary complexity

---

## Decision: Simple menu loop with input validation

**Choice**: Numbered menu (1-7) with while loop and try/except input handling

**Rationale**:
- Standard CLI pattern, familiar to users
- Easy to validate numeric input
- Clear navigation structure
- No external dependencies

**Alternatives considered**:
- Click/Argparse: External dependencies, designed for command-line arguments not interactive menus
- curses/TUI: Platform-dependent, steeper learning curve

---

## Decision: pytest for testing

**Choice**: Use pytest framework for all tests

**Rationale**:
- Standard Python testing framework
- Simple assertion syntax
- Good for both unit and integration tests
- No external dependencies if using Python 3.10+ (unittest also works)

**Alternatives considered**:
- unittest: Built-in but more verbose
- doctest: Limited to docstring examples

---

## Decision: Clean separation (models/services/cli)

**Choice**: Three distinct packages with clear boundaries

**Rationale**:
- Follows clean architecture principles
- Easy to test each layer independently
- Clear separation of concerns
- Extensible for future phases

**Alternatives considered**:
- Single file: Hard to test, unclear boundaries
- Too many files: Over-engineering for single-phase app
