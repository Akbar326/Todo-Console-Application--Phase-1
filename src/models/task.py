"""Task data model for the Todo Console Application."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """Represents a single task in the todo list."""

    id: int
    title: str
    description: str
    completed: bool = False

    def __str__(self) -> str:
        """Return a string representation of the task.

        Returns:
            A formatted string showing the task ID, status, title, and description.
        """
        status = "✅" if self.completed else "❌"
        return f"{self.id} | {status} | {self.title} | {self.description}"