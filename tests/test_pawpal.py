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


def test_sort_by_time_returns_chronological_order():
    owner = Owner("Katrina")
    pet = Pet("Mochi", "Dog", 3)
    owner.add_pet(pet)

    pet.add_task(Task("Late task", "18:00", due_date=date.today()))
    pet.add_task(Task("Early task", "08:00", due_date=date.today()))
    pet.add_task(Task("Middle task", "12:00", due_date=date.today()))

    scheduler = Scheduler(owner)
    result = scheduler.generate_daily_plan()

    descriptions = [task.description for _, task in result]
    assert descriptions == ["Early task", "Middle task", "Late task"]


def test_filter_tasks_by_pet_name():
    owner = Owner("Katrina")
    pet1 = Pet("Mochi", "Dog", 3)
    pet2 = Pet("Luna", "Cat", 5)
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    pet1.add_task(Task("Walk", "09:00"))
    pet2.add_task(Task("Brush fur", "10:00"))

    scheduler = Scheduler(owner)
    filtered = scheduler.filter_tasks(pet_name="Mochi")

    assert len(filtered) == 1
    assert filtered[0][0].name == "Mochi"
    assert filtered[0][1].description == "Walk"


def test_daily_recurring_task_creates_next_instance():
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


def test_detect_conflicts_finds_same_time_tasks():
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