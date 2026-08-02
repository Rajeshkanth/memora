from pydantic import BaseModel


class WifiConnectRequest(BaseModel):
    ssid: str
    password: str