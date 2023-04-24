# Class models

# Key Topics

1. UML Class diagrams (what they are for and how to read them)
2. Discovering objects (noun discovery method) and associations (Class, Responsibilities, Collaboration(CRC) method)

# Requirements Analysis Framework

- Requirements analysis generates an analysis model with 3 parts
  - Functional model: use cases & scenarios
  - Static analysis object model: class & object diagrams
  - Dynamic model: statechart & sequence diagrams (later in the unit)
- This week we will look at static class models
- Goal is to investigate the problem domain as far as possible before moving to the solution domain (for design & implementation)

# 1. UML Class diagrams

# Why build class models?

- Why do we build class models? In order to ...:
  1. Build, as quickly and cheaply as possible, a system that satisfies our current requirements
  2. Build a system which will be easy to maintain and adapt to future requirements

# What is a UML class diagram?

- A class diagram describes the types of objects in the system and the various kinds of static relationships that exist among them.
- Class diagrams also show the properties and operation of a class and the constraints that apply to the way objects are connected.

# UML class diagram for an online shop (example 1)

<img src="./../image/lec6pic1.png">

# UML Class diagram interpretation

1. 1 customer has 0 or more orders, but each order has a single customer
2. An order comprises one or more order lines
3. Many order lines refer to a product
4. Corporate customer and personal customer are special types of customer
5. A corporate customer is supported by 0 or 1 sales reps who are order company employees - that is they may have a sales rep or may not

# Example 1 with more detail

<img src="../image/lec6pic2.png">

# Example 2

<img src="../image/lec6pic3.png">

# Index

- Classes
- Associations
- Attributes
- Generalization
- Constraints

# Class Diagrams

<img src="../image/lec6pic4.png">

- Class diagrams represent the structure of the system
- Class diagrams are used
  - during requirements analysis to model problem domain concepts
  - during system design to model subsystems and interfaces
  - during object design to model classes

# Classes

<img src="../image/lec6pic5.png">

- A **class** represent a concept
- A class encapsulates state **(attributes)** and behavior **(operations)**
- Each attribute has a **type**
- Each operation has a **signature**
- The class name is the only mandatory information

# Associations

<img src="../image/lec6pic6.png">

- Associations denote relationships between classes
- _A_ is associated with _B_ is: _A_ has to know about _B_
- The multiplicity of an association end denotes how many objects the source object can legitimately
- reference

# 1-to-1 and 1-to-Many Associations

<img src="../image/lec6pic7.png">

# Multiplicity

- The multiplicity of a property is an indication of how many objects may fill the property
- The most common multiplicities you will see are
  - 1 (An order must have exactly one customer)
  - 0..1 (A corporate customer may or may not have a single sales rep)
  - (A customer need not place an Order; there is no upper limit to the number of Orders. That is, zero or more orders)
- If I have a multivalued property, I prefer to use a plural form for its name.
- In attributes, you come across various terms that refer to the multiplicity
  - Optional implies a lower bound of 0
  - Mandatory implies a lower bound of 1 or possibly more
  - Single-valued implies an upper bound of 1
  - Multivalued implies an upper bound of more that 1: usually \*

# Practice

# Attributes

- Properties represent structual features of a class. As a first approximation, you can think of properties as corresponding to fields in a class
- The attribute notation describes a property as a line of text within the class box itself
- Properties are a single concept, but they appear in two quite distinct notations: attributes and associations
- Although they look quite different on a diagram, they are really the same thing

# Attribute or Associations

<img src="../image/lec6pic8.png">

# Which to use?

- With two notations for the same thing, the obvious question is
- Why should you use one or the other?
- In general:
  - **Attribute** for small things,
    - such as dates or Booleans - in general, value
