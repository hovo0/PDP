class Stack:
    """
    Stack data structure implementation.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the stack is empty.
        :return: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Add an item to the top of the stack.
        :param item: The item to be added.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item at the top of the stack.
        :return: The item at the top of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        :return: The item at the top of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """
        Return the number of items in the stack.
        :return: The size of the stack.
        """
        return len(self.items)


s = Stack()

s.push("A")
s.push("B")
s.push("C")

print(s.size())  # 3

item = s.peek()
print(item)  # "C"

item = s.pop()
print(item)  # "C"

print(s.size())  # 2
