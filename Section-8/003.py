# Sending value to generators
# We know that yield gets us the values, but we can also send the values to yield keyword

def chai_customer():
    print("Welcome! What chai would you like ?")

    # The generator will pause at this statement, waiting for the value to be send using the send() method
    order = yield
    while True:
        print(f"Preparing : {order}")
        order = yield

stall = chai_customer() # stall variable will be just storing the reference of the chai_customer method
next(stall) # This will run the function till the first yield, this is the starting point of the generator

stall.send("Masala Chai")
stall.send("Lemon Tea")

