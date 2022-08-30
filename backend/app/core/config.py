from pydantic import BaseSettings


class Settings(BaseSettings):
    URL: str
    # We need this first to get the total of free games to loop through.
    FIRST_GAME_ARIA: str
    XPATH_GAME: str
    XPATH_TIME: str
    SELENIUM_GRID_HOST: str

    class Config:
        case_sensitive = True

settings = Settings()