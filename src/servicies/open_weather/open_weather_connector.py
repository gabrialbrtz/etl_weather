import requests
import pandas as pd
import os
from dotenv import load_dotenv


class OpenWeatherConnector:
    """
    Open Weather connector API to get the info of some endpoints
    1000 free calls per day

    API Documentation:
    https://openweathermap.org/api
    """

    def __init__(self):
        """
        Constructor function of the class OpenWeatherConnector

        api_key: str
        url_weather: str
        """
        self.load_env = load_dotenv()
        self.api_key = os.getenv("OPEN_WEATHER_API_KEY")
        self.url_weather = "https://api.openweathermap.org/data/2.5/weather?q={city},ES&units=metric&appid={API}"

    def get_current_weather_cities(self, cities: list) -> list:
        """
        Get the current weather of various cities at the same time

        Parameters:
        -------------
        self: constructor
            Parameter of the __init__ function

        cities: list
            List of the city names that you need to get data

        Returns:
        -------------
        json_list: list
            List of the data received from the API in json format
        """
        json_list = []
        for city in cities:

            url_city = self.url_weather.format(city=city, API=self.api_key)
            response = requests.get(url_city)

            if response.status_code == 200:
                data_weather = response.json()
                json_list.append(data_weather)

            else:
                print(f"Error en la solicitud para {city}. Código de estado: {response.status_code}")

        return json_list

    def get_current_weather(self, city: str) -> str:
        """
        Get the current weather of a city

        Parameters:
        -------------
        self: constructor
            Parameter of the __init__ function

        city: str
            City name that you need to get data

        Returns:
        -------------
        data_weather: str
            Data of the current weather of the city that you choose in json format

        """

        url_city = self.url_weather.format(city=city, API=self.api_key)

        response = requests.get(url_city)

        if response.status_code == 200:
            data_weather = response.json()
        else:
            print(f"Error en la solicitud para {city}. Código de estado: {response.status_code}")

        return data_weather

    @staticmethod
    def split_weather_column(df: pd.DataFrame) -> pd.DataFrame:
        """
        Function to split de column weather in more subcolumns

        Parameters:
        -------------
        df: pd.DataFrame
            Pandas DataFrame

        Return:
        -------------
        df: pd.DataFrame
            Pandas DataFrame with the column 'weather' split in various subcolumns
        """
        df[['weather_id', 'weather_main', 'weather_description', 'weather_icon']] = df['weather'].apply(
            lambda x: pd.Series([x[0]['id'], x[0]['main'], x[0]['description'], x[0]['icon']])
        )
        return df
