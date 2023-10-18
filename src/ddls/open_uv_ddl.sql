CREATE TABLE `tfm-etl-weather-project.data_warehouse.openuv`(
    result_uv FLOAT64,
    result_uv_max FLOAT64,
    result_ozone FLOAT64,
    result_safe_exposure_time_st1 INT64,
    result_safe_exposure_time_st2 INT64,
    result_safe_exposure_time_st3 INT64,
    result_safe_exposure_time_st4 INT64,
    result_safe_exposure_time_st5 INT64,
    result_safe_exposure_time_st6 INT64,
    result_sun_info_sun_position_azimuth FLOAT64,
    result_sun_info_sun_position_altitude FLOAT64,
    city_name STRING,
    result_uv_time DATETIME,
    result_uv_max_time DATETIME,
    result_ozone_time DATETIME

);
