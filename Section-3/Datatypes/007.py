# Basics of list in python
my_first_list = [1, 2, 3, 4, 5, False, 5.5, "Sagar"]
print(f"My first list : {my_first_list}")
my_first_list.append(6) # Append element to the list
print(f"My first list after append : {my_first_list}")
my_first_list.remove("Sagar")
print(f"My first list after remove : {my_first_list}")
print(f"Length of my first list : {len(my_first_list)}")


list_of_numbers = [1,2,3,3,5,55]
print(f"Max in list is : {max(list_of_numbers)}")
print(f"Min in list is : {min(list_of_numbers)}")