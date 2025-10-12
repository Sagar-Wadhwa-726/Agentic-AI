# nested models
from pydantic import BaseModel

class Address(BaseModel):
    street : str
    city : str
    postal_code : str

# user contains a reference of Address model
# validation for address is also applied (hierarichal data structure)
class User(BaseModel):
    id : int
    name : str
    address : Address

address = Address(
    street='123',
    city='Jaipur',
    postal_code='302001'
)

user = User(
    id=1,
    name="Sagar",
    address=address
)

user_date = {
    "id":1,
    "name":"Sagar",
    "address":{
        "street" : "321 something",
        "city" : "Delhi",
        "postal_code" : "20020"
    }
}

user = User(**user_date)
print(user)


