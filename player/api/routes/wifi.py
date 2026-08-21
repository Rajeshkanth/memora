from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.services.wifi import WifiService
from api.models.wifi import WifiConnectRequest

router = APIRouter(prefix="/wifi", tags=["Wi-Fi"])

templates = Jinja2Templates(directory="api/templates")

@router.get("", response_class=HTMLResponse)
def wifi_page(request: Request):

    networks = WifiService.scan()

    return templates.TemplateResponse(
        request,
        "wifi.html",
        {
            "request": request,
            "networks": networks,
        },
    )

@router.post("/connect")
def connect(request: WifiConnectRequest):

    return WifiService.connect(request)

@router.get("/scan")
def current():

    return WifiService.scan()

