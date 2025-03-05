import requests
import json
import pandas as pd

# Define the base URL for your CTFd instance
base_url = "http://CTFd_DOMAIN/api/v1/users"

# Your admin access token
access_token = "your_admin_access_token_here"

# Path to your Excel file
excel_file = "users.xlsx"

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)

# Ensure the Excel file contains columns for 'name', 'email', and 'password'
required_columns = ['username', 'email', 'password']
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"The Excel file must contain the following columns: {', '.join(required_columns)}")

# Set headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {access_token}",
}

# Iterate over the rows in the DataFrame and send a POST request for each user
for index, row in df.iterrows():
    user_payload = {
        "name": row['username'],
        "email": row['email'],
        "password": row['password'],
        "type": "admin",
        "verified": True,
        "hidden": False,
        "banned": False,
        "fields": []
    }

    # Send POST request to create the user
    response = requests.post(base_url, headers=headers, data=json.dumps(user_payload))

    # Check the response and print feedback
    if response.status_code == 201:
        print(f"User '{row['username']}' created successfully.")
    else:
        print(f"Failed to create user '{row['username']}': {response.status_code} - {response.text}")

