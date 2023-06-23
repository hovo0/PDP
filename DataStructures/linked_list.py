class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Add item from end
        :param data:
        :return:
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        """
        Add item from start
        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, value):
        """
        Delete item by given value
        :param value:
        :return:
        """
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        """
        Print Linked List
        :return:
        """
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')


my_list = LinkedList()

my_list.append(1) # 1 -> None

my_list.append(2) # 1 -> 2 -> None

my_list.append(3) # 1 -> 2 -> 3 -> None

my_list.prepend(0) # 0 -> 1 -> 2 -> 3 -> None

my_list.delete_by_value(2) # 0 -> 1 -> 3 -> None

my_list.print_list()  # 0 -> 1 -> 3 -> None

