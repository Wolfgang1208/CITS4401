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
- indirect viewpoints
- domain viewpoints

# Putting this into Practice

<img src="../image/lec3pic1.png">

# Requirements Negotiation

# Conflict / Negotiation

- Conflict resolution

# Detecting Conflicts

# Use order of Priority

# MoSCoW method

# Formal Methods

- Construct a mathematical model of the requirements
- Use logical analysis to verify properties and identify inconsistencies
- Most methods have tool support and some have automatic analysis
- Popular models include 1st order logic, set theory, temporal logic, state machines

# Weaknesses

- What are the weaknesses of these 3 strategies for large projects?

# Resolving conflicts

# Why?

-

# Negotiation for agile software development

# Win-Win Spiral

- Multi-stakeholder involvement with coordination and collaboration based on
  - **Win conditions**
  - **Conflict/Risk/Uncertainty specifications**
  - **Points of Agreement**

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
