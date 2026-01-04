# API Contracts: Todo Console Application

## TaskManager Service Contracts

### Public Interface

#### `add_task(title: str, description: str) -> Task`
- **Purpose**: Creates a new task with the given title and description
- **Preconditions**:
  - title must be a non-empty string
  - description can be any string (including empty)
- **Postconditions**:
  - New Task object is created with unique ID
  - Task is stored in the manager
  - New task has completed=False by default
- **Returns**: Task object with assigned ID
- **Errors**: ValueError if title is empty

#### `get_all_tasks() -> List[Task]`
- **Purpose**: Retrieves all tasks managed by this instance
- **Preconditions**: None
- **Postconditions**: None
- **Returns**: List of all Task objects (empty list if no tasks)
- **Errors**: None

#### `get_task(task_id: int) -> Optional[Task]`
- **Purpose**: Retrieves a specific task by its ID
- **Preconditions**: None
- **Postconditions**: None
- **Returns**: Task object if found, None if not found
- **Errors**: None

#### `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]`
- **Purpose**: Updates an existing task's title and/or description
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Task properties are updated if provided
- **Returns**: Updated Task object if successful, None if task not found
- **Errors**: None

#### `delete_task(task_id: int) -> bool`
- **Purpose**: Removes a task from the manager
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Task is removed from storage
- **Returns**: True if task was deleted, False if not found
- **Errors**: None

#### `toggle_task_status(task_id: int) -> Optional[Task]`
- **Purpose**: Toggles the completion status of a task
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Task's completed status is flipped
- **Returns**: Updated Task object if successful, None if task not found
- **Errors**: None

## CLI Interface Contracts

### User Input Validation

#### Menu Selection
- Accepts integer input from 1-6
- Invalid input shows error message and returns to menu
- Out of range input shows error message and returns to menu

#### Task ID Input
- Accepts integer input for task operations
- Invalid input shows error message and returns to menu
- Non-existent task ID shows appropriate error message

#### Task Title/Description Input
- Title must be non-empty string
- Description can be empty string
- Invalid input (empty title) shows error message and returns to menu