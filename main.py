from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=60)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["GET"],
    allow_headers = [""]
)

@app.get("/")
def getinfo():
    if "info" in cache:
        return cache["info"]

    current_time = datetime.now(timezone.utc)
    formatted_time = current_time.isoformat(timespec="seconds").replace("+00:00", 'Z')

    data = {
        "email": "Bojzino128@gmail.com",
        "current_datetime": formatted_time,
        "github_url": "https://github.com/iamthedarksaint/hng_stage_zero_public_api"
    }

    cache["info"] = data

    return data