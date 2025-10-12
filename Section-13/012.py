# Serialization - converting complex data structures (pydantic models) to easily stored/transmitted data structures like python dictionaries, JSON, XML (not used much)

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str
    zip_code : str

class User(BaseModel):
    id : int
    name : str
    email : str
    is_active : bool = True
    created_at : datetime
    address : Address
    tags: List[str] = []
    model_config = ConfigDict(
        json_encoders={datetime : lambda value : value.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=1,
    name="Sagar Wadhwa",
    email="sagarwadhwa888@gmail.com",
    created_at=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="something",
        city="delhi",
        zip_code="230493"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)


json_str = user.model_dump_json()
print("="*30)
print(json_str)

# json converted to string which can be converted back to JSON - json encoded string