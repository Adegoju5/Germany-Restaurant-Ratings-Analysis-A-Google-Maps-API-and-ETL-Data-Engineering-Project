from google.cloud import bigquery
from google.oauth2 import service_account

key_path = '/Users/debowalealex/downloads/nth-glider-362309-ed1a06b4521f.json'

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# Create a client to interact with BigQuery
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Define the schema for the table
schema = [
    bigquery.SchemaField('place_id', 'STRING', mode='REQUIRED'),
    bigquery.SchemaField('name', 'STRING', mode='REQUIRED'),
    bigquery.SchemaField('address', 'STRING', mode='REQUIRED'),
    bigquery.SchemaField('rating', 'FLOAT'),
]

# Define the table reference
table_ref = client.dataset('restaurants').table('restaurant')

# Define the table configuration
table_config = bigquery.Table(table_ref, schema=schema)

# Create the table if it doesn't exist
try:
    table = client.create_table(table_config)
    print('Table created successfully.')
except Exception as e:
    if 'Already Exists' in str(e):
        print('Table already exists.')
    else:
        print('Error creating table: {}'.format(e))
