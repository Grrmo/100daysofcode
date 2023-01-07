def main():
    # Welcome to the program
    print("Welcome to the tip calculator")

    # Ask for the variables we need to use for the calculator
    total = float(input("What was the total bill? $"))
    people = int(input("How many people to split the bill? "))
    percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

    # Print the mathemagical result
    print('Each person should pay ${0:.2f}'.format((total + (total * percentage / 100)) / people))


if __name__ == "__main__":
    main()
