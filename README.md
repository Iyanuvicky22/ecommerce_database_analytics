# **Project: E-commerce Backend System with PostgreSQL & FastAPI**

## **Goal:**
Mentees will:
- **Design a relational database** based on the dataset.
- **Load the provided CSV data into PostgreSQL.**
- **Write SQL queries** for business insights.
- **Expose API endpoints with FastAPI.**
- **Implement indexing and optimization.**
- **Use SQLAlchemy ORM for queries and operations.**
- **Document the API with Swagger UI (`/docs`).**

---

## **Dataset Information**
https://github.com/Data-Epic/database-fundamentals/blob/main/E_commerce_dataset.csv.
This dataset contains **real-world e-commerce transactions** with columns like:
- **Order details** (`Order_Date`, `Order_Priority`, `Payment_method`)
- **Customer information** (`Customer_id`, `Gender`, `Device_Type`, `Customer_Login_Type`)
- **Product information** (`Product_Category`, `Product`, `Quantity`, `Discount`, `Sales`)
- **Financial information** (`Profit`, `Shipping_cost`)

---

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
    │   ├── ecommerce_dataset.csv  (*Add the Provided Dataset Here*)
    ├── scripts/
    │   ├── load_data.py (*Script to load CSV into PostgreSQL*)
```

---

## **Tasks**

### **🔹 Task 1: Define the PostgreSQL Database Schema**
- Create a database named **`ecommerce_db`**.
- Define tables in **SQLAlchemy ORM**:

### **Customers Table**
| Column        | Type                | Description                     |
|--------------|--------------------|---------------------------------|
| `id`         | SERIAL PRIMARY KEY  | Unique customer identifier      |
| `customer_id` | VARCHAR(20) UNIQUE | Matches `Customer_id` from CSV  |
| `gender`     | VARCHAR(10)         | Male/Female                     |
| `device_type` | VARCHAR(20)        | Web, Mobile                     |
| `login_type`  | VARCHAR(20)        | Member, Guest                   |

### **Orders Table**
| Column         | Type               | Description                        |
|---------------|-------------------|------------------------------------|
| `id`         | SERIAL PRIMARY KEY | Unique order ID                   |
| `customer_id` | VARCHAR(20)       | Foreign Key → Customers(customer_id) |
| `order_date`  | DATE              | Date order was placed             |
| `order_priority` | VARCHAR(10)    | Critical, High, etc.              |
| `payment_method` | VARCHAR(20)    | Credit Card, PayPal, etc.         |

### **Products Table**
| Column            | Type              | Description                          |
|------------------|----------------|----------------------------------|
| `id`            | SERIAL PRIMARY KEY | Unique product identifier         |
| `product_category` | VARCHAR(50)      | Matches `Product_Category` from CSV |
| `product_name`  | VARCHAR(100)      | Matches `Product` from CSV         |

### **Order Items Table**
| Column         | Type             | Description                       |
|--------------|-----------------|---------------------------------|
| `id`         | SERIAL PRIMARY KEY | Unique order item identifier   |
| `order_id`   | INTEGER           | Foreign Key → Orders(id)       |
| `product_id` | INTEGER           | Foreign Key → Products(id)     |
| `quantity`   | INTEGER           | Units purchased                |
| `discount`   | DECIMAL(5,2)      | Discount applied (%)           |
| `sales`      | DECIMAL(10,2)     | Sales revenue from the item    |
| `profit`     | DECIMAL(10,2)     | Profit from the item           |
| `shipping_cost` | DECIMAL(10,2)  | Cost of shipping               |

---

### **🔹 Task 2: Load the CSV Data into PostgreSQL**
- Write a script (`scripts/load_data.py`) to **import `ecommerce_dataset.csv` into PostgreSQL**.
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

---

## **Deadline**
🕒 **Submit by Saturday, March 8th, 2025, 10:00 AM.**

## **Submission**
📌 **Share your PR** in the `task-submissions` channel and tag your mentors.  
📌 **GitHub Repository:** [TBD – Create a repo and link here]  

---

## **Rubrics**
| Category | Criteria |
|----------|----------|
| **Database Schema** | Tables correctly structured with appropriate constraints. |
| **Data Import** | CSV is correctly loaded into PostgreSQL. |
| **SQL Queries** | Queries return correct business insights. |
| **API Implementation** | FastAPI endpoints work correctly. |
| **Optimization** | Indexing improves query speed. |
| **Code Quality** | Code is well-structured and documented. |
| **Git Usage** | Proper commit messages and repository organization. |
