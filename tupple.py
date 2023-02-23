# Take user input for t1 and t2 as comma-separated values
t1 = tuple(map(int, input("Enter values for tuple t1: ").split(",")))
t2 = tuple(map(int, input("Enter values for tuple t2: ").split(",")))

# (a) Remove duplicates from the tuples
t1 = tuple(set(t1))
t2 = tuple(set(t2))

# (b) Create a tuple t3 which contains elements alternatively from t1 and t2
t3 = tuple([val for pair in zip(t1, t2) for val in pair] + list(t1[len(t2):]) + list(t2[len(t1):]))

# (c) Create a tuple t4 which contains those elements that are only in t1, not in t2
t4 = tuple(set(t1) - set(t2))

# Print the results
print(f"t1 without duplicates: {t1}")
print(f"t2 without duplicates: {t2}")
print(f"t3 alternating elements: {t3}")
print(f"t4 with elements only in t1: {t4}")
"""
The program takes user input for the tuples t1 and t2 as comma-separated values using the input() function and the map() function to convert the input to integers.

To remove duplicates from the tuples, we convert them to sets using the set() function and then convert them back to tuples using the tuple() function.

To create a new tuple t3 containing elements alternatively from t1 and t2, we use a list comprehension and the zip() function to iterate over both tuples in parallel, and then concatenate any remaining elements at the end.

To create a new tuple t4 containing elements only in t1, we use set difference (-) between t1 and t2.

Finally, we print the results using the print() function.
"""

