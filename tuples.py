def main():
    while True:
        choice = input("What program would you like to access.\n1. Rearrange\n2. Glue\n3. Repeat\n4. Quit\n")
        if choice == '1':
            print(rearrange())
        elif choice == '2':
            print(glue())
        elif choice == '3':
            print(repeat())
        elif choice == '4':
            break 
        else:
            print("Invalid input\n")


# Write a Python function that takes a list of tuples and returns a list sorted by the second element in each tuple.
def rearrange():
    tuple_list = [] 
    while True: 
        user_input = input("Enter a tuple (e.g., (1, 2)) or 'done' to finish: ") 
        if user_input.lower() == 'done': 
            break 
        try: 
            # Convert input to a tuple 
            single_tuple = eval(user_input) 
            if isinstance(single_tuple, tuple): 
                tuple_list.append(single_tuple) 
            else: 
                print("Input is not a valid tuple.") 
        except Exception as e: 
            print(f"Error parsing input: {e}") 
     
    new_tuple_list = sorted(tuple_list, key=lambda x: x[1])
    return new_tuple_list
    

# Write a Python function that takes two tuples and returns a tuple that is the concatenation of the two tuples.
def glue():
    count = 0
    tuple_list = []
    while count < 2:
        user_input = input("Enter a tuple (e.g., (1, 2))\n")
        try: 
            # Convert input to a tuple 
            single_tuple = eval(user_input) 
            if isinstance(single_tuple, tuple): 
                tuple_list.append(single_tuple) 
            else: 
                print("Input is not a valid tuple.") 
        except Exception as e: 
            print(f"Error parsing input: {e}")
            
        count += 1

    if len(tuple_list) == 2:
        x, y = (tuple_list)
        new_tuple_list = ((x) + (y))
        return new_tuple_list
    else:
        return "Error: Two tuple are required.\n"
        

# Write a Python program to find the repeated items of a tuple.
def repeat():
    tuple_list = []
    duplicates = []

    while True: 
        user_input = input("Enter a tuple (e.g., (1, 2)) or 'done' to finish: ") 
        if user_input.lower() == 'done': 
            break 
        try: 
            # Convert input to a tuple 
            single_tuple = eval(user_input) 
            if isinstance(single_tuple, tuple):
                if single_tuple in tuple_list:
                    duplicates.append(single_tuple)
                else:
                    tuple_list.append(single_tuple) 
            else: 
                print("Input is not a valid tuple.") 
        except Exception as e: 
            print(f"Error parsing input: {e}")

    return f"The duplicates are: {duplicates}\n"
       

if __name__ == "__main__":
    main()