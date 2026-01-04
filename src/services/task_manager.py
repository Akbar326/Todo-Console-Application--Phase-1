"""TaskManager service for the Todo Console Application."""

from typing import Dict, List, Optional
from src.models.task import Task


class TaskManager:
    """Manages tasks in memory for the todo application."""

    def __init__(self):
        """Initialize the TaskManager with an empty task dictionary and next ID counter."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and description.

        Args:
            title: The title of the task (required)
            description: The description of the task (optional)

        Returns:
            The newly created Task object with a unique ID

        Raises:
            ValueError: If the title is empty or contains only whitespace
        """
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task_id = self._next_id
        self._next_id += 1

        task = Task(id=task_id, title=title.strip(), description=description.strip())
        self._tasks[task_id] = task

        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the manager.

        Returns:
            A list of all Task objects, sorted by ID
        """
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            The updated Task object if successful, None if task not found
        """
        task = self._tasks.get(task_id)
        if task is None:
            return None

        if title is not None:
            task.title = title.strip() if title.strip() else task.title
        if description is not None:
            task.description = description.strip()

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_task_status(self, task_id: int) -> Optional[Task]:
        """
        Toggle the completion status of a task.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            The updated Task object if successful, None if task not found
        """
        task = self._tasks.get(task_id)
        if task is None:
            return None

        task.completed = not task.completed
        return task