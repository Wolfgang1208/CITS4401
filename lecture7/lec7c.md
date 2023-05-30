# Design Rationale

# Using Rationale to Document Designs

# Overview

- Purpose of design documentation
- Good and bad documentation

# Purpose of design documentation

- Why write design documentation?

  - Explain your design choices to later developers
  - Ensure they don't duplicate research or work you've already donee

- Suppose you need a regular expression library for your project, and the language you are working with (C++, say) doesn't have one built in
- You might spend significant time evaluating alternatives
- Especially if problems occur with the library down the track, it can be very frustrating to later developers if you don't record:
  - what alternatives were considered?
  - why was package X not chosen?
  - what would be the consequences for the system of changing the library used?

### Provide newcomers to the development team with an understanding of the system, its architecture, and design choices made

- Sometime, teams document their methods and classes well - but don't explain how they fit together overall, or what the major components of the system are
- This can make it very difficult for new members of the development team to know how to navigate their way through the codebase, or understande what the major components are

### Ensure team has a shared understanding of decisions made

- Writing down design decisions helps make explicit exactly what they are - otherwise, different team members might have different ideas about what was decided and why
