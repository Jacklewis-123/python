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


# Convert a string containing numbers separated by commas into a list of integers.
def number_list():
    numbers = input("Can you give me a set of numbers each separated by a comma: ")
    try:
        split_list = list(map(int, numbers.split(',')))
        return f"The modified list, with the strings converted to integers: {split_list}"
    except ValueError:
        return "Please enter only numbers separated by commas."


# Calculate the average of a list of numbers without using built-in functions like sum() or len().
def average():
    try:
        length = int(input("How many numbers would you like to add: "))
        total = 0
        for i in range(length):
            num = int(input("Please add number: "))
            total += num
        avg = total / length
        return f"The average of the list of numbers provided: {avg}"
    except ValueError:
        return "Please enter valid integers."
    except ZeroDivisionError:
        return "The list cannot have zero numbers."


# Return the key with the highest value from a dictionary.
def highest_value():
    try:
        current_dict = {}
        n = int(input("How many items do you want to hold in the dictionary: "))
        for i in range(n):
            key = input(f"Add a key to the dictionary: ")
            value = int(input(f"Add the value to be associated with key '{key}': "))
            current_dict[key] = value

        highest_key = max(current_dict, key=current_dict.get)  # Get key with the highest value
        return f"The key with the highest value is: {highest_key} with value {current_dict[highest_key]}"
    except ValueError:
        return "Please ensure that values are integers."


if __name__ == "__main__":
    main()
