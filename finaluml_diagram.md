# PawPal+ Final UML

```mermaid
classDiagram
    class Owner {
        -name: str
        -pets: List[Pet]
        -preferences: List[str]
        +add_pet(pet)
        +get_all_tasks()
    }

    class Pet {
        -name: str
        -species: str
        -age: int
        -tasks: List[Task]
        +add_task(task)
        +get_tasks()
    }

    class Task {
        -description: str
        -time: str
        -frequency: str
        -due_date: date
        -completed: bool
        +mark_complete()
    }

    class Scheduler {
        -owner: Owner
        +get_all_tasks()
        +get_todays_tasks()
        +sort_by_time(tasks)
        +filter_tasks(completed, pet_name)
        +detect_conflicts()
        +mark_task_complete(pet_name, task_description)
        +generate_daily_plan()
        +explain_plan()
    }

    Owner "1" --> "*" Pet : has
    Pet "1" --> "*" Task : has
    Scheduler "1" --> "1" Owner : manages