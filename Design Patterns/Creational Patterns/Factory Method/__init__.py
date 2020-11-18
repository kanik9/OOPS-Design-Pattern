"""
Factory Design Pattern :
    1. Factory Method is a creational design pattern used to create concrete implementations of a common interface.
    2. It separates the process of creating an object from the code that depends on the interface of the object.
    3. The central idea in Factory Method is to provide a separate component with the responsibility to decide which
       concrete implementation should be used based on some specified parameter

    1. The Problems With Complex Conditional Code :
        1. Complex logical code uses if/elif/else structures to change the behavior of an application.Using if/elif/else
           conditional structures makes the code harder to read, harder to understand, and harder to maintain.

          - When a new format is introduced:
                                The method will have to change to implement the serialization to that format.

          - When the Song object changes:
                                Adding or removing properties to the Song class will require the implementation to
                                change in order to accommodate the new structure.

         - When the string representation for a format changes (plain JSON vs JSON API):
                                The .serialize() method will have to change if the desired string representation for a
                                format changes because the representation is hard-coded in the .serialize() method
                                implementation.

    2. A General Purpose Object Factory :
        1. It provides great flexibility to support new formats and avoids modifying existing code.
        2. Factory Method can be used to solve a wide range of problems. An Object Factory gives additional flexibility
           to the design when requirements change. Ideally, you’ll want an implementation of Object Factory that can be
           reused in any situation without replicating the implementation



Links TO Be used to learn :
    1. Example Link : https://realpython.com/factory-method-python/
    2. Video Link   : https://www.youtube.com/watch?v=EcFVTgRHJLM&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=4&t=486s
    3. Book Name    : Head First Design Pattern .
    4. GeeksForGeeks: https://www.geeksforgeeks.org/design-patterns-set-2-factory-method/
    5. More code on git-hube



"""