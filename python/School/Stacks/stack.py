"""
A class for the Stack object

NOTE FOR INSTRUCTOR:
I implemented this just using built in Python lists,
I don't know if we were suppose to implement this some other way,
but that's how things are for now.
"""


class Stack:
    """
    Stack objects, to hold data

    Methods:
        push(item): push an item onto the stack. Size increases by 1
        pop(): remove the top item from the stack and return it
            Raise an IndexError if the stack is empty
        top(): return the item on top of the stack without removing it
            Raise an IndexError if the stack is empty
        size(): return the number of items on the stack
        clear(): empty the stack
    """

    def __init__(self):
        self.our_stack = []

    def push(self, item):
        """
        push(item): push an item onto the stack
        Size increases by 1

        Parameters:
            item(str/float): item to be pushed onto the top of the stack
        """
        try:
            self.our_stack.append(float(item))
        except:
            self.our_stack.append(item)

    def pop(self):
        """
        remove the top item from the stack and return it
        Raise an IndexError if the stack is empty

        I could just use the list.pop() method, but that feels like cheating because it's so easy
        """
        if self.size() <= 0:
            raise IndexError("The stack is empty!")
        item = self.our_stack[-1]
        self.our_stack = self.our_stack[0:-1]
        return item

    def top(self):
        """
        return the item on top of the stack without removing it
        Raise an IndexError if the stack is empty
        """
        if self.size() <= 0:
            raise IndexError("The stack is empty!")
        return self.our_stack[-1]

    def size(self):
        """return the number of items on the stack"""
        return len(self.our_stack)

    def clear(self):
        """empty the stack"""
        self.our_stack = []
