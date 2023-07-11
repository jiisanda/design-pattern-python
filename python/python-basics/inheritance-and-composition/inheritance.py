"""
Behind every successful man, there is always a women to encourage and support her...
"""

class SuccessfulMan:
    def __init__(self, name: str):
        self.name = name
    
    def success(self):
        print(f"{self.name} is successful...")


class Woman:
    def support(self, name: str):
        pass


class Mother(Woman):
    def support(self, man: str):
        print(f"{man.name}'s mother to support and encourage him.")


class Crush(Woman):
    def support(self, man: str):
        print(f"{man.name}'s crush to encourage him to hit Gym...")


class GF(Woman):
    def support(self, man: str):
        print(f"{man.name}'s GF to support him")


class Sister(Woman):
    def support(self, man: str):
        print(f"{man.name}'s sister to encourage and support him.")
