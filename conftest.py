from pathlib import Path

import pytest
from playwright.sync_api import expect
from config import ORANGEHRM_URL

AUTH_FILE = Path(__file__).parent / "playwright" / ".auth" / "orangehrm.json"


@pytest.fixture
def auth_page(browser):
    if not AUTH_FILE.exists():
        pytest.fail("Login state not found. Run auth_setup.py first.")

    context = browser.new_context(storage_state=str(AUTH_FILE))
    page = context.new_page()

    # Load the saved session by navigating to OrangeHRM.
    page.goto(ORANGEHRM_URL)

    try:
        expect(
            page.get_by_role("heading", name="Dashboard")
        ).to_be_visible(timeout=10000)
    except AssertionError:
        context.close()
        pytest.fail("Saved login state is invalid or expired. Run auth_setup.py again.")

    yield page
    context.close()