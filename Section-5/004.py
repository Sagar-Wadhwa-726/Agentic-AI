# You want to simulate tea heating
# It starts at 40 degress celcius and boils at 100 degrees celcius

# Task : 
# Use a while loop
# Increase temperature by 15 until it reaches or exceeds 100 degrees
# Print each temperature step

temperature = 40
print(f"Current temperature is {temperature}°C")
while(temperature<100):
    temperature += 15
    print(f"Current temperature is {temperature}°C")
print("Tea is boiled now!")