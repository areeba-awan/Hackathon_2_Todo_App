# Hackathon 2 Todo App

A Phase I in-memory Todo Console Application built with Python using Spec-Driven Development (SDD) methodology.

## Overview

This is a menu-driven command-line todo list manager that provides complete CRUD (Create, Read, Update, Delete) operations for managing tasks. The application runs entirely in-memory with no persistence beyond the current session.

## Features

- **Add Task** - Create new tasks with descriptions
- **View Tasks** - Display all tasks with status indicators
- **Update Task** - Modify existing task descriptions
- **Delete Task** - Remove tasks with confirmation
- **Mark Complete** - Toggle tasks to done status
- **Mark Incomplete** - Toggle tasks back to pending status
- **Exit** - Gracefully close the application

## Quick Start

### Requirements

- Python 3.10 or higher
- No external dependencies (uses only Python standard library)

### Running the Application

```bash
# Run from project root
python -m src.cli.main

# Or navigate directly
cd src/cli && python main.py
```

### Running Tests

```bash
pytest tests/unit/
# or
python -m unittest discover tests/unit/
```

## Project Structure

```
Hackathon_2_Todo_App/
├── Phase I/                          # Main application directory
│   ├── src/                          # Source code
│   │   ├── models/task.py           # Task and TaskList data models
│   │   ├── services/todo_service.py # Business logic and CRUD operations
│   │   └── cli/                     # Menu system and CLI handlers
│   ├── tests/unit/                  # Unit tests
│   ├── specs/                       # Feature specifications (SDD)
│   ├── history/                     # Prompt History Records
│   └── CLAUDE.md                    # SDD guidelines and constitution
└── README.md
```

## Architecture

The application follows **Clean Architecture** with three layers:

| Layer | Location | Responsibility |
|-------|----------|----------------|
| Data | `src/models/` | Data structures (Task, TaskList) |
| Business Logic | `src/services/` | TodoService with validation |
| Presentation | `src/cli/` | Menu display and user input |

## Technology Stack

- **Language**: Python 3.10+
- **Testing**: unittest
- **Dependencies**: None (standard library only)

## Data Model

- **Task**: Simple dataclass with `id`, `description`, and `is_complete`
- **TaskList**: Collection manager with sequential ID generation
- All operations validated in the service layer

## Development Methodology

This project uses **Spec-Driven Development (SDD)**, a methodology that emphasizes:

1. **Constitution** - Project principles and rules
2. **Specification** - Feature requirements and user stories
3. **Plan** - Implementation design and decisions
4. **Tasks** - Implementation checklist with test cases
5. **Prompt History Records** - Documentation of all decisions

## License

MIT License
