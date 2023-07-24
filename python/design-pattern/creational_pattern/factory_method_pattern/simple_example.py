from abc import ABCMeta, abstractstaticmethod
from typing import Optional


class IHito(metaclass=ABCMeta):

    @abstractstaticmethod
    def hito_method(self):
        """Interface Method"""
        ...


class Gakusei(IHito):

    def __init__(self):
        self.name = "私はハルです！"

    def hito_method(self):
        return "学生です！"


class Sensei(IHito):

    def __init__(self):
        self.name = "私は山下です！"

    def hito_method(self):
        return "先生です！"


class HitoFactory:

    @staticmethod
    def build_hito(hito_type: str) -> IHito | str:

        if hito_type == "gakusei":
            return Gakusei()

        elif hito_type == "sensei":
            return Sensei()

        return "Invalid Class!"


if __name__ == '__main__':

    choice = input("Enter the person type: \n")
    hito = HitoFactory.build_hito(choice)
    print(hito.hito_method())
