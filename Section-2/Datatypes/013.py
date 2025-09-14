import arrow

# A date that was created a while ago
past_time = arrow.get('2024-09-01T10:00:00+00:00')

# A date in the future
future_time = arrow.utcnow().shift(minutes=+30)

print(f"Past time (humanized): {past_time.humanize()}")
print(f"Future time (humanized): {future_time.humanize()}")

# Automatically parse a common ISO 8601 string
date_from_string = arrow.get('2024-10-27T14:30:00')
print(f"Parsed date: {date_from_string}")

# Format the date into a custom string
formatted_date = date_from_string.format('YYYY-MM-DD HH:mm:ss')
print(f"Formatted date: {formatted_date}")