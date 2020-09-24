from time import perf_counter
import sys
global func_calls
global cache_hits
func_calls = 0
cache_hits = 0
cache = {}

def weight_on(r, c):
    global func_calls
    global cache_hits
    if (r, c) in cache:
        cache_hits += 1
        return cache[(r, c)]
    func_calls += 1
    if r < 1:
        cache[(r, c)] = 0
        return 0
    if r == 1:
        cache[(r, c)] = 100
        return 100
    row_above = r - 1
    left_coord = c - 1
    left_weight = weight_on(row_above, left_coord) + 200
    right_weight = weight_on(row_above, c) + 200
    if left_coord < 0:
        left_weight = 0
    if c >= r:
        right_weight = 0
    above_weight = (left_weight + right_weight) / 2
    cache[(r, c)] = above_weight
    return above_weight

def main():
    with open("part3.txt", "w") as file:
        time_start = perf_counter()
        if len(sys.argv) == 1:
            rows = 7
        else:
            rows = sys.argv[1] + 1
        for r in range(rows):
            col = r + 1
            row_string = ""
            for c in range(col):
                row_string += f"{weight_on(r, c):.2f} "
            print(row_string)
            file.write(f"{row_string}\n")
        time_stop = perf_counter()
        time_total = time_stop - time_start
        print("\n")
        file.write("\n")
        print(f"Elapsed time: {time_total} seconds")
        file.write(f"Elapsed time: {time_total} seconds\n")
        print(f"Number of function calls: {func_calls}")
        file.write(f"Number of function calls: {func_calls}\n")
        print(f"Number of cache hits: {cache_hits}")
        file.write(f"Number of cache hits: {cache_hits}")

if __name__ == "__main__":
    main()