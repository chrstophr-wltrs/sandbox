class Countculator:
    def __init__(self):
        self.fact_dict = {0: 1, 1:1, 2: 2}

    def fact(self, n:int):
        if n in self.fact_dict:
            return self.fact_dict[n]
        x = n * self.fact(n - 1)
        self.fact_dict[n] = x
        return x

    def perm(self, n:int, r = None):
        if (r is None) or (r >= n):
            return self.fact(n)

        min = n - r
        total = 1
        while n > min:
            total = total * n
            n -= 1
        return total

    def choose(self, n:int, r:int):
        return self.fact(n) / self.fact(r) * self.fact(n - r)

    def process_string(self, string:str):
        split_string = string.strip().split(" ")
        # Process the necessary methods
        for i in range(len(split_string)):
            el = split_string[i]
            call = el[0]
            if call == "!":
                # Factorial call (wrong syntax)
                split_string[i] = self.fact(int(el[1:]))
            elif el[-1] == "!":
                # Factorial call (correct syntax)
                split_string[i] = self.fact(int(el[:-1]))
            elif call in ["p", "P", "C", "c"]:
                # Multiple factors
                factors = el[el.index("(") + 1:el.index(")")].strip().split(",")
                if call in ["p", "P"]:
                    # Permutation call
                    split_string[i] = self.perm(int(factors[0]), int(factors[1]))
                else:
                    # Choose/Combination call
                    split_string[i] = self.choose(int(factors[0]), int(factors[1]))
        
        # Parse algebra from the list as necessary
        while "*" in split_string:
            split_string[split_string.index("*")] = float(split_string.pop(split_string.index("*") - 1)) * float(split_string.pop(split_string.index("*") + 1))
        while "/" in split_string:
            split_string[split_string.index("/")] = float(split_string.pop(split_string.index("/") - 1)) / float(split_string.pop(split_string.index("/") + 1))
        while "+" in split_string:
            split_string[split_string.index("+")] = float(split_string.pop(split_string.index("+") - 1)) + float(split_string.pop(split_string.index("+") + 1))
        while "-" in split_string:
            split_string[split_string.index("-")] = float(split_string.pop(split_string.index("-") - 1)) - float(split_string.pop(split_string.index("-") + 1))
        
        return split_string[0]
        
def main():
    counter = Countculator()
    math_string = input("Enter the values to process: ")
    while math_string != "":
        print(f"Answer: {counter.process_string(math_string)}\n")
        math_string = input("Enter the values to process: ")
    print("Goodbye!")

if __name__ == "__main__":
    main()