from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username : str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError('Username must be atleast 4 characters !')
        return v;

# model validator validates the entire model, or we can say that it accesses all the values at the same time
class SignupData(BaseModel):
    password : str
    confirm_password : str

    # runs after the field validation
    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match !")
        return values;




     



