classDiagram
    class Owner {
        -name: str
        -pets: list
        -preferences: list
        +add_pet(pet)
        +get_all_tasks()
    }

    class Pet {
        -name: str
        -species: str
        -age: int
        -tasks: list
        +add_task(task)
        +get_tasks()
    }

    class Task {
        -description: str
        -duration: int
        -priority: int
        -completed: bool
        +mark_complete()
    }

    class Scheduler {
        -owner: Owner
        +generate_daily_plan()
        +filter_tasks()
        +sort_by_priority()
        +explain_plan()
    }

    Owner "1" --> "*" Pet : has
    Pet "1" --> "*" Task : has
    Scheduler "1" --> "1" Owner : manages