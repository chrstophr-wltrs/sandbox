from random import seed, sample
from time import perf_counter
from typing import Callable
from math import sqrt

seed(27538649)

def linear_search(lyst: list, target: int):
    """
    Performs a linear sort for the target
    
    Parameters:
        lyst (list): a large list of elements, which will be searched for by the function
        target (int): the desired integer

    Returns True if target is found within lyst, otherwise returns False
    """
    for i in lyst:
        if i == target:
            return True
    return False

def binary_search(lyst: list, target: int):
    """
    Performs a binary sort for the target
    
    Parameters:
        lyst (list): a large SORTED list of elements, which will be searched for by the function
        target (int): the desired integer

    Returns True if target is found within lyst, otherwise returns False
    """
    left_boundary = 0
    right_boundary = len(lyst) - 1
    while left_boundary <= right_boundary:
        midpoint = (left_boundary + right_boundary) // 2
        if lyst[midpoint] == target:
            return True
        elif target < lyst[midpoint]:
            right_boundary = midpoint - 1
        else:
            left_boundary = midpoint + 1
    return False

def jump_search(lyst: list, target: int):
    """
    Performs a jump sort for the target
    
    Parameters:
        lyst (list): a large SORTED list of elements, which will be searched for by the function
        target (int): the desired integer

    Returns True if target is found within lyst, otherwise returns False
    """
    search_point = 0
    jump = round(sqrt(len(lyst)))
    while search_point <= len(lyst) - 1:
        if lyst[search_point] == target:
            return True
        elif lyst[search_point] < target:
            search_point += jump
        else:
            break
    return linear_search(lyst[search_point - jump:], target)

def time_test(lyst: list, search_func: Callable):
    """
    Performs the timing tests for the search function in question
    
    Parameters
        lyst (list): a large list of elements, from which will be extracted the test conditions
        search_func (function): the function that is being tested
    """
    minimum = ["Minimum", lyst[0]]
    medium = ["Median", lyst[len(lyst) // 2]]
    maximum = ["Maximum", lyst[-1]]
    missing = ["Missing", -1]
    parameters_list = [minimum, medium, maximum, missing]
    print(f"Beginning test for {search_func.__name__} function...")
    for i in parameters_list:
        start_time = perf_counter()
        search_result = search_func(lyst, i[1])
        stop_time = perf_counter()
        print(f"Time for {search_func.__name__} to search for {i[0]} value ({i[1]}): {stop_time - start_time:.7f} seconds ({search_result})")
    print(f"Completed all time tests for {search_func.__name__}!")


def main():
    """Main function, does the tests, prints out how well each search does."""
    print("Generating list for search testing...")
    gen_start = perf_counter()
    search_list = sample(range(100000000), 50000000)
    print(f"List generated in {perf_counter() - gen_start:.2f} seconds, n = {len(search_list):,}")
    print("Sorting the search list...")
    sort_start = perf_counter()
    search_list.sort()
    print(f"Sorted list in {perf_counter() - sort_start:.2f} seconds!")
    print("Beginning testing of search functions...")
    time_test(search_list, linear_search)
    time_test(search_list, binary_search)
    time_test(search_list, jump_search) 

if __name__ == "__main__":
    main()