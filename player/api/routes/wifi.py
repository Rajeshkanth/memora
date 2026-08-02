from fastapi import APIRouter

from api.services.wifi import WifiService
from api.models.wifi import WifiConnectRequest

router = APIRouter(prefix="/wifi", tags=["Wi-Fi"])


@router.get("/networks")
def networks():

    return WifiService.scan()

@router.post("/connect")
def connect(request: WifiConnectRequest):

    return WifiService.connect(request)

@router.get("/current")
def current():

    return WifiService.current()