import extract_script_ow
import transform_script_ow
import load_script_ow
import logging
from src.utils.constans import cities

# Config of logging

logging.basicConfig(
    level=logging.DEBUG,  # Show all level's logging
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format of the message
    handlers=[
        logging.StreamHandler(),  # Print in console
        logging.FileHandler("etl_open_weather.log")  # Save a .log document with every log
    ]
)


def main():
    # Execute extract_script_ow.py
    json_list = extract_script_ow.extract_data(list_cities=cities)

    # Execute transform_script_ow.py
    df_final = transform_script_ow.transform_data(list_json=json_list)

    # Execute load_script_ow.py
    load_script_ow.load_data(df=df_final)


if __name__ == "__main__":
    main()
