from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    kaggle_username: str = "yumizzzz"
    kaggle_api_token: str = ""
    kaggle_competition_name: str = ""

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def kaggle_kernel_slug(self) -> str:
        return f"{self.kaggle_competition_name}-deps"

    @property
    def kaggle_dataset_slug(self) -> str:
        return f"{self.kaggle_competition_name}-codes"

    @property
    def kaggle_sub_kernel_slug(self) -> str:
        return f"{self.kaggle_competition_name}-sub"


settings = Settings()
