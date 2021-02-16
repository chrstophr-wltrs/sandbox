from random import seed, sample
from time import perf_counter
from typing import Callable

seed(27538649)

def selection_sort(lyst: list[int], left: int = -1):
    """
    Sorts the list using a selection sort

    NOTE: MODIFIES THE BASE LIST

    Parameters:
        lyst (list): a list of integers
        left (int): the leftmost index of the boundary of the portion of the list that's being sorted (default = -1)
    """
    while left < len(lyst) - 1: 
        # Increment to the next left boundary
        left += 1
        
        # Search for the index of the minimum value
        mindex = lyst.index(min(lyst[left:]))

        # Swap the minimum value to the end of the sorted boundary
        lyst[left], lyst[mindex] = lyst[mindex], lyst[left]
    
    return(lyst)


def insertion_sort(lyst: list[int]):
    """
    Sorts the list using insertion sort

    Parameters:
        lyst (list): a list of unsorted integers

    returns the sorted list
    """
    for i in range(1, len(lyst)):
        index = i
        while (index > 0) and lyst[index - 1] > lyst[index]:
            lyst[index - 1], lyst[index] = lyst[index], lyst[index - 1]
            index -= 1
    
    return lyst

def mergesort(lyst: list[int]):
    """
    Sorts the list using merge sort

    Parameters:
        lyst (list): a list of unsorted integers
    
    returns the sorted list
    """
    def merge(a: list[int], b: list[int]):
        """
        Helper function for mergesort
        
        Parameters:
            a (list): a list of integers
            b (list): a list of integers

        returns c, a sorted list of integers
        """
        c = []
        
        # Repeat until one or both of the parent lists are empty
        while (len(a) > 0) and (len(b) > 0):
            if a[0] > b[0]:
                c.append(b[0])
                b.pop(0)
            else:
                c.append(a[0])
                a.pop(0)
        
        # Check a for any extra elements
        while len(a) > 0:
            c.append(a[0])
            a.pop(0)
        
        # Check b for any extra elements
        while len(b) > 0: 
            c.append(b[0])
            b.pop(0)
        
        return c

    if len(lyst) == 1:
        return lyst
    
    midpoint = len(lyst) // 2

    first_half = lyst[0:midpoint]
    second_half = lyst[midpoint:]

    first_half = mergesort(first_half)
    second_half = mergesort(second_half)

    return merge(first_half, second_half)

def quicksort(lyst: list[int], left: int = 0, right: int = None):
    """
    Sorts the list using quicksort.
    
    NOTE: MODIFIES THE BASE LIST

    Parameters:
        lyst (list): a list of integers
        left (int): the index of the leftmost boundary for sorting
        right (int): the index of the rightmost boundary for sorting

    returns the sorted list 
    """
    
    def quick_minisort(arr: list[int], l: int, r: int):
        """
        Helper function for quicksort(), does the actual movement of values

        Parameters:
            arr (list): a list of integers (NOTE: DO NOT USE A SUB-LIST)
            l (int): the leftmost boundary that's being sorted
            r (int): the rightmost boundary of what's being sorted

        returns the final index of the pivot point
        """
        
        pivot_value = arr[r]
        lower_boundary = l - 1
        for marker in range(l, r):
            if arr[marker] < pivot_value:
                lower_boundary += 1
                arr[lower_boundary], arr[marker] = arr[marker], arr[lower_boundary]
        lower_boundary += 1
        arr[lower_boundary], arr[r] = arr[r], arr[lower_boundary]
        return lower_boundary
    
    if right == None:
        right = len(lyst) - 1

    if left >= right:
        return

    p = quick_minisort(lyst, left, right)

    quicksort(lyst, left, p - 1)
    quicksort(lyst, p + 1, right)
    
    return lyst

def is_sorted(lyst: list[int]):
    """returns True if the list is sorted, returns False if list is not sorted."""
    for i in range(1, len(lyst)):
        if lyst[i - 1] > lyst[i]:
            return False
    return True

def main():
    """Main function, does the tests, prints out how well each sort does."""
    
    def time_test(test_tup: tuple[int], sort_func: Callable):
        """
        Helper function for main, tests the sort speed of a function
        
        Parameters
            lyst (tuple): a large list of elements, unsorted
            sort_func (function): the function that is being tested
        """
        test_list = list(test_tup)
        print(f"Beginning test for {sort_func.__name__} function...")
        start_time = perf_counter()
        sorted_list = sort_func(test_list)
        stop_time = perf_counter()
        if is_sorted(sorted_list) == True:
            sort_result = "sorted"
        else:
            sort_result = "not sorted"
        print(f"Time for {sort_func.__name__} to sort: {stop_time - start_time:.4f} seconds ({sort_result}!)")
        return sorted_list
    
    def test_allgorithms():
        """Helper function for main, times all of the sort functions"""
        n = 15000
        # Generate list of random integers for sort testing
        print("Generating list for sort testing...")
        gen_start = perf_counter()
        messy_tuple = tuple(sample(range(n * 2), n))
        print(f"List generated in {perf_counter() - gen_start:.2f} seconds, n = {n:,}")

        sort_methods = (quicksort, selection_sort, insertion_sort, mergesort, sorted)

        # Test each of the sort algorithms
        for func in sort_methods:
            time_test(messy_tuple, func)
    
    test_allgorithms()
    
        

if __name__ == "__main__":
    main()