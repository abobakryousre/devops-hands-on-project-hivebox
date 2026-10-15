from dotenv import load_dotenv
import os
load_dotenv()
APP_VERSION = os.environ.get("APP_VERSION","0.0.0")
if __name__ == "__main__":
    print(f"App Version: {APP_VERSION}")
