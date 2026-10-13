from pathlib import Path
from playwright.sync_api import sync_playwright, expect
from config import ORANGEHRM_URL, ORANGEHRM_USERNAME, ORANGEHRM_PASSWORD

AUTH_FILE = Path(__file__).parent / "playwright" / ".auth" / "orangehrm.json"
AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(ORANGEHRM_URL)
    page.get_by_placeholder("Username").fill(ORANGEHRM_USERNAME)
    page.get_by_placeholder("Password").fill(ORANGEHRM_PASSWORD)
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

    context.storage_state(path=str(AUTH_FILE))
    browser.close()

print(f"Saved login state to: {AUTH_FILE}")