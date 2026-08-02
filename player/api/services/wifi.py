from managers.wifi_manager import WifiManager


class WifiService:

    @staticmethod
    def scan():

        return WifiManager.scan()

    @staticmethod
    def connect(request):

        return WifiManager.connect(
            request.ssid,
            request.password,
        )

    @staticmethod
    def current():

        return WifiManager.current()