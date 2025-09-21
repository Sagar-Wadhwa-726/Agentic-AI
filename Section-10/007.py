# File handling with try except and with

# try:
#     file = open("order.txt", "w")
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()

# if we don't want to write try except, we can use with operator
# closing and gracefully file handling exception is handled on its own behind the scenes

# file.__enter__() -> as soon as we take the reference of the file
# file.__exit__() -> called when the file has to be closed
with open("order.txt","w") as file:
    file.write("Ginger Tea - 4 cups")