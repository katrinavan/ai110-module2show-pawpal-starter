# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Smarter Scheduling

The scheduling system now includes several algorithmic improvements:
- Tasks can be sorted by time in chronological order.
- Tasks can be filtered by completion status or pet name.
- Daily and weekly recurring tasks automatically create the next occurrence when marked complete.
- The scheduler can detect simple conflicts when two tasks are scheduled at the same exact time.

## Testing PawPal+

The PawPal+ system includes automated tests to verify core scheduling behavior.

To run the tests:
```bash
python -m pytest
To run the tests:
~~~bash
python -m pytest
~~~

The current test suite checks:
- task completion status updates correctly
- adding a task increases a pet's task count
- tasks are sorted in chronological order
- daily recurring tasks create a new task for the next day
- conflict detection flags duplicate task times
- pets with no tasks return an empty schedule

**Confidence Level:** 4/5 stars.  
The current implementation is reliable for the main scheduling behaviors that were tested, but additional edge cases such as invalid time formats and more advanced overlapping task logic could still be added in future iterations.
~~~
## 4. Testing and Verification

**a. What you tested**

I tested several core behaviors of the PawPal+ system. These included verifying that calling `mark_complete()` changes a task's status, adding a task to a pet increases the pet's task count, sorting returns tasks in chronological order, daily recurring tasks create a new task for the next day, and conflict detection flags tasks scheduled at the same exact time. I also tested an edge case where a pet has no tasks to confirm the scheduler returns an empty schedule instead of failing. These tests were important because they covered both the main happy-path functionality and a few realistic edge cases.

**b. Confidence**

I am fairly confident that the scheduler works correctly for the current implementation because the core features were verified through automated tests and the demo script also worked as expected. My confidence level is 4 out of 5 stars. If I had more time, I would test additional edge cases such as invalid time formats, overlapping tasks with durations, and more advanced scheduling rules involving owner preferences and priorities.
