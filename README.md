# Database Fundamentals

A FastAPI-based REST API for e-commerce data management and analytics.

## Overview

This project provides a comprehensive API for accessing and analyzing e-commerce data stored in a PostgreSQL database. It offers endpoints for retrieving customer information, order details, product data, and generating analytical insights about sales performance, revenue, and discount impacts.

## Features

- **Data Access**: Fetch customers, orders, and products with pagination support
- **Individual Record Retrieval**: Retrieve specific customers and orders by ID
- **Analytics**:
  - Top-performing products analysis
  - Revenue and profit reporting
  - Discount impact assessment

## Prerequisites

- Python 3.13 or higher
- PostgreSQL database
- Python dependencies (see Installation)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Data-Epic/database-fundamentals/tree/ecommerce-api
   cd database-fundamentals
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install .
   ```

## Configuration

The application connects to a PostgreSQL database. The connection details are managed in the CRUD module. Ensure your database is properly set up before running the application.

Default database configuration:
- URL: `postgresql://username:password@localhost/ecommerce_db`

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000.

## API Documentation

Once the server is running, you can access the automatically generated API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Available Endpoints

#### Base Route
- `GET /`: Welcome message

#### Customer Data
- `GET /customers/`: List all customers (paginated)
- `GET /customers/{customer_id}`: Get customer by ID

#### Order Data
- `GET /orders/`: List all orders (paginated)
- `GET /orders/{order_id}`: Get order by ID

#### Product Data
- `GET /products/`: List all products (paginated)

#### Analytics
- `GET /analytics/top-products/`: Get top-performing products
- `GET /analytics/revenue/`: Get total profit and revenue analysis
- `GET /analytics/discount-impact/`: Get discount impact on sales

## **Project Structure**

```

ecommerce_api/

    ├── .gitignore

    ├── .env.example

    ├── README.md

    ├── main.py

    ├── pyproject.toml

    ├── poetry.lock

    ├── database/

    │   ├── __init__.py

    │   ├── models.py

    │   ├── crud.py

    │   ├── db_setup.py

    ├── api/

    │   ├── __init__.py

    │   ├── routes.py

    ├── data/

    │   ├── ecommerce_dataset.csv  (*Provided Dataset*)

    ├── scripts/

    │   ├── load_data.py (*Script to load CSV into PostgreSQL*)

```



## Error Handling

The API implements comprehensive error handling for database connection issues and unexpected errors. All endpoints return consistent response structures with appropriate success/failure indicators and error messages.

Response Format:
```json
{
  "message": "Status message",
  "success": true/false,
  "data": {...}  // or null in case of errors
}
```

## Database Models

The application uses SQLAlchemy ORM with the following models:
- `Customer`: Customer information
- `Orders`: Order details
- `Products`: Product catalog
- `OrderItem`: (referenced in analytics functions)

## Future Improvements

- Add authentication and authorization
- Implement POST, PUT, DELETE operations
- Add more advanced analytics capabilities
- Improve error handling with specific error types
- Add unit and integration tests


## Author

Damilola Adeniyi - adeniiyidamilola246@gmail.com