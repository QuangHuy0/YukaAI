import os
from kivy.config import Config

width,height= 1920,1080

Config.set('graphics','width', width)
Config.set('graphics','height',height)
Config.set('graphics','fullcreen','True')

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

IP_ADDR_API_URL = os.environ.get("IPS_ADDR_API_URL")
NEWS_FETCH_API_URL = os.environ.get("NEWS_FETCH_API_URL")
NEWS_FETCH_API_KEY = os.environ.get("NEWS_FETCH_API_KEY")
WEATHER_FORECAST_API_URL = os.environ.get("WEATHER_FORECAST_API_URL")
WEATHER_FORECAST_API_KEY = os.environ.get("WEATHER_FORECAST_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


SMTP_URL = os.environ.get("SMTP_URL")
SMTP_POST = os.environ.get("SMTP_POST")

SCREEN_WIDTH = Config.getint('graphics','width')
SCREEN_HEIGHT = Config.getint('graphics','height')