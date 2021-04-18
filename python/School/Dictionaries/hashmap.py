class Pair:
    """A key-value pair"""
    def __init__(self, key, value):
        """
        a key-value pair

        Attributes:
            key(any): the reference used to find the pair
            value(any): the associated value of the key
        """

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
        self.current_capacity = capacity
        self.entries = 0
        self.table = [None] * self.current_capacity

    def get(self, key):
        """
        Return the value for key if key is in the dictionary
        
        If key is not in the dictionary, 
        raise a KeyError
        """
        pass

    def set(self, key, value):
        """
        add the (key,value) pair to the hashMap

        After adding, if the load-factor>= 80%, 
        rehash the map into a map double its current capacity
        """
        pass

    def remove(self, key):
        """
        Remove the key and its associated value from the map
        
        If the key does not exist, nothing happens
        
        Do not rehash the table after deleting keys
        """
        pass

    def clear(self):
        """empty the HashMap"""
        self.entries = 0
        self.table = [None] * self.current_capacity
        return self

    def capacity(self):
        """
        Return the current capacity--number of buckets--in the map
        """
        return self.current_capacity
    
    def size(self):
        """
        Return the number of key-value pairs in the map
        """
        return self.entries
    
    def keys(self):
        """
        Return a list of keys
        """
        keys = []
        for i in self.table:
            if i is not None:
                keys.append(i.key)
        return keys