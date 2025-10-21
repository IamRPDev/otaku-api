from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OTAKU_ANALYTICS_ENABLED: bool = False
    OTAKU_DATABASE_URL: str = "sqlite:///./otaku.db"
    OTAKU_REDIS_URL: str = "redis://redis:6379/0"
    class Config: env_file = ".env"

settings = Settings()
app = FastAPI(default_response_class=ORJSONResponse)

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.get("/v1/search")
def search(q: str):
    return {"query": q, "hits": []}
