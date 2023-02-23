# Write a python program to print the following pattern.
#   *
#  ***
# *****
#  ***
#   *


n = 3  # number of rows in the top half of the pattern

# Generate top half of the pattern
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(2*i-1))

# Generate bottom half of the pattern
for i in range(n-1, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))
