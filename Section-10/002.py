# try except else and finally - 
"""Inside the try block place that piece of code which can throw error, except block will be handling that error, if we don't go inside the except block, the else block will be executed, and the finally block will be executed always, no matter if the exception occurs or not"""

def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai . . . ")
        if(flavor == "unknown"):
            raise ValueError("We don't know that flavor !")
    except ValueError as e:
        print("Error : ", e)
    else:
        print(f"{flavor} chai is ready !")
    finally:
        print("Next customer please !")

serve_chai("masala")
serve_chai("unknown")