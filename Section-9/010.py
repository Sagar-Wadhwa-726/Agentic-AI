# Class Method v/s static method
# static methods are can't initialize the objects

class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    # behind the scene the same constructor is being called, we can just pass the object in different formats

    # we are accepting the values in a dictionary format, class methods does not get self, it gets cls, which is a whole class referecne
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["small", "medium", "large"]
    
print(ChaiUtils.is_valid_size("medium"))

order1 = ChaiOrder.from_dict({
    "tea_type" : "masala",
    "sweetness" : "medium",
    "size" : "large"
})

order2 = ChaiOrder.from_string("Ginger-Low-Small")

order3 = ChaiOrder("lemon", "low", "large")

print(order1)
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)