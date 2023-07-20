"""
Singleton Pattern

- Refers to "having only one object of a class"
- and to provide a global point of access to it.

Solution:
- Make class itself responsible for keeping track of its sole instance.
- The class can ensure that no other instance can be created, 
and it provides a way to access the instance. 

Implementation:
- The following is the naive approach for singleton.
- This will behave incorrectly in multithreaded environment.
Multiple threads can call the creation method simultaneously and get 
several instances of Singleton class.
"""

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def some_logic(self):
        ...


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print(f"Singleton working! Both have same id as {id(s1)}")
    else:
        print("Singleton Failed.")