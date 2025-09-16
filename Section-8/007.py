# Authorization decorator
from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role!="admin":
            print(f"Access denied, only admin function !")
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_inventory(role):
    print("Access Granted to Tea Inventory")

access_inventory("user")
access_inventory("admin")