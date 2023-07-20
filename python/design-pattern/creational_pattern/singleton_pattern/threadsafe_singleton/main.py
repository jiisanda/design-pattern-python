"""
To fix the problem, we will have to synchronize threads during 
the first creation of the Singleton Object
"""
from threading import Lock, Thread

class SingletonMeta(type):

    _instance = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):

        with cls._lock:
            if cls not in cls._instance:
                instance = super().__call__(*args, **kwargs)
                cls._instance[cls] = instance
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):

    value: str = None

    def __init__(self, value:str) -> None:
        self.value = value

    def some_logic(self) -> None:
        ...


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == '__main__':
    print(
        "If we see the same values, then singleton was reused 🥳\n"
        "If you see different values, then two singletons were created! 👎\n"
        "RESULT:"
    )

    process1 = Thread(target=test_singleton, args=('FOO',))
    process2 = Thread(target=test_singleton, args=('BAR',))
    process1.start()
    process2.start()


"""
What we are doing in line 15 is, say that the program has just been launched. Since there's
Singleton instance yet, multiple threads can simultaneously pass the previous conditional 
and reach the point almost at the same time. the first of them will acquire lock and will 
proceed further, while the rest will wait here.

After line 15, The first thread acquires the lock, creates the Singleton Instance. Once it
leaves the lock block, the thread that is waiting for the lock to release may then enter the
conditional statement. But since as previously, the singleton field is already initialized,
the thread won't create a new object.
"""