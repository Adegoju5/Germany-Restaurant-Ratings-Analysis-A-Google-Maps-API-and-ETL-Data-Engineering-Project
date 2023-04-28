import pyarrow
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from sqlalchemy import create_engine

# MySQL connection details
mysql_host = '127.0.0.1'
mysql_user = 'root'
mysql_password = 'root'
mysql_port = 3307
mysql_database = 'api_de_project'
mysql_table = 'restaurants'

# BigQuery connection details
bq_project = 'nth-glider-362309'
bq_dataset = 'restaurants'
bq_table = 'restaurant'
bq_credentials = service_account.Credentials.from_service_account_file('/Users/debowalealex/downloads/nth-glider-362309-ed1a06b4521f.json')

# Connect to MySQL using create_engine
mysql_conn_str = f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}"
mysql_engine = create_engine(mysql_conn_str)
mysql_conn = mysql_engine.connect()

# Extract data from MySQL into a pandas dataframe
df = pd.read_sql(f"SELECT place_id, name, address, rating FROM {mysql_table}", con=mysql_conn)

# Extract city from address column and create a new column for it
df['city'] = df['address'].str.split().str[-1]
df.drop('address', axis=1, inplace=True)

# Reorder columns so that rating comes last
df = df.reindex(columns=['place_id', 'name', 'city', 'rating'])

# Load data into BigQuery
bq_client = bigquery.Client(project=bq_project, credentials=bq_credentials)
bq_table_ref = bq_client.dataset(bq_dataset).table(bq_table)
job_config = bigquery.LoadJobConfig()
job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
job_config.source_format = bigquery.SourceFormat.PARQUET

job = bq_client.load_table_from_dataframe(df, bq_table_ref, job_config=job_config)
job.result()  # Wait for the job to complete

print(f'{job.output_rows} rows loaded into BigQuery table {bq_project}.{bq_dataset}.{bq_table}')


