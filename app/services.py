from .database import bookings_collection
from .models import BookingSchema
from bson import ObjectId

async def add_booking(booking_data: dict):
    result = await bookings_collection.insert_one(booking_data)
    return str(result.inserted_id)

async def get_bookings(filter_query={}):
    cursor = bookings_collection.find(filter_query)
    return await cursor.to_list(length=100)

async def get_booking_by_id(booking_id: str):
    return await bookings_collection.find_one({"_id": ObjectId(booking_id)})

async def delete_booking(booking_id: str):
    result = await bookings_collection.delete_one({"_id": ObjectId(booking_id)})
    return result.deleted_count > 0
