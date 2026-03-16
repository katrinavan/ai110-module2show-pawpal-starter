from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    duration: int
    priority: int
    completed: bool = False

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):
        pass

    def get_tasks(self):
        pass


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)
    preferences: List[str] = field(default_factory=list)

    def add_pet(self, pet):
        pass

    def get_all_tasks(self):
        pass


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def generate_daily_plan(self):
        pass

    def filter_tasks(self):
        pass

    def sort_by_priority(self):
        pass

    def explain_plan(self):
        pass