import os
from dotenv import load_dotenv

load_dotenv()

ORANGEHRM_URL = os.getenv("ORANGEHRM_URL")
ORANGEHRM_USERNAME = os.getenv("ORANGEHRM_USERNAME")
ORANGEHRM_PASSWORD = os.getenv("ORANGEHRM_PASSWORD")

missing = [
    name
    for name, value in {
        "ORANGEHRM_URL": ORANGEHRM_URL,
        "ORANGEHRM_USERNAME": ORANGEHRM_USERNAME,
        "ORANGEHRM_PASSWORD": ORANGEHRM_PASSWORD,
    }.items()
    if not value
]

if missing:
    raise ValueError(f"Missing environment variables: {', '.join(missing)}")
