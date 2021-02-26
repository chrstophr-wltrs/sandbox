from course import Course

class Courselist:
    """
    Linked list representing all of the courses for 1 student at a university

    Attributes: 
        head(Course): the first course of the list, completely empty except for the next pointer
        index(int): the current index of the list, used for __next__() calls
    """
    def __init__(self):
        pass

    def insert(self, Course):
        """insert the specified Course in Course Number ascending order"""
        pass

    def remove(self, number): 
        """remove the first occurrence of the specified Course"""
        pass

    def remove_all(self, number):
        """removes ALL occurrences of the specified Course"""
        pass

    def find(self, number):
        """find the first occurrance of the specified course in the list or return -1"""
        pass

    def size(self):
        """return the number of items in the list"""
        pass

    def calculate_gpa(self):
        """return the GPA using all courses in the list"""
        pass

    def is_sorted(self):
        """return True if the list is sorted by Course Number, False otherwise"""
        pass

    def __str__(self):
        """returns a string with each Course’s data on a separate line"""
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass