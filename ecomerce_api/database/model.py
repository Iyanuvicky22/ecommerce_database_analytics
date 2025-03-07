

Customers Table
Column	Type	Description
id	SERIAL PRIMARY KEY	Unique customer identifier
customer_id	VARCHAR(20) UNIQUE	Matches Customer_id from CSV
gender	VARCHAR(10)	Male/Female
device_type	VARCHAR(20)	Web, Mobile
login_type	VARCHAR(20)	Member, Guest
Orders Table
Column	Type	Description
id	SERIAL PRIMARY KEY	Unique order ID
customer_id	VARCHAR(20)	Foreign Key → Customers(customer_id)
order_date	DATE	Date order was placed
order_priority	VARCHAR(10)	Critical, High, etc.
payment_method	VARCHAR(20)	Credit Card, PayPal, etc.
Products Table
Column	Type	Description
id	SERIAL PRIMARY KEY	Unique product identifier
product_category	VARCHAR(50)	Matches Product_Category from CSV
product_name	VARCHAR(100)	Matches Product from CSV
Order Items Table
Column	Type	Description
id	SERIAL PRIMARY KEY	Unique order item identifier
order_id	INTEGER	Foreign Key → Orders(id)
product_id	INTEGER	Foreign Key → Products(id)
quantity	INTEGER	Units purchased
discount	DECIMAL(5,2)	Discount applied (%)
sales	DECIMAL(10,2)	Sales revenue from the item
profit	DECIMAL(10,2)	Profit from the item
shipping_cost	DECIMAL(10,2)	Cost of shipping
