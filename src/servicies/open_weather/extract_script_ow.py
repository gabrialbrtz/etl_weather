import requests.exceptions
import logging
from src.servicies.open_weather.open_weather_connector import OpenWeatherConnector


def extract_data(list_cities):

    # Connection to the OpenUVConnector

    logging.info("Starting connection with Open Weather API")
    connector = OpenWeatherConnector()

    # Get current weather data from the API
    logging.info('Extracting data from the API...')

    try:
        json_list = connector.get_current_weather_cities(list_cities)
        logging.info('Data obtained from the API successfully')
        return json_list

    except requests.exceptions.RequestException as e:
        print(f"Error of connexion: {e}")
        logging.error("Data extraction failed")

