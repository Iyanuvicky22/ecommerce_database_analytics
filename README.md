# Project: E-commerce Backend System with PostgreSQL & FastAPI 
## Project Overview
As a data engineer for an e-commerce website, you are given a CSV dataset containing raw transactional data. Your task is to design and implement a robust data pipeline that efficiently processes, stores, and exposes insights from this data. To achieve this, you first model the data into four key tables: Orders, Customers, Products, and Order Items. The Customers table holds user details, while the Products table contains product information. The Orders table tracks each transaction, linking customers to their purchases, and the Order Items table breaks down each order into individual product purchases, capturing quantities and prices. Once the schema is defined, you store the structured data in a PostgreSQL database, optimizing it with indexing and foreign key relationships for efficient queries. Next, you perform various computations, such as calculating total sales, customer lifetime value, and product performance metrics, directly in the database. To expose this data, you build a FastAPI endpoint that allows users to query and visualize key analytics, such as top-selling products, customer purchase behavior, and revenue trends.

## Prerequisites:
Before starting this project, you should:
- Have basic knowledge of SQL (SELECT, INSERT, JOIN, INDEXING).
- Understand relational databases and how tables relate via foreign keys.
- Be familiar with Python, particularly working with Pandas, FASTAPI and SQLAlchemy.
- Have PostgreSQL installed and running on your system.

**Goal**:
1) Design a relational database based on the dataset.
2) Load the provided CSV data into PostgreSQL.
3) Write SQL queries for business insights.
4) Expose API endpoints with FastAPI.
5) Implement indexing and optimization.
6) Use SQLAlchemy ORM for queries and operations.
7) Document the API with Swagger UI (/docs)

## Database Schema
- Order details (Order_Date, Order_Priority, Payment_method)
- Customer information (Customer_id, Gender, Device_Type, Customer_Login_Type)
- Product information (Product_Category, Product)
- Financial information (Quantity, Discount, Sales, Profit, Shipping_cost)

## Project Structure
```
ecommerce_api/
    ├── .gitignore
    ├── README.md
    ├── main.py
    ├── pyproject.toml
    ├── poetry.lock
    ├── database/
    │   ├── __init__.py
    │   ├── models.py (*Models[database tables], relationships and indexes creation.)
    │   ├── crud.py   (*Database queries for insights.*)
    │   ├── db_setup.py  (*Database setup and connection.*)
    ├── data/
    │   ├── ecommerce_dataset.csv  (*Provided Dataset*)
    ├── scripts/
    │   ├── __init__.py
    │   ├── load_data.py (*Script to load CSV into PostgreSQL*)
    ├── tests/
    │   ├── __init__.py
    │   ├── test_load_data.py (*Testing the load_data script.*)
    ├── images/
    │   ├── Ecommerce Database Project Process Map.jpg
    │   ├── ecommerce database schema [MConverter.eu].png
    │   ├── FastAPI structure.png
```

### Project Flow Architecture
![alt text](images/flow_architecture.png)

### Database Schema and Relationships
![alt text](images/database_schema.png)

### INSIGHTS GLEANED FROM THE DATABASE.
#### 1️⃣ Customer Insights
* Q1) Total number of unique customers
![alt text](images/Q1.png)
* Q2) Number of customers per device type (Web/Mobile)
![alt text](images/Q2.png)
* Q3) Percentage of members vs. guest users.
![alt text](images/Q3.png)


#### 2️⃣ Product Performance
* Q4) Top 5 best-selling products based on sales.
![alt text](images/Q4.png)
* Q5) Top 3 product categories with the highest revenue.
![alt text](images/Q5.png)
* Q6) Products with the highest profit margins.
![alt text](images/Q6.png)

#### 3️⃣ Order Analysis
* Q7) Average order size (quantity per order).
![alt text](images/Q7.png)
* Q8) Total revenue and profit.
![alt text](images/Q8.png)
* Q9) Percentage of orders placed with High or Critical priority.
![alt text](images/Q9.png)

#### 4️⃣ Discount Impact
* Q10) Does higher discount % lead to more sales?
![alt text](images/Q10.png)
```
The optimum discount rate that yielded most sales is 30%. 
Higher than does not translate to more sales. 
50% and 10% discounts yielded the least two sales in ranking.
```


### **🔹API Endpoints with FastAPI**
**Endpoint	             Method	      Description**
```
*/customers/*	            GET	    Get all customers
*/customers/{customer_id}*	GET   	Get details of a specific customer
*/orders/*	                GET	    Get all orders
*/orders/{order_id}*        GET	    Get details of a specific order
*/products/*	            GET	    Get all products
*/analytics/top-products/*	GET	    Get top-selling products
*/analytics/revenue/*	    GET	    Get total revenue & profit
```
##### FastAPI endpoint structure.
![alt text](<images/FastAPI structure.png>)

### **🔹Implemented Indexing & Query Optimization**
CREATE INDEX idx_order_customer ON Orders(customer_id);\
CREATE INDEX idx_product_sales ON OrderItems(product_id);


## Interacting with the project
### ** Clone the PR
```cmd
git clone https://github.com/Data-Epic/database-fundamentals.git
```

### **2. Install Poetry**
```cmd
pipx install poetry
```
### **3. Install Dependencies**
```cmd
poetry install
```
### **4. Activate Virtual Environment**
```cmd
poetry update
```
### **5. Setup Local DB
```
In env file: (I used postgres)
DB_URL ='postgresql://user:password@host:port/db_name'
Check the link below for help.
[text](https://www.strongdm.com/blog/postgres-create-database#:~:text=Open%20a%20terminal%20on%20Unix,%E2%80%9Cpostgres%E2%80%9D%20with%20that%20name.)

### **5. Run the API**
```cmd
poetry run fastapi dev main.py
```

## **Usage**
### **FastAPI Swagger UI**
Once the API is running, visit:
```
http://127.0.0.1:8000/docs
```
This provides an interactive interface to test the API endpoints.

Also you can visit the link below for extensive info on the API
```
http://127.0.0.1:8000/redoc 
```

### Dependencies
```
pandas (>=2.2.3,<3.0.0)
sqlalchemy (>=2.0.38,<3.0.0)
psycopg2 (>=2.9.10,<3.0.0)
fastapi (>=0.115.11,<0.116.0)
dotenv (>=0.9.9,<0.10.0)

[tool.poetry.group.dev.dependencies]
black = "^25.1.0" - for code formatting
```

## Author : Arowosegbe Victor Iyanuoluwa.
