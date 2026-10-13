import re
from playwright.sync_api import expect
from config import ORANGEHRM_URL, ORANGEHRM_USERNAME, ORANGEHRM_PASSWORD
import json
from pathlib import Path
from playwright.sync_api import expect
from config import ORANGEHRM_URL

TEST_DATA_PATH = Path(__file__).parent / "test_data" / "orangehrm_data.json"

with open(TEST_DATA_PATH, encoding="utf-8") as file:
    TEST_DATA = json.load(file)


def login_as_admin(page):
    page.goto(ORANGEHRM_URL)
    page.get_by_placeholder("Username").fill(ORANGEHRM_USERNAME)
    page.get_by_placeholder("Password").fill(ORANGEHRM_PASSWORD)
    page.get_by_role("button", name="Login").click()


def test_admin_can_login(page):
    login_as_admin(page)
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


def test_admin_can_log_out(page):
    login_as_admin(page)

    page.locator(".oxd-userdropdown-tab").click()
    page.get_by_role("menuitem", name="Logout").click()

    expect(page).to_have_url(re.compile(r".*/auth/login"))
    expect(page.get_by_placeholder("Username")).to_be_visible()

    # Check that required field messages appear when the login form is empty
def test_login_with_empty_fields_shows_required_messages(page):
    page.goto(ORANGEHRM_URL)
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Required", exact=True).first).to_be_visible()
    expect(page.get_by_text("Required", exact=True).nth(1)).to_be_visible()


# Check that an incorrect password is rejected
def test_invalid_login(page):
    data = TEST_DATA["invalid_login"]

    page.goto(ORANGEHRM_URL)
    page.get_by_placeholder("Username").fill(data["username"])
    page.get_by_placeholder("Password").fill(data["password"])
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text(data["expected_message"])).to_be_visible()



# Check the forgot-password page opens
def test_forgot_password_page(page):
    data = TEST_DATA["forgot_password"]

    page.goto(ORANGEHRM_URL)
    page.get_by_text(data["link_text"], exact=True).click()

    expect(
        page.get_by_role("heading", name=data["expected_heading"])
    ).to_be_visible()
    expect(
        page.get_by_placeholder(data["username_placeholder"])
    ).to_be_visible()


# Check that the Admin module opens after login
def test_open_admin_module(page):
    login_as_admin(page)
    page.get_by_role("link", name="Admin").click()

    expect(page.get_by_role("heading", name="Admin")).to_be_visible()


# Check that the PIM employee-management module opens
def test_open_pim_module(page):
    login_as_admin(page)
    page.get_by_role("link", name="PIM").click()

    expect(page.get_by_role("heading", name="PIM")).to_be_visible()


# Check that the Leave module opens
def test_open_leave_module(page):
    login_as_admin(page)
    page.get_by_role("link", name="Leave").click()

    expect(
        page.get_by_role("heading", name="Leave", exact=True)
    ).to_be_visible()