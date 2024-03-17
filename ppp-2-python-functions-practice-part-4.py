#Write a Python function called max_num()to find the maximum of three numbers.
numbers = [1, 2, 10 , 3]
def max_num(numbers):
    return max(numbers)
highest_number = max_num(numbers)

print(highest_number)

#Write a Python function called mult_list() to multiply all the numbers in a list.

my_num = [5, 10, 20]

def mult_list(my_num):
    result = 1
    for num in my_num:
        result = result * num
    return result

multiply_list = mult_list(my_num)
print(multiply_list)


#Write a Python function called rev_string() to reverse a string.

my_string = 'Chicken'

def rev_string(my_string):
    reversed_string = my_string[::-1]
    return reversed_string

ckn_backwards = rev_string(my_string)
print(ckn_backwards)

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.


def num_within():
    




# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
