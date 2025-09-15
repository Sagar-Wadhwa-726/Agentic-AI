# List comprehensions

my_numbers_list = [1, 2, 3, 4, 5]
my_squares_list = [number**2 for number in my_numbers_list if number % 2 == 0]
print(my_squares_list)

# Set comprehensions

my_unique_characters = {char for char in "sagar wadhwa"}
print(my_unique_characters)

# Dictionary comprehension
my_dict = {num: num**2 for num in range(1, 6)}
print(my_dict)

# Generator comprehension for memory optimization, provides a stream rather than storing all values in memory
my_gen = sum(num**2 for num in range(1, 6))
print(my_gen)

my_dict = {
    "name": ["sagar"],
    "age": [24],
    "city": ["new delhi"]
}

print(my_dict.values())

# A dictionary which contains the keys as the names of the teas and the values 
# contains the spices which are used in that particular tea. There can be duplication in the spices
# used for multiple tea items.
tea_dict = {
    "masala_tea": ["ginger", "cardamom", "clove", "cinnamon", "black_pepper"],
    "ginger_tea": ["ginger", "cardamom"],
    "green_tea": ["jasmine", "lemon"],
    "lemon_tea": ["lemon", "ginger", "honey"]
}
my_unique_spices = {inner_list for item in tea_dict.values() for inner_list in item}
print(my_unique_spices)


# Dictionary comprehension
tea_prices_inr = {
    "masala_tea": 20,
    "ginger_tea": 15,
    "green_tea": 25,
    "lemon_tea": 18
}

tea_prices_usd = {key:value/80 for key, value in tea_prices_inr.items()}
print(tea_prices_usd)

# Generator comprehension
