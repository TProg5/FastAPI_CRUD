from pydantic_settings import BaseSettings


class DataBaseSettings(BaseSettings):
    DATABASE_URL: str = "hard/database.sqlite"


database_settings = DataBaseSettings()