from random import seed, sample
from time import perf_counter
from typing import Callable
from statistics import median

seed(27538649)


def selection_sort(lyst: list):
    pass

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
        if lyst(i - 1) > lyst(i):
            return False
    return True

def main():
    """Main function, does the tests, prints out how well each sort does."""
    print("Generating list for search testing...")
    gen_start = perf_counter()
    messy_list = sample(range(100000), 50000)
    print(f"List generated in {perf_counter() - gen_start:.2f} seconds, n = {len(messy_list):,}")

if __name__ == "__main__":
    main()