# Todo Console Application

A simple, interactive command-line todo application built in Python that allows users to manage tasks entirely in memory.

## Features

- **Add Tasks**: Create new tasks with titles and descriptions
- **View Tasks**: Display all tasks with clear status indicators (complete/incomplete)
- **Update Tasks**: Modify existing task details (title and description)
- **Delete Tasks**: Remove tasks using unique task IDs
- **Mark Complete/Incomplete**: Toggle task completion status

## Technology Stack

- **Language**: Python 3.13+
- **Tooling**: UV package manager
- **Development**: Claude Code, SpecKit Plus

## Setup & Installation

1. Ensure you have Python 3.13+ installed on your system
2. Install UV package manager if not already installed:
   ```bash
   pip install uv
   ```
3. Clone or download this repository
4. Navigate to the project directory

## Running the Application

To run the Todo Console Application:

```bash
python -m src.cli.main
```

This will start the interactive command-line interface where you can manage your tasks.

## How to Use

Once the application is running, you'll see the main menu with the following options:

1. **Add task**: Enter a title and optional description to create a new task
2. **View tasks**: Display all tasks with their status (✅ for complete, ❌ for incomplete)
3. **Update task**: Modify an existing task by providing its ID and new details
4. **Delete task**: Remove a task by providing its unique ID
5. **Mark task complete/incomplete**: Toggle the status of a task by providing its ID
6. **Exit**: Quit the application

All data is stored in memory only and will be lost when the application exits.