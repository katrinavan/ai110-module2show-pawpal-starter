from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    """Represents a single pet care task."""
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Stores pet details and its care tasks."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Represents the pet owner and all of their pets."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))
        return all_tasks


class Scheduler:
    """Retrieves, organizes, and manages tasks across pets."""

    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        """Get all pet-task pairs from the owner."""
        return self.owner.get_all_tasks()

    def filter_tasks(self, completed=None):
        """Filter tasks by completion status if provided."""
        tasks = self.get_all_tasks()

        if completed is None:
            return tasks

        filtered = []
        for pet, task in tasks:
            if task.completed == completed:
                filtered.append((pet, task))
        return filtered

    def sort_by_time(self, tasks=None):
        """Sort tasks by time string like HH:MM."""
        if tasks is None:
            tasks = self.get_all_tasks()
        return sorted(tasks, key=lambda pair: pair[1].time)

    def generate_daily_plan(self):
        """Generate a readable daily plan sorted by time."""
        return self.sort_by_time()

    def explain_plan(self):
        """Explain why the daily plan was ordered this way."""
        return "The plan is organized by task time so the owner can follow the day in chronological order."