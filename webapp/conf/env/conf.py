CONFIG = {
    "DJANGO_LOG_LEVEL": "INFO",
    "DATABASE": {
        "HOST": "localhost",
        "USERNAME": "test",
        "PASSWORD": "test",
        "DB_NAME": "dratini",
        "PORT": "5432",
    },
    "DEBUG": False,
    "ALLOWED_HOSTS": ["*"],
}

EXTERNAL_SERVICES = {
    "GOOGLE": {
        "HOST": "XXX",
        "HEADERS": {
            "Content-Type": "application/json"
        },
        "KEY": "XXX",
    },
}
