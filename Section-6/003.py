# Types of functions in python

# 1. pure v/s impure functinos
# 2. recursive functions
# 3. lambda functions (anonymous functions)

# PURE function, output is deterministic, no side effects
def multiple(cups):
    return 10 * cups

multiple(5)

# IMPURE functions, output is non-deterministic, side effects
x = 10
def impure_multiple(cups):
    global x
    x = 20
    return x * cups

# RECURSIVE functions
n = 5

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

# LAMBDA functions (anonymous functions)
add = lambda a,b : a+b

my_scores_list = [1,2,3,4,5,6,7,8,9,10]
squared_scores = list(map(lambda a : a*a, my_scores_list))
print(squared_scores)
