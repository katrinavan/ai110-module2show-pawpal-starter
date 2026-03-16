# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The three core actions a user should be able to perform in PawPal+ are:
1. Add a pet and store basic information about that pet.
2. Add and manage pet care tasks such as feeding, walks, medication, or grooming.
3. Generate and view a daily care plan based on task priority and constraints.

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler.

The **Owner** class represents the user of the application and stores information about the owner's pets and preferences. It is responsible for managing pets and retrieving tasks across all pets.

The **Pet** class represents an individual pet and stores basic information such as name, species, age, and a list of care tasks associated with that pet.

The **Task** class represents a specific pet care activity such as feeding, walking, or grooming. Each task stores information like description, duration, priority, and whether it has been completed.

The **Scheduler** class is responsible for generating a daily care plan. It gathers tasks from all pets, considers priorities and constraints, and organizes tasks into a schedule for the owner.

This design separates data (Owner, Pet, Task) from scheduling logic (Scheduler), making the system easier to maintain and expand.

**b. Design changes**

After reviewing my UML and class skeleton, I made small refinements rather than major design changes. I confirmed that the relationship structure should stay simple: an Owner has many Pets, each Pet has many Tasks, and the Scheduler is responsible for organizing tasks into a daily plan. I also made sure that the Scheduler handled planning logic instead of placing too much logic inside the Owner or Pet classes. This change keeps responsibilities clearer and makes the system easier to maintain as I moved into implementation.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler currently considers task time as the main constraint and uses chronological order to organize the daily plan. I decided that time mattered most for this initial version because it creates a clear and practical daily schedule for the pet owner. I also included task completion status so finished tasks can be separated from unfinished ones. In later versions, I could expand the scheduler to include stronger priority-based logic and owner preferences.

**b. Tradeoffs**

One tradeoff my scheduler makes is that conflict detection only checks for exact matching task times instead of more advanced overlapping durations. This tradeoff is reasonable because it keeps the algorithm simple, readable, and easy to test while still catching the most obvious scheduling issues for this version of the app.
---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools to help brainstorm the class structure, generate the initial UML diagram, and turn that design into Python class skeletons and working code. AI was also helpful for suggesting method names, organizing responsibilities across classes, and drafting simple tests. The most helpful prompts were specific requests such as asking for a Mermaid class diagram, asking how the Scheduler should interact with the Owner and Pet classes, and asking for a clean Python dataclass skeleton based on the UML.

**b. Judgment and verification**

One moment where I did not accept an AI suggestion as-is was when I reviewed the initial design and realized I needed to keep the system simple for Phase 1 and Phase 2. Instead of adding too many advanced scheduling features immediately, I kept the Scheduler focused on the core planning behavior. I verified the design by checking that the relationships matched the assignment requirements, making sure each class had a clear responsibility, and testing the code through a demo script and basic pytest tests.

---

## 4. Testing and Verification

**a. What you tested**

I tested that calling `mark_complete()` changes a task's completion status and that adding a task to a pet increases the number of tasks stored for that pet. I also verified the overall class interaction by running a demo script that created an owner, multiple pets, several tasks, and a generated daily schedule. These tests were important because they confirmed the most basic system behaviors were working correctly before moving on to the user interface.

**b. Confidence**

I am fairly confident that the basic scheduler works correctly for the current implementation because the main classes connect properly, the demo script runs, and the initial tests pass. If I had more time, I would test edge cases such as duplicate task times, empty task lists, invalid time formats, and more advanced scheduling rules involving priority and preferences.

---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is building a clean class structure that separates pet/task data from scheduling logic. This made the code easier to understand and gave me a strong foundation for the next phases of the project.

**b. What you would improve**

If I had another iteration, I would improve the scheduler so it considered more factors beyond time, such as task priority, owner preferences, and conflicts between tasks. I would also make the explanation of the generated plan more detailed and user-friendly.

**c. Key takeaway**

One important thing I learned is that designing the system structure first makes implementation much easier later. I also learned that AI is most useful when I give it specific, focused prompts and then verify its suggestions instead of accepting everything automatically.