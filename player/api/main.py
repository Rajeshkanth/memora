from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routes import home, media, settings, wifi
from api.services.media import MediaService

app = FastAPI(title="Memora API")

app.mount("/static", StaticFiles(directory="api/static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(home.router)
app.include_router(media.router)
app.include_router(settings.router)
app.include_router(wifi.router)

MediaService.initialize()