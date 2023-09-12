import os

from dotenv import dotenv_values

SERVICE_ENV = os.getenv("SERVICE_ENV", "local")

if SERVICE_ENV == "prod":
    DEBUG = False
    config_values = {}
elif SERVICE_ENV == "test":
    DEBUG = True
    config_values = dotenv_values(".env/test")
else:
    DEBUG = True
    config_values = dotenv_values(".env/local")
