from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    KAGGLE_USERNAME: str = "yumizzzz"
    KAGGLE_API_TOKEN: str = ""
    KAGGLE_COMPETITION_NAME: str = ""

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def KAGGLE_KERNEL_SLUG(self) -> str:
        return f"{self.KAGGLE_COMPETITION_NAME}-deps"


settings = Settings()
