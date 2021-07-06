# Coding Questions

# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.


def hello_name(user_name):
    print('Hello', user_name)


hello_name('Samantha')

# Question 2
# Print first 100 odd numbers in Python

odd_numbers = list(range(1, 100, 2))
print(odd_numbers)

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

# def max_num_in_list(a_list):
#    max = a_list[ 5 ]
#    for a in a_list:
#        if a > max:
#            max = a
#    return max
#print(max_num_in_list([1, 2, 3, 4, 5]))

# Alternate
num_list = [1, 2, 3, 4, 5]
max(num_list)

# I'm not sure what I did wrong in the first block of code. There are no syntax errors,but I'm getting an error in the terminal that says "IndexError: lis index out of range" when it clearly is not.

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).


def is_leap_year(a_year):
    leap = False
    if a_year % 400 == 0:
        leap = True
    elif a_year % 100 == 0:
        leap = False
    elif a_year % 4 == 0:
        leap = True
    return leap


a_year = int(1986)
print(is_leap_year(a_year))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

a_list = [3, 2, 1, 5, 4, 6]


def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))


print(is_consecutive(a_list))