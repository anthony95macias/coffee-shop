# from fastapi import FastAPI
# import psycopg2
# from dotenv import load_dotenv
# import os

# load_dotenv()  # Load environment variables from .env file

# app = FastAPI()

# # Retrieve the database credentials from environment variables
# db_user = os.getenv("DB_USER")
# db_password = os.getenv("DB_PASSWORD")
# db_host = os.getenv("DB_HOST")
# db_port = os.getenv("DB_PORT")
# db_name = os.getenv("DB_NAME")

# conn_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# # Connect to the database
# try:
#     conn = psycopg2.connect(conn_string)
#     # Create a cursor object
#     cursor = conn.cursor()

#     # Display records from the Products table
#     cursor.execute("SELECT * FROM coffee_store.Products;")
#     records = cursor.fetchall()
#     print("\nRecords from the Products table:")
#     for record in records:
#         print(record)

#     # Display records from the Customers table
#     cursor.execute("SELECT * FROM coffee_store.Customers;")
#     records = cursor.fetchall()
#     print("\nRecords from the Customers table:")
#     for record in records:
#         print(record)

#     # Display records from the Orders table
#     cursor.execute("SELECT * FROM coffee_store.Orders;")
#     records = cursor.fetchall()
#     print("\nRecords from the Orders table:")
#     for record in records:
#         print(record)

#     # Display records from the OrderDetails table
#     cursor.execute("SELECT * FROM coffee_store.OrderDetails;")
#     records = cursor.fetchall()
#     print("\nRecords from the OrderDetails table:")
#     for record in records:
#         print(record)

#     # Close the cursor and connection to the database
#     cursor.close()
#     conn.close()
# except psycopg2.Error as e:
#     print(f"Database connection failed due to {e}")
