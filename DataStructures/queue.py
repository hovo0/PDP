"""
This module defines the Queue class for implementing a queue data structure.
"""

class Queue:
    """
    Queue is a class that represents a queue data structure.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Check if the queue is empty.
        :return: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        :param item: The item to be added.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the start of the queue.
        :return: The item at the start of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        """
        Return the number of items in the queue.
        :return: The size of the queue.
        """
        return len(self.items)


q = Queue()

q.enqueue("1")
q.enqueue("2")
q.enqueue("3")

print(q.size())  # 3

item = q.dequeue()
print(item)  # 1

print(q.size())  # 2

q.enqueue("4")

while not q.is_empty():
    item = q.dequeue()
    print(item)  # 2, 3, 4
