def main():
    while True:
        choice = input("What program would you like to access.\n1. Second largest number\n2. Remove duplicates\n3. Rotate numbers\n4. Quit\n")
        if choice == '1':
            print(second_largest_number())
        elif choice == '2':
            print(remove_duplicates())
        elif choice == '3':
            print(rotate())
        elif choice == '4':
            break 
        else:
            print("Invalid input\n")

# Write a Python program that finds the second largest number in a list.
def second_largest_number():
    numbers = []
    
    while True:
        try:
            number = int(input("Add a number to the list: "))
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Ask if the user wants to add more numbers
        while True:
            proceed = input("Do you want to add more numbers (Y or N): ").upper()
            if proceed == 'N':
                break
            elif proceed == 'Y':
                break
            else:
                print("Please enter Y or N")
        
        # Break out of the main loop if the user does not want to continue
        if proceed == 'N':
            break

    # After the loop ends, check if there are at least two unique numbers
    if len(set(numbers)) < 2:
        return "Not enough unique numbers to determine the second largest.\n"
    else:
        numbers = sorted(set(numbers))
        return f"The second largest number in the list is: {numbers[-2]}\n"



# Write a Python function that removes duplicates from a list.
def remove_duplicates():
    index = []
    
    while True:
        try:
            item = input("Add an item to the list: ")
            index.append(item)
        except ValueError:
            print("Please enter a valid input.")
            continue

        # Ask if the user wants to add more numbers
        while True:
            proceed = input("Do you want to add more items (Y or N): ").upper()
            if proceed == 'N':
                break
            elif proceed == 'Y':
                break
            else:
                print("Please enter Y or N")
        
        # Break out of the main loop if the user does not want to continue
        if proceed == 'N':
            break

    # After the loop ends, check if there are at least two unique numbers
    index = sorted(set(index))
    return f"The list is: {', '.join(index)}\n"  

# Write a Python function that rotates a list by a given number of positions to the right.
def rotate():
    lst = []
    
    # Collect items from the user
    while True:
        item = input("Add an item to the list: ")
        lst.append(item)

        # Ask if the user wants to add more items
        while True:
            proceed = input("Do you want to add more items (Y or N): ").upper()
            if proceed == 'N':
                break
            elif proceed == 'Y':
                break
            else:
                print("Please enter Y or N")
        
        # Break out of the main loop if the user does not want to continue
        if proceed == 'N':
            break

    if not lst:
        return "The list is empty. Cannot rotate an empty list.\n"

    length = len(lst)

    while True:
        try:
            move = int(input("How many positions to the right do you want to rotate the list: "))
            if move < 0:
                print("Please enter a non-negative integer.")
                continue
            move = move % length  # Adjust move to handle large values
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    rotated_list = lst[-move:] + lst[:-move]
    return f"The rotated list is: {', '.join(rotated_list)}\n"


if __name__ == "__main__":
    main()