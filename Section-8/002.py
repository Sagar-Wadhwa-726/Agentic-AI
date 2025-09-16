# Infinte generator - useful for stream, and real time system, where we need to constantly get something, for this we need a really good memory so use with caution

"""Imagine once you get a cup of tea, you can refill it any number of times"""
def infinite_chai():
    count = 1
    while True:
        yield f"Refill count is : {count}"
        count+=1

refill = infinite_chai()

for _ in range(6):
    print(next(refill))

