# Настройки бота

from pathlib import Path

from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE_PATH = BASE_DIR / '.env.dev'


print(f'{ENV_FILE_PATH=}')

class Settings(BaseSettings):
    VK_TOKEN: SecretStr = Field(alias='VK_TOKEN')

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        env_file_encoding='utf-8',
        extra='ignore',
    )


settings = Settings()

print(f'{settings=}')
