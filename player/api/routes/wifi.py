from fastapi import APIRouter

from api.services.wifi import WifiService
from api.models.wifi import WifiConnectRequest

router = APIRouter(prefix="/wifi", tags=["Wi-Fi"])


@router.post("/connect")
def connect(request: WifiConnectRequest):

    return WifiService.connect(request)

@router.get("/wifi")
def current():

    return WifiService.scan()

