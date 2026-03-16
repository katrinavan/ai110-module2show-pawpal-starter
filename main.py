from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(schedule):
    print("\n=== Today's Schedule ===")
    for pet, task in schedule:
        status = "Done" if task.completed else "Pending"
        print(
            f"{task.time} | {pet.name} ({pet.species}) | "
            f"{task.description} | {task.frequency} | {status}"
        )


def main():
    owner = Owner("Katrina")

    pet1 = Pet("Mochi", "Dog", 3)
    pet2 = Pet("Luna", "Cat", 5)

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    pet1.add_task(Task("Morning walk", "08:00", "daily"))
    pet1.add_task(Task("Feed breakfast", "09:00", "daily"))
    pet2.add_task(Task("Brush fur", "07:30", "weekly"))
    pet2.add_task(Task("Feed dinner", "18:00", "daily"))

    scheduler = Scheduler(owner)
    daily_plan = scheduler.generate_daily_plan()

    print_schedule(daily_plan)
    print("\nExplanation:")
    print(scheduler.explain_plan())


if __name__ == "__main__":
    main()