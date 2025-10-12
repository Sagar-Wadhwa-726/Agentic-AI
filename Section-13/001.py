# Type hints powering schema validation through Pydantic
"""
1. Pydantic provides data validation - data parsing and validation, api development, config management, data serialization/deserialization.
2. Setting management 

All pydantic models inherit from the basemodel

Avoids changing of the type of the data 

name = "sagar"
name = 87 // can be avoided with the help of pydantic
"""
from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool

input_data = {
    'id' : '101', # type annotation
    'name' : 'sagar',
    'is_active' : True
}

# unpack the dictionary - otherwise we are passing just one object which is the dictionary
user = User(**input_data)

print(user)

# pydantic ensures data integrity, also if a data type is having some mismatch then pydantic will try to convert it firstly to the expected data type if possible, and if it can be done, if not possible, it will throw validation error

