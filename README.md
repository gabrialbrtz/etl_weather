# ETL Weather project 

Code repository for my master's thesis in which I develop two ETL pipelines to make meteorological data available in the Google Big Query data warehouse

Steps:

1. Clone the repo to your local directory

```
git clone git@github.com:gabrialbrtz/etl_weather.git
```

2. Install requirements.txt to get every library of the project
```
pip install -r requirements.txt
```

3. Create your own account on Open Weather and Open UV to get your API Keys.
```
https://openweathermap.org/
https://www.openuv.io/
```
5. Create your own project in Google Cloud, create a JSON credentials file and put in your local repository

```
https://cloud.google.com/
```

6. If you want to automatizate both ETL pipelines you can use Google Cloud services as Cloud Functions and Cloud Scheduler
