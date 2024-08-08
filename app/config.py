from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    SECRETKEY: str
    ALGORITHM: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}"

    class Config:
        env_file = ".env"



settings = Settings()
