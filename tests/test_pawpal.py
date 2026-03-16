from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_complete_changes_status():
    task = Task("Feed breakfast", "08:00")
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet("Mochi", "Dog", 3)
    assert len(pet.tasks) == 0

    pet.add_task(Task("Walk", "09:00"))

    assert len(pet.tasks) == 1


def test_sorting_correctness_returns_chronological_order():
    owner = Owner("Katrina")
    pet = Pet("Mochi", "Dog", 3)
    owner.add_pet(pet)

    pet.add_task(Task("Late task", "18:00", due_date=date.today()))
    pet.add_task(Task("Early task", "08:00", due_date=date.today()))
    pet.add_task(Task("Middle task", "12:00", due_date=date.today()))

    scheduler = Scheduler(owner)
    plan = scheduler.generate_daily_plan()

    descriptions = [task.description for _, task in plan]
    assert descriptions == ["Early task", "Middle task", "Late task"]


def test_recurrence_logic_creates_next_daily_task():
    owner = Owner("Katrina")
    pet = Pet("Mochi", "Dog", 3)
    owner.add_pet(pet)

    pet.add_task(Task("Morning walk", "09:00", "daily", date.today()))
    scheduler = Scheduler(owner)

    scheduler.mark_task_complete("Mochi", "Morning walk")

    assert len(pet.tasks) == 2
    assert pet.tasks[0].completed is True
    assert pet.tasks[1].completed is False
    assert pet.tasks[1].due_date == date.today() + timedelta(days=1)


def test_conflict_detection_flags_duplicate_times():
    owner = Owner("Katrina")
    pet1 = Pet("Mochi", "Dog", 3)
    pet2 = Pet("Luna", "Cat", 5)
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    pet1.add_task(Task("Walk", "09:00", due_date=date.today()))
    pet2.add_task(Task("Brush fur", "09:00", due_date=date.today()))

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "Conflict" in conflicts[0]


def test_pet_with_no_tasks_returns_empty_schedule():
    owner = Owner("Katrina")
    pet = Pet("Mochi", "Dog", 3)
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    plan = scheduler.generate_daily_plan()

    assert plan == []