# CLI Contracts: Phase I - In-Memory Todo Console Application

## Menu Interface

### Main Menu Display

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

### User Input Contract

| Menu Option | Input | Expected Behavior |
|-------------|-------|-------------------|
| Add Task | Text (1-1000 chars) | Creates task, displays confirmation |
| View Tasks | None | Displays all tasks or "No tasks" message |
| Update Task | ID (integer) + Text | Updates task, displays confirmation |
| Delete Task | ID (integer) | Deletes task, displays confirmation |
| Mark Complete | ID (integer) | Updates status, displays confirmation |
| Mark Incomplete | ID (integer) | Updates status, displays confirmation |
| Exit | None | Terminates application |

## Command Specifications

### Add Task

**Input Prompt**:
```
Enter task description:
```

**Input Validation**:
- Must be non-empty string
- Must contain at least one non-whitespace character
- Leading/trailing whitespace preserved

**Success Output**:
```
Task added (ID: {id})
```

**Error Output**:
```
Error: Task description cannot be empty.
```

---

### View Tasks

**Output Format**:
```
=== Tasks ===
[ ] 1. Buy groceries
[ ] 2. Walk the dog
[X] 3. Call mom
```

**Empty List Output**:
```
No tasks yet. Add one to get started!
```

**Format Specification**:
- `[ ]` for incomplete, `[X]` for complete
- Space between bracket and ID
- Period after ID
- Task description as entered

---

### Update Task

**Input Prompt 1**:
```
Enter task ID:
```

**Input Prompt 2**:
```
Enter new description:
```

**Input Validation**:
- ID must be existing positive integer
- Description must be non-empty

**Success Output**:
```
Task {id} updated.
```

**Error Output (Invalid ID)**:
```
Error: Task {id} not found.
```

**Error Output (Empty Description)**:
```
Error: Task description cannot be empty.
```

---

### Delete Task

**Input Prompt**:
```
Enter task ID:
```

**Success Output**:
```
Task {id} deleted.
```

**Error Output (Invalid ID)**:
```
Error: Task {id} not found.
```

---

### Mark Complete

**Input Prompt**:
```
Enter task ID:
```

**Success Output**:
```
Task {id} marked complete.
```

**Error Output (Invalid ID)**:
```
Error: Task {id} not found.
```

---

### Mark Incomplete

**Input Prompt**:
```
Enter task ID:
```

**Success Output**:
```
Task {id} marked incomplete.
```

**Error Output (Invalid ID)**:
```
Error: Task {id} not found.
```

---

### Exit

**Output**:
```
Goodbye!
```

(Program terminates with exit code 0)

## Input Error Handling

### Invalid Menu Selection

**Trigger**: User enters non-integer or integer outside 1-7 range

**Output**:
```
Invalid choice. Please enter a number between 1 and 7.
```

**Behavior**: Re-display menu, prompt again

---

### Non-numeric ID

**Trigger**: User enters text when numeric ID expected

**Output**:
```
Error: Please enter a valid number.
```

**Behavior**: Re-prompt for same ID

---

### Keyboard Interrupt (Ctrl+C)

**Output**:
```
\nGoodbye!
```

**Behavior**: Immediate termination, exit code 0

---

### Unexpected Error

**Output**:
```
An unexpected error occurred: {error}
```

**Behavior**: Option to continue or exit (implementation detail)
