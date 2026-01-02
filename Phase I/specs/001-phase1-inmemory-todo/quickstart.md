# Quickstart: Phase I - In-Memory Todo Console Application

**Feature**: 001-phase1-inmemory-todo
**Generated**: 2026-01-02

## Prerequisites

- Python 3.10 or higher
- Terminal access

## Installation

```bash
# No external dependencies
# Just ensure Python 3.10+ is installed
python3 --version
```

## Running the Application

```bash
# From project root
python -m todo_app.main

# Or
cd todo_app
python main.py
```

## User Guide

### Main Menu

```
=== Todo App ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit
Enter choice (1-7):
```

### Adding a Task

1. Select option `1`
2. Enter task description when prompted
3. Task is added with unique ID

### Viewing Tasks

1. Select option `2`
2. See all tasks with ID, description, and status
3. Format: `[ ] ID. Description` (incomplete), `[X] ID. Description` (complete)

### Updating a Task

1. Select option `3`
2. Enter the task ID to update
3. Enter the new description
4. Task is updated

### Deleting a Task

1. Select option `4`
2. Enter the task ID to delete
3. Task is permanently removed

### Marking Complete/Incomplete

1. Select option `5` (complete) or `6` (incomplete)
2. Enter the task ID
3. Task status is updated

### Exiting

Select option `7` to exit. All data is lost (no persistence).

## Error Handling

- Invalid menu choices: Re-prompted with valid options
- Non-numeric ID: Error message, try again
- Invalid ID: "Task not found" message
- Empty description: Error message, operation cancelled
- Empty list operations: "No tasks exist" message
- Ctrl+C: Graceful exit with goodbye message
