import os

"""
This module explains what an object in Object-Oriented Programming is.

Object-Oriented Programming is a style of programming, in which objects are 
created to represent ideas in a program. Objects have characteristics and 
behaviors; They store information, and they do things.

In Object-Oriented Programming, just like in real life, we like objects 
because they make things easier.

For this example we'll use a cup as our object. If I am thirsty, I can go 
to the sink and drink right from the faucet.
"""


def drink_from_faucet():
    """Scott takes a drink of water from the faucet."""
    print("Scott drinks from the faucet. The water splashes all over and makes a mess.")


# if __name__ == "__main__":
#     os.system("clear")
#     print("Scott is thirsty.")
#     drink_from_faucet()


"""
Instead of making a mess I can decide to use a cup.

Since we are programming I have to explain to the computer what a cup is. I'll
make a class called cup and I'll give it two characteristics
(color and status) and two behaviors (fill and drink).
"""


class Cup:
    """Makes drinking easier."""

    def __init__(self, color):
        """Creates our Cup. Sets the color."""
        self.color = color
        self.status = "Empty"
        os.system("clear")
        print(
            f"A new cup was created. It is the color {self.color}, and is currently {self.status}. "
        )
        input()

    def fill(self):
        if self.status == "Empty":
            print("Scott filled his cup from the faucet.")
            self.status = "Full"
            print(f"The cup is {self.status}.")
            input()

        else:
            print("The cup already has water in it.")
            input()

    def drink(self):
        if self.status == "Full":
            print("Scott drinks his water. He is happy.")
            self.status = "Empty"
            input()

        else:
            print("Scott tries to drink from the cup, but it is empty.")
            input()


if __name__ == "__main__":
    # Make a cup.
    cup = Cup(color="Red")

    # Fill the cup.
    cup.fill()

    # Drink from the cup.
    cup.drink()

    # Drink from the cup again.
    cup.drink()
