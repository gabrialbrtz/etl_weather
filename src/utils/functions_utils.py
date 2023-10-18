import pandas as pd
import numpy as np


def json_to_pandas_normalize(list_json: list) -> pd.DataFrame:
    """
    Function to normalize list of jsons converting this list in a Pandas DataFrame

    Parameters:
    -----------
    list_json: list
        List of json data

    Return:
    ----------
    df_final: pd.DataFrame
        Pandas DataFrame

    """
    df_norm = [pd.json_normalize(json) for json in list_json]
    df_final = pd.concat(df_norm, ignore_index=True)

    return df_final


def json_to_pandas(json: str) -> pd.DataFrame:
    """
    Function to transform json data to pandas DataFrame

    Parameters:
    -------------
    json: str
        Data in json format

    Returns:
    ------------
    df: pd.DataFrame
        Pandas DataFrame

    """
    df = pd.json_normalize(json)
    return df


def delete_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Function to delete columns of a dataframe

    Parameters:
    -------------
    df: pd.DataFrame
        pandas DataFrame

    columns: list
        List of column names that you want to delete of the dataframe

    Return:
    -------------
    df: pd.DataFrame
      pandas DataFrame
    """
    df = df.drop(columns, axis=1)
    return df


def add_column(df: pd.DataFrame, column: list, column_name: str) -> pd.DataFrame:
    """
    Function to add columns for the right side

    Parameters:
    ------------
    df: pd.DataFrame
        Pandas DataFrame

    column: list
        Column that you need to add in list format

    column_name: str
        Name of the new column

    Return:
    ----------
    df: pd.DataFrame
        Pandas DataFrame
    """
    df[column_name] = column
    return df


def add_columns_df(df: pd.DataFrame, columns: pd.DataFrame) -> pd.DataFrame:
    """
    Function to add some columns in pandas dataframe format to a existing pandas dataframe

    Parameters:
    ------------
    df: pd.DataFrame
        Pandas DataFrame

    columns: pd.DataFrame
        Pandas DataFrame

    Return:
    -----------
    df: pd.DataFrame
        Pandas DataFrame
    """
    for col, values in columns.items():
        df[col] = values
    return df


def replace_dot_for_underscore(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to replace in name columns of a dataframe '.' for '_'
    Parameters:
    ------------
    df: pd.DataFrame
        Pandas DataFrame

    Return:
    ------------
    df: pd.DataFrame
        Pandas DataFrame

    """
    df = df.rename(columns=lambda x: x.replace(".", "_"))
    return df


def replace_value(df: pd.DataFrame, value: int = None) -> pd.DataFrame:
    """
    Function to replace NaN for a new number. By default value = None

    Parameters:
    -----------
    df: pd.DataFrame
        Pandas DataFrame

    value: int
        Value that you need instead of NaN

    Return:
    df: pd.DataFrame
        Pandas DataFrame

    """
    df = df.replace(np.nan, value)
    return df


def np_bytes(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Function to convert column types into np.bytes_ for load data to bq

    Parameters:
    ------------
    df: pd.DataFrame
        Pandas DataFrame

    columns: list
        List of column names

    Return:
    -----------
    df: pd.DataFrame
        Pandas DataFrame
    """

    for col in columns:
        df[col] = df[col].astype(np.bytes_)
    return df
