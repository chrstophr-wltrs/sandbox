from time import perf_counter

class HumanPyramid:
    """
    Handy little object to hold on to the methods and counters for recursive human pyramid experiments
    """
    def __init__(self, person_weight:int = 200):
        self.function_calls = 0
        self.cache_hits = 0
        self.cache_flag = False
        self.person_weight = person_weight
    
    def weight_on(self, coords:tuple):
        """
        returns the weight on a person recursively

        Parameters:
            coords(tuple): tuple of 2 integers
        """
        self.function_calls += 1
        if coords == (0,0):
            # top of the pyramid
            return 0
        row = coords[0]
        col = coords[1]
        if (col < 0) or (col > row):
            # no person here
            return self.person_weight * -1
        left, right = (row - 1, col - 1), (row - 1, col)
        l_weight = self.weight_on(left) + self.person_weight
        r_weight = self.weight_on(right) + self.person_weight
        return (l_weight + r_weight) / 2
    
    def test_recursive(self, rows):
        self.function_calls = 0
        curr_r, curr_c = 0,0
        self.start_time = perf_counter()
        while 

def main():
    pass

if __name__ == "__main__":
    main()