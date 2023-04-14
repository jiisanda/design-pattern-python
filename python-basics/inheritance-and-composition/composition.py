"""
Behind every successful man, there is always a women to encourage and support her...
"""

class SuccessfulMan:
    def __init__(self, name: str, support: str):
        self.name = name
        self.support = support
    
    def succeed(self):
        self.support.support_and_encourage(self)


class Support:
    def __init__(self, name: str):
        self.name = name
    
    def support_and_encourage(self, man):
        pass


class Mother(Support):
    def support_and_encourage(self, man: str):
        print(f"{man.name}'s mother supported and encourages him.")


class Crush(Support):
    def support_and_encourage(self, man: str):
        print(f"{man.name}'s crush encouraged him to go Gym.")


class GF(Support):
    def support_and_encourage(self, man: str):
        print(f"{man.name}'s GF supported him...")


class Sister(Support):
    def support_and_encourage(self, man: str):
        print(f"{man.name}'s sister supported and encouraged him...")
