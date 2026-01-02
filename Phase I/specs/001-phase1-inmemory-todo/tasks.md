---
description: "Atomic implementation tasks for Phase I in-memory todo console application"
---

# Tasks: Phase I - In-Memory Todo Console Application

**Input**: Design documents from `/specs/001-phase1-inmemory-todo/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/, quickstart.md
**Feature**: 001-phase1-inmemory-todo
**Generated**: 2026-01-02

**Tests**: NOT REQUESTED - tests are optional and were not specified in the feature requirements

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create src/__init__.py making src a Python package
- [X] T002 Create src/models/__init__.py making models a Python package
- [X] T003 Create src/services/__init__.py making services a Python package
- [X] T004 Create src/cli/__init__.py making cli a Python package
- [X] T005 Create tests/unit/__init__.py making unit tests a Python package
- [X] T006 Create tests/integration/__init__.py making integration tests a Python package

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data models and storage - MUST complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [X] T007 Create Task dataclass in src/models/task.py with id, description, is_complete fields per data-model.md
- [X] T008 Create TaskList class in src/models/task.py with tasks list and _next_id counter per plan.md
- [X] T009 Create TodoService class in src/services/todo_service.py with __init__ only (stub CRUD methods)

**Checkpoint**: Foundation ready - user story implementation can now begin in sequential order

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) MVP

**Goal**: Users can add tasks with non-empty descriptions

**Independent Test**: Launch app, select "Add Task", enter description, verify task appears in list

**Reference**: spec.md Acceptance Scenarios 1-3, plan.md CLI handlers, contracts/cli-interface.yaml

### Implementation for User Story 1

- [X] T010 [US1] Implement TodoService.add_task() in src/services/todo_service.py (validate description, create Task with next ID, append to list)
- [X] T011 [US1] Create handle_add_task() function in src/cli/handlers.py (prompt for description, call service, display result)
- [X] T012 [US1] Implement input validation for empty/whitespace descriptions with error message per contracts/cli-interface.yaml

**Checkpoint**: User Story 1 complete - can add tasks with validation

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Users can view all tasks with ID, description, and completion status

**Independent Test**: Add tasks, select "View Tasks", verify all tasks display correctly

**Reference**: spec.md Acceptance Scenarios 1-3, plan.md CLI handlers

### Implementation for User Story 2

- [X] T013 [US2] Implement TodoService.get_all_tasks() in src/services/todo_service.py (return copy of tasks list)
- [X] T014 [US2] Create handle_view_tasks() function in src/cli/handlers.py (get tasks from service, format and display)
- [X] T015 [US2] Handle empty task list case with "No tasks exist" message per contracts/cli-interface.yaml
- [X] T016 [US2] Format task display with status indicator [ ] or [X] per quickstart.md

**Checkpoint**: User Story 2 complete - can view all tasks with status

---

## Phase 5: User Story 3 - Update Existing Tasks (Priority: P1)

**Goal**: Users can update task descriptions by ID

**Independent Test**: Add task, select "Update Task", enter valid ID and new description, verify task updated

**Reference**: spec.md Acceptance Scenarios 1-3, plan.md CLI handlers

### Implementation for User Story 3

- [X] T017 [US3] Implement TodoService.update_task() in src/services/todo_service.py (validate task exists, validate new description, update)
- [X] T018 [US3] Create handle_update_task() function in src/cli/handlers.py (prompt for ID, prompt for new description, call service)
- [X] T019 [US3] Implement error handling for invalid task ID with "Task not found" message
- [X] T020 [US3] Implement validation for empty/whitespace new descriptions

**Checkpoint**: User Story 3 complete - can update task descriptions

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P1)

**Goal**: Users can delete tasks by ID

**Independent Test**: Add task, select "Delete Task", enter valid ID, verify task removed

**Reference**: spec.md Acceptance Scenarios 1-3, plan.md CLI handlers

### Implementation for User Story 4

- [X] T021 [US4] Implement TodoService.delete_task() in src/services/todo_service.py (validate task exists, remove from list, return success)
- [X] T022 [US4] Create handle_delete_task() function in src/cli/handlers.py (prompt for ID, call service, confirm deletion)
- [X] T023 [US4] Implement error handling for invalid task ID with "Task not found" message
- [X] T024 [US4] Verify deleted task no longer appears in view output

**Checkpoint**: User Story 4 complete - can delete tasks

---

## Phase 7: User Story 5 - Mark Complete/Incomplete (Priority: P1)

**Goal**: Users can toggle task completion status

**Independent Test**: Add task, mark complete, verify status change, mark incomplete, verify status change

**Reference**: spec.md Acceptance Scenarios 1-4, plan.md CLI handlers

### Implementation for User Story 5

- [X] T025 [US5] Implement TodoService.mark_complete() in src/services/todo_service.py (validate task exists, set is_complete=True)
- [X] T026 [US5] Implement TodoService.mark_incomplete() in src/services/todo_service.py (validate task exists, set is_complete=False)
- [X] T027 [US5] Create handle_mark_complete() function in src/cli/handlers.py (prompt for ID, call service, confirm)
- [X] T028 [US5] Create handle_mark_incomplete() function in src/cli/handlers.py (prompt for ID, call service, confirm)
- [X] T029 [US5] Implement error handling for invalid task ID with "Task not found" message
- [X] T030 [US5] Verify completed tasks display with [X] status indicator in view output

**Checkpoint**: User Story 5 complete - can mark tasks complete/incomplete

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Input validation, error handling, startup/exit flow

- [X] T031 Create display_menu() function in src/cli/menu.py showing all 7 menu options per quickstart.md
- [X] T032 Create get_user_choice() function in src/cli/menu.py (validate input 1-7, re-prompt on invalid)
- [X] T033 Create main_loop() function in src/cli/menu.py (while True loop, display menu, get choice, dispatch to handler)
- [X] T034 Implement choice routing in main_loop() to call appropriate handle_* function per contracts/cli-interface.yaml
- [X] T035 Implement exit option (7) with goodbye message per quickstart.md
- [X] T036 Handle Ctrl+C gracefully with goodbye message per quickstart.md
- [X] T037 Implement consistent error message pattern "Error: [description]" with "Hint: [action]" per plan.md
- [X] T038 Create main entry point in src/cli/menu.py (if __name__ == "__main__": main_loop())

---

## Dependencies & Execution Order

### Phase Dependencies

| Phase | Dependencies | Blocks |
|-------|--------------|--------|
| Setup (1) | None | Foundational |
| Foundational (2) | Setup | All User Stories |
| US1 Add Tasks (3) | Foundational | US2 |
| US2 View Tasks (4) | Foundational, US1 | US3 |
| US3 Update Tasks (5) | Foundational, US2 | US6 |
| US4 Delete Tasks (6) | Foundational, US3 | US7 |
| US5 Mark Complete (7) | Foundational, US4 | Polish |
| Polish (8) | All user stories | None |

### User Story Dependencies

All user stories depend on Foundational (Phase 2). Since all stories are P1, they should be implemented sequentially:
- **User Story 1**: Add Tasks - Can start after Foundational
- **User Story 2**: View Tasks - Can start after Foundational (depends on US1 for testing)
- **User Story 3**: Update Tasks - Can start after Foundational (depends on US2 for testing)
- **User Story 4**: Delete Tasks - Can start after Foundational (depends on US3 for testing)
- **User Story 5**: Mark Complete - Can start after Foundational (depends on US4 for testing)

### Within Each User Story

- Models before services (done in Foundational)
- Services before CLI handlers
- Core implementation before error handling
- Story complete before moving to next story

### Parallel Opportunities

Within each user story, independent components can be done in parallel:
- T010 [US1] add_task() service - must be done before T011
- T011 [US1] handle_add_task() CLI - can run in parallel with T012 (different files)

Different user stories CANNOT run in parallel due to sequential dependencies for testing.

---

## Parallel Example: Within User Story 1

```bash
# These tasks can run in parallel:
Task T010: "Implement TodoService.add_task() in src/services/todo_service.py"
Task T012: "Implement input validation for empty/whitespace descriptions"
```

# Within User Story 2

```bash
# T013 must complete before T014 and T015 can start
# T014 and T015 can run in parallel (different functions)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test adding tasks independently
5. Deploy/demo if only User Story 1 is needed

### Full Implementation (All User Stories)

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test → Checkpoint
3. Add User Story 2 → Test → Checkpoint
4. Add User Story 3 → Test → Checkpoint
5. Add User Story 4 → Test → Checkpoint
6. Add User Story 5 → Test → Checkpoint
7. Add Polish → Complete
8. Full application ready

### Sequential Strategy

With single developer, work through phases sequentially:
- Phases 1-2: Foundation (must complete once)
- Phase 3: US1 Add Tasks (complete, test)
- Phase 4: US2 View Tasks (complete, test)
- Phase 5: US3 Update Tasks (complete, test)
- Phase 6: US4 Delete Tasks (complete, test)
- Phase 7: US5 Mark Complete (complete, test)
- Phase 8: Polish (complete)

---

## Task Summary

| Phase | Tasks | Description |
|-------|-------|-------------|
| 1 | T001-T006 | Setup project structure |
| 2 | T007-T009 | Foundational data models |
| 3 | T010-T012 | US1: Add Tasks |
| 4 | T013-T016 | US2: View Tasks |
| 5 | T017-T020 | US3: Update Tasks |
| 6 | T021-T024 | US4: Delete Tasks |
| 7 | T025-T030 | US5: Mark Complete/Incomplete |
| 8 | T031-T038 | Polish & Cross-Cutting |
| **Total** | **38 tasks** | **ALL COMPLETED** |

**Minimum Viable Scope (MVP)**: Phases 1-3 + Phase 8 (Add Task + View + Menu) = 21 tasks

---

## References

| Document | Path | Used For |
|----------|------|----------|
| Feature Spec | spec.md | User stories, acceptance scenarios, functional requirements |
| Implementation Plan | plan.md | Project structure, class signatures, control flow |
| Data Model | data-model.md | Task/TaskList fields, validation rules |
| CLI Contract | contracts/cli-interface.yaml | Menu structure, input/output formats |
| Service Contract | contracts/todo-service.yaml | Service method signatures |
| Quickstart | quickstart.md | Usage examples, error handling patterns |
