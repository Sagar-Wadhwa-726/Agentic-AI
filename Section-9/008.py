# Method resolution order - MRO

class A:
    label = "A : Base Class"

class B:
    label = "B : Masala Blend"

class C(A):
    label = "C : Herbal Blend"

class D(C, B):
    pass

cup = D()

# the label will be printed of that class which is being inherited first, in this case it is the class C
print(cup.label)