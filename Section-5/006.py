# Walrus operator in python
# :=

# Walrus operator is used to assign value to a variable as part of an expression.
t1 = 5
t2 = 5
x = t1+t2
if(x:=t1+t2):
    print("x is greater than 5")


available_sizes = ["small", "medium", "large"]
if(entered_size := input("Enter the size :")) in available_sizes:
    print(f"{entered_size} is available")