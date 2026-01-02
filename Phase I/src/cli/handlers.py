"""CLI handlers for todo application operations with enhanced UX."""

from src.services.todo_service import TodoService


# ANSI color codes
class Colors:
    """Terminal color codes for enhanced output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright foreground colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Background colors
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"


def print_success(message: str) -> None:
    """Print a success message in green."""
    print(f"{Colors.GREEN}[OK] {message}{Colors.RESET}")


def print_error(message: str, hint: str = "") -> None:
    """Print an error message in red with optional hint."""
    print(f"{Colors.RED}✗ {message}{Colors.RESET}")
    if hint:
        print(f"{Colors.DIM}  → {hint}{Colors.RESET}")


def print_info(message: str) -> None:
    """Print an info message in cyan."""
    print(f"{Colors.CYAN}→ {message}{Colors.RESET}")


def print_header(message: str) -> None:
    """Print a header message in bold cyan."""
    print(f"{Colors.BOLD}{Colors.CYAN}{message}{Colors.RESET}")


def print_task(task, index: int = None) -> None:
    """Print a single task with nice formatting."""
    task_num = f"#{task.id}" if index is None else f"#{index}"
    status = f"{Colors.GREEN}[X]{Colors.RESET}" if task.is_complete else f"{Colors.YELLOW}[ ]{Colors.RESET}"
    status_text = "DONE" if task.is_complete else "TODO"

    # Color code based on status
    status_color = Colors.GREEN if task.is_complete else Colors.YELLOW

    print(f"  {Colors.BOLD}{task_num:<4}{Colors.RESET} {status}  {status_color}{status_text:<6}{Colors.RESET}  {task.description}")


def get_valid_description(prompt: str = "Description: ") -> str:
    """Get a non-empty description from user input with enhanced prompts."""
    while True:
        desc = input(f"{Colors.CYAN}{prompt}{Colors.RESET}").strip()
        if not desc:
            print_error("Task description cannot be empty", "Type something and press Enter")
        else:
            return desc


def get_valid_task_id(prompt: str = "Task ID: ") -> int:
    """Get a valid task ID from user input with enhanced prompts."""
    while True:
        try:
            task_id = int(input(f"{Colors.CYAN}{prompt}{Colors.RESET}"))
            if task_id <= 0:
                print_error("Task ID must be a positive number", "Enter a number like 1, 2, 3...")
                continue
            return task_id
        except ValueError:
            print_error("Please enter a valid number", "Numbers only, like 1 or 2")


def handle_add_task(service: TodoService) -> None:
    """Handle the Add Task menu option with enhanced UX."""
    print_header("\n--- Add New Task ---\n")
    try:
        description = get_valid_description("What needs to be done?")
        task = service.add_task(description)
        print_success(f"Task added: \"{task.description}\"")
        print_info(f"Task #{task.id} created")
    except ValueError as e:
        print_error(str(e))
    except (EOFError, KeyboardInterrupt):
        print_info("Operation cancelled")


def handle_view_tasks(service: TodoService) -> None:
    """Handle the View Tasks menu option with enhanced formatting."""
    tasks = service.get_all_tasks()

    print_header("\n--- Your Tasks ---\n")

    if not tasks:
        print_info("No tasks yet!")
        print("  Add your first task using option 1")
        return

    # Stats
    total = len(tasks)
    completed = sum(1 for t in tasks if t.is_complete)
    pending = total - completed

    print(f"\n{Colors.DIM}Progress: {completed}/{total} done ({pending} pending){Colors.RESET}")
    print()

    for i, task in enumerate(tasks, 1):
        print_task(task, index=i)

    # Footer stats
    print(f"\n{Colors.DIM}─{Colors.RESET}" * 40)
    stats = f"{Colors.GREEN}[OK] {completed}{Colors.RESET} completed  ·  {Colors.YELLOW}[ ] {pending}{Colors.RESET} pending"
    print(f"  {stats}")


def handle_update_task(service: TodoService) -> None:
    """Handle the Update Task menu option with enhanced UX."""
    print_header("\n--- Update Task ---\n")
    try:
        task_id = get_valid_task_id("Which task to update? (ID)")

        task = service.get_task(task_id)
        if task is None:
            print_error(f"Task #{task_id} not found", "Use View Tasks to see all tasks")
            return

        print(f"\nCurrent: \"{task.description}\"")
        print()
        description = get_valid_description("New description (or press Enter to keep current): ")

        if description.strip() == "":
            print_info("No changes made")
            return

        success = service.update_task(task_id, description)
        if success:
            print_success("Task updated successfully!")
            print(f"  \"{description}\"")
        else:
            print_error("Failed to update task")

    except (ValueError, EOFError, KeyboardInterrupt):
        print_info("Operation cancelled")


def handle_delete_task(service: TodoService) -> None:
    """Handle the Delete Task menu option with confirmation."""
    print_header("\n--- Delete Task ---\n")
    try:
        task_id = get_valid_task_id("Which task to delete? (ID)")

        task = service.get_task(task_id)
        if task is None:
            print_error(f"Task #{task_id} not found", "Use View Tasks to see all tasks")
            return

        # Show task and confirm
        print()
        print(f"  Task: \"{task.description}\"")
        status = "Done" if task.is_complete else "Todo"
        print(f"  Status: {status}")
        print()

        confirm = input(f"{Colors.YELLOW}Delete this task? [y/N]: {Colors.RESET}").strip().lower()

        if confirm != 'y':
            print_info("Cancelled - task not deleted")
            return

        success = service.delete_task(task_id)
        if success:
            print_success("Task deleted")
        else:
            print_error("Failed to delete task")

    except (EOFError, KeyboardInterrupt):
        print_info("Operation cancelled")


def handle_mark_complete(service: TodoService) -> None:
    """Handle the Mark Complete menu option."""
    print_header("\n--- Mark Complete ---\n")
    try:
        task_id = get_valid_task_id("Which task is done? (ID)")

        task = service.get_task(task_id)
        if task is None:
            print_error(f"Task #{task_id} not found", "Use View Tasks to see all tasks")
            return

        if task.is_complete:
            print_info(f"Task #{task_id} is already marked as complete")
            return

        success = service.mark_complete(task_id)
        if success:
            print_success(f"Marked \"{task.description}\" as complete!")
        else:
            print_error("Failed to update task")

    except (EOFError, KeyboardInterrupt):
        print_info("Operation cancelled")


def handle_mark_incomplete(service: TodoService) -> None:
    """Handle the Mark Incomplete menu option."""
    print_header("\n--- Mark Incomplete ---\n")
    try:
        task_id = get_valid_task_id("Which task is not done? (ID)")

        task = service.get_task(task_id)
        if task is None:
            print_error(f"Task #{task_id} not found", "Use View Tasks to see all tasks")
            return

        if not task.is_complete:
            print_info(f"Task #{task_id} is already marked as incomplete")
            return

        success = service.mark_incomplete(task_id)
        if success:
            print_success(f"Marked \"{task.description}\" as todo again")
        else:
            print_error("Failed to update task")

    except (EOFError, KeyboardInterrupt):
        print_info("Operation cancelled")
