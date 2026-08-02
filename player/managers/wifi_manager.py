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
                "SSID,SIGNAL,SECURITY",
                "device",
                "wifi",
                "list",
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        networks = []

        seen = set()

        for line in result.stdout.splitlines():

            parts = line.split(":")

            if len(parts) < 3:
                continue

            ssid = parts[0].strip()

            signal = parts[1].strip()

            security = ":".join(parts[2:]).strip()

            if not ssid:
                continue

            if ssid in seen:
                continue

            seen.add(ssid)

            networks.append(
                {
                    "ssid": ssid,
                    "signal": int(signal),
                    "security": security,
                    # "connected":
                }
            )

        return sorted(
            networks,
            key=lambda x: x["signal"],
            reverse=True,
        )

    @staticmethod
    def connect(ssid: str, password: str):

        result = subprocess.run(
            [
                "nmcli",
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