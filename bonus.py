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

    numbers = input("Can you give me a set of numbers each seperated by a comma: ")
    split_list = numbers.split(',')
    split_list = list(map(int, split_list))
    return f"The modified list, with the strings converted to integers: {split_list}"
    


# Write a Python function that calculates the average of a list of numbers without using built-in functions like sum() or len().
def average():
    
    length = int(input("How many numbers would you like to add: "))
    total = 0
    
    for i in range(length):
        num = int(input("Please add number: "))
        total += num
    
    avg = total / length
    avg = float(avg)
    return f"The average of the list of numbers provided: {avg}"
 
    
# Write a Python function that takes a dictionary with string keys and integer values and returns the key with the highest value.
def highest_value():
    

if __name__ == "__main__":
    main()