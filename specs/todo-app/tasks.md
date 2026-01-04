---
description: "Task list for Todo Console Application implementation"
---

# Tasks: Todo Console Application

**Input**: Design documents from `/specs/todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan
- [ ] T002 Initialize Python 3.13 project with basic dependencies
- [ ] T003 [P] Configure linting and formatting tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Create Task data model in src/models/task.py
- [ ] T005 Create TaskManager service in src/services/task_manager.py
- [ ] T006 Create CLI interface structure in src/cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with a title and description

**Independent Test**: User can run the application, select add task option, provide title and description, and see the task created with a unique ID and marked as incomplete

### Implementation for User Story 1

- [X] T007 [P] [US1] Implement Task dataclass with id, title, description, completed attributes in src/models/task.py
- [X] T008 [US1] Implement TaskManager.add_task method in src/services/task_manager.py
- [X] T009 [US1] Implement CLI add task menu option in src/cli/main.py
- [X] T010 [US1] Add input validation for task title in src/cli/main.py
- [X] T011 [US1] Add unique ID generation in src/services/task_manager.py
- [X] T012 [US1] Test add task functionality manually via console

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to view a list of all tasks with clear status indicators

**Independent Test**: User can run the application, add tasks, then view the task list to see all tasks with their unique IDs, titles, descriptions, and completion status clearly indicated

### Implementation for User Story 2

- [X] T013 [P] [US2] Implement TaskManager.get_all_tasks method in src/services/task_manager.py
- [X] T014 [US2] Implement CLI view tasks menu option in src/cli/main.py
- [X] T015 [US2] Add task display formatting with status indicators in src/cli/main.py
- [X] T016 [US2] Implement status indicator logic (complete/incomplete) in src/cli/main.py
- [X] T017 [US2] Test view tasks functionality manually via console

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Enable users to mark tasks as complete or incomplete

**Independent Test**: User can run the application, add a task, then mark it as complete and verify the status changes, then mark it as incomplete and verify the status changes back

### Implementation for User Story 3

- [X] T018 [P] [US3] Implement TaskManager.toggle_task_status method in src/services/task_manager.py
- [X] T019 [US3] Implement CLI toggle task status menu option in src/cli/main.py
- [X] T020 [US3] Add input validation for task ID in src/cli/main.py
- [X] T021 [US3] Implement status display updates in CLI after toggle in src/cli/main.py
- [X] T022 [US3] Test mark task complete/incomplete functionality manually via console

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Enable users to update existing task details

**Independent Test**: User can run the application, add a task, then update its title or description and verify the changes are saved

### Implementation for User Story 4

- [X] T023 [P] [US4] Implement TaskManager.update_task method in src/services/task_manager.py
- [X] T024 [US4] Implement CLI update task menu option in src/cli/main.py
- [X] T025 [US4] Add input validation for update task in src/cli/main.py
- [X] T026 [US4] Test update task functionality manually via console

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P2)

**Goal**: Enable users to delete tasks using a unique task ID

**Independent Test**: User can run the application, add a task, then delete it using its unique ID and verify it's no longer in the task list

### Implementation for User Story 5

- [X] T027 [P] [US5] Implement TaskManager.delete_task method in src/services/task_manager.py
- [X] T028 [US5] Implement CLI delete task menu option in src/cli/main.py
- [X] T029 [US5] Add input validation for delete task in src/cli/main.py
- [X] T030 [US5] Test delete task functionality manually via console

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T031 [P] Add comprehensive error handling for invalid inputs across all CLI operations
- [X] T032 [P] Add proper menu navigation and user flow in src/cli/main.py
- [X] T033 [P] Add documentation strings to all functions in src/models/task.py and src/services/task_manager.py
- [X] T034 [P] Implement graceful exit option in src/cli/main.py
- [X] T035 [P] Add input validation across all user inputs in src/cli/main.py
- [X] T036 Run quickstart validation to ensure all features work as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement Task dataclass with id, title, description, completed attributes in src/models/task.py"
Task: "Implement TaskManager.add_task method in src/services/task_manager.py"
Task: "Implement CLI add task menu option in src/cli/main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence