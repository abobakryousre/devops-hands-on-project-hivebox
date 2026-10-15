from dotenv import load_dotenv
import os
load_dotenv()


def main():
    APP_VERSION = os.environ.get("APP_VERSION")
    if APP_VERSION is None:
        APP_VERSION = "1.0.0"  # Default version if not set in .env
    print(f"App Version: {APP_VERSION}")


if __name__ == "__main__":
    main()
