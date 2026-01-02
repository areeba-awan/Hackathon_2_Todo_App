"""Menu system and application entry point for the todo application with enhanced UX."""

import sys
import os
from src.services.todo_service import TodoService
from src.cli.handlers import (
    handle_add_task,
    handle_view_tasks,
    handle_update_task,
    handle_delete_task,
    handle_mark_complete,
    handle_mark_incomplete,
    Colors,
    print_header,
    print_error,
)


def clear_screen() -> None:
    """Clear the terminal screen for a fresh display."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu() -> None:
    """Print the main menu options with keyboard shortcuts."""
    # Use colors for enhanced display (ASCII for Windows compatibility)
    print(f"\n{Colors.BOLD}{Colors.CYAN}========================================{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}  TODO LIST MANAGER{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}========================================{Colors.RESET}\n")

    print(f"  {Colors.GREEN}[a]{Colors.RESET} or {Colors.GREEN}1{Colors.RESET}  Add a new task")
    print(f"  {Colors.BLUE}[v]{Colors.RESET} or {Colors.BLUE}2{Colors.RESET}  View all tasks")
    print(f"  {Colors.YELLOW}[u]{Colors.RESET} or {Colors.YELLOW}3{Colors.RESET}  Update a task")
    print(f"  {Colors.RED}[d]{Colors.RESET} or {Colors.RED}4{Colors.RESET}  Delete a task")
    print(f"  {Colors.GREEN}[c]{Colors.RESET} or {Colors.GREEN}5{Colors.RESET}  Mark as complete [OK]")
    print(f"  {Colors.YELLOW}[i]{Colors.RESET} or {Colors.YELLOW}6{Colors.RESET}  Mark as incomplete [ ]")
    print(f"  {Colors.BRIGHT_BLACK}[x]{Colors.RESET} or {Colors.BRIGHT_BLACK}7{Colors.RESET}  Exit")
    print()


def get_user_choice() -> str:
    """Get and validate user menu selection with keyboard shortcuts.

    Returns:
        The validated user choice string
    """
    # Map shortcuts to numbers
    shortcut_map = {
        'a': '1', 'A': '1',
        'v': '2', 'V': '2',
        'u': '3', 'U': '3',
        'd': '4', 'D': '4',
        'c': '5', 'C': '5',
        'i': '6', 'I': '6',
        'x': '7', 'X': '7', 'q': '7', 'Q': '7',
    }

    valid_choices = {"1", "2", "3", "4", "5", "6", "7"}

    while True:
        choice = input(f"{Colors.CYAN}Choose an option: {Colors.RESET}").strip()

        # Check for keyboard shortcuts first
        if choice in shortcut_map:
            choice = shortcut_map[choice]

        if choice in valid_choices:
            return choice

        # Enhanced error message
        print_error("Invalid option", "Enter 1-7 or a shortcut key like a, v, u, d, c, i, x")


def handle_choice(service: TodoService, choice: str) -> bool:
    """Route user choice to appropriate handler with enhanced error handling.

    Args:
        service: The TodoService instance
        choice: The user's menu choice

    Returns:
        True if user wants to exit, False otherwise
    """
    handlers = {
        "1": ("Add Task", handle_add_task),
        "2": ("View Tasks", handle_view_tasks),
        "3": ("Update Task", handle_update_task),
        "4": ("Delete Task", handle_delete_task),
        "5": ("Mark Complete", handle_mark_complete),
        "6": ("Mark Incomplete", handle_mark_incomplete),
    }

    if choice == "7":
        return True

    handler_info = handlers.get(choice)
    if handler_info:
        name, handler = handler_info
        try:
            handler(service)
            # Small delay before showing menu again for better UX
            import time
            time.sleep(0.5)
        except KeyboardInterrupt:
            print()
            print_info("Operation interrupted (press Enter to continue)")
            try:
                input()
            except:
                pass
        except EOFError:
            print()
            print_info("Operation cancelled")
        except Exception as e:
            print_error(f"Something went wrong: {e}", "Please try again")

    return False


def main_loop() -> None:
    """Run the main menu loop until user exits."""
    service = TodoService()

    # Welcome banner
    clear_screen()
    print(f"\n{Colors.BOLD}{Colors.GREEN}Welcome to Todo List Manager!{Colors.RESET}")
    print(f"{Colors.DIM}Manage your tasks efficiently{Colors.RESET}\n")

    try:
        while True:
            try:
                display_menu()
                choice = get_user_choice()
                should_exit = handle_choice(service, choice)
                if should_exit:
                    print(f"\n{Colors.BOLD}{Colors.GREEN}Thanks for using Todo List Manager!{Colors.RESET}")
                    print(f"{Colors.DIM}See you next time!{Colors.RESET}\n")
                    break
            except KeyboardInterrupt:
                print()
                print_info("Use 'x' or '7' to exit, or press Ctrl+C again to force quit.")
                continue
            except EOFError:
                print(f"\n\n{Colors.BRIGHT_BLACK}Goodbye!{Colors.RESET}")
                break
    except KeyboardInterrupt:
        # Force quit on second Ctrl+C
        print(f"\n\n{Colors.BRIGHT_BLACK}Goodbye!{Colors.RESET}")


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print(f"\n{Colors.BRIGHT_BLACK}Goodbye!{Colors.RESET}")
        sys.exit(0)
