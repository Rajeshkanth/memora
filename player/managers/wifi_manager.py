import subprocess


class WifiManager:

    @staticmethod
    def scan():

        result = subprocess.run(
            [
                "nmcli",
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
                }
            )

        return sorted(
            networks,
            key=lambda x: x["signal"],
            reverse=True,
        )