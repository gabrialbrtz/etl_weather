import pandas as pd
import pytz
from datetime import datetime


def timestamp_unix_to_date(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Convert a timestamp (unit = 's') valor to a datetime ('%Y-%m-%d') in a specific column on a dataframe.

    Parameters:
    -------------
    df: pd.DataFrame
        Pandas DataFrame

    column_name: str
        Column name of the column that you need to convert from timestamp to datetime

    Return:
    -------------
    df: pd.DataFrame
        Pandas DataFrame
    """
    df['date'] = df[column_name].apply(
        lambda x: pd.to_datetime(x, unit='s').strftime('%Y-%m-%d'))
    return df


def timestamp_unix_to_hours(df: pd.DataFrame, column_name: str,
                            new_col_name: str, zone: str = 'Europe/Amsterdam') -> pd.DataFrame:
    """
    Convert a timestamp (unit = 's') valor to a hours ('%h-%m-%s') in a specific column on a dataframe.

    Parameters:
    -------------
    df: pd.DataFrame
        Pandas DataFrame

    column_name: str
        Column name of the column that you want to transform in hours

    new_col_name: str
        New name for the new column transformed

    zone: str
        UTC timezone. By default = 'Europe/Amsterdam'

    Return:
    -------------
    df: pd.DataFrame
        pandas DataFrame
    """
    timezone = pytz.timezone(zone)
    df[new_col_name] = df[column_name].apply(lambda x: pd.to_datetime(x, unit='s').tz_convert(
        timezone).strftime('%H:%M:%S'))
    return df


def timestamp_unix_to_date_hours(df: pd.DataFrame, column_name: str,
                                 new_col_name: str, zone: str = 'Europe/Amsterdam') -> pd.DataFrame:
    """
    Convert a timestamp (unit = 's') valor to a hours ('%Y-%m-%d %h-%m-%s') in a specific column on a dataframe.

    Parameters:
    -------------
    df: pd.DataFrame
        Pandas DataFrame

    column_name: str
        Column name of the column that you want to transform in date-hours

    new_col_name: str
        New name for the new column transformed

    zone: str
        UTC timezone. By default = 'Europe/Amsterdam'

    Return:
    -------------
    df: pd.DataFrame
        pandas DataFrame
    """
    timezone = pytz.timezone(zone)
    df[new_col_name] = df[column_name].apply(lambda x: pd.to_datetime(x, unit='s').tz_localize('UTC').tz_convert(
        timezone).strftime('%Y-%m-%d %H:%M:%S'))
    return df


def isodate_to_date(iso_date: str) -> str:
    """
    Function to convert ISO 8601 YYYY-MM-DDTHH:MM:SS.SSSZ to %Y-%m-%d %H:%M:%S

    Parameters:
    ------------
    iso_date: str
        datetime in format ISO 8601 in str

    Returns:
    -----------
    dt_date: str
        date transformed from ISO 8601 to date-hour format

    """
    dt = datetime.fromisoformat(iso_date[:-1])
    dt_date = dt.strftime("%Y-%m-%d %H:%M:%S")
    return dt_date
