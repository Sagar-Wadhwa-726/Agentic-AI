# Inheritance and composition in python
class BaseChai:
    def __init__(self, type_):
        self.type_ = type_

    def prepare(self):
        print(f"Preparing {self.type_} chai . . . .")
    
# inheritance in python
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves")
    
class ChaiShop:
    # this variable can store any other class - this is composition
    # We now have access to everything in BaseChai class
    chai_cls = BaseChai

    def __init__(self):
        # calling the constructor of the base class
        self.chai = self.chai_cls("Regular")

    def server(self):
        print(f"Serving {self.chai.type_} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.server()
fancy.server()
fancy.chai.add_spices()



