"""
This module provides a binary tree implementation.
"""


class Node:
    """
    Node class for the binary tree.
    """

    def __init__(self, data):
        """
        Initialize a new node with the given data.

        :param data: The data for the node.
        """
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary tree class.
    """

    def __init__(self):
        """
        Initialize an empty binary tree.
        """
        self.root = None

    def insert(self, data):
        """
        Insert a new node with the given data into the binary tree.

        :param data: The data for the new node.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        """
        Helper method to recursively insert a new node into the binary tree.

        :param data: The data for the new node.
        :param node: The current node in the recursive traversal.
        """
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        """
        Search for a node with the given data in the binary tree.

        :param data: The data to search for.
        :return: The node with the given data if found, None otherwise.
        """
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        """
        Helper method to recursively search for a node with the given data in the binary tree.

        :param data: The data to search for.
        :param node: The current node in the recursive traversal.
        :return: The node with the given data if found, None otherwise.
        """
        if node is None or node.data == data:
            return node

        if data < node.data:
            return self._search_recursive(data, node.left)
        return self._search_recursive(data, node.right)

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the binary tree and print the node values.
        """
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        """
        Helper method to recursively perform an inorder traversal of the binary tree.

        :param node: The current node in the recursive traversal.
        """
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)

    def preorder_traversal(self):
        """
        Perform a preorder traversal of the binary tree and print the node values.
        """
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        """
        Helper method to recursively perform a preorder traversal of the binary tree.

        :param node: The current node in the recursive traversal.
        """
        if node is not None:
            print(node.data, end=" ")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def postorder_traversal(self):
        """
        Perform a postorder traversal of the binary tree and print the node values.
        """
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        """
        Helper method to recursively perform a postorder traversal of the binary tree.

        :param node: The current node in the recursive traversal.
        """
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")


# Create a binary tree
tree = BinaryTree()

# Insert nodes
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(4)
tree.insert(7)
tree.insert(9)

# Perform inorder traversal
print("Inorder traversal:")
tree.inorder_traversal()  # Output: 2 3 4 5 7 8 9

# Perform preorder traversal
print("\nPreorder traversal:")
tree.preorder_traversal()  # Output: 5 3 2 4 8 7 9

# Perform postorder traversal
print("\nPostorder traversal:")
tree.postorder_traversal()  # Output: 2 4 3 7 9 8 5

# Search for a node.
result = tree.search(4)
if result:
    print("\nNode found:", result.data)
else:
    print("\nNode not found")
