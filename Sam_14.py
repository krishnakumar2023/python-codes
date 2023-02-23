# Take a number as user input and convert it to its binary equivalent. Raise and handle the
# appropriate exception if the user enters anything other than a number

while True:
    try:
        # get the number from the user
        num = int(input("Enter a number: "))
        # convert the number to its binary equivalent
        binary = bin(num)
        print(f"The binary equivalent of {num} is {binary}")
        break
    except ValueError:
        print("Invalid input! Please enter a number.")
