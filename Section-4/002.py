# Ternary operator in python
# order_amount = 350
# isDeliveryFree = True if order_amount > 300 else False
# print(isDeliveryFree)

# Match case in python

seat_type = input("Enter the seat type : ").lower()

match seat_type:
    case "sleeper":
        print("Your seat is in Sleeper class")
    case "ac":
        print("Your seat is in AC class")
    case "general":
        print("Your seat is in General class")
    case "luxury":
        print("Your seat is in Luxury class")
    case _:
        print("Invalid seat type")