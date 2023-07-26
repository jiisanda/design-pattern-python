"""
Creates a copy of the existing object, without making the code dependent on their classes.

IDEA: Just clone the prototype instead of constructing a new object from scratch.

The interface lets you clone an object without coupling your code to the class of the object.
Usually, such an interface contains a single clone method.

Remember: copy() is only valid for collections that are mutable or contain mutable items,
a copy is sometimes needed so one can change one copy without changing the other.

Different Categories of Copy:
1) Shallow Copy: Copies and creates new reference one level deep

"""
import copy

from abc import ABCMeta, abstractmethod
from typing import List


class IPrototype(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def clone(self, mode: int):
        """This will return one of the Shape subclasses."""


class Document(IPrototype):

    def __init__(self, name: str, l: List[List[int]]):
        self.name = name
        self.list = l

    def clone(self, mode: int):
        """This clone method uses different copy methods"""
        if mode == 1:
            # result is level 1 of shallow copy
            copied_list = self.list

        elif mode == 2:
            # result is level 2 shallow copy of the Shape
            # since it creates only new reference for the 1st level string
            copied_list = copy.copy(self.list)

        elif mode == 3:
            # recursive deep copy. Slower but results in a new copy
            # where no sub element are shard as a reference
            copied_list = copy.deepcopy(self.list)

        return type(self)(
            self.name, # a shallow copy is returned to the named property
            copied_list # copy method decided by the mode argument
        )

    def __str__(self):
        """Overriding the __self__ for our object"""
        return f"{id(self)}\tname={self.name}\tlist={self.list}"


if __name__ == '__main__':
    ORIGINAL_DOCUMENT = Document(name="Original", l=[[1, 2, 3, 4], [5, 6, 7, 8]])
    print(f"original:\t{ORIGINAL_DOCUMENT}")
    print()

    DOCUMENT_COPY_1 = ORIGINAL_DOCUMENT.clone(1)              # shallow copy
    DOCUMENT_COPY_1.name = "Copy 1"
    # this allows modified ORIGINAL_DOCUMENT because of the shallow copy
    DOCUMENT_COPY_1.list[1][2] = 200
    print(f"copy (1):\t{DOCUMENT_COPY_1}")
    print(f"original:\t{ORIGINAL_DOCUMENT}")
    print()

    DOCUMENT_COPY_2 = ORIGINAL_DOCUMENT.clone(2)              # level 2 shallow copy
    DOCUMENT_COPY_2.name = "Copy 2"
    # this will NOT modify ORIGINAL_DOCUMENT because it changes the height reference
    # that was deep copied when using mode 2
    DOCUMENT_COPY_2.list[1] = [11, 12, 13, 14]
    print(f"copy (2):\t{DOCUMENT_COPY_2}")
    print(f"original:\t{ORIGINAL_DOCUMENT}")
    print()

    DOCUMENT_COPY_3 = ORIGINAL_DOCUMENT.clone(2)              # level 2 shallow copy
    DOCUMENT_COPY_3.name = "Copy 3"
    # this does modifies ORIGINAL_DOCUMENT because it changes the element of list[1][0]
    # that was not deep copied recursively
    DOCUMENT_COPY_3.list[1][0] = 140
    print(f"copy (3):\t{DOCUMENT_COPY_3}")
    print(f"original:\t{ORIGINAL_DOCUMENT}")
    print()

    DOCUMENT_COPY_4 = ORIGINAL_DOCUMENT.clone(3)               # deep copy
    DOCUMENT_COPY_4.name = "Copy 4"
    # This does NOT modify ORIGINAL_DOCUMENT because it
    # deep copies all levels recursively when using mode 3
    DOCUMENT_COPY_4.list[1][0] = "5678"
    print(f"copy (4):\t{DOCUMENT_COPY_4}")
    print(f"original:\t{ORIGINAL_DOCUMENT}")
    print()
