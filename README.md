# Solid Coder

In Solid Coder, the goal is to learn to recognize code that can be improved, and learn about how to fix it in a working codebase. We'll couple several well-known schools of software engineering thought together in order to take a holistic approach to identifying and fixing problems.

## Syllabus
### 1. Long Method

- **Code Smell**: Methods that are too long and do too much.

- **Solution Pattern**:
  - **Extract Method**: Break down the method into smaller, more focused methods.
  - **Strategy Pattern**: Encapsulate algorithms into separate classes.

- **SOLID Principle**:
  - **Single Responsibility Principle (SRP)**: Each method or class should have only one reason to change.

- **Clean Code Practices**:
  - **Meaningful Names**: Use descriptive names for methods.
  - **Small Functions**: Keep functions small and focused.

- **Pragmatic Programmer Skills**:
  - **DRY (Don't Repeat Yourself)**: Avoid code duplication by extracting common functionality.

---

### 2. Duplicated Code

- **Code Smell**: Same code appears in multiple places.

- **Solution Pattern**:
  - **Template Method**: Define the skeleton of an algorithm, deferring steps to subclasses.
  - **Decorator Pattern**: Add responsibilities to objects dynamically.

- **SOLID Principle**:
  - **Open/Closed Principle (OCP)**: Classes should be open for extension but closed for modification.

- **Clean Code Practices**:
  - **Refactor Mercilessly**: Continuously improve the codebase.

- **Pragmatic Programmer Skills**:
  - **Code Reuse**: Promote reusability to reduce redundancy.

---

### 3. Feature Envy

- **Code Smell**: A method accesses the data of another object more than its own.

- **Solution Pattern**:
  - **Move Method**: Relocate methods to the class they belong to.
  - **Visitor Pattern**: Separate algorithms from the objects on which they operate.

- **SOLID Principle**:
  - **Law of Demeter**: A method should only communicate with its immediate friends.

- **Clean Code Practices**:
  - **Encapsulation**: Keep data and behavior in the same place.

- **Pragmatic Programmer Skills**:
  - **Decoupling**: Reduce dependencies between modules.

---

### 4. Large Class

- **Code Smell**: Classes that have too many responsibilities.

- **Solution Pattern**:
  - **Extract Class**: Divide the class into smaller classes with focused responsibilities.
  - **Facade Pattern**: Provide a simplified interface to a complex subsystem.

- **SOLID Principle**:
  - **Single Responsibility Principle (SRP)**: Keep classes focused on a single task.

- **Clean Code Practices**:
  - **Organize for Readability**: Structure code for ease of understanding.

- **Pragmatic Programmer Skills**:
  - **Modularity**: Build software in modules for better maintainability.

---

### 5. Switch Statements

- **Code Smell**: Frequent use of switch or case statements.

- **Solution Pattern**:
  - **Polymorphism**: Use inheritance and method overriding.
  - **State Pattern**: Allow an object to alter its behavior when its internal state changes.

- **SOLID Principle**:
  - **Open/Closed Principle (OCP)**: Avoid modifying existing code when adding new functionality.

- **Clean Code Practices**:
  - **Replace Conditionals with Polymorphism**: Use object-oriented principles.

- **Pragmatic Programmer Skills**:
  - **Flexibility and Extensibility**: Design systems that can evolve.

---

### 6. Data Clumps

- **Code Smell**: Groups of data that always appear together.

- **Solution Pattern**:
  - **Introduce Parameter Object**: Combine data into a single object.
  - **Builder Pattern**: Construct complex objects step by step.

- **SOLID Principle**:
  - **Single Responsibility Principle (SRP)**: Objects should have a single responsibility.

- **Clean Code Practices**:
  - **Group Related Data**: Organize data logically.

- **Pragmatic Programmer Skills**:
  - **Abstraction**: Simplify complex reality by modeling classes appropriate to the problem.

---

### 7. Primitive Obsession

- **Code Smell**: Overuse of primitive data types.

- **Solution Pattern**:
  - **Replace Primitives with Rich Domain Objects**: Create classes for more complex data.
  - **Factory Pattern**: Encapsulate object creation.

- **SOLID Principle**:
  - **Encapsulation**: Hide the internal representation of data.

- **Clean Code Practices**:
  - **Use Meaningful Abstractions**: Represent concepts with appropriate types.

- **Pragmatic Programmer Skills**:
  - **Domain Modeling**: Reflect the real-world domain in code.

---

### 8. Divergent Change

- **Code Smell**: One class is commonly changed in different ways for different reasons.

- **Solution Pattern**:
  - **Facade Pattern**: Simplify interactions with complex systems.
  - **Observer Pattern**: Allow objects to be notified of state changes.

- **SOLID Principle**:
  - **Single Responsibility Principle (SRP)**: Separate concerns into different classes.

- **Clean Code Practices**:
  - **Separate Concerns**: Divide code based on functionality.

- **Pragmatic Programmer Skills**:
  - **Anticipating Change**: Design systems that can accommodate future changes.

---

### 9. Shotgun Surgery

- **Code Smell**: A single change requires many small changes in various classes.

- **Solution Pattern**:
  - **Move Method**: Centralize functionality.
  - **Mediator Pattern**: Reduce direct dependencies between objects.

- **SOLID Principle**:
  - **Dependency Inversion Principle (DIP)**: Depend on abstractions, not concretions.

- **Clean Code Practices**:
  - **Minimize Coupling**: Reduce interdependencies.

- **Pragmatic Programmer Skills**:
  - **Loose Coupling**: Design modules that interact through minimal interfaces.

---

### 10. Parallel Inheritance Hierarchies

- **Code Smell**: Adding a new class to one hierarchy requires adding a class to another.

- **Solution Pattern**:
  - **Strategy Pattern**: Define a family of algorithms.
  - **Bridge Pattern**: Separate abstraction from implementation.

- **SOLID Principle**:
  - **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types.

- **Clean Code Practices**:
  - **Proper Use of Inheritance**: Use inheritance judiciously.

- **Pragmatic Programmer Skills**:
  - **Simplicity**: Keep designs as simple as possible.

---

## Mermaid Diagram of the Skill Tree

```mermaid
graph TD;
    %% Define Code Smells
    CS1[Long Method]
    CS2[Duplicated Code]
    CS3[Feature Envy]
    CS4[Large Class]
    CS5[Switch Statements]
    CS6[Data Clumps]
    CS7[Primitive Obsession]
    CS8[Divergent Change]
    CS9[Shotgun Surgery]
    CS10[Parallel Inheritance Hierarchies]
    
    %% Define Solution Patterns
    SP1[Extract Method]
    SP2[Strategy Pattern]
    SP3[Template Method]
    SP4[Decorator Pattern]
    SP5[Move Method]
    SP6[Visitor Pattern]
    SP7[Extract Class]
    SP8[Facade Pattern]
    SP9[Polymorphism]
    SP10[State Pattern]
    SP11[Introduce Parameter Object]
    SP12[Builder Pattern]
    SP13[Replace Primitives with Rich Domain Objects]
    SP14[Factory Pattern]
    SP15[Mediator Pattern]
    SP16[Observer Pattern]
    SP17[Bridge Pattern]
    
    %% Define SOLID Principles
    SRP[Single Responsibility Principle]
    OCP[Open/Closed Principle]
    LSP[Liskov Substitution Principle]
    DIP[Dependency Inversion Principle]
    LoD[Law of Demeter]
    Enc[Encapsulation]
    
    %% Define Clean Code Practices
    CC1[Meaningful Names]
    CC2[Small Functions]
    CC3[Refactor Mercilessly]
    CC4[Encapsulation]
    CC5[Organize for Readability]
    CC6[Replace Conditionals with Polymorphism]
    CC7[Group Related Data]
    CC8[Use Meaningful Abstractions]
    CC9[Separate Concerns]
    CC10[Minimize Coupling]
    CC11[Proper Use of Inheritance]
    
    %% Define Pragmatic Programmer Skills
    PP1[DRY]
    PP2[Code Reuse]
    PP3[Decoupling]
    PP4[Modularity]
    PP5[Flexibility and Extensibility]
    PP6[Abstraction]
    PP7[Domain Modeling]
    PP8[Anticipating Change]
    PP9[Loose Coupling]
    PP10[Simplicity]
    
    %% Connect Code Smells to Solution Patterns
    CS1 --> SP1
    CS1 --> SP2
    CS2 --> SP3
    CS2 --> SP4
    CS3 --> SP5
    CS3 --> SP6
    CS4 --> SP7
    CS4 --> SP8
    CS5 --> SP9
    CS5 --> SP10
    CS6 --> SP11
    CS6 --> SP12
    CS7 --> SP13
    CS7 --> SP14
    CS8 --> SP8
    CS8 --> SP16
    CS9 --> SP5
    CS9 --> SP15
    CS10 --> SP2
    CS10 --> SP17
    
    %% Connect Solution Patterns to SOLID Principles
    SP1 --> SR