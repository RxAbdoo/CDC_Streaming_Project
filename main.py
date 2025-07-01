import faker
import psycopg2
from datetime import datetime
import random
import time

fake = faker.Faker()

def generate_transaction():
    user = fake.simple_profile()
    return { 
        "transaction_id": fake.uuid4(),
        "user_id": user['username'],
        "timestamp": datetime.utcnow(),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(['USD', 'GBP']),
        "city": fake.city(),
        "country": fake.country(),
        "merchant_name": fake.company(),
        "paymentmethod": random.choice(['credit_card', 'debit_card', 'online_transfer']),
        "ipAddress": fake.ipv4(),
        "affiliateid": fake.uuid4()
    }

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS transactions(
                transaction_id VARCHAR(255) PRIMARY KEY,
                user_id VARCHAR(255),
                timestamp TIMESTAMP,
                amount DECIMAL,
                currency VARCHAR(255),
                city VARCHAR(255),
                country VARCHAR(255),
                merchant_name VARCHAR(255),
                paymentmethod VARCHAR(255),
                ipAddress VARCHAR(255),
                affiliateid VARCHAR(255)
            )
        """)
    conn.commit()

if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="financial_db",
        user="postgres",
        password="postgres",
        port=5432
    )
    create_table(conn)

    while True:
        transaction = generate_transaction()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO transactions(
                    transaction_id, user_id, timestamp, amount, currency, city,
                    country, merchant_name, paymentmethod, ipAddress, affiliateid
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                transaction["transaction_id"],
                transaction["user_id"],
                transaction["timestamp"],
                transaction["amount"],
                transaction["currency"],
                transaction["city"],
                transaction["country"],
                transaction["merchant_name"],
                transaction["paymentmethod"],
                transaction["ipAddress"],
                transaction["affiliateid"]
            ))
        conn.commit()
        print("Inserted:", transaction)
        time.sleep(2)
