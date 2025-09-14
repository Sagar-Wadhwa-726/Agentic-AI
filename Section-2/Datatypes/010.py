# Dictionary in python
my_first_dictionary = dict(name = "Sagar", marks = 100, isPassed = True)
print(f"My first dictionary : {my_first_dictionary}")

payment_details = {
    "gateway" : "paytm",
    "amount" : 500,
    "status" : "success"
}

print(f"Payment details : {payment_details} ")
payment_details["amount"]   = 600  # Updating value in dictionary
payment_details["freeTier"] = False # Adding new key-value pair in dictionary'
print(f"Payment details : {payment_details} ")
del payment_details["amount"]
print(f"Payment details : {payment_details}")
print(f"Keys in payment details : {payment_details.keys()}")
print(f"Values in payment details : {payment_details.values()}")
print(f"Is sugar in this dictionary ? {"amount" in payment_details}")

print(f"Printing both the keys and the values : {payment_details.items()}")