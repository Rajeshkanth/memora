from pydantic import BaseModel


class WifiNetwork(BaseModel):
    ssid: str
    signal: int
    security: str
    connected: bool


class WifiConnectRequest(BaseModel):
    ssid: str
    password: str


class WifiConnectResponse(BaseModel):
    success: bool
    message: str