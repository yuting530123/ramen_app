import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL not set")
    return psycopg2.connect(DATABASE_URL)
<<<<<<< HEAD
    print("DATABASE_URL:", DATABASE_URL)
=======

>>>>>>> 207d954c6427222bd45563920f1241a32af4404a
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        flavor VARCHAR(50) NOT NULL,
        toppings TEXT[],
        total INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
<<<<<<< HEAD
print("🔥 insert_order 開始")
=======

>>>>>>> 207d954c6427222bd45563920f1241a32af4404a
def insert_order(flavor, toppings, total):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO orders (flavor, toppings, total)
        VALUES (%s, %s, %s)
    """, (flavor, toppings, total))

    conn.commit()
    cursor.close()
    conn.close()
<<<<<<< HEAD
    print("有存資料")

def get_orders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT flavor, toppings, total FROM orders ORDER BY id DESC")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
=======
>>>>>>> 207d954c6427222bd45563920f1241a32af4404a
