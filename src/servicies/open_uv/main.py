import extract_script_ou
import transform_script_ou
import load_script_ou
import logging
from src.utils.constans import locations

# Config of logging

logging.basicConfig(
    level=logging.DEBUG,  # Show all level's logging
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format of the message
    handlers=[
        logging.StreamHandler(),  # Print in console
        logging.FileHandler("etl_open_uv.log")  # Save a .log document with every log
    ]
)


def main():
    # Execute extract_script_ou.py
    json_list = extract_script_ou.extract_data(location_list=locations)

    # Execute transform_script_ou.py
    df_uv = transform_script_ou.transform_data(json_data=json_list)

    # Execute load_script_ou.py
    load_script_ou.load_data(df_uv)


if __name__ == "__main__":
    main()
