from fastapi import APIRouter, HTTPException, Query
from typing import List
from .models import BookingSchema
from .services import add_booking, get_bookings, get_booking_by_id, delete_booking

router = APIRouter()

@router.post("/bookings", response_model=dict)
async def create_booking(booking: BookingSchema):
    booking_id = await add_booking(booking.dict())
    return {"message": "Booking created", "id": booking_id}

@router.get("/bookings", response_model=List[BookingSchema])
async def list_bookings(date: str = Query(None), vendor: str = Query(None)):
    filters = {}
    if date:
        filters["booking_date"] = date
    if vendor:
        filters["vendor"] = vendor
    bookings = await get_bookings(filters)
    return bookings

@router.get("/bookings/{id}", response_model=BookingSchema)
async def get_booking(id: str):
    booking = await get_booking_by_id(id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.delete("/bookings/{id}")
async def remove_booking(id: str):
    success = await delete_booking(id)
    if not success:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted"}
