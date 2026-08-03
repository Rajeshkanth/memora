import subprocess


class WifiManager:

    NMCLI = ["sudo", "nmcli"]

    @staticmethod
    def scan():

        result = subprocess.run(
            WifiManager.NMCLI +
            [
                "-t",
                "-f",
                "IN-USE,SSID,SIGNAL,SECURITY",
                "device",
                "wifi",
                "list",
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        networks = {}

        for line in result.stdout.splitlines():

            parts = line.split(":", 3)

            if len(parts) < 4:
                continue

            in_use = parts[0].strip()
            ssid = parts[1].strip()
            signal = int(parts[2])
            security = parts[3].strip()

            if not ssid:
                continue

            connected = in_use == "*"

            existing = networks.get(ssid)

            if existing is None:

                networks[ssid] = {
                    "ssid": ssid,
                    "signal": signal,
                    "security": security,
                    "connected": connected,
                }

                continue

            if signal > existing["signal"]:
                existing["signal"] = signal
                existing["security"] = security

            if connected:
                existing["connected"] = True

        return sorted(
            networks.values(),
            key=lambda x: (
                not x["connected"],
                -x["signal"]
            )
        )

    @staticmethod
    def connect(ssid: str, password: str):

        result = subprocess.run(
            WifiManager.NMCLI + [
                "device",
                "wifi",
                "connect",
                ssid,
                "password",
                password,
            ],
            capture_output=True,
            text=True,
        )

        return {
            "success": result.returncode == 0,
            "message": result.stdout.strip() or result.stderr.strip(),
        }

    @staticmethod
    def current():

        result = subprocess.run(
            WifiManager.NMCLI + [
                "-t",
                "-f",
                "ACTIVE,SSID,SIGNAL",
                "device",
                "wifi",
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        for line in result.stdout.splitlines():

            parts = line.split(":")

            if len(parts) < 3:
                continue

            if parts[0] != "yes":
                continue

            return {
                "ssid": parts[1],
                "signal": int(parts[2]),
            }

        return None

    @staticmethod
    def _run_nmcli(*args):
        return subprocess.run(
            ["sudo", "nmcli", *args],
            capture_output=True,
            text=True,
        )