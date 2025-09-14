# Advanced data type in python
import arrow

# Get the current time in UTC
print(f"Current time in UTC : {arrow.utcnow()}")

# Get the current time in local timezone
print(f"Current time in local timezone : {arrow.now()}")

# Converting the time to specific timezone
print(f"Current time in Asia/Kolkata timezone : {arrow.now('US/Pacific')}")
