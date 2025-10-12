from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name : str
    last_name : str

    # v will take multiple parameters one by one, firstly it will run on first_name, then on the last_name
    @field_validator('first_name', 'last_name')
    def names_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError('Names must be capitalized')
        return v
    

class User(BaseModel):
    email : str

    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()
    
class Product(BaseModel):
    price : str # $4.44

    # this validation will run before any other validaiton being executed by pydantic
    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str) and v.startswith('$'):
            return float(v[1:])
        return float(v)
    
class DateRange(BaseModel):
    start_date : datetime
    end_date : datetime

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('End Date must be after Start Date')
        return values