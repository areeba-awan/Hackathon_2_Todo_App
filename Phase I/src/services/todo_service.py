"""Todo service for managing tasks in memory."""

from typing import List
from src.models.task import Task, TaskList


class TodoService:
    """Handles all CRUD operations on tasks.

    The service layer contains all business logic and validation.
    Data models (Task, TaskList) are simple containers with no behavior.
    """

    def __init__(self) -> None:
        self._task_list = TaskList()

    def add_task(self, description: str) -> Task:
        """Add a new task with the given description.

        Args:
            description: Non-empty string (whitespace preserved)

        Returns:
            The created Task with assigned ID

        Raises:
            ValueError: If description is empty or whitespace-only
        """
        if not description or description.strip() == "":
            raise ValueError("Description cannot be empty.")
        return self._task_list.add(description)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks in insertion order.

        Returns:
            Copy of all tasks (empty list if none exist)
        """
        return self._task_list.get_all()

    def get_task(self, task_id: int) -> Task | None:
        """Get a single task by ID.

        Args:
            task_id: The unique task identifier

        Returns:
            The Task if found, None otherwise
        """
        return self._task_list.get_by_id(task_id)

    def update_task(self, task_id: int, new_description: str) -> bool:
        """Update a task's description.

        Args:
            task_id: The unique task identifier
            new_description: Non-empty string

        Returns:
            True if task was updated, False if not found

        Raises:
            ValueError: If new_description is empty or whitespace-only
        """
        if not new_description or new_description.strip() == "":
            raise ValueError("Description cannot be empty.")
        return self._task_list.update(task_id, new_description)

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: The unique task identifier

        Returns:
            True if task was deleted, False if not found
        """
        return self._task_list.delete(task_id)

    def mark_complete(self, task_id: int) -> bool:
        """Mark a task as complete.

        Args:
            task_id: The unique task identifier

        Returns:
            True if task was marked, False if not found
        """
        return self._task_list.mark_complete(task_id)

    def mark_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete.

        Args:
            task_id: The unique task identifier

        Returns:
            True if task was marked, False if not found
        """
        return self._task_list.mark_incomplete(task_id)
