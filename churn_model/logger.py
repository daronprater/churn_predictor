import sqlite3
from datetime import datetime

def log_prediction_to_db(customer_id, prediction, probability):
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT,
            prediction TEXT,
            probability REAL,
            timestamp TEXT
        )
    ''')

    # Insert prediction
    cursor.execute('''
        INSERT INTO predictions (customer_id, prediction, probability, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (customer_id, prediction, probability, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()
