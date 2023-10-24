import json
import pickle
import sqlite3


f = open("default-cards-20231023210947.json", "r")

# Define JSON string
jsonString = f.read()

# Convert JSON String to Python
jsonObjects = json.loads(jsonString)

# # sanity check count
# print(len(jsonObjects))

columns = set()

for card in jsonObjects:
    columns = columns.union(set(card.keys()))

conn = sqlite3.connect(f"mtg_cards.db")

cursor = conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS defaultcards ("
sql += " VARCHAR, scryfall_".join(columns)
sql += " VARCHAR);"
print(sql)

cursor.execute(sql)
conn.commit()

for card in jsonObjects:
    columns = ", scryfall_".join(card.keys())
    values = "', '".join(map(str, card.values()))
    sql = f"INSERT INTO defaultcards ({columns}) VALUES ({values});"
    print(sql)
    cursor.execute(sql)
    conn.commit()
