# init - constructor which is used to initialize the attributes of an object with some values
# this is called while creating an object of the class

class ChaiOrder:
    def __init__(self, type_, size):
        # it is allowed to create variables here even if they are not present in the class
        # this is allowed in the special method constructor only __init__
        self.type = type_
        self.size = size
    
    def summary(self):
        return f"{self.size} ml of {self.type} chai"
    
order = ChaiOrder("Masala", 200) # instance of the class - object
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())


