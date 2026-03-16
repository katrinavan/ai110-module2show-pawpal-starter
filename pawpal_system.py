from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional


@dataclass
class Task:
    """Represents a single pet care task."""
    description: str
    time: str
    frequency: str = "once"   # once, daily, weekly
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_complete(self) -> Optional["Task"]:
        """Mark the task complete and return the next recurring task if needed."""
        self.completed = True

        if self.frequency == "daily":
            return Task(
                description=self.description,
                time=self.time,
                frequency=self.frequency,
                due_date=self.due_date + timedelta(days=1),
                completed=False,
            )

        if self.frequency == "weekly":
            return Task(
                description=self.description,
                time=self.time,
                frequency=self.frequency,
                due_date=self.due_date + timedelta(weeks=1),
                completed=False,
            )

        return None


@dataclass
class Pet:
    """Stores pet details and a list of tasks."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Manages multiple pets and provides access to their tasks."""
    name: str
    pets: List[Pet] = field(default_factory=list)
    preferences: List[str] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[tuple[Pet, Task]]:
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))
        return all_tasks


class Scheduler:
    """Retrieves, organizes, and manages tasks across pets."""

    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def get_all_tasks(self) -> List[tuple[Pet, Task]]:
        """Get all pet-task pairs."""
        return self.owner.get_all_tasks()

    def get_todays_tasks(self) -> List[tuple[Pet, Task]]:
        """Return only tasks due today."""
        today = date.today()
        return [
            (pet, task)
            for pet, task in self.get_all_tasks()
            if task.due_date == today
        ]

    def sort_by_time(self, tasks: Optional[List[tuple[Pet, Task]]] = None) -> List[tuple[Pet, Task]]:
        """Sort tasks by HH:MM time."""
        if tasks is None:
            tasks = self.get_todays_tasks()
        return sorted(tasks, key=lambda pair: pair[1].time)

    def filter_tasks(
        self,
        completed: Optional[bool] = None,
        pet_name: Optional[str] = None,
    ) -> List[tuple[Pet, Task]]:
        """Filter tasks by completion status and/or pet name."""
        tasks = self.get_all_tasks()

        if completed is not None:
            tasks = [(pet, task) for pet, task in tasks if task.completed == completed]

        if pet_name is not None:
            tasks = [(pet, task) for pet, task in tasks if pet.name.lower() == pet_name.lower()]

        return tasks

    def detect_conflicts(self) -> List[str]:
        """Return warnings for tasks scheduled at the same date and time."""
        tasks = self.get_all_tasks()
        warnings = []

        for i in range(len(tasks)):
            pet1, task1 = tasks[i]
            for j in range(i + 1, len(tasks)):
                pet2, task2 = tasks[j]

                if task1.due_date == task2.due_date and task1.time == task2.time:
                    warnings.append(
                        f"Conflict: {pet1.name} has '{task1.description}' and "
                        f"{pet2.name} has '{task2.description}' at {task1.time} on {task1.due_date}."
                    )

        return warnings

    def mark_task_complete(self, pet_name: str, task_description: str) -> bool:
        """Mark a task complete and create the next recurring task when needed."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                for task in pet.tasks:
                    if task.description.lower() == task_description.lower() and not task.completed:
                        next_task = task.mark_complete()
                        if next_task is not None:
                            pet.add_task(next_task)
                        return True
        return False

    def generate_daily_plan(self) -> List[tuple[Pet, Task]]:
        """Generate today's schedule in chronological order."""
        return self.sort_by_time(self.get_todays_tasks())

    def explain_plan(self) -> str:
        """Explain the algorithm choice."""
        return (
            "The schedule is sorted by time, can be filtered by task status or pet, "
            "creates follow-up tasks for recurring items, and uses lightweight conflict detection "
            "for exact matching times."
        )