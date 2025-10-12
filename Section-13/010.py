# Advanced nested model patterns
from pydantic import BaseModel
from typing import Optional, List, Union

class Address(BaseModel):
    street : str
    city : str
    postal_code : str

class Company(BaseModel):
    name : str
    address : Optional[Address] = None


class Employee(BaseModel):
    name : str
    company : Optional[Company] = None

class TextContent(BaseModel):
    type : str = 'Text'
    content : str

class ImageContent(BaseModel):
    type : str = "Image"
    url : str
    alt_text : str

class Article(BaseModel):
    title : str

    # mix of both
    sections : List[Union[TextContent, ImageContent]]

# deeply nested structure

class Country(BaseModel):
    name : str
    code : str

class State(BaseModel):
    name : str
    country : Country

class City(BaseModel):
    name : str
    state : State

class Address(BaseModel):
    street : str
    city : City
    postal_code : str

class Organization(BaseModel):
    name : str
    head_quarter : Address

    # Whatever value branches will be having should be confirming to the Address pydantic model
    branches : List[Address] = []
    
