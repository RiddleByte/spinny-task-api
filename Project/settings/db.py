# -*- coding: utf-8 -*-
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
from .config import config_values

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config_values.get("mysql_db_name"),
        "USER": config_values.get("mysql_db_username"),
        "PASSWORD": config_values.get("mysql_db_password"),
        "HOST": config_values.get("mysql_db_host"),
        "PORT": config_values.get("mysql_db_port"),
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}
