def main():

    nested_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
    while True:
        choice = input("What program would you like to access.\n1. Count the specific number of certain elements\n2. Common keys\n3. Flattening a nested list\n4. Quit\n")
        if choice == '1':
            print(numbers())
        elif choice == '2':
            print(common_keys())
        elif choice == '3':
            print(flatten(nested_list))
        elif choice == '4':
            break 
        else:
            print("Invalid input\n") 




# Write a Python program that counts the number of elements in a list that are of a specific data type (e.g., integers, strings).
def numbers():
    check_list = ['Hello', 'Goodbye', 'yes', 1, 2, 3.4, 8.2, (1, 2, 3), [1, 2, 3]]
    
    while True:
        type_count = 0  
        type = input("What type of element do you want to look for in the list?\n1. Strings\n2. Integers\n3. Floats\n4. Tuples\n5. Lists\nEnter number: ")
        
        if type == '1':
            for i in check_list:
                if isinstance(i, str):
                    type_count += 1
            item_type = "string"
        
        elif type == '2':
            for i in check_list:
                if isinstance(i, int):
                    type_count += 1
            item_type = "integer"
        
        elif type == '3':
            for i in check_list:
                if isinstance(i, float):
                    type_count += 1
            item_type = "float"
        
        elif type == '4':
            for i in check_list:
                if isinstance(i, tuple):
                    type_count += 1
            item_type = "tuple"
        
        elif type == '5':
            for i in check_list:
                if isinstance(i, list):
                    type_count += 1
            item_type = "list"
        
        else:
            print("Invalid input. Please choose a number between 1 and 5.")
            continue
        
        # Print message based on count
        if type_count == 1:
            return f"\nThere is 1 {item_type} contained within the list.\n"
        else:
            return f"\nThere are {type_count} {item_type}s contained within the list.\n"


# Write a Python function that takes a list of dictionaries and returns a list of keys that are common to all dictionaries.
def common_keys():
    check_list = [
        {'name': 'Jack', 'age': 35, 'location': 'Chard', 'job': 'Electrical Engineer'},
        {'name': 'Jan', 'age': 38, 'job': 'Retired'},
        {'name': 'Hattie', 'location': 'Chard', 'job': 'Commercial Operation Executive'},
        {'name': 'Frank', 'age': 11, 'location': 'Broadstairs', 'job': 'Unemployed'}
    ]

    # Step 1: Create a list of sets with keys from each dictionary
    key_sets = [set(d.keys()) for d in check_list]
    # check_list is a list of dictionaries.
    # d.keys() gets all the keys from each dictionary d in check_list.
    # set(d.keys()) converts the keys of each dictionary into a set. This is because sets are ideal for operations like intersections.
    # [set(d.keys()) for d in check_list] uses a list comprehension to apply set(d.keys()) to each dictionary d in check_list, 
    # resulting in a list of sets. Each set in the list contains the keys of one dictionary.
    for index, key_set in enumerate(key_sets):
        print(f"Dictionary {index + 1}: {key_set}")

    # Step 2: Find the intersection of all key sets
    common_keys = set.intersection(*key_sets)
    # key_sets is a list of sets where each set contains keys from one dictionary.
    # *key_sets uses the unpacking operator * to pass each set in key_sets as separate arguments to the set.intersection() method.
    # set.intersection(*key_sets) calculates the intersection of all these sets. 
    # This means it finds the keys that are present in every set (and thus every dictionary).

    return f"\nThe common keys that feature across all dictionaries are: {common_keys}\n"

    # Here's a step-by-step explanation of what happens in the code:

    # Convert Dictionary Keys to Sets:
    # For each dictionary in check_list, get its keys.
    # Convert these keys into a set. Each set represents the keys of one dictionary.

    # Store Sets in a List:
    # Create a list where each item is a set of keys from a dictionary.

    # Find Common Keys:
    # Use the intersection method to find keys that appear in all sets. This method returns the common elements across all the sets.


# Write a Python function that flattens a nested list (i.e., a list containing lists).
def flatten(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            # Recursively flatten the sublist
            flat_list.extend(flatten(element))
            # If element is a list, the function calls itself recursively with this sublist (flatten(element)). 
            # This recursive call will return a flattened version of the sublist. 
            # The extend method is then used to add all the elements from the flattened sublist into flat_list.
        else:
            flat_list.append(element)
            # If element is not a list, it's a base case element and is simply appended to flat_list.

    return f"The flatened list is: {flat_list}\n"


if __name__ == "__main__":
    main()

