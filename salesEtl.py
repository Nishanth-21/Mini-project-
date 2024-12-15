import pandas as pd
import sqlite3

def extractdata(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print("File not found")
        return None

def transformdata(data):
    data = data.dropna()
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
    if 'price' in data.columns and 'quantity' in data.columns:
        data['total'] = data['price'] * data['quantity']
    return data

def loaddata(data, db_name="pipeline.db"):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales(
                        id INTEGER PRIMARY KEY,
                        product TEXT,
                        price FLOAT,
                        quantity INTEGER,
                        total FLOAT)''')
    inst = '''INSERT INTO sales(product, price, quantity, total) VALUES(?, ?, ?, ?)'''
    cursor.executemany(inst, data[['product', 'price', 'quantity', 'total']].values.tolist())
    connection.commit()
    connection.close()

def pipeline(filepath):
    data = extractdata(filepath)
    if data is not None:
        transed = transformdata(data)
        loaddata(transed)

filepath = 'sales.csv'
pipeline(filepath)
