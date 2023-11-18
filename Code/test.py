import requests
import json
import pandas as pd

from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_ID = os.getenv("DATABASE_ID")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")

#setup
NOTION_API_URL = "https://api.notion.com/v1/"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Load the CSV file
csv_path = 'Code/output_file.csv'


df = pd.read_csv(csv_path)

existing_book_names = set()

response = requests.post(
    f"{NOTION_API_URL}databases/{DATABASE_ID}/query",
    headers=headers,
)
if response.status_code == 200:
    existing_records = response.json().get('results', [])
    existing_book_names = {record['properties']['Book Name']['title'][0]['text']['content'] for record in existing_records}

# Iterate through rows and create Notion pages
for index, row in df.iterrows():
    book_name = row['Book name']

    # Check if the record exists
    if book_name in existing_book_names:
        print(f"Record for '{book_name}' already exists. Skipping.")
        continue

    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Book Name": {"title": [{"text": {"content": row['Book name']}}]},
            "Average rating from all members": {"number": row['Average rating from all members']},
            "Number of Favorites": {"number": row['Number of Favorites']},
        },
    }

    # Create a new page in the Notion database
    response = requests.post(
        f"{NOTION_API_URL}pages",
        headers=headers,
        data=json.dumps(data),
    )

    if response.status_code == 200:
        print(f"Data for '{book_name}' successfully written to Notion database.")
        # Update the set of existing book names
        existing_book_names.add(book_name)
    else:
        print(f"Error: {response.status_code}, {response.text}")
