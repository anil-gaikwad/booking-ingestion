from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BookingSchema(BaseModel):
    booking_id: str = Field(..., title="Unique Booking ID")
    customer_name: str = Field(..., title="Customer Name")
    booking_date: datetime = Field(..., title="Booking Date")
    amount: float = Field(..., title="Booking Amount")
    vendor: str = Field(..., title="Vendor Name")

    class Config:
        from_attributes = True
