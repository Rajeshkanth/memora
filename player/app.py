from constants import APP_NAME, VERSION
from core.player import MemoraPlayer


def main():
    print("=" * 40)
    print(f"        {APP_NAME}")
    print(f"        {VERSION}")
    print("=" * 40)

    player = MemoraPlayer()
    player.start()


if __name__ == "__main__":
    main()