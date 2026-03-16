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

The **Task** class represents a specific pet care activity such as feeding, walking, or grooming. Each task stores information like description, time, frequency, due date, and whether it has been completed.

The **Scheduler** class is responsible for generating a daily care plan. It gathers tasks from all pets, sorts and filters them, detects simple conflicts, and organizes tasks into a schedule for the owner.

This design separates data (Owner, Pet, Task) from scheduling logic (Scheduler), making the system easier to maintain and expand.

**b. Design changes**

After reviewing my UML and class skeleton, I made small refinements rather than major design changes. I expanded the Scheduler so it could sort tasks by time, filter by status or pet name, detect conflicts, and handle recurring tasks. I also updated the Task class to include `due_date` and `frequency`, since those became necessary once recurring tasks were added. These changes made the design more aligned with the final implementation while still keeping responsibilities clear.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler mainly considers task time, task completion status, pet name, and recurrence. I decided that time mattered most for this version because it creates a clear, readable schedule for the pet owner and is easy to verify. I also included recurring behavior and conflict detection because they made the app feel more functional without making the logic too complicated.

**b. Tradeoffs**

One tradeoff my scheduler makes is that conflict detection only checks for exact matching task times instead of more advanced overlapping durations. This tradeoff is reasonable because it keeps the algorithm simple, readable, and easy to test while still catching the most obvious scheduling issues for this version of the app.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools to help brainstorm the class structure, generate the initial UML diagram, turn the design into Python skeletons, and refine the backend methods. AI was also useful for drafting tests, explaining bugs, and helping translate the logic into a working Streamlit interface. The most helpful prompts were specific ones that asked for UML, Python dataclasses, or targeted logic changes rather than very broad prompts.

**b. Judgment and verification**

One moment where I did not accept an AI suggestion as-is was when I reviewed whether to make the scheduler too advanced too early. Instead of immediately adding overly complex priority balancing and duration-based overlap logic, I kept the design focused on the project requirements and the most readable implementation. I verified AI suggestions by comparing them against the assignment, checking whether each class still had a clear responsibility, and running the code and tests before keeping the changes.

---

## 4. Testing and Verification

**a. What you tested**

I tested several core behaviors of the PawPal+ system. These included verifying that calling `mark_complete()` changes a task's status, adding a task to a pet increases the pet's task count, sorting returns tasks in chronological order, daily recurring tasks create a new task for the next day, and conflict detection flags tasks scheduled at the same exact time. I also tested an edge case where a pet has no tasks to confirm the scheduler returns an empty schedule instead of failing. These tests were important because they covered both the main happy-path functionality and realistic edge cases.

**b. Confidence**

I am fairly confident that the scheduler works correctly for the current implementation because the core features were verified through automated tests and the demo script worked as expected. My confidence level is 4 out of 5 stars. If I had more time, I would test additional edge cases such as invalid time formats, overlapping tasks with durations, and more advanced scheduling rules involving owner preferences.

---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is building a clean class structure that separates pet and task data from scheduling logic. That separation made each phase easier because I could improve the algorithmic layer without needing to redesign the whole app.

**b. What you would improve**

If I had another iteration, I would improve the scheduler so it considered more factors beyond exact task times, such as task priority, owner preferences, and task duration. I would also improve the UI further by allowing editing, deleting, and marking tasks complete directly from the browser.

**c. Key takeaway**

One important thing I learned is that designing the system structure first makes implementation much easier later. I also learned that working with AI is most effective when I stay in control of the decisions, use targeted prompts, and verify suggestions through testing and review.

## 6. AI Strategy Reflection

Working with separate chat sessions or phases helped me stay organized because each step had a clear purpose, such as design, implementation, testing, or polishing. The most effective Copilot use was asking focused questions about one file or one method at a time, since that gave more accurate and manageable suggestions. One example of an AI suggestion I modified was keeping the scheduler simpler instead of immediately accepting more complicated scheduling logic. This project taught me that I needed to act like the lead architect: AI could generate ideas and drafts quickly, but I still had to decide what actually fit the assignment and made the system clean.