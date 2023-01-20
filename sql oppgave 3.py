import sqlite3 
import csv

con = sq.connect('info-info.db')

c.execute(
    """
    CREATE TABLE sales (
        SalesID INTEGER ,
        OrderID TEXT NOT NULL,
        ProductID TEXT NOT NULL,
        Sales REAL,
        Quantity INTEGER,
        Discount REAL,
        Profit REAL,
        PRIMARY KEY(SalesID),
        FOREIGN KEY(OrderID) REFERENCES orders(OrderID),
        FOREIGN KEY(ProductID) REFERENCES products(ProductID)
        );
     """
)

# ORDERS
c.execute(
    """
    CREATE TABLE orders (
        OrderID TEXT,
        OrderDate TEXT,
        ShipDate TEXT,
        ShipMode TEXT,
        CustomerID TEXT,
        PRIMARY KEY(OrderID),
        FOREIGN KEY(CustomerID) REFERENCES customers(CustomerID)
        );
    """
)

# CUSTOMERS
c.execute(
    """
    CREATE TABLE customers (
        CustomerID TEXT PRIMARY KEY,
        CustomerName TEXT,
        Segment TEXT,
        Country TEXT,
        City TEXT,
        State TEXT,
        PostalCode TEXT,
        Region TEXT
        );
    """
)

# PRODUCTS
c.execute(
    """
    CREATE TABLE products (
        ProductID TEXT PRIMARY KEY,
        Category TEXT,
        SubCategory TEXT,
        ProductName TEXT
        );
    """
)