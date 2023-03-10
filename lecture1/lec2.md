# Requirements Engineering

- **Requirements Engineering** is an activity that includes requirements _elicitation and analysis_.
- **Requirements Elicitation** is an activity during which project participants defeine the _purpose of the system_.
- Requirement Analysis is an activity during which developers _ensure that the system requirements are correct, complete, consistent and unambiguous_.

# Requirements Example:

- 1, Write a program that will read in a list of 100 positive integers, sort them into ascending order, display the sorted list and display the average of those values.
- 2, Develop an automated system taht will allow us to process orders at least 24 hours sooner, on the average, and will allow us to ship our products to customers at least 3 days sooner than currently
- 3, Develop the software that will allow the Z-676 airliner to land itself, without pilot intervention, at major airports.
- 4, Develop a new personal productivity product for small computers that will sell at least one million copies at a retail price of at least $200

# Why is requirement difficult?

## Why do you think requirements change so much?

- Software Engineering is a creative, problem solving activity
- Real customers are not sure what they want
- Large software system have many different
- Real developers are not sure how to build it
- Real requirements creepy
- People may not have the main knowledges
- They want the SW but they dont know the reality.
- The idea is good and useful. But somehow against the local law.
  - so they want to change their requirements.
- under estimated the value of the SW

# Requirements Tips

- It is difficult to capture intent with only "words"
  - So use some diagrams/pictures
- Tips: PowerPoint is a fast & cheap way to mock-up a user interface. Can be 1/10 the time to do mock-ups in code.

# Requirement Engineering approach

- a system's users seldom know exactly what they want and cannot articulate all they know.
- even if we could state all requirements, there are many details that we can only discover once we are well into implementation
- even if we knew all the details, as humans we can master only complexity to an extent
- even if we could master all the complexity. external forces lead to changes in requirement, some of which may invalidate earlier diecisions

# Why is requirement engineering important

- poor requirements capture leads to SW developers solving the wrong problem or attemping an infeasible problem (this takes money)
- Misunderstanding the requirements leads to a chaotic development process (this takes money)

# The 4 Major Activities of Requiremnets Engineering

- Elicitation
  - discover the requirements
- Analysis
  - ensure the requirements are correct, complete, consistent and unambiguous.
- Specification
  - document the requirements
- Validation
  - ensure that the system addresses the client's needs

# What is a Software Requirement?

1. A condition or capability needed by a user to solve a problem or achieve an objective.
2. A condition or capability that must be met or possessed by a system or system component to satisfy a contract, standard, specification, or other formally imposed documents.
3. A documented representation of condition or capability as (1) and (2)

# Functional Requirement

- An area of functionality the system must support
- The functional requirements describe the interactions betwee the actors and the sustem independent of the realization of th system
  - e.g. The system will display a user's current bank account balance

# Non-functional Requirement

- A user-visible constraint on the system.
- Non-functional requirements describe user-visible aspects of the system that are not directly related with the functionality of the system.
  - e.g. The system will display user bank account details within 5 seconds.
- _Performance Requirements Note_
  - Often high risk requirement are due to external factors like system load so be careful.
  - One solution is averaging.
    - The system will display user bank account details within 5 seconds when averaged for all such requests over a 24 hour period.

# Quality Attribute

- A class of non-functional requiremnts
- E.g.
  - usability
  - reliability
  - security
  - safety

# Project Requirements

- Business Requirements
  - describe in business terms what must be delivered or accomplished to provide value
- Product Requirements
  - describe the system or product which is one of several possible ways to accomplish the business requirements
- Process Requirements
  - describe the processes the developing organization must follow and the constraints that they must obey.

# E.g. Project Requirements

1. A maximum development cost requirement (a **process requirement**) may be imposed to help.
2. A maximum sales price requirement (a **product requirement**)
3. A requirement for the product to be maintainable (a **product requirement**)
4. Requirements to follow particular development styles (e.g. OOP), style-guides, or a review/inspection process (**process requirement**)

# Review Answers

- People **don't** necessarily know what they want
- Delivering some software **may lead to new requirements**
- Software is **complex** with many stakeholders and many requirements

- Requirements change so much that it is difficult to predict in advance which software requirements **will persist and which will change**.
- It is equally difficult to predict how customer priorities will change as the project proceeds
- It is often difficult for people to **verbalize** their software needs **until they see a working prototype** and realize that they had forgotten to consider something important