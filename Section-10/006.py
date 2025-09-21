# Bill app with exception handling

class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menus = {
        "masala" : 20,
        "ginger" : 40
    }

    try:
        if flavor not in menus:
            raise InvalidChaiError("That chai is not available !")
        if not isinstance(cups, int):
            raise TypeError("The number of cups must be an integer !")
        total = menus[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai : Rs.{total} . . please pay ASAP")
    except Exception as e:
        print("Error :", e)
    finally:
        print("Thank you for visiting Chai n Code")

bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)

