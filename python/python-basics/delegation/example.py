from delegation import Delegator

class Human():
    def speak(self):
        print("Hello")


class Child(Human):
    def speak(self):
        print("hey!")
    def take_out_trash(self):
        print("Okay I will do it!")
    def do_the_dishes(self):
        print("Not my turn today!")


class Wife(Human):
    def speak(self):
        print("Hi!")
    def cook_dinner(self):
        print("I am out!")
    def do_the_dishes(self):
        print("I am not well!")


class Parent(Delegator, Human):
    DELEGATED_METHODS = {
        'child':[
            'take_out_trash',
            'do_the_dishes'
        ],
        'wife' : [
            'cook_dinner'
        ]
    }
    
    def __init__(self):
        self.child = Child()
        self.wife = Wife()


if __name__ == '__main__':
    parent = Parent()
    parent.take_out_trash()
    parent.do_the_dishes()
    parent.cook_dinner()
    parent.shout()      # exception