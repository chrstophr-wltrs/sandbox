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
            return f'Node {self.data}, left: {self.left.data}, right: {self.right.data}'
        
        def __repr__(self):
            return f'Node {self.data}, left: {self.left.data}, right: {self.right.data}'


    def __init__(self):
        """
        A binary search tree, constructed from Nodes

        Attributes:
            root(Node): The root node of the tree, which has no parents
        """
        self.root = None

    def is_empty(self):
        """Return True if empty, False otherwise"""
        return self.root is None

    def size(self):
        """Return the number of items in the tree"""
        def sz(tree):
            if tree is None:
                return 0
            else:
                return sz(tree.left) + sz(tree.right) + 1
        
        return sz(self.root)

    def height(self):
        """
        Return the height of the tree
        which is the length of the path from the root to its deepest leaf
        
        Parameters:
            tree(Node): the root point of the tree we're exploring
        """
        def ht(tree):
            if tree is None:
                return 0
            else:
                return max(ht(tree.left), ht(tree.right)) + 1
        
        return ht(self.root)
        
    
    def find_node(self, node, parent = None):
        """
        Special recursive helper method,
        assists the other tree-traversal methods

        NOTE: method searchs for NODES, and while it may
        check node data for comparisons, this method is
        very different from find()

        Parameters:
            node(Node): the node we're searching for
            parent(Node): the parent node, used for recursion
        
        Result: 
            -1: Node isn't in tree, data less than parent
            0: Node is present in tree (the present Node is returned)
            1: Node isn't in tree, data greater than parent
            
            Return (parent/target node, result)
        """
        # Used for recursive tree traversal
        # If parent hasn't been defined, then start at the root
        if parent is None:
            parent = self.root
        
        # Begin searching for item
        if node.data == parent.data:
            return parent, 0
        else:
            if node.data < parent.data:
                # Node might be a left child
                if parent.left is None:
                    # Node isn't in tree, is less than parent
                    return parent, -1
                else:
                    # Search for node in left subtree
                    return self.find_node(node, parent.left)
            elif node.data > parent.data:
                # Node might be a right child
                if parent.right is None:
                    # Node isn't in tree, is greater than parent
                    return parent, 1
                else:
                    # Search for node in right subtree
                    return self.find_node(node, parent.right)

    def add(self, item):
        """
        Add item to its proper place in the tree, Return the modified tree
        
        Parameters:
            item(any): the data for the node we're adding
        """
        node = self.Node(item)

        # When adding the first item
        if self.root is None:
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
        def delete(node, data):
            """Recursive deleting, helper method for remove()"""
            if node is None:
                return None
            if data == node.data:
                # Found node to delete
                if node.left is None and node.right is None:
                    # node has no children
                    return None
                if node.left is None:
                    # node has right children
                    return node.right
                if node.right is None:
                    # node has left children
                    return node.left
                
                # node has 2 children
                next_highest = node.right
                # Find the next highest value in tree
                while next_highest.left is not None:
                    next_highest = next_highest.left
                node.data = next_highest.data
                node.right = delete(node.right, next_highest.data)
                return node
            # Continue searching for node
            elif data < node.data:
                node.left = delete(node.left, data)
                return node
            elif data > node.data:
                node.right = delete(node.right, data)
                return node
            else:
                raise ValueError(f"data to be removed ({data}) is neither <, ==, or > anything in tree")

        self.root = delete(self.root, item)
        return self

    def find(self, item):
        """
        Return the matched item; If item is not in the tree, raise a ValueError
        
        Parameters:
            item(any): the data for the node we're finding
        """
        node = self.Node(item)
        if self.root is None:
            raise ValueError(f"Node {node.data} not present in tree")
        parent, result = self.find_node(node)

        if result == 0:
            return parent.data
        else:
            raise ValueError(f"Node {node.data} not present in tree")

    def inorder(self):
        """Return a list with the data items in order of inorder traversal"""
        def lnr(node):
            """Recursive behavior for in-order processing"""
            if node is None:
                return
            lnr(node.left)
            lyst.append(node.data)
            lnr(node.right)
        lyst = []
        lnr(self.root)
        return lyst

    def preorder(self):
        """Return a list with the data items in order of preorder traversal"""
        def nlr(node):
            """Recursive behavior for pre-order processing"""
            if node is None:
                return
            lyst.append(node.data)
            nlr(node.left)
            nlr(node.right)
        lyst = []
        nlr(self.root)
        return lyst

    def postorder(self):
        """Return a list with the data items in order of postorder traversal"""
        def lrn(node):
            """Recursive behavior for post-order processing"""
            if node is None:
                return
            lrn(node.left)
            lrn(node.right)
            lyst.append(node.data)
        lyst = []
        lrn(self.root)
        return lyst

    def rebalance(self,):
        """
        rebalance the tree, Return the modified tree
        
        The rebalancing algorithm you will implement is as follows:
            1. do an inorder traversal of the tree and write the node values out to a list
                    If you wish you can use a generator to easily create this list
            2. take the middle value as root
            3. split the list in left and right halves, excluding the middle value
            4. recursively rebuild the tree, using steps 2 and 3 until done
        """
        def bal(lyst):
            """
            Recursively build the tree
            """                
            if len(lyst) == 0:
                return None
            midex = len(lyst) // 2
            node = self.Node(lyst[midex])
            before = lyst[:midex]
            after = lyst[midex + 1:]
            if len(before) == 1:
                node.left = self.Node(before[0])
            else:
                node.left = bal(before)
            if len(after) == 1:
                node.right = self.Node(after[0])
            else:
                node.right = bal(after)
            return node

        starter_list = self.inorder()
        self.root = bal(starter_list)
        return self
    
    def __str__(self):
        return f'Binary Tree, root: {self.root.data}'
        
    def __repr__(self):
        return f'Binary Tree, root: {self.root.data}'
