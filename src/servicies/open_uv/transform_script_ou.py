from open_uv_connector import OpenUVConnector
from src.utils.date_utils import isodate_to_date
from src.utils.functions_utils import delete_columns, add_column, add_columns_df, replace_value, \
    replace_dot_for_underscore
from src.utils.functions_utils import json_to_pandas_normalize
from src.utils.constans import locations
import logging
from src.utils.exceptions import ExceptionClause


def transform_data(json_data):
    logging.info("Starting transforming process of the data obtained")
    connector = OpenUVConnector()

    logging.info("Parsing data from json to pandas Dataframe...")

    try:
        uv_df = json_to_pandas_normalize(json_data)
        logging.info("Data transformed to pandas dataframe successfully")

    except ExceptionClause("Parse data to pandas failed") as error:
        logging.error("Transforming data from json to pandas failed!")
        logging.error(f"Exception: {error}")

    logging.info("Creating a list of the city names")

    try:
        city_names = connector.get_city_names(locations)

    except ExceptionClause("List of city names not created") as error:
        logging.error("Creation of the list city names failed")
        logging.error(f"Exception: {error}")

    logging.info("Adding a list city column to the dataframe...")

    try:
        uv_df = add_column(df=uv_df, column=city_names, column_name='city_name')

    except ExceptionClause("Add columns failed") as error:
        logging.error("Columns not added to the dataframe")
        logging.error(f"Exception: {error}")

    logging.info("Deleting unnecessary columns...")

    try:
        uv_df = delete_columns(df=uv_df, columns=['result.sun_info.sun_times.solarNoon',
                                                  'result.sun_info.sun_times.nadir',
                                                  'result.sun_info.sun_times.sunrise',
                                                  'result.sun_info.sun_times.sunset',
                                                  'result.sun_info.sun_times.sunriseEnd',
                                                  'result.sun_info.sun_times.sunsetStart',
                                                  'result.sun_info.sun_times.dawn',
                                                  'result.sun_info.sun_times.dusk',
                                                  'result.sun_info.sun_times.nauticalDawn',
                                                  'result.sun_info.sun_times.nauticalDusk',
                                                  'result.sun_info.sun_times.nightEnd',
                                                  'result.sun_info.sun_times.night',
                                                  'result.sun_info.sun_times.goldenHourEnd',
                                                  'result.sun_info.sun_times.goldenHour'])
        logging.info("Columns deleted!")

    except ExceptionClause("Columns selected not eliminated!") as error:
        logging.error("Columns not deleted")
        logging.error(f"Exception: {error}")

    logging.info("Converting ISO datetimes columns to a timestamp format...")
    try:
        time_cols = ['result.uv_time', 'result.uv_max_time', 'result.ozone_time']
        time_cols_converted = uv_df[time_cols].applymap(isodate_to_date)
        logging.info("Columns transformed from ISO datetimes to a timestamp format")

    except ExceptionClause("Columns didn't transform to a timestamp format") as error:
        logging.error(f"Exception: {error}")

    logging.info("Adding the new columns in timestamp...")
    try:
        uv_df = add_columns_df(df=uv_df, columns=time_cols_converted)
        logging.info("New columns added!")

    except ExceptionClause("New columns in timestamp didn't added") as error:
        logging.error(f"Exception: {error}")

    logging.info("Deleting columns old columns in ISO datetimes")
    try:
        uv_df = delete_columns(df=uv_df, columns=time_cols)
        logging.info("Old columns deleted!")

    except ExceptionClause("Old columns in ISO dates were not removed") as error:
        logging.error(f"Exception: {error}")

    # Replace "." for "_"

    logging.info("Replace '.' for '_' ")
    try:
        uv_df_clean = replace_dot_for_underscore(uv_df)
        logging.info("Dots replaced for underscore successfully!")
        return uv_df_clean

    except ExceptionClause("Dots were not replace for underscores") as error:
        logging.error(f"Exception: {error}")
