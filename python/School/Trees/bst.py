"""
Project: Binary Search Trees
Author: Chris Walters
Course: CS 2550
Date: 4/3/2021

Description: the bst module, used for testing!
"""

class BST():
    """
    A binary search tree, constructed from Nodes

    Attributes:
        root(Node): The root node of the tree, which has no parents
    
    Methods:
        is_empty(): Return True if empty, False otherwise
        size(): Return the number of items in the tree
        height(): Return the height of the tree, which is the length of the path from the root to its deepest leaf
        add(item): Add item to its proper place in the tree, Return the modified tree
        remove(item): Remove item from the tree, Return the modified tree
        find(item): Return the matched item, If item is not in the tree, raise a ValueError
        inorder(): Return a list with the data items in order of inorder traversal
        preorder(): Return a list with the data items in order of preorder traversal
        postorder(): Return a list with the data items in order of postorder traversal
        rebalance(): rebalance the tree, Return the modified tree
    """
    
    class Node():
        """
        Node of a binary search tree, helper class of BST

        Attributes:
            data(any): the contents of the Node, will typically be a dict or a Pair
            left(Node): points to the 'left' node descendent
            right(Node): points to the 'right' node descendent
        """

        def __init__(self, data):
            """
            Node of a binary search tree, specifically used to count letters

            Attributes:
                data(any): the contents of the Node, will typically be a dict or a Pair
                left(Node): points to the 'left' node descendent
                right(Node): points to the 'right' node descendent 
            """
            self.data = data
            self.left = None
            self.right = None

        def __str__(self):
            return f"{self.data}, left: {self.left.data}, right: {self.right.data}"

    def __init__(self):
        """
        A binary search tree, constructed from Nodes

        Attributes:
            root(Node): The root node of the tree, which has no parents
        """
        self.root = None

    def is_empty(self):
        """Return True if empty, False otherwise"""
        return self.root == None

    def size(self):
        """Return the number of items in the tree"""
        pass

    def height(self):
        """Return the height of the tree, which is the length of the path from the root to its deepest leaf"""
        pass

    def add(self, item):
        """Add item to its proper place in the tree, Return the modified tree"""
        pass

    def remove(self, item):
        """Remove item from the tree, Return the modified tree"""
        pass

    def find(self, item):
        """Return the matched item; If item is not in the tree, raise a ValueError"""
        pass

    def inorder(self):
        """Return a list with the data items in order of inorder traversal"""
        pass

    def preorder(self):
        """Return a list with the data items in order of preorder traversal"""
        pass

    def postorder(self):
        """Return a list with the data items in order of postorder traversal"""
        pass

    def rebalance(self):
        """
        rebalance the tree, Return the modified tree
        
        The rebalancing algorithm you will implement is as follows:
            1.do an inorder traversal of the tree and write the node values out to a list. If you wish you can use a generator to easily create this list.
            2.take the middle value as root
            3.split the list in left and right halves, excluding the middle value
            4.recursively rebuild the tree, using steps 2 and 3 until done.
        """
        pass