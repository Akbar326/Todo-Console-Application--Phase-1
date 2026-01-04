# Quickstart Guide: Todo Console Application

## Phase 1: Getting Started

### Prerequisites
- Python 3.13 or higher
- UV package manager (optional, for dependency management)

### Project Setup

1. **Clone or create the project directory**
   ```bash
   mkdir todo-console-app
   cd todo-console-app
   ```

2. **Create the directory structure**
   ```bash
   mkdir -p src/models src/services src/cli tests/unit tests/integration
   ```

3. **Create the main files**
   - `src/models/task.py` - Task data model
   - `src/services/task_manager.py` - Task management logic
   - `src/cli/main.py` - Main CLI entry point

### Running the Application

```bash
python src/cli/main.py
```

### Basic Usage Flow

1. **Launch the application**
   ```bash
   $ python src/cli/main.py
   ```

2. **You'll see the main menu:**
   ```
   Todo Console Application
   ========================
   1. Add task
   2. View tasks
   3. Update task
   4. Delete task
   5. Mark task complete/incomplete
   6. Exit
   ```

3. **Follow the on-screen prompts** to manage your tasks

### Example Task Management Session

```
$ python src/cli/main.py
Todo Console Application
========================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task complete/incomplete
6. Exit
Choose an option: 1
Enter task title: Buy groceries
Enter task description: Milk, bread, eggs
Task added successfully with ID: 1

Choose an option: 2
ID | Status | Title | Description
---|--------|-------|-------------
1  | ❌     | Buy groceries | Milk, bread, eggs

Choose an option: 5
Enter task ID to toggle: 1
Task 1 marked as complete.

Choose an option: 2
ID | Status | Title | Description
---|--------|-------|-------------
1  | ✅     | Buy groceries | Milk, bread, eggs

Choose an option: 6
Goodbye!
```

### Development Commands

- **Run the application**: `python src/cli/main.py`
- **Run unit tests**: `python -m pytest tests/unit/`
- **Run integration tests**: `python -m pytest tests/integration/`
- **Run all tests**: `python -m pytest tests/`

### Key Files Overview

- `src/models/task.py`: Defines the Task dataclass
- `src/services/task_manager.py`: Contains all business logic for task operations
- `src/cli/main.py`: Handles user interface and input/output
- `tests/unit/`: Unit tests for individual components
- `tests/integration/`: Tests for the complete workflow