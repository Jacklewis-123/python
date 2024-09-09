def main():
    while True:
        choice = input("What program would you like to access.\n1. Convert a string to a list of integers\n2. Average a list of numbers\n3. Return the highest value key\n4. Quit\n")
        if choice == '1':
            print(number_list())
        elif choice == '2':
            print(average())
        elif choice == '3':
            print(highest_value())
        elif choice == '4':
            break 
        else:
            print("Invalid input\n") 


# Write a Python function that takes a string containing numbers separated by commas and returns a list of integers.
def number_list():
    pass


# Write a Python function that calculates the average of a list of numbers without using built-in functions like sum() or len().
def average():
    pass


# Write a Python function that takes a dictionary with string keys and integer values and returns the key with the highest value.
def highest_value():
    pass