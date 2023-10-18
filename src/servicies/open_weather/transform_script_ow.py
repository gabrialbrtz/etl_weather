from src.servicies.open_weather.open_weather_connector import OpenWeatherConnector
from src.utils.functions_utils import json_to_pandas_normalize, delete_columns, \
    replace_dot_for_underscore
from src.utils.date_utils import timestamp_unix_to_date, timestamp_unix_to_date_hours
import logging
from src.utils.exceptions import ExceptionClause
import pandas as pd
from datetime import datetime


def transform_data(list_json):
    connector = OpenWeatherConnector()

    logging.info("Transforming data extracted from the Open Weather API...")
    logging.info('Beginning the transformation...')

    # Normalized json data to pandas dataframe

    try:
        df_pandas = json_to_pandas_normalize(list_json)
        logging.info("Data transformed to pandas DataFrame")

    except ExceptionClause("Data can't be normalized from json to pandas") as error:
        logging.error(f"Exception:", str(error))
        logging.error("Data transformation to pandas failed")

    # Split weather column into various columns

    try:
        df_pandas = connector.split_weather_column(df_pandas)
        logging.info("json weather column split in various columns")

    except ExceptionClause("Weather column can't be split in various columns") as error:
        logging.error(f"Exception:", str(error))
        logging.error("Data column weather can't be split in various columns")

    # Timestamp to date for dt column

    try:
        df_pandas = timestamp_unix_to_date(df_pandas, 'dt')
        logging.info("Timestamp transformed to date succesfully")

    except ExceptionClause("Timestamp don't transformed to date") as error:
        logging.error("Exception:", str(error))
        logging.error("Data can't be transform to date")

    # Timestamp to hours for sunrise and sunset

    try:
        df_pandas = timestamp_unix_to_date_hours(df_pandas, 'sys.sunrise', 'sunrise', 'Europe/Amsterdam')
        df_pandas = timestamp_unix_to_date_hours(df_pandas, 'sys.sunset', 'sunset', 'Europe/Amsterdam')
        logging.info("Data from Timestamp transformed to hours succesfully")

    except ExceptionClause("Timestamp don't transformed to hours") as error:
        logging.error("Exception:", str(error))
        logging.error("Data can't be transform to hours")

    # Clean unnecessary columns

    try:
        df_pandas_clean = delete_columns(df_pandas, ['weather_id', 'weather_icon', 'cod', 'base',
                                                     'sys.type', 'sys.id', 'dt', 'sys.sunrise', 'sys.sunset',
                                                     'weather'])
        logging.info("Unnecessary columns eliminated")

    except ExceptionClause("Unnecessary columns didn't eliminated") as error:
        logging.error("Exception:", str(error))
        logging.error("Unnecessary columns didnt eliminated")

    # Replace "." for "_"

    try:
        df_pandas_clean = replace_dot_for_underscore(df_pandas_clean)
        logging.info("dot changed for underscore")

    except ExceptionClause("dot can't be change for underscore") as error:
        logging("Exception:", str(error))
        logging.error("Dot cant be change for underscore")

    # Changing types on many columns for Big Query upload

    try:
        df_pandas_clean['date'] = pd.to_datetime(df_pandas_clean['date'])
        df_pandas_clean['sunrise'] = pd.to_datetime(df_pandas_clean['sunrise'])
        df_pandas_clean['sunset'] = pd.to_datetime(df_pandas_clean['sunset'])
        logging.info("Columns type changed for Big Query")

    except ExceptionClause("Columns type can't be changed") as error:
        logging("Exception:", str(error))
        logging.error("Columns type can't be changed")

    # Adding a date insertion column in dataframe

    try:
        df_pandas_clean['date_insertion'] = datetime.now()
        logging.info("date_insertion column created")
        return df_pandas_clean

    except ExceptionClause("Date time of the insertion failed") as error:
        logging("Exception:", str(error))
        logging.error("Date time of the insertion didn't capture")

