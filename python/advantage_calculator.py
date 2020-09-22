import dice

def main():
    number_of_tests = int(input("How many tests would you like to run? "))
    print("Processing, please wait...")
    sum = 0
    for i in range(number_of_tests):
        roll = min(dice.roll('2d20'))
        sum += roll
    average = sum / number_of_tests
    average_d20_roll = 10.5
    difference = round((average - average_d20_roll), 1)
    print(f"The average for the full test was {average}")
    print(f"Meaning disadvantage is worth about {difference}")

if __name__ == '__main__':
    main()