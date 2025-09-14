import decimal

# Set the precision for Decimal calculations
decimal.getcontext().prec = 28 # Set precision to 28 digits

# Create Decimal objects (always from strings for precision)
d1 = decimal.Decimal('0.1')
d2 = decimal.Decimal('0.2')

# Perform addition
result_add_dec = d1 + d2
print(f"0.1 + 0.2 with Decimal: {result_add_dec}") # Prints 0.3 exactly

# Compare with standard float addition
result_add_float = 0.1 + 0.2
print(f"0.1 + 0.2 with float: {result_add_float}") # Prints 0.30000000000000004

# A more complex example showing precision control
ctx = decimal.Context(prec=5) # New context with precision of 5
d3 = ctx.create_decimal('1') / ctx.create_decimal('3')
print(f"1/3 with precision 5: {d3}")

ctx.prec = 50 # Increase precision to 50
d4 = ctx.create_decimal('1') / ctx.create_decimal('3')
print(f"1/3 with precision 50: {d4}")