"""
Project: HashMap ADT
Author: Chris Walters
Course:  CS 2420 Spring 2021
Date: 17 Apr 2021

Description: contains the classes for a key-value pair and a HashMap
"""
class Pair:
    """A key-value pair"""
    def __init__(self, key, value):
        """
        a key-value pair

        Attributes:
            key(any): the reference used to find the pair
            value(any): the associated value of the key
        """
        self.key = key
        self.value = value

class HashMap:
    """
    A hash table, with associated key-value pairs
    """
    def __init__(self, capacity:int = 7):
        """
        Create a hash table

        Attributes:
            capacity(int): the starting capacity for the HashMap
        """
        self.entries = 0
        self.starting_capacity = capacity
        self.table = [None] * self.starting_capacity
        self.max_load_factor = .8

    def hash(self, key:tuple):
        """
        Returns the index for a given key

        Parameters:
            key(tuple[float]): tuple of 2 numbers
        """
        return (key[0] * key[0] + key[0] + key[1]) % self.capacity()

    def get(self, key):
        """
        Return the value for key if key is in the dictionary
        
        If key is not in the dictionary, 
        raise a KeyError
        """
        ind = self.hash(key)
        target = self.table[ind]
        if target.key == key:
            return target.value
        if isinstance(target, list):
            for i in target:
                if i.key == key:
                    return i.value
        raise KeyError(f"key {key} not in HashMap")

    def resize(self):
        """resize the Hash table"""
        old_hash = self.table
        self.entries = 0
        self.table = [None] * ((self.capacity() * 2) - 1)
        for i in old_hash:
            # Add items from sub-lists
            if isinstance(i, list):
                for j in i:
                    self.set(j.key, j.value)
            # Add regular items
            elif i is not None:
                self.set(i.key, i.value)
        return self

    def set(self, key, value):
        """
        add the (key,value) pair to the hashMap

        After adding, if the load-factor>= 80%, 
        rehash the map into a map double its current capacity
        """
        new_pair = Pair(key, value)
        ind = self.hash(key)
        target = self.table[ind]
        # no item @ target index
        if target is None:
            self.table[ind] = new_pair
        # collission with a sub-list
        elif isinstance(target, list):
            for i in target:
                # item to add is already in sub-list
                if i.key == key:
                    i.value = value
                    return
            target.append(new_pair)
        # item to add is already in HashMap
        elif target.key == key:
            self.table[ind].value = value
            return
        # collission with a single item
        else:
            self.table[ind] = [target, new_pair]
        self.entries += 1
        if (self.entries / self.capacity()) >= self.max_load_factor:
            self.resize()

    def remove(self, key):
        """
        Remove the key and its associated value from the map
        
        If the key does not exist, nothing happens
        
        Do not rehash the table after deleting keys
        """
        ind = self.hash(key)
        target = self.table[ind]
        if isinstance(target, list):
            for i, v in enumerate(target):
                if v.key == key:
                    self.table[ind].pop(i)
                    self.entries -= 1
                    if len(self.table[ind]) == 1:
                        # sub-list only has 1 item,
                        # replacing sub-list with single item
                        self.table[ind] = self.table[ind][0]
        elif target.key == key:
            self.table[ind] = None
            self.entries -= 1

    def clear(self):
        """empty the HashMap"""
        self.entries = 0
        self.table = [None] * self.starting_capacity
        return self

    def capacity(self):
        """Return the current capacity--number of buckets--in the map"""
        return len(self.table)
    
    def size(self):
        """Return the number of key-value pairs in the map"""
        return self.entries
    
    def keys(self):
        """Return a list of keys"""
        keys = []
        for i in self.table:
            # get keys from sub-lists
            if isinstance(i, list):
                for j in i:
                    keys.append(j.key)
            # get keys from first-level items
            elif i is not None:
                keys.append(i.key)
        return keys