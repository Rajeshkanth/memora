from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routes import home, media
from api.services.media import MediaService

app = FastAPI(title="Memora API")

app.mount("/static", StaticFiles(directory="api/static"), name="static")

app.include_router(home.router)
app.include_router(media.router)

MediaService.initialize()