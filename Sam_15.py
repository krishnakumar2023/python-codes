# Write a python function to search an element in a list. The function should accept a list
# as an argument and return the index of the element if it is found otherwise it should
# return -1.
# Perform the following operations if the element is found:
# a. Check if the element is a digit
# b. Print the datatype of the element found
# c. Remove the element from the list

def search_and_operate(lst, elem):
    index = -1
    if elem in lst:
        index = lst.index(elem)
        if str(elem).isdigit():
            print(f"The element {elem} is a digit.")
        else:
            print(f"The element {elem} is not a digit.")
        print(f"The datatype of the element is {type(elem).__name__}.")
        lst.remove(elem)
    return index

my_list = [1, 2, 3, 'four', 5]
elem = 'four'

index = search_and_operate(my_list, elem)

if index != -1:
    print(f"The element was found at index {index}.")
    print(f"The list after removing the element is: {my_list}")
else:
    print("The element was not found in the list.")
