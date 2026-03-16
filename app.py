import streamlit as st
from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾")
st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Katrina")

owner = st.session_state.owner
scheduler = Scheduler(owner)

st.header("Add a Pet")
with st.form("add_pet_form"):
    pet_name = st.text_input("Pet Name")
    pet_species = st.text_input("Species")
    pet_age = st.number_input("Age", min_value=0, step=1)
    add_pet_button = st.form_submit_button("Add Pet")

    if add_pet_button:
        if pet_name and pet_species:
            owner.add_pet(Pet(pet_name, pet_species, pet_age))
            st.success(f"{pet_name} was added successfully.")
        else:
            st.warning("Please fill in the pet name and species.")

st.header("Current Pets")
if owner.pets:
    for pet in owner.pets:
        st.write(f"**{pet.name}** ({pet.species}, age {pet.age})")
else:
    st.write("No pets added yet.")

st.header("Add a Task")
if owner.pets:
    with st.form("add_task_form"):
        pet_names = [pet.name for pet in owner.pets]
        selected_pet_name = st.selectbox("Choose a Pet", pet_names)
        task_description = st.text_input("Task Description")
        task_time = st.text_input("Task Time (HH:MM)")
        task_frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])
        add_task_button = st.form_submit_button("Add Task")

        if add_task_button:
            selected_pet = None
            for pet in owner.pets:
                if pet.name == selected_pet_name:
                    selected_pet = pet
                    break

            if task_description and task_time and selected_pet:
                selected_pet.add_task(
                    Task(
                        description=task_description,
                        time=task_time,
                        frequency=task_frequency,
                        due_date=date.today(),
                    )
                )
                st.success(f"Task added for {selected_pet.name}.")
            else:
                st.warning("Please complete all task fields.")
else:
    st.write("Add a pet first before creating tasks.")

st.header("Today's Schedule")
daily_plan = scheduler.generate_daily_plan()

if daily_plan:
    schedule_rows = []
    for pet, task in daily_plan:
        schedule_rows.append(
            {
                "Time": task.time,
                "Pet": pet.name,
                "Species": pet.species,
                "Task": task.description,
                "Frequency": task.frequency,
                "Status": "Done" if task.completed else "Pending",
            }
        )
    st.table(schedule_rows)
else:
    st.write("No tasks scheduled yet.")

st.header("Conflict Warnings")
conflicts = scheduler.detect_conflicts()
if conflicts:
    for conflict in conflicts:
        st.warning(conflict)
else:
    st.success("No conflicts detected.")

st.header("Plan Explanation")
st.write(scheduler.explain_plan())