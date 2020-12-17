from msort import mergesort, by_name, by_id

def main():
    with open("data.csv", "r") as file:
        employees = [tuple(map(str.strip, line.split(","))) for line in file]
    mergesort(employees, by_id)
    with open("by_id.txt", "a") as file:
        for tup in employees:
            file.write(f"{tup}\n")
    mergesort(employees, by_name)
    with open("by_name.txt", "a") as file:
        for tup in employees:
            file.write(f"{tup}\n")


if __name__ == "__main__":
    main()