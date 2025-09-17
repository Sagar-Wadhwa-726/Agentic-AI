# Static methods in python - these are the methods which don't belong to an object but belong to a class as a whole

class ChaiUtils:
    # this is a decorator
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = "water , milk,     ginger, honey   "

# obj = ChaiUtils()
# obj.clean_ingredients(raw)

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)