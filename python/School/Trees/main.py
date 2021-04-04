'''
Project: Binary Search Trees
Author: Chris Walters
Course: CS 2550
Date: 4/3/2021

Description: Main function for testing the bst module

Lessons Learned: I guess we'll see! 
EDIT: Well, I hate recursion with every fiber of my being, and I want to die, but apart from that, valuable lessons were learned.

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST
from time import sleep


class Pair:
    '''
    Encapsulate letter, count pair as a single entity.
    
    Relational methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.
    
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    tree = BST()
    with open('around-the-world-in-80-days-3.txt', 'r') as file:
        for line in file:
            for char in line:
                if (char not in whitespace) and (char not in punctuation):
                    if tree.is_empty():
                        pair = Pair(char)
                        tree.add(pair)
                    else:
                        try:
                            pair = tree.find(Pair(char))
                            pair.count += 1
                        except(ValueError):
                            pair = Pair(char)
                            tree.add(pair)
    return tree

def main():
    ''' 
    Program kicks off here.
    '''
    tree = make_tree()
    print("...")
    sleep(4)
    print("I worked")
    sleep(2)
    print("I worked so hard")
    sleep(6)
    print("I want")
    sleep(3)
    print("to cry")
    sleep(5)
    print("But it's finally done")
    sleep(4)
    print("Wait, you want to actually SEE something?")
    sleep(3)
    print("Uh...")
    sleep(3)
    print("I guess I can try ordering the tree around")
    sleep(4)
    print("Here goes")
    sleep(3)
    print("Pre order:")
    sleep(3)
    print(tree.preorder())
    sleep(10)
    print("In order:")
    sleep(3)
    print(tree.inorder())
    sleep(10)
    print("Post order:")
    print(tree.postorder())
    sleep(10)
    print("Time for testing!")
    
if __name__ == "__main__":
    main()
