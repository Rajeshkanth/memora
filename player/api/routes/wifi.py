from fastapi import APIRouter

from api.services.wifi import WifiService

router = APIRouter(prefix="/wifi", tags=["Wi-Fi"])


@router.get("/networks")
def networks():

    return WifiService.scan()