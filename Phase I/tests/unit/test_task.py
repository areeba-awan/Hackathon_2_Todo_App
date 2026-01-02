"""Unit tests for the Task and TaskList models."""

import unittest
from src.models.task import Task, TaskList


class TestTask(unittest.TestCase):
    """Tests for the Task dataclass."""

    def test_task_creation(self):
        """Test creating a task with all fields."""
        task = Task(id=1, description="Test task", is_complete=False)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.is_complete, False)

    def test_task_default_complete_status(self):
        """Test that is_complete defaults to False."""
        task = Task(id=1, description="Test task")
        self.assertFalse(task.is_complete)

    def test_task_equality(self):
        """Test task equality by value."""
        task1 = Task(id=1, description="Test", is_complete=False)
        task2 = Task(id=1, description="Test", is_complete=False)
        self.assertEqual(task1, task2)

    def test_task_inequality(self):
        """Test task inequality with different values."""
        task1 = Task(id=1, description="Test", is_complete=False)
        task2 = Task(id=2, description="Test", is_complete=False)
        self.assertNotEqual(task1, task2)


class TestTaskList(unittest.TestCase):
    """Tests for the TaskList class."""

    def test_empty_task_list(self):
        """Test empty task list initialization."""
        task_list = TaskList()
        self.assertEqual(len(task_list.tasks), 0)
        self.assertEqual(task_list._next_id, 1)

    def test_add_task(self):
        """Test adding a task."""
        task_list = TaskList()
        task = task_list.add("Buy groceries")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy groceries")
        self.assertFalse(task.is_complete)
        self.assertEqual(len(task_list.tasks), 1)
        self.assertEqual(task_list._next_id, 2)

    def test_add_multiple_tasks(self):
        """Test adding multiple tasks with sequential IDs."""
        task_list = TaskList()
        task1 = task_list.add("First task")
        task2 = task_list.add("Second task")
        task3 = task_list.add("Third task")
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)
        self.assertEqual(task_list._next_id, 4)

    def test_get_by_id_existing(self):
        """Test getting an existing task by ID."""
        task_list = TaskList()
        task_list.add("Test task")
        found = task_list.get_by_id(1)
        self.assertIsNotNone(found)
        self.assertEqual(found.id, 1)
        self.assertEqual(found.description, "Test task")

    def test_get_by_id_nonexistent(self):
        """Test getting a non-existent task by ID."""
        task_list = TaskList()
        found = task_list.get_by_id(999)
        self.assertIsNone(found)

    def test_get_all(self):
        """Test getting all tasks."""
        task_list = TaskList()
        task_list.add("Task 1")
        task_list.add("Task 2")
        all_tasks = task_list.get_all()
        self.assertEqual(len(all_tasks), 2)
        # Verify it's a copy, not the original list
        self.assertIsNot(all_tasks, task_list.tasks)

    def test_update_existing_task(self):
        """Test updating an existing task."""
        task_list = TaskList()
        task_list.add("Original description")
        success = task_list.update(1, "New description")
        self.assertTrue(success)
        task = task_list.get_by_id(1)
        self.assertEqual(task.description, "New description")

    def test_update_nonexistent_task(self):
        """Test updating a non-existent task."""
        task_list = TaskList()
        success = task_list.update(999, "New description")
        self.assertFalse(success)

    def test_delete_existing_task(self):
        """Test deleting an existing task."""
        task_list = TaskList()
        task_list.add("Task to delete")
        self.assertEqual(len(task_list.tasks), 1)
        success = task_list.delete(1)
        self.assertTrue(success)
        self.assertEqual(len(task_list.tasks), 0)

    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task."""
        task_list = TaskList()
        success = task_list.delete(999)
        self.assertFalse(success)

    def test_mark_complete(self):
        """Test marking a task as complete."""
        task_list = TaskList()
        task_list.add("Test task")
        success = task_list.mark_complete(1)
        self.assertTrue(success)
        task = task_list.get_by_id(1)
        self.assertTrue(task.is_complete)

    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task_list = TaskList()
        task_list.add("Test task")
        task_list.mark_complete(1)
        success = task_list.mark_incomplete(1)
        self.assertTrue(success)
        task = task_list.get_by_id(1)
        self.assertFalse(task.is_complete)

    def test_id_stability_after_deletion(self):
        """Test that IDs remain stable after deletion."""
        task_list = TaskList()
        task_list.add("Task 1")
        task_list.add("Task 2")
        task_list.add("Task 3")
        task_list.delete(2)  # Delete middle task
        new_task = task_list.add("Task 4")
        self.assertEqual(new_task.id, 4)  # Should get ID 4, not reuse 2


if __name__ == "__main__":
    unittest.main()
