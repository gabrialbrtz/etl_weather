from google.api_core.exceptions import NotFound
from google.cloud import bigquery
from google.oauth2 import service_account
from src.utils.big_query import load_pandas_to_bq
import logging
from src.utils.exceptions import ExceptionClause
from src.utils.constans import path_credentials_bq


def load_data(df):
    logging.info("Loading data to Big Query...")
    logging.info("Loading data process starting")

    try:

        # Client Big Query
        client = bigquery.Client(credentials=service_account.Credentials.from_service_account_file(path_credentials_bq))

        # Big Query (project_id,dataset_id,table_id)
        project_id = 'tfm-etl-weather-project'
        dataset_id = 'data_warehouse'
        table_id = 'openweather'
        table_name = f'{dataset_id}.{table_id}'

        # Check if table exists in BigQuery
        table_ref = f"{project_id}.{dataset_id}.{table_id}"
        try:
            client.get_table(table_ref)  # Attempt to get the table
            table_exists = True
        except NotFound:
            table_exists = False

        # If the table doesn't exist, CREATE TABLE WITH A SCHEMA
        if not table_exists:
            path_ddl = r"C:\Users\gabri\Documents\Developer\etl_weather\src\ddls\open_weather_ddl.sql"
            with open(path_ddl, 'r') as f:
                ddl_sql = f.read()
            query_job = client.query(ddl_sql)
            query_job.result()  # Wait for the query to complete

        # Load pandas df to Big Query
        load_pandas_to_bq(path=path_credentials_bq,
                          df=df,
                          table_name=table_name,
                          project_id=project_id,
                          type='append')
        logging.info("Load table to bq succesfully")

    except ExceptionClause("Load to Big Query failed") as error:
        logging.error("Exception:", str(error))
        logging.error("Failed load to BQ")
