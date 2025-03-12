from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = "booking_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
bookings_collection = db["bookings"]
