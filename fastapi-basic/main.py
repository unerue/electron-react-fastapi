import requests
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
db = [
    {"name": "Moscow", "timezone": "Europe/Moscow"},
    {"name": "Seoul", "timezone": "Asia/Seoul"},
]


class City(BaseModel):
    name: str
    timezone: str


@app.get("/")
async def index():
    return {"key": "value"}


@app.get("/cities")
async def get_cities():
    results = []
    for city in db:
        r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
        current_time = r.json()["datetime"]
        results.append({
            "name": city["name"], "timezone": city["timezone"], "current_time:": current_time
        })
    return results


@app.get("/cities{city_id}")
async def get_city(city_id: int):
    city = db[city_id - 1]
    r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
    current_time = r.json()["datetime"]
    return {
        "name": city["name"], "timezone": city["timezone"], "current_time:": current_time
    }


@app.post("/cities")
async def create_city(city: City):
    # city.model_bump() use instead of city.dict()
    db.append(city.model_dump())
    return db[-1]


@app.delete("/cities{city_id}")
async def delete_city(city_id: int):
    db.pop(city_id - 1)
    return {}
