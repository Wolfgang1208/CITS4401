# Software architecture

# Summary

- what is a software architecture?
- pipe and filter
- repository
- blackboard
- layered
- client server; process control

# Motivation

- As the size of software systems increase, the algorithms and data structures of the computation no longer constitute the major design problems. When systems are constructed from many components, the organization of the overall system - the software architecture - presents a new set of design problems

# Software architecture focus

- gross organisation and global control structure
- protocols for communication, synchronization and data access
- assignment of functionality to design elements
- physical distribution of design elements
- composition of design elements
- scaling and performance
- selection among design alternatives

# Common framework

- All software architectures have 3 common elements
- Components
  - A software architecture consists of a collection of computational components
- Connectors
  - the interactions between those components (e.g. procedure call, event broadcast, database queries or pipes)
- Constraints
  - A software architecture might have some constraints imposed on it. e.g. topological constraint of having no cycles

# Questions for a new software architecture

- What is the structural pattern?
- What is the underlying computational model?
- What arer the essential invariants of the style?
- What are some common examples of its use?
- What are the advantages and disadvantages of using that style?
- What are some common specializations?
