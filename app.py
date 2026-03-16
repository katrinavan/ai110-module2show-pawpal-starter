import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.title("PawPal+")

# Keep owner in memory across reruns
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Katrina")

owner = st.session_state.owner
scheduler = Scheduler(owner)

# -------------------------
# Add a Pet
# -------------------------
st.header("Add a Pet")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet Name")
    pet_species = st.text_input("Species")
    pet_age = st.number_input("Age", min_value=0, step=1)
    add_pet_button = st.form_submit_button("Add Pet")

    if add_pet_button:
        new_pet = Pet(pet_name, pet_species, pet_age)
        owner.add_pet(new_pet)
        st.success(f"{pet_name} was added!")

# -------------------------
# Show Pets
# -------------------------
st.header("Current Pets")

if owner.pets:
    for pet in owner.pets:
        st.write(f"**{pet.name}** ({pet.species}, age {pet.age})")
else:
    st.write("No pets added yet.")

# -------------------------
# Add a Task
# -------------------------
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

            if selected_pet:
                new_task = Task(task_description, task_time, task_frequency)
                selected_pet.add_task(new_task)
                st.success(f"Task added for {selected_pet.name}!")
else:
    st.write("Add a pet first before creating tasks.")

# -------------------------
# Show Today's Schedule
# -------------------------
st.header("Today's Schedule")

daily_plan = scheduler.generate_daily_plan()

if daily_plan:
    for pet, task in daily_plan:
        status = "Done" if task.completed else "Pending"
        st.write(
            f"**{task.time}** — {pet.name} — {task.description} "
            f"({task.frequency}) — {status}"
        )
else:
    st.write("No tasks scheduled yet.")

# -------------------------
# Explain Plan
# -------------------------
st.header("Plan Explanation")
st.write(scheduler.explain_plan())

# For the UI and backend integration phase, I connected `app.py` to my logic layer in `pawpal_system.py` by importing the Owner, Pet, Task, and Scheduler classes. I used `st.session_state` to store the Owner object so pets and tasks would persist across Streamlit reruns. I then connected the form inputs in the UI to class methods such as `add_pet()` and `add_task()`, which allowed user actions in the browser to update the underlying Python objects directly.