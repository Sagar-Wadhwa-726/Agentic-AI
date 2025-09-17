# Property decorator - can be used to restrict the access to the property
class TeaLeaf:
    def __init__(self, age):
        # _age (underscore) -> it should not be allowed to touch directly, there should be a way to access this property
        self._age = age
    
    # age will be referring to _age
    # this is also acting like a getter
    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, age):
        if 1 <= age <=5:
            self._age = age
        else:
            raise ValueError("Tea Leaf age must be between 1 and 5 years (inclusive)")
    
    # @age.getter
    # def age(self):
    #     return self._age
    

leaf = TeaLeaf(2)
print(leaf.age)

leaf.age = 5
print(leaf.age)