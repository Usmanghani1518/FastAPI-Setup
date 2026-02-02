from dotenv import load_dotenv
from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field,PostgresDsn

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = Field("Brandmize AI", env="APP_NAME")
    APP_VERSION: str = Field("1.0.0", env="APP_VERSION")
    DEBUG: bool = Field(True, env="DEBUG")

    DATABASE_URI: PostgresDsn = Field(..., env="DATABASE_URI")

    ACCESS_TOKEN_SECRET: str = Field(..., env="ACCESS_TOKEN_SECRET")
    REFRESH_TOKEN_SECRET: str = Field(..., env="REFRESH_TOKEN_SECRET")
    ALGORITHM: str = Field("HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(7, env="REFRESH_TOKEN_EXPIRE_DAYS")

    SMTP_FROM_USER: str = Field(..., env="SMTP_FROM_USER")
    SMTP_SERVER: str = Field(..., env="SMTP_SERVER")
    SMTP_PORT: str = Field(..., env="SMTP_PORT")
    SMTP_FROM_ADDRESS: str = Field(..., env="SMTP_FROM_ADDRESS")
    SMTP_PASSWORD: str = Field(..., env="SMTP_PASSWORD")

    ALLOW_ORIGINS: list[str] = Field(["*"], env="ALLOW_ORIGINS")
    ALLOW_CREDENTIALS: bool = Field(True, env="ALLOW_CREDENTIALS")
    ALLOW_METHODS: list[str] = Field(["*"], env="ALLOW_METHODS")
    ALLOW_HEADERS: list[str] = Field(["*"], env="ALLOW_HEADERS")

    SENDGRID_API_KEY: str | None = Field(None, env="SENDGRID_API_KEY")
    STRIPE_API_KEY: str | None = Field(None, env="STRIPE_API_KEY")
    OPENAI_API_KEY: str | None = Field(None, env="OPENAI_API_KEY")

    DEFAULT_PAGE_SIZE: int = Field(20, env="DEFAULT_PAGE_SIZE")
    MAX_PAGE_SIZE: int = Field(100, env="MAX_PAGE_SIZE")

    REDIS_URL: str | None = Field(None, env="REDIS_URL")

    model_config = SettingsConfigDict(
        env_file=".env",          
        env_file_encoding="utf-8", 
        case_sensitive=False,      
        extra="ignore",            
    )


settings = Settings()
