# Requirement Analysis

- What is
- This topic is concerned with the process of analyzing requirements to
  - **Detect and resolve conflicts** between requirements
  - **Discover the bounds** of the software and how it must interact with its organizational and operational environment
  - **Elaborate** system requirements to derive software requirements

# Types of Requirements

- Functional
  - Describe the _functions_ that the SW is to perform.
    - e.g. The SW shall enable a student to enroll in a class.
- Non-functional
  - Requirements that contrain the solution
  - e.g. Student addresses and other personal information should not be released to any unauthorized party.
- Product
  - a need or constraint on the software to be developed
    - e.g. The SW shall verify that a student meets all prereqs before she registers for a course.
- Process
  - a requirement constraining the development of the SW
    - e.g. The SW development team shall be cerified for ISO9001 quality standards.
- Emergent
  - requirements can not be addressed be a single component but depend on the interoperation of components
    - e.g. a throughput requirement for a call-centre

# Examples of Non-functional Requirements

- Performance
  - The SW will respond to client web activity in a timely and convenient way
- Maintainability
  - The SW will be implemented using modern programming practices that maximize the maintainability and resuability of designs and code.
- Interoperability
  - The SW shall run on XX phones and YY devices.
- Useabaility
  - The SW shall conform to ISO 9241 usability standard [ref]
- Safety
  - The SW will transition to an agreed safe state within 1 second of any sensor readings outside their thresholds.
- Reliability
  - The SW shall be available for use as much as comparable productivity tools.
- Security
  - The SW shall protect users' personal information from XXX penetration attacks.
- Privacy
  - The SW shall protect each user account with password entry.

# More requirements classifications

- Requirement Priority
  - The higher the priority the more essential the requirement is meeting the overall goal of the SW. A fixed-point scale such as **Must have, Should have, Could have, and Won't have.**
- Requirement Scope
  - The extent to which a requirement affects the SW and components.
    - e.g. Non-functional requirements such as response times have global scope: their satisfaction can not be allocated to a single component.
- Requirement Volatility
  - Some requirements will change druing the lifetime of the SW and even during development. It is useful to estimate the likelihood that a requirement will change so that developers can consider designs that are more tolerant of change.

# Viewpoints of Requirements

- interactor viewpoints
  - people or other systems that interact directly with the system
  - e.g. ATM customer, the bank's database
- indirect viewpoints
  - stakeholders who do not use the system, but influence requirements
  - e.g. bank management and security people
- domain viewpoints
  - constraints of the domain that influence requirements
  - e.g. standards for interbank communication

# Putting this into Practice

- Q: How do we capture all these potentially important properties of requirements?
- A: Volere snow card prompts the user for relevant information

<img src="../image/lec3pic1.png">

# Requirements Negotiation

# Conflict / Negotiation

- Another term commonly used for the **Requirements Negotiation** subtopic is **Conflict Resolution**.
- The both concern resolving problems with requirements where **conflicts** occur
  - between two stakeholders requiring mutually incompatible features
  - between requirements and resources
  - between functional and non-functional requirements
- In most cases, it is unwise for the software engineer to make a unilateral(单方面) decision
- So it becomes necessary to consult with the stakeholders to reach a consensus on an appropriate tradeoff.
- It is often important, for contractual reasons, that such decisions be traceable back to the customer

# Detecting Conflicts

# Use order of Priority

- Determines the degree of importance of each requirements to the customer
- There may not be enough time or resources to implement all requirements, so the most critical should be implemented first.
- Helps to identify conflicting requirements
- Identifying which requirements should be done first, and which should be left to successive releases, can help you plan successive releases of a product.

# MoSCoW method

- Must have, Should have, Could have, Won't have
- We can ask the client to group their requirements of the system into two lists: the DO list and the NOT DO list
- The MoSCoW rules have an advantage over the simple ranking method
  - e.g. if there are many (1000) requirements then ranking using numbers from 1 to 1000 would be difficult, but grouping them into two lists using the MoSCoW rules would be a lot easier.

# Formal Methods

- Construct a mathematical model of the requirements
- Use logical analysis to verify properties and identify inconsistencies
- Most methods have tool support and some have automatic analysis
- Popular models include 1st order logic, set theory (e.g. Z theory), temporal logic, state machines

# Weaknesses

- What are the weaknesses of these 3 strategies for large projects?
- The requirements are not turly independent, yet all these strategies assume they are.
- The client might not know their priorities
- Different stakeholders do not usually agree with the priorities of the requirements.

# Resolving conflicts

# Why negotiation?

- Negotiation is introduced to facilitate requirements elicitation and analysis
  - Encourages communication
  - Aids in understanding
  - Reveal conflict, solution exploration, collaborative resolution
  - Improve agreement level
  - Develop stakeholders' satifaction
  - Improves requirements quality

# Negotiation for agile software development

- Negotiation for traditional software methods focuses on revealing conflicts and improving understanding of requirements
- As agile methods focus on **involvement of customer**, whose role is to provide and prioritize new system requirements, negotiation for agile software development should therefore focus on resolving these system requirements
  - e.g.
  - Can they be implemented within the time frame?
  - Can they be implemented within the budget?
  - Can these requirements be prioritized?
- Agile methods have to reply on contract where customer pays for time spent on system development rather than the time on developing a specific set of requirements
  - Negotiate on what to be delivered
  - Software developer should be realistic on what they can deliver (i.e., do not over-promise just to get the contract signed)

# Win-Win Spiral

- Multi-stakeholder involvement with coordination and collaboration based on
  1. **Win conditions**
  - Capture the desired objectives of the individuals
  2. **Conflict/Risk/Uncertainty specifications**
  - Capture the conflicts between win conditions and their associated risks and uncertainties
  3. **Points of Agreement**
  - Capture the agreed upon set of conditions which satisfy stakeholder win conditions and also define the system objectives

# Feasibility Studies

- INPUT
  - set of preliminary business requirements
  - an outline description of the system
  - how the system is intended to support business processes
- OUTPUT
  - a report recommending whether or not it is worth carrying on with the requirements engineering and system development process

# Requirements Evolution

# Issues

- issues
- definitions
- techniques

# Traceability tables

- Uniquely number all requirements
- Identify specific aspects of the system or its environment classified by
