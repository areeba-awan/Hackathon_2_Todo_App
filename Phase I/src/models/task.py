"""Task data model for the in-memory todo application."""

from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    """Represents a single todo task.

    Attributes:
        id: Unique identifier (1-based, sequential, auto-assigned)
        description: The task description text (non-empty string)
        is_complete: Whether the task is completed (default: False)
    """
    id: int
    description: str
    is_complete: bool = False


class TaskList:
    """In-memory collection of tasks.

    Maintains tasks in insertion order and generates unique sequential IDs.
    """

    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self._next_id: int = 1

    def add(self, description: str) -> Task:
        """Add a new task with auto-assigned ID.

        Args:
            description: The task description (non-empty, validated by caller)

        Returns:
            The newly created Task
        """
        task = Task(id=self._next_id, description=description)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_by_id(self, task_id: int) -> Task | None:
        """Find task by ID.

        Args:
            task_id: The task identifier to search for

        Returns:
            The Task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all(self) -> List[Task]:
        """Return all tasks in insertion order.

        Returns:
            Copy of the tasks list to prevent external modification
        """
        return self.tasks.copy()

    def update(self, task_id: int, new_description: str) -> bool:
        """Update task description by ID.

        Args:
            task_id: The task identifier
            new_description: The new description (non-empty, validated by caller)

        Returns:
            True if task was updated, False if not found
        """
        task = self.get_by_id(task_id)
        if task is not None:
            task.description = new_description
            return True
        return False

    def delete(self, task_id: int) -> bool:
        """Delete task by ID.

        Args:
            task_id: The task identifier

        Returns:
            True if task was deleted, False if not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def mark_complete(self, task_id: int) -> bool:
        """Mark task as complete.

        Args:
            task_id: The task identifier

        Returns:
            True if task was marked, False if not found
        """
        task = self.get_by_id(task_id)
        if task is not None:
            task.is_complete = True
            return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """Mark task as incomplete.

        Args:
            task_id: The task identifier

        Returns:
            True if task was marked, False if not found
        """
        task = self.get_by_id(task_id)
        if task is not None:
            task.is_complete = False
            return True
        return False
