# Data Model: Phase I - In-Memory Todo Console Application

**Feature**: 001-phase1-inmemory-todo
**Generated**: 2026-01-02

## Entities

### Task

Represents a single todo item stored in memory.

**Fields**:

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `int` | > 0, unique, auto-assigned | Unique identifier for the task |
| `description` | `str` | 1-1000 chars, required | The task description text |
| `is_complete` | `bool` | default: `False` | Whether the task is completed |

**State Transitions**:

```
          ┌─────────────────┐
          │   Task Created  │
          └────────┬────────┘
                   │
          ┌────────▼────────┐
          │ is_complete=    │
          │ False (default) │
          └────────┬────────┘
                   │
     ┌─────────────┼─────────────┐
     │             │             │
┌────▼────┐  ┌─────▼─────┐  ┌────▼────┐
│  Mark   │  │  Update   │  │ Delete  │
│Complete │  │Description│  │         │
└────┬────┘  └─────┬─────┘  └─────────┘
     │             │
     │    ┌────────▼────────┐
     │    │ is_complete=    │
     │    │ True            │
     │    └────────┬────────┘
     │             │
     │    ┌────────▼────────┐
     │    │  Mark Incomplete│
     │    └────────┬────────┘
     │             │
     └─────────────┘
          │
          ▼
    Task Deleted (removed from memory)
```

**Lifecycle**:
1. Created via `TaskService.add_task(description)`
2. May be updated via `TaskService.update_task(id, description)`
3. May be marked complete/incomplete via `TaskService.mark_complete(id)` / `mark_incomplete(id)`
4. Deleted via `TaskService.delete_task(id)`
5. All data lost when application exits (no persistence)

### TaskList (Service Layer)

Manages all Task instances in memory.

**Internal State**:

| Field | Type | Description |
|-------|------|-------------|
| `_tasks` | `dict[int, Task]` | ID-to-Task mapping for O(1) lookups |
| `_id_counter` | `int` | Next available ID for new tasks |

**Relationships**:
- One TaskList contains zero or more Tasks
- Each Task has exactly one parent TaskList (via reference)
- Tasks are identified by their `id` within the TaskList

**Validation Rules** (enforced by service layer):
- Task IDs must exist before update/delete/mark operations
- Task descriptions must be non-empty and non-whitespace-only
- Duplicate IDs are impossible (auto-increment)
- Deleted task IDs are not reused
