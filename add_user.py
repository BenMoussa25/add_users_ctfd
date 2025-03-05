import requests
import json
import pandas as pd
import hashlib
import random
import string

# Define the base URL for your CTFd instance
base_url = "http://CTFd_DOMAIN/api/v1/users"

# Your admin access token
access_token = "your_admin_access_token_here"

# Path to your Excel file
excel_file = "../users.xlsx"

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)

# Ensure the Excel file contains columns for 'name' and 'email'
required_columns = ['username', 'email']
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"The Excel file must contain the following columns: {', '.join(required_columns)}")

# Set headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {access_token}",
}

# Function to generate MD5 hash for password
def generate_md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

# Function to generate a random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# List to store the hashed passwords for each user
hashed_passwords = []

# Iterate over the rows in the DataFrame and send a POST request for each user
for index, row in df.iterrows():
    # Generate a random password
    random_password = generate_random_password()

    # Generate MD5 hash of the password
    hashed_password = generate_md5_hash(random_password)

    # Add the hashed password to the DataFrame
    df.loc[index, 'hashed_password'] = hashed_password

    user_payload = {
        "name": row['username'],
        "email": row['email'],
        "password": hashed_password,  # Use the hashed password here
        "type": "user",
        "verified": True,
        "hidden": False,
        "banned": False,
        "fields": []
    }

    # Send POST request to create the user
    response = requests.post(base_url, headers=headers, data=json.dumps(user_payload))

    # Check the response and print feedback
    if response.status_code == 200:
        print(f"User '{row['username']}' created successfully with password: {random_password}")
    else:
        print(f"Failed to create user '{row['username']}': {response.status_code} - {response.text}")

# Save the updated DataFrame with the hashed passwords back to the Excel file
df.to_excel(excel_file, index=False)
print(f"Hashed passwords have been added to '{excel_file}'")
