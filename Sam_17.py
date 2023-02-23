# Write a python program to generate the following pattern.
#      1
#     2  2
#    3  3  3
#     2  2
#       1


n = 3  # number of rows in the top half of the pattern

# Generate top half of the pattern
for i in range(1, n+1):
    print(' '*(n-i) + (str(i) + ' ') * i)

# Generate bottom half of the pattern
for i in range(n-1, 0, -1):
    print(' '*(n-i) + (str(i) + ' ') * i)
