# Why do requirements need tests?

- An essential property of a software requirement is that it should be possible to **show** (validate) that the finished product satisfies it.
- Requirements that cannot be validated are really just "wishes"
- An important taks is therefore planning how to verify each requirement
- In most cases, acceptance tests are prescribed based on how end-users typically conduct business using the system

# Requirement Test

- A test for a requirement is a way to demonstrate whether a system satisfies the requirement
- Best to think about and write the tests at the same time as writing the requirement
- The test is a type of contract for that requirement
- See also "Fit Criterion" - how will we know if this requirement has been satisfied?

# Testing Requirements

- Engineers arent typically great at assessing the testability of requirements
- Agile deals with this by bringing testers in right from the start

# Verifiable Requirements Specs

- Definition. A requirement spec is **verifiable**
- if and only if every requirement statement is verifiable
- iff there is some finite cost-effective way in which a person or machine can check to see if the SW product meets the requirement
- We can use test cases, analysis or inspection to decide

# Some Objective Metrics for Non-functional Requirements

- Performance Speed
  - Number of processed transactions per second
  - User/event response time
  - Screen refresh time
  - e.g. the system shall respond to user requests in < 1 second when the system is running at normal user load of < 100 concurrent users
  - e.g. The traffic gate shall close in a most 3 seconds
- Size
  - Kilobytes
  - Number of RAM chips
  - e.g. The installed app requires less than 200MB of memory on an Android phone
- Realiability
- Robustness
- Integrity
- Ease of Use
- Portability

# Hard-to-test requirements

- System requirements
  - requirements which apply to system as a whole
  - In general, these are the most difficult requirements to validate irrespective of the method used as they may be influenced by any of the functional requirements
  - Hard to test for non-functional system-wide characteristices such as usability
- Exclusive requirements
  - Requirements which exclude specific behaviour
  - For example, a requirement may state that system failures must never corrupt the system databse
  - It is not possible to test such a requirement exhaustively
- Some non-functional requirements
  - Some non-functional requirements, such as reliability requirements, can only be tested with a large test set.
