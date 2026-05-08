from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    supabase_service_key: str
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expire_min: int = 10080  # 7 Days

    class Config:
        env_file = ".env"


settings = Settings()
