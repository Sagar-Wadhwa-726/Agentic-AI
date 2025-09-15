# for else in python
# the else code is only executed if we do not hit a break statement

staff_list = [("Sagar", "Manager"), ("John", "Developer"), ("Doe", "Designer")]

for name, role in staff_list:
    if(role == "CEO"):
        print(f"Found the CEO: {name}")
        break
else:
    print("No CEO found in the staff list")