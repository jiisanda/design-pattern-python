"""
Factory Method Pattern
Define an interface for creating an object, but letting subclasses decide which class
to instantiate. 
Uses abstract class to define and maintain relationships between objects. 
Participants:
- Product(CharacterProduct)
- ConcreteProducts(WarriorProduct, ArcherProduct, MagicianProduct)
- Creator(Character)
- ConcreteCreators(Warrior, Archer, Magician)
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Character(ABC):
    """
    Creator class declares the factory method that is supposed to return an object 
    of CharacterProduct class. The Creator's subclasses usually provides the implementation 
    of this method.
    """

    @abstractmethod
    def display(self):
        ...

    def some_operation(self) -> str:
        character = self.display()

        return f"Creator: The same creator's code has just worked with {character.operation()}"


class Warrior(Character):

    def display(self) -> CharacterProduct:
        return WarriorProduct()


class Archer(Character):

    def display(self) -> CharacterProduct:
        return ArcherProduct()


class Magician(Character):

    def display(self) -> CharacterProduct:
        return MagicianProduct()
        # print("Magician wears a smart 3-piece suit...")


class CharacterProduct(ABC):
    """
    This interface declares the operations that all concrete products must implement.
    """
    
    @abstractmethod
    def operation(self) -> str:
        ...


class WarriorProduct(CharacterProduct):
    def operation(self) -> str:
        return "{Result of Warrior wearing a Armor}"


class ArcherProduct(CharacterProduct):
    def operation(self) -> str:
        return "{Result of Archer wearing a Bracer}"


class MagicianProduct(CharacterProduct):
    def operation(self) -> str:
        return "{Result of Magician wearing a smart Suit}"


def client_code(creator: CharacterCreator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """
    print(
        f"Client: I don't know who the creator's class is, but it still works.\n"
        f"{creator.some_operation()}", end=""
    )


if __name__ == '__main__':
    print("App: Launched with the WarriorCreator.")
    client_code(Warrior())
    print("\n")

    print("App: Launched with the ArcherCreator.")
    client_code(Archer())
    print("\n")

    print("App: Launched with the MagicianCreator.")
    client_code(Magician())
