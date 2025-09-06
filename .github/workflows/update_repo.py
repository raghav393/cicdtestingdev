import requests
import json

# Set your Databricks workspace URL and personal access token
DATABRICKS_URL = 'https://adb-3605750019002736.16.azuredatabricks.net'
TOKEN = 'dapif12b4c91da44cd7a89c0a7ec8e33ae70'

# Define the repo ID and branch/tag to update
repo_id = 3912074432659232
new_branch_or_tag = 'main'

# Set up the API endpoint
endpoint = f'{DATABRICKS_URL}/api/2.0/repos/{repo_id}'

# Prepare the payload
payload = {
    'branch': new_branch_or_tag
}

# Define headers
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

# Send the PATCH request
response = requests.patch(endpoint, headers=headers, data=json.dumps(payload))

# Handle response
if response.status_code == 200:
    repo_details = response.json()
    print('Repository updated successfully:', repo_details)
else:
    print(f'Failed to update repo: {response.status_code} - {response.text}')
