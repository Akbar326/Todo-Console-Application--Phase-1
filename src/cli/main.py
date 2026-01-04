"""Main CLI interface for the Todo Console Application."""

import sys
import os
from typing import Optional

# Add the project root to the Python path to enable imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.task_manager import TaskManager
from src.models.task import Task


class TodoCLI:
    """Command-line interface for the todo application."""

    def __init__(self):
        """Initialize the CLI with a TaskManager instance."""
        self.task_manager = TaskManager()

    def display_menu(self):
        """Display the main menu options."""
        print("\nTodo Console Application")
        print("========================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task complete/incomplete")
        print("6. Exit")
        print()

    def get_user_choice(self) -> str:
        """Get and validate user menu choice."""
        try:
            choice = input("Choose an option: ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            sys.exit(0)

    def add_task(self):
        """Handle adding a new task."""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Error: Task title cannot be empty.")
            return

        description = input("Enter task description (optional): ").strip()

        try:
            task = self.task_manager.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_tasks(self):
        """Handle viewing all tasks."""
        print("\n--- View All Tasks ---")
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print("ID | Status | Title | Description")
        print("---|--------|-------|-------------")
        for task in tasks:
            status = "✅" if task.completed else "❌"
            print(f"{task.id:2} | {status:6} | {task.title} | {task.description}")

    def update_task(self):
        """Handle updating an existing task."""
        print("\n--- Update Task ---")
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        # Check if task exists
        existing_task = self.task_manager.get_task(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        print(f"Current task: {existing_task}")

        new_title = input(f"Enter new title (current: '{existing_task.title}', press Enter to keep current): ").strip()
        new_description = input(f"Enter new description (current: '{existing_task.description}', press Enter to keep current): ").strip()

        # Only update if user provided new values
        title_to_update = new_title if new_title else None
        description_to_update = new_description if new_description else None

        if title_to_update is None and description_to_update is None:
            print("No changes made.")
            return

        updated_task = self.task_manager.update_task(
            task_id,
            title_to_update if title_to_update else None,
            description_to_update if description_to_update != existing_task.description else None
        )

        if updated_task:
            print("Task updated successfully.")
        else:
            print("Error updating task.")

    def delete_task(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        success = self.task_manager.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} not found.")

    def toggle_task_status(self):
        """Handle toggling task completion status."""
        print("\n--- Toggle Task Status ---")
        try:
            task_id = int(input("Enter task ID to toggle: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        task = self.task_manager.toggle_task_status(task_id)
        if task:
            status = "complete" if task.completed else "incomplete"
            print(f"Task {task_id} marked as {status}.")
        else:
            print(f"Error: Task with ID {task_id} not found.")

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo Console Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.toggle_task_status()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1-6.")

            # Pause to let user see the result before showing menu again
            input("\nPress Enter to continue...")


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()