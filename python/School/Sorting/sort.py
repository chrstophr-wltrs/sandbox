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
    while True: 
        # We've sorted the entire list, time to break the loop
        if left == len(lyst) - 1:
            break
        
        # Increment to the next left boundary
        left += 1
        
        # Search for the index of the minimum value
        mindex = lyst.index(min(lyst[left:]))

        # Swap the minimum value to the end of the sorted boundary
        lyst[left], lyst[mindex] = lyst[mindex], lyst[left]
    
    return(lyst)


def insertion_sort(lyst: list):
    pass

def mergesort(lyst: list):
    pass

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
    
    def quick_minisort(arr: list, l: int, r: int):
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

def is_sorted(lyst: list):
    """returns True if the list is sorted, returns False if list is not sorted."""
    for i in range(1, len(lyst)):
        if lyst[i - 1] > lyst[i]:
            return False
    return True

def main():
    """Main function, does the tests, prints out how well each sort does."""
    
    def time_test(test_tup: tuple, sort_func: Callable):
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
    
    # Generate list of random integers for sort testing
    print("Generating list for sort testing...")
    gen_start = perf_counter()
    messy_tuple = tuple(sample(range(50000), 25000))
    print(f"List generated in {perf_counter() - gen_start:.2f} seconds, n = {len(messy_tuple):,}")

    sort_methods = (quicksort, selection_sort)
    
    mini_list = [3, 7, -5, 4, 18, -9, 13]

    # Test each of the sort algorithms
    for func in sort_methods:
        time_test(messy_tuple, func)

if __name__ == "__main__":
    main()