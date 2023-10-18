from src.servicies.open_uv.open_uv_connector import CityCoord

cities = [
    "Madrid", "Valencia", "Alicante", "Almería", "Granada", "Jaén", "Málaga", "Córdoba",
    "Cádiz", "Huelva", "Sevilla", "Badajoz", "Cáceres", "Albacete", "Toledo", "Salamanca",
    "Castellón de la Plana", "Barcelona", "Tarragona", "Gerona", "Vitoria-Gasteiz", "Oviedo",
    "Ávila", "Burgos", "Santander", "Ciudad Real", "Cuenca", "Guadalajara", "San Sebastian", "Huesca",
    "Palma", "La Coruña", "Logroño", "Las Palmas de Gran Canaria", "León", "Lérida",
    "Lugo", "Murcia", "Pamplona", "Orense", "Palencia", "Pontevedra", "Segovia", "Soria",
    "Santa Cruz de Tenerife", "Teruel", "Valladolid", "Bilbao", "Zamora", "Zaragoza"
]

locations = [
    CityCoord(40.40, -3.69, "Madrid"), CityCoord(39.47, -0.38, "Valencia"),
    CityCoord(38.35, -0.49, "Alicante"), CityCoord(36.83, -2.46, "Almeria"),
    CityCoord(37.18, -3.60, "Granada"), CityCoord(37.78, -3.78, "Jaén"),
    CityCoord(36.72, -4.42, "Málaga"), CityCoord(37.89, -4.78, "Cordoba"),
    CityCoord(36.51, -6.28, "Cadiz"), CityCoord(37.26, -6.94, "Huelva"),
    CityCoord(37.39, -5.99, "Sevilla"), CityCoord(38.88, -6.97, "Badajoz"),
    CityCoord(39.47, -6.38, "Cáceres"), CityCoord(38.99, -1.86, "Albacete"),
    CityCoord(39.86, -4.03, "Toledo"), CityCoord(40.96, -5.67, "Salamanca"),
    CityCoord(39.98, -0.05, "Castellón de la Plana"), CityCoord(41.38, 2.18, "Barcelona"),
    CityCoord(41.12, 1.24, "Tarragona"), CityCoord(41.97, 2.82, "Gerona"),
    CityCoord(42.85, -2.67, "Vitoria-Gasteiz"), CityCoord(43.36, -5.85, "Oviedo"),
    CityCoord(40.66, -4.69, "Ávila"), CityCoord(42.35, -3.69, "Burgos"),
    CityCoord(43.46, -3.83, "Santander"), CityCoord(38.98, -3.93, "Ciudad Real"),
    CityCoord(40.07, -2.14, "Cuenca"), CityCoord(40.63, -3.16, "Guadalajara"),
    CityCoord(43.31, -1.99, "San Sebastian"), CityCoord(42.13, -0.41, "Huesca"),
    CityCoord(39.59, 2.71, "Palma"), CityCoord(43.36, -8.41, "La Coruña"),
    CityCoord(42.46, -2.44, "Logroño"), CityCoord(28.12, -15.43, "Las Palmas de Gran Canaria"),
    CityCoord(42.60, -5.57, "León"), CityCoord(41.61, 0.63, "Lerida"),
    CityCoord(43.01, -7.56, "Lugo"), CityCoord(37.99, -1.13, "Murcia"),
    CityCoord(42.81, -1.64, "Pamplona"), CityCoord(42.33, -7.86, "Orense"),
    CityCoord(42.01, -4.53, "Palencia"), CityCoord(42.43, -8.64, "Pontevedra"),
    CityCoord(40.94, -4.11, "Segovia"), CityCoord(41.77, -2.48, "Soria"),
    CityCoord(28.46, -16.26, "Tenerife"), CityCoord(40.34, -1.11, "Teruel"),
    CityCoord(41.65, -4.72, "Valladolid"), CityCoord(43.26, -2.93, "Bilbao"),
    CityCoord(41.50, -5.75, "Zamora"), CityCoord(41.65, -0.89, "Zaragoza")
]

path_credentials_bq = 'C:/Users/gabri/Documents/Developer/etl_weather/tfm-etl-weather-project-05b75b65d201.json'
