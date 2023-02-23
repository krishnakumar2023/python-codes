# Write a program to print prime numbers in a range, where range is taken as input from
# the user

# function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# get the range from the user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# print the prime numbers in the range
print("Prime numbers in the range", start, "to", end, "are:")
for num in range(start, end+1):
    if is_prime(num):
        print(num)
