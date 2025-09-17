# Attribute shadowing in python
class Chai:
    temperature = "Hot"
    strength = "Strong"

# object of chai class
cutting_chai = Chai()

print(cutting_chai.temperature)

cutting_chai.temperature = "Mild"
cutting_chai.cup = "small"
print("Cup size is :", cutting_chai.cup)
print("After changing :", cutting_chai.temperature)
print("Direct look into the class :", Chai.temperature)

del cutting_chai.temperature
del cutting_chai.cup

# If object attribtue no longer available, fallbacks to the value of the attribute in the class itself
print(cutting_chai.temperature)
# print("Cup size is :", cutting_chai.cup)



