import json
import pickle
import sqlite3


f = open("default-cards-20231023210947.json", "r")

# Define JSON string
jsonString = f.read()

# Convert JSON String to Python
jsonObjects = json.loads(jsonString)

# # check count
# print(len(jsonObjects))

columns = set()

for card in jsonObjects:
    columns = columns.union(set(card.keys()))

conn = sqlite3.connect(f"mtg_cards.db")

cursor = conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS cycles ("
sql += " VARCHAR, pos_".join(columns)
sql += " VARCHAR);"
print(sql)

cursor.execute(sql)
conn.commit()
