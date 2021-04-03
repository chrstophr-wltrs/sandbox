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
    
    def find_node(self, node, parent = None, removing = False):
        """
        Special recursive helper method,
        assists the other tree-traversal methods

        NOTE: method searchs for NODES, and while it may
        check node data for comparisons, this method is
        very different from find()

        Parameters:
            node(Node): the node we're searching for
            parent(Node): the parent node, used for recursion
            removing(bool): determines whether we are removing the target node
        
        Result (When Removing):
            -1: Child is found, is a left child of parent
            1: Child is found, is right child of parent
            Return (parent node, result)

        Result (When Not Removing): 
            -1: Node isn't in tree, data less than parent
            0: Node is present in tree (the present Node is returned)
            1: Node isn't in tree, data greater than parent
            Return (parent/target node, result)
        """
        # Used for recursive tree traversal
        # If parent hasn't been defined, then start at the root
        if parent == None:
            parent = self.root
        
        if removing:
            if node.data == parent.left.data:
                return (parent, -1)
            if node.data == parent.right.data:
                return (parent, 1)

        # Begin searching for item
        if node.data == parent.data:
            return (parent, 0)
        else:
            if node.data < parent.data:
                # Node might be a left child
                if parent.left == None:
                    # Node isn't in tree, is less than parent
                    return (parent, -1)
                else:
                    # Search for node in left subtree
                    self.find_node(node, parent.left)
            elif node.data > parent.data:
                # Node might be a right child
                if parent.right == None:
                    # Node isn't in tree, is greater than parent
                    return (parent, 1)
                else:
                    # Search for node in right subtree
                    self.find_node(node, parent.right)

    def add(self, item):
        """
        Add item to its proper place in the tree, Return the modified tree
        
        Parameters:
            item(any): the data for the node we're adding
        """
        node = self.Node(item)

        # When adding the first item
        if self.root == None:
            self.root = node
        else:
            parent, result = self.find_node(node)
            if result == -1:
                parent.left = node
            elif result == 1:
                parent.right = node
            else:
                raise ValueError(f"Node {node.data} already present in tree")
        return self

    def remove(self, item):
        """
        Remove item from the tree, Return the modified tree
        
        You can simplify the remove algorithm by always deleting a leaf node.
        If the root node or an interior node is deleted,
            copy the information from the appropriate leaf node,
            then delete the leaf

        Parameters:
            item(any): the data for the node we're removing
        """
        node = self.Node(item)
        parent, result = self.find_node(node)
        left_child, right_child = parent.left, parent.right
        if result == 0:

        return self

    def find(self, item):
        """
        Return the matched item; If item is not in the tree, raise a ValueError
        
        Parameters:
            item(any): the data for the node we're finding
        """
        node = self.Node(item)
        
        parent, result = self.find_node(node)

        if result == 0:
            return parent.data
        else:
            raise ValueError(f"Node {node.data} not present in tree")

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
        return self