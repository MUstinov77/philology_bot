from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    admin_id: SecretStr
    developer_id: SecretStr
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='UTF-8'
    )


config = Settings()
