def main():
    while True:
        choice = input("What program would you like to access.\n1. Merge\n2. Swap\n3. Sort\n4. Quit\n")
        if choice == '1':
            print(merge())
        elif choice == '2':
            print(swap())
        elif choice == '3':
            print(sort())
        elif choice == '4':
            break 
        else:
            print("Invalid input\n")    
    

def create_dict(allow_multiple=True):
    """
    Create one or more dictionaries based on the allow_multiple flag.
    
    Parameters:
    allow_multiple (bool): If True, allows creating multiple dictionaries.
                           If False, creates a single dictionary.
    """
    
    if allow_multiple:
        num_dicts = int(input("How many dictionaries do you want to create? "))
    else: 
        num_dicts = 1
    
    dict_list = []

    # Loop to create the specified number of dictionaries
    for _ in range(num_dicts):
        current_dict = {}
        n = int(input(f"How many items do you want to hold in dictionary {_+1}: "))

        for i in range(n):
            key = input(f"Add a key to dictionary {_+1}: ")
            value = input(f"Add the value to be associated with key '{key}': ")
            current_dict[key] = value
        
        dict_list.append(current_dict)
    
    if num_dicts == 1:
        return dict_list[0]  # Return a single dictionary
    else:
        return dict_list      # Return a list of dictionaries


def multiple_dicts():
    # Create two dictionaries
    dicts = create_dict(allow_multiple=True)
    
    if len(dicts) < 2:
        print("You need to create at least two dictionaries.")
        return multiple_dicts()  # Call again to ensure two dictionaries are created
    return dicts[:2]  # Return only the first two dictionaries


def single_dict():
    # Create a single dictionary
    return create_dict(allow_multiple=False)


# Write a Python program that merges two dictionaries.
def merge():
    dict1, dict2 = multiple_dicts()  # Unpack the two dictionaries from the list

    print(f"Dictionary 1: {dict1}")
    print(f"Dictionary 2: {dict2}")

    # Merge the dictionaries
    merged_dict = {**dict1, **dict2}
    return f"The merged dictionary is: {merged_dict}"


# Write a Python function that takes a dictionary and returns a new dictionary with the keys and values swapped.
def swap():
    old_dict = single_dict()  # Get a single dictionary
    new_dict = {value: key for key, value in old_dict.items()}  # Swap keys and values
    return new_dict


# Write a Python program to sort a dictionary by its values.
def sort():
    old_dict = single_dict()  # Get a single dictionary
    # Sort by values (x[1])
    sorted_dict = sorted(old_dict.items(), key=lambda x: x[1], reverse=False)
    return dict(sorted_dict)  # Convert back to a dictionary


if __name__ == "__main__":
    main()
