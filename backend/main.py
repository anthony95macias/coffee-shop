from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, for development only
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Retrieve the database credentials from environment variables
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

conn_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

@app.get("/products")
async def get_all_products():
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM coffee_store.products;")  # Adjust the table name if necessary
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed due to {e}")

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        # cursor.execute("SELECT * FROM coffee_store.products WHERE productid = %s;", (product_id,))
        cursor.execute("SELECT * FROM coffee_store.products;")  # Adjust the table name if necessary
        record = cursor.fetchone()
        cursor.close()
        conn.close()
        if record:
            return record
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed due to {e}")

@app.get("/customers")
async def get_customers():
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee_store.customers;")
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return records
    except psycopg2.Error as e:
        return {"error": f"Database connection failed due to {e}"}

@app.get("/orders")
async def get_orders():
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee_store.orders;")
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return records
    except psycopg2.Error as e:
        return {"error": f"Database connection failed due to {e}"}

@app.get("/order_details")
async def get_order_details():
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee_store.orderdetails;")
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return records
    except psycopg2.Error as e:
        return {"error": f"Database connection failed due to {e}"}

# If you're using `if __name__ == "__main__":` to run your application,
# make sure it's at the bottom of the file.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
