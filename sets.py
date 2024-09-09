def main():
    while True:
        choice = input("What program would you like to access.\n1. Find the intersection\n2. Remove elements that feature in both sets\n3. Check subsets\n4. Quit\n")
        if choice == '1':
            print(intersection())
        elif choice == '2':
            print(remove())
        elif choice == '3':
            print(subset())
        elif choice == '4':
            break 
        else:
            print("Invalid input\n")   


# Write a Python program that finds the intersection of two sets.
def intersection():
    set_1 = {1,2,3}
    set_2 = {4,5,6}
    set_3 = set()

    for i in set_1:
        if i in set_2:
            set_3.add(i)

    if len(set_3) == 0:
        return "There are no items that appear in both sets\n"
    if len(set_3) == 1:
        return f"There is one item that appears in both sets: {set_3}\n"
    if len(set_3) >= 2:
        return f"The items that appear in both sets: {set_3}\n"


# Write a Python function that removes all elements from a set that are present in another set.
def remove():
    set_1 = {1,2,3,4,5}
    set_2 = {4,5,6}
    set_3 = set()

    for i in set_1:
        if i not in set_2:
            set_3.add(i)

    return f"The new set with the items removed: {set_3}\n" 
    

# Write a Python program to check if a given set is a subset of another set.
def subset():
    set_1 = {1,2,3,4,5}
    set_2 = {1,2,3,4,5}
    set_3 = set()

    for i in set_1:
        if i in set_2:
            set_3.add(i)
            print(len(set_3))
    
    if len(set_1) == len(set_3):
        return f"set_1 is a subset of set_2.\nSet 1: {set_1}\nSet 2: {set_2}\n"
    else:
        return f"set_1 is not a subset of set_2.\nThe items that are in set_1 but not in set_2 are: {set_3} "


if __name__ == "__main__":
    main()

