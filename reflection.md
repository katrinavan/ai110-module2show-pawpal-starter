# PawPal+ Project Reflection

## 1. System Design

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

After reviewing my UML and class skeleton, I made small refinements rather than major design changes. I confirmed that the relationship structure should stay simple: an Owner has many Pets, each Pet has many Tasks, and the Scheduler is responsible for organizing tasks into a daily plan. I also made sure that the Scheduler handled planning logic instead of placing too much logic inside the Owner or Pet classes. This change keeps responsibilities clearer and makes the system easier to maintain as I move into implementation.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
