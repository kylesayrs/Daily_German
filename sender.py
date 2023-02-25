#!/usr/bin/python3

import sqlite3
from datetime import date
import json
import requests

# Global variables
DB_FILE = "german_phrases.db"
NUM_TOTAL_PHRASES = 5000
INC = 14
START_DATE = date(2020, 12, 27)

# Pushover
raise ValueError("Environment not set!")
URL = None
USER_KEY = None
DEVICE = None
TOKEN = None
TITLE = None

#
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# Get date
today = date.today()
diff = (today - START_DATE).days
phrase_index = (diff * INC) % NUM_TOTAL_PHRASES

# Get phrase
c.execute('''SELECT * FROM Phrases LIMIT 1 OFFSET (?)''', (phrase_index, ))
row = c.fetchone()
conn.close()

# Create message
message = '***{de}***\n\n{en}'.format(de=row[0].replace('\n', ''),
                                  en=row[1])
payload = { "token": TOKEN,
            "user": USER_KEY,
            "device": DEVICE,
            "title": TITLE,
            "message": message}

# Send request
x = requests.post(URL, payload)
print(payload)
print(x)
print(x.content)
