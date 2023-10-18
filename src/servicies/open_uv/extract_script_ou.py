from open_uv_connector import OpenUVConnector
import logging
import requests.exceptions


def extract_data(location_list):

    # Connection to the OpenUVConnector

    logging.info("Starting connection with Open UV API")
    connector = OpenUVConnector()

    # Get current uv data from the API

    logging.info("Getting data from current uv...")

    try:
        uv_json_data = connector.get_current_uv(location_list)
        logging.info("Data extracted succesfully!")
        return uv_json_data

    except requests.exceptions.ConnectionError as error:
        logging.error("Data extraction failed")
        logging.error(f"Exception: {error}")
