class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Check is queue is empty
        :return:
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Add item from end
        :param item:
        :return:
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove item from start
        :return:
        """
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue("1")
q.enqueue("2")
q.enqueue("3")


print(q.size())  #  3

item = q.dequeue()
print(item)  # 1
#
print(q.size())  # 2

q.enqueue("4")


while not q.is_empty():
    item = q.dequeue()
    print(item) # 2, 3, 4
