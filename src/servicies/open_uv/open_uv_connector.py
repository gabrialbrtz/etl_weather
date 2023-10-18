import os
from datetime import datetime
import requests
from dotenv import load_dotenv


class CityCoord:
    """
    Class for creation city objects with latitude, longitude and city name
    """

    def __init__(self, lat, lng, city):
        self.lat = lat
        self.lng = lng
        self.city = city


class OpenUVConnector:
    """
    Open UV connector API to get the info of some endpoints
    50 free calls per day

    API Documentation:
    https://www.openuv.io/
    """

    def __init__(self):
        """
        Constructor function of the class OpenWeatherConnector

        api_key: str
        url: str
        """
        self.load_env = load_dotenv()
        self.api_key = os.getenv('OPEN_UV_API_KEY')
        self.url = "https://api.openuv.io/api/v1/uv"

    def get_current_uv(self, locations: list) -> list:
        """
        Get current data of the UV in various cities

        Parameters:
        -------------
        locations: list
            List of CityCoord objects of the class CityCoord

        Returns:
        ------------
        uv_list_json: list
            List of the data response of the endpoint in json format

        """
        uv_list_json = []
        for location in locations:
            current_date = datetime.now()
            iso_date = current_date.isoformat()

            headers = {
                "x-access-token": self.api_key,
                "Content-Type": "application/json"
            }

            params = {
                "lat": location.lat,
                "lng": location.lng,
                "dt": iso_date
            }

            response = requests.get(url=self.url, headers=headers, params=params)

            if response.status_code == 200:
                result = response.json()
                uv_list_json.append(result)
            else:
                print(f"Error in: {location.city} with code error {response.status_code}")
                print(response.text)

        return uv_list_json

    @staticmethod
    def get_city_names(locations: list) -> list:
        """
        Get the city name of every object of a list of CityCoord

        Parameters:
        ------------
        locations: list
            List of CityCoord objects of the class CityCoord

        Return:
        ------------
        city_names: list
            list of strings with the city names

        """
        city_names = [location.city for location in locations]
        return city_names
