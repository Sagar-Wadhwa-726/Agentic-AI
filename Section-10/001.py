# Exception handling - when the flow of the program deviates from the normal flow, then it can be called as exception

# It is always good to gracefully handle the exceptions, otherwise the program can crash entirely, whenever the exception occurs, our program should not crash, just handle the exception

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
print(first_number/second_number)