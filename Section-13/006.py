# computed property in pydantic
from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price : float
    quantity : int
    
    # this field will be calculated on the go
    # this field is a property which means it can be accessed just like other data members
    @computed_field
    @property
    def total_price(self) -> float : 
        return self.price * self.quantity

class Booking(BaseModel):
    user_id : int
    room_id : int
    nights : int = Field(
        ...,
        ge=1
    )
    rate_per_night : float

    @computed_field
    @property
    def total_amount(self) -> float : 
        return self.nights * self.rate_per_night


booking = Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=100.0
)

print(booking.total_amount)
print(booking.model_dump()) 