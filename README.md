# booking-ingestion

## 📁 Project Structure ##

```bash
booking-ingestion/
│── app/
│   ├── main.py                # Entry point of the FastAPI application
│   ├── models.py              # Database models (MongoDB schema)
│   ├── database.py            # MongoDB connection setup
│   ├── routes.py              # API routes
│   ├── schemas.py             # Pydantic validation schemas
│   ├── services.py            # Business logic (CRUD operations)
│── tests/
│   ├── test_bookings.py       # Unit tests for API endpoints
│── docs/
│   ├── roadmap.md             # Roadmap for production-grade system
│── docker-compose.yml         # Docker configuration for MongoDB
│── requirements.txt           # Dependencies
│── README.md                  # Setup guide and API documentation

```
