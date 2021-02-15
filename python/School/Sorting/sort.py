from random import seed, sample
from time import perf_counter
from typing import Callable

seed(27538649)


def selection_sort(lyst: list):
    pass

def insertion_sort(lyst: list):
    pass

def mergesort(lyst: list):
    pass

def quicksort(lyst: list):
    pass

def is_sorted(lyst: list):
    pass

def main():
    """Main function, does the tests, prints out how well each sort does."""
    print("Generating list for search testing...")
    gen_start = perf_counter()
    search_list = sample(range(500000), 50000)
    print(f"List generated in {perf_counter() - gen_start:.2f} seconds, n = {len(search_list):,}")

if __name__ == "__main__":
    main()