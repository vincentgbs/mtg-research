import json
import pickle
import sqlite3

# base_url = "https://data.scryfall.io/default-cards/"
file_name = "default-cards-20231023210947.json"

# ## UNTESTED
# import os
# import shutil
# import requests
# from pathlib import Path
#
# def download_file(url, target_dir):
#     local_filename = url.split('/')[-1]
#     path = os.path.join("/{}/{}".format(target_dir, local_filename))
#     with requests.get(url, stream=True) as r:
#         with open(path, 'wb') as f:
#             shutil.copyfileobj(r.raw, f)
#     return local_filename
#
# pwd = Path(__file__).parent
# download_file(base_url + file_name, pwd)

f = open(file_name, "r")

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
