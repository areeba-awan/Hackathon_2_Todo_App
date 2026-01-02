"""Unit tests for the TodoService."""

import unittest
from src.services.todo_service import TodoService


class TestTodoService(unittest.TestCase):
    """Tests for the TodoService class."""

    def setUp(self):
        """Set up test fixtures."""
        self.service = TodoService()

    def test_add_task_valid_description(self):
        """Test adding a task with valid description."""
        task = self.service.add_task("Buy groceries")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy groceries")
        self.assertFalse(task.is_complete)

    def test_add_task_preserves_whitespace(self):
        """Test that whitespace in description is preserved."""
        task = self.service.add_task("  Task with spaces  ")
        self.assertEqual(task.description, "  Task with spaces  ")

    def test_add_task_empty_raises_error(self):
        """Test that empty description raises ValueError."""
        with self.assertRaises(ValueError):
            self.service.add_task("")

    def test_add_task_whitespace_only_raises_error(self):
        """Test that whitespace-only description raises ValueError."""
        with self.assertRaises(ValueError):
            self.service.add_task("   ")

    def test_get_all_empty(self):
        """Test getting all tasks when empty."""
        tasks = self.service.get_all_tasks()
        self.assertEqual(tasks, [])

    def test_get_all_with_tasks(self):
        """Test getting all tasks."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 2)

    def test_get_task_existing(self):
        """Test getting an existing task."""
        self.service.add_task("Test task")
        task = self.service.get_task(1)
        self.assertIsNotNone(task)
        self.assertEqual(task.description, "Test task")

    def test_get_task_nonexistent(self):
        """Test getting a non-existent task."""
        task = self.service.get_task(999)
        self.assertIsNone(task)

    def test_update_task_valid(self):
        """Test updating a task with valid description."""
        self.service.add_task("Original")
        success = self.service.update_task(1, "Updated")
        self.assertTrue(success)
        task = self.service.get_task(1)
        self.assertEqual(task.description, "Updated")

    def test_update_task_invalid_id(self):
        """Test updating a non-existent task."""
        success = self.service.update_task(999, "New description")
        self.assertFalse(success)

    def test_update_task_empty_description_raises_error(self):
        """Test that empty description raises ValueError."""
        self.service.add_task("Test task")
        with self.assertRaises(ValueError):
            self.service.update_task(1, "")

    def test_delete_task_valid(self):
        """Test deleting a valid task."""
        self.service.add_task("Task to delete")
        success = self.service.delete_task(1)
        self.assertTrue(success)
        self.assertEqual(len(self.service.get_all_tasks()), 0)

    def test_delete_task_invalid_id(self):
        """Test deleting a non-existent task."""
        success = self.service.delete_task(999)
        self.assertFalse(success)

    def test_mark_complete(self):
        """Test marking a task as complete."""
        self.service.add_task("Test task")
        success = self.service.mark_complete(1)
        self.assertTrue(success)
        task = self.service.get_task(1)
        self.assertTrue(task.is_complete)

    def test_mark_complete_invalid_id(self):
        """Test marking a non-existent task as complete."""
        success = self.service.mark_complete(999)
        self.assertFalse(success)

    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        self.service.add_task("Test task")
        self.service.mark_complete(1)
        success = self.service.mark_incomplete(1)
        self.assertTrue(success)
        task = self.service.get_task(1)
        self.assertFalse(task.is_complete)

    def test_mark_incomplete_invalid_id(self):
        """Test marking a non-existent task as incomplete."""
        success = self.service.mark_incomplete(999)
        self.assertFalse(success)

    def test_sequential_id_generation(self):
        """Test that IDs are generated sequentially."""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        task3 = self.service.add_task("Task 3")
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)


if __name__ == "__main__":
    unittest.main()
