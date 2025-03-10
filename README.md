# **Project: E-commerce Backend System with PostgreSQL & FastAPI**

## **Prerequisites:**
Before starting this project, you should:
- Have basic knowledge of SQL (SELECT, INSERT, JOIN, INDEXING).
- Understand relational databases and how tables relate via foreign keys.
- Be familiar with Python, particularly working with Pandas and SQLAlchemy.
- Have PostgreSQL installed and running on your system.

---
## **Goal:**
- Design a relational database based on the dataset.
- Load the provided CSV data into PostgreSQL.
- Write SQL queries for business insights.
- Expose API endpoints with FastAPI.
- Implement indexing and optimization.
- Use SQLAlchemy ORM for queries and operations.
- Document the API with Swagger UI (`/docs`)

---
## **Dataset Information**
https://github.com/Data-Epic/database-fundamentals/blob/main/data/ecommerce_dataset.csv.
This dataset simulates **real-world e-commerce transactions** with columns like:
- **Order details** (`Order_Date`, `Order_Priority`, `Payment_method`)
- **Customer information** (`Customer_id`, `Gender`, `Device_Type`, `Customer_Login_Type`)
- **Product information** (`Product_Category`, `Product`, `Quantity`, `Discount`, `Sales`)
- **Financial information** (`Profit`, `Shipping_cost`)


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

### **Data Architecture**
![Data Architecture](images/architecture.jpg)
---


## **Tasks**

### **🔹 Task 1: Define the PostgreSQL Database Schema**
- Create a database named **`ecommerce_db`**.
- Define tables in **SQLAlchemy ORM**:

### **Data Modelling**
![data Model](images/data-modelling.jpg)
---

### **🔹 Task 2: Load the CSV Data into PostgreSQL**
- Write a script (`scripts/load_data.py`) to **import `ecommerce_dataset.csv` into the four different PostgreSQL tables created above.**.
- Ensure proper **data type conversions** (dates, decimals, etc.).
- **Handle duplicates** using `ON CONFLICT` to avoid inserting the same customers multiple times.

---

### **🔹 Task 3: Write SQL Queries for Business Insights**
Write SQL queries to **analyze e-commerce performance**:

1️⃣ **Customer Insights**
   - Total number of **unique customers**.
   - Number of **customers per device type (Web/Mobile)**.
   - Percentage of **members vs. guest users**.

2️⃣ **Product Performance**
   - Top **5 best-selling products** based on sales.
   - Top **3 product categories** with the highest revenue.
   - Products with the **highest profit margins**.

3️⃣ **Order Analysis**
   - Average **order size (quantity per order)**.
   - Total **revenue and profit**.
   - Percentage of orders placed with **High or Critical priority**.

4️⃣ **Discount Impact**
   - Does **higher discount % lead to more sales**?  
   *(Hint: Compare Sales vs. Discount using `GROUP BY discount`)*

---

### **🔹 Task 4: Expose API Endpoints with FastAPI**
Develop the following REST API endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/customers/` | **GET** | Get all customers |
| `/customers/{customer_id}` | **GET** | Get details of a specific customer |
| `/orders/` | **GET** | Get all orders |
| `/orders/{order_id}` | **GET** | Get details of a specific order |
| `/products/` | **GET** | Get all products |
| `/analytics/top-products/` | **GET** | Get top-selling products |
| `/analytics/revenue/` | **GET** | Get total revenue & profit |

- Use **SQLAlchemy ORM** to **interact with PostgreSQL**.
- Document all endpoints in **Swagger UI (`/docs`)**.

---

### **🔹 Task 5: Implement Indexing & Query Optimization**
1. **Create an index** on high-frequency search columns:
   ```sql
   CREATE INDEX idx_order_customer ON Orders(customer_id);
   CREATE INDEX idx_product_sales ON OrderItems(product_id);
   ```
2. **Explain how indexing improves query performance.**
3. **Use EXPLAIN ANALYZE** to compare indexed vs. non-indexed queries.


