# Implementation Plan: Phase I - In-Memory Todo Console Application

**Branch**: `001-phase1-inmemory-todo` | **Date**: 2026-01-02 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-phase1-inmemory-todo/spec.md`

## Summary

A simple Python console application for managing todo tasks in memory. Single-user, single-session, menu-driven interface. No persistence, no external dependencies, no web frameworks. Implements CRUD operations for tasks (Add, View, Update, Delete, Mark Complete/Incomplete).

## Technical Context

**Language/Version**: Python 3.10+ (stdlib only, no external dependencies)
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory list (session-scoped, lost on exit)
**Testing**: pytest (Python's built-in unittest framework acceptable)
**Target Platform**: Console/Terminal (CLI application)
**Project Type**: Single-file Python script (minimum viable)
**Performance Goals**: 100% operation success rate; sub-second response times
**Constraints**: No databases, No file storage, No web frameworks, No external services, No future phase concepts (Phase I only)
**Scale/Scope**: Single user, single session, in-memory (max ~1000 tasks practical limit)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Rule | Status | Notes |
|------|--------|-------|
| Spec-Driven Development (SDD) | PASS | Plan follows Spec → Plan → Tasks → Implement workflow |
| No Manual Coding | PASS | Code will be written by agents from approved tasks |
| No Feature Invention | PASS | Implementation strictly follows Phase I spec |
| Phase Scope Isolation | PASS | No future-phase features included |
| Clean Architecture | PASS | Separation of data layer and CLI layer |
| Separation of Concerns | PASS | Distinct modules for data and presentation |

## Project Structure

### Documentation (this feature)

```text
specs/001-phase1-inmemory-todo/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── models/
│   └── task.py          # Task dataclass and TaskList
├── services/
│   └── todo_service.py  # Business logic (CRUD operations)
└── cli/
    ├── __init__.py
    ├── menu.py          # Menu display and navigation
    └── handlers.py      # User input handling per menu option

tests/
├── unit/
│   ├── test_task.py
│   └── test_service.py
└── integration/
    └── test_cli.py
```

**Structure Decision**: Single Python project with clear separation between data models (`models/`) and CLI presentation (`cli/`). `services/` contains business logic. This mirrors Clean Architecture principles while keeping the console-only Phase I scope minimal.

## Technical Design

### Data Model

```python
# src/models/task.py
from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    """Represents a single todo task."""
    id: int              # Unique identifier (1-based, sequential)
    description: str     # Task description (non-empty string)
    is_complete: bool    # Completion status (default: False)

class TaskList:
    """In-memory collection of tasks."""
    tasks: List[Task]    # Ordered list of Task objects
    _next_id: int        # Counter for generating unique IDs (starts at 1)
```

**Key Design Decisions**:
- `Task` uses `dataclass` for minimal boilerplate and value semantics
- `TaskList` maintains tasks in insertion order (list preserves order)
- `_next_id` ensures stable, sequential ID assignment (never reuses deleted IDs)
- No validation in data models (delegated to service layer)

### ID Generation Strategy

- **Approach**: Simple integer counter (`_next_id`) starting at 1
- **Rationale**: Meets spec requirement for unique sequential IDs
- **No Reuse**: Deleted task IDs are not reused (avoids confusion with stale references)
- **Implementation**: `_next_id` increments by 1 each time a task is added

### Service Layer (Business Logic)

```python
# src/services/todo_service.py
class TodoService:
    """Handles all CRUD operations on tasks."""

    def __init__(self) -> None:
        self._task_list = TaskList()

    def add_task(self, description: str) -> Task:
        """Add a new task with the given description."""
        # Validates non-empty description
        # Creates Task with next available ID
        # Appends to task list
        # Returns created Task

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks in insertion order."""

    def update_task(self, task_id: int, new_description: str) -> bool:
        """Update task description by ID. Returns True if successful."""

    def delete_task(self, task_id: int) -> bool:
        """Delete task by ID. Returns True if successful."""

    def mark_complete(self, task_id: int) -> bool:
        """Mark task as complete. Returns True if successful."""

    def mark_incomplete(self, task_id: int) -> bool:
        """Mark task as incomplete. Returns True if successful."""
```

**Separation of Concerns**:
- Service layer handles all business rules (validation, state changes)
- No user input/output code in service layer (pure Python functions)
- Data models are simple containers (no behavior)

### CLI Layer (Presentation)

```python
# src/cli/menu.py
def display_menu() -> None:
    """Print the main menu options."""

def get_user_choice() -> str:
    """Get and validate user menu selection."""

def main_loop() -> None:
    """Run the main menu loop until user exits."""
    while True:
        display_menu()
        choice = get_user_choice()
        handle_choice(choice)

# src/cli/handlers.py
def handle_add_task(service: TodoService) -> None:
    """Prompt for description, validate, call service."""

def handle_view_tasks(service: TodoService) -> None:
    """Get tasks from service, display formatted list."""

def handle_update_task(service: TodoService) -> None:
    """Prompt for ID and new description, call service."""

def handle_delete_task(service: TodoService) -> None:
    """Prompt for ID, call service."""

def handle_mark_complete(service: TodoService) -> None:
    """Prompt for ID, call service."""

def handle_mark_incomplete(service: TodoService) -> None:
    """Prompt for ID, call service."""
```

**Control Flow**:
1. `main_loop()` displays menu and gets user choice
2. Route to appropriate `handle_*` function
3. `handle_*` functions collect input, call service, display result
4. Loop continues until user selects "Exit"

### Error Handling Strategy

| Scenario | Handling |
|----------|----------|
| Empty/whitespace description | Display error message, prompt again |
| Invalid task ID (non-existent) | Display error message, return to menu |
| Non-numeric ID input | Display error, prompt for valid input |
| Unexpected exception | Display generic error, continue (no crash) |

**Error Message Pattern**:
```
Error: [Clear description of what went wrong]
Hint: [Action user should take]
```

**Input Validation**:
- All user inputs validated before service calls
- `str.strip()` preserves whitespace in stored description (per spec)
- Empty strings rejected with clear error

### Menu Structure

```
=== Todo List ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit

Enter your choice (1-7):
```

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |

This implementation is intentionally minimal for Phase I scope.
