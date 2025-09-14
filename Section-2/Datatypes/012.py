import arrow

# Get the current date and time
now = arrow.utcnow()
print(f"Current time: {now}")

# Calculate the date three months from now
future_date = now.shift(months=+3)
print(f"Three months from now: {future_date}")

# Calculate the date five days ago
past_date = now.shift(days=-5)
print(f"Five days ago: {past_date}")

past_date = now.shift(microseconds=-500 * 10**6)
print(past_date)