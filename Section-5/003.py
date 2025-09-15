# Zip can be used to comnbine two lists, or iterate over two lists simultaneously
names = ["Sagar", "Rohan", "Mohan"]
bills = [100, 200, 300]

for item in zip(names, bills):
    print(f"{item[0]} paid Rs.{item[1]}")