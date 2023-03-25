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
  - vs Waterfall when testers see everything much later in the process when it is often too late to change/fix the requirements as they are documented and agreed

# Verifiable Requirements Specs

- Definition. A requirement spec is **verifiable**
- if and only if every requirement statement is verifiable
- iff there is some finite cost-effective way in which a person or machine can check to see if the SW product meets the requirement
- **We can use test cases, analysis or inspection to decide**

# Some Objective Metrics for Non-functional Requirements

- Performance Speed
  - Number of processed transactions per second
  - User/event response time
  - Screen refresh time
    - e.g. the system shall respond to user requests in < 1 second when the system is running at normal user load of < 100 concurrent users
    - Test: Write a script to run 100 common user requests and launch this script 99 times (worst case). Measure the total response time for each request (or all) and test 100 requests can be served in <100 seconds.
  - e.g. The traffic gate shall close in a most 3 seconds
- Size
  - Kilobytes
  - Number of RAM chips
  - e.g. The installed app requires less than 200MB of memory on an Android phone
  - Test: Generate an executable file for the app on (different versions) of Android phone and check that the app size is <200 MB for all versions.
- Realiability
  - Mean time to failure
  - Probability of unavailability
  - Rate of failure occurrence
  - e.g. The system shall be available to users for at least 14000 minutes in any 24 hour period
  - Test: Write a script to run continuous "normal" interactions and run it for a long term. Record any time the system is not available. Note these types of requirements are hard to test effectively.
- Robustness
  - Time to re-start after system failure
  - Percentage of events causing failure
  - Probability of data corruption on failure
- Integrity
  - Maximum permitted data loss after system failure
  - e.g. No more than 1 minute of entered data can be lost if the system crashes
  - Test: Write a script that continuously enters data. Write another script that crashes the system at random times. For each crash, measure the amount of data that was lost i.e. not saved before the crash.
- Ease of Use
  - Training time taken to learn 75% of user facilities
  - Average number of errors made by users in a given time period
  - Number of help frames
  - e.g. Users who have completed the system tutorial should be able to complete the PlanTrip use case within 2 minutes
- Portability
  - Percentage of target-dependent statements
  - Number of target systems
  - e.g. Tha app shall run on all Android phones models since 2015 for all operating system versions from 7 onwards.

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
