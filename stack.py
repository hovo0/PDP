class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Check is empty
        :return:
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Add some items to the stack
        :param item:
        :return:
        """
        self.items.append(item)

    def pop(self):
        """
        Remove an item from the stack
        :return:
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Peek at the item on top of the stack
        :return:
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """
        Check the size of the stack
        :return:
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