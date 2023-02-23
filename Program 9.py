# Q9  Write a python function which accepts a number as an argument and returns True if
# the number is an Armstrong number. e.g. 371 = (3**3+7**3+1**3)..

def check_armstrong(num):
    num_list= [int(x) for x in str(num)]
    arm_num = 0
    for i in num_list:
        arm_num += i**3
    if arm_num == num:
        print(f"{num} is an Armstrong number!!!")
    else:
        print(f"{num} is not an Armstrong number!!!")

# Sample Usage
check_armstrong(int(input("Enter a Number to check for Armstrong Number.")))

