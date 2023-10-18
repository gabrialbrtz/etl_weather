import pandas as pd
from google.oauth2 import service_account
import pandas_gbq


def load_pandas_to_bq(path: str, df: pd.DataFrame, table_name: str, project_id: str, type: str) -> None:
    """
    Function to load pandas Dataframe into Big Query table

    Parameters:
    ------------
    path: str
        path of the json credentials of Big Query

    df: pd.DataFrame
        Pandas dataframe that you want to upload as table to Big Query

    table_name: str
        Name of the table that you want to create in BigQuery "database_name.table_name".
        For example 'databasegabriel.tabla1'

    project_id: str
        Name of the project in Google Cloud Platform

    type: str
        'replace' if this table exists replace for this new table
        'append' if this table exists append new data

    Return:
        None
    """
    bq_cred = service_account.Credentials.from_service_account_file(path)
    pandas_gbq.to_gbq(df,
                      table_name,
                      project_id=project_id,
                      if_exists=type,
                      credentials=bq_cred,
                      progress_bar=True)





