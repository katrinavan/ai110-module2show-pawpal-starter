from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(title, tasks_with_pets):
    print(f"\n=== {title} ===")
    if not tasks_with_pets:
        print("No tasks found.")
        return

    for pet, task in tasks_with_pets:
        status = "Done" if task.completed else "Pending"
        print(
            f"{task.due_date} | {task.time} | {pet.name} ({pet.species}) | "
            f"{task.description} | {task.frequency} | {status}"
        )


def main():
    owner = Owner("Katrina")

    mochi = Pet("Mochi", "Dog", 3)
    luna = Pet("Luna", "Cat", 5)

    owner.add_pet(mochi)
    owner.add_pet(luna)

    # add tasks out of order to test sorting
    mochi.add_task(Task("Morning walk", "09:00", "daily", date.today()))
    mochi.add_task(Task("Medication", "08:00", "once", date.today()))
    luna.add_task(Task("Brush fur", "09:00", "weekly", date.today()))
    luna.add_task(Task("Feed dinner", "18:00", "daily", date.today()))

    scheduler = Scheduler(owner)

    # today's plan
    todays_plan = scheduler.generate_daily_plan()
    print_schedule("Today's Schedule", todays_plan)

    # filtering
    incomplete_tasks = scheduler.filter_tasks(completed=False)
    print_schedule("Incomplete Tasks", scheduler.sort_by_time(incomplete_tasks))

    mochi_only = scheduler.filter_tasks(pet_name="Mochi")
    print_schedule("Mochi's Tasks", scheduler.sort_by_time(mochi_only))

    # conflict detection
    print("\n=== Conflict Warnings ===")
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for conflict in conflicts:
            print(conflict)
    else:
        print("No conflicts found.")

    # recurring task demo
    print("\n=== Marking a Recurring Task Complete ===")
    scheduler.mark_task_complete("Mochi", "Morning walk")
    updated_mochi = scheduler.filter_tasks(pet_name="Mochi")
    print_schedule("Updated Mochi Tasks", scheduler.sort_by_time(updated_mochi))

    print("\n=== Plan Explanation ===")
    print(scheduler.explain_plan())


if __name__ == "__main__":
    main()