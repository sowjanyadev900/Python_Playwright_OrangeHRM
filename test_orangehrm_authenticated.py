from playwright.sync_api import expect


def test_dashboard_is_displayed(auth_page):
    expect(
        auth_page.get_by_role("heading", name="Dashboard")
    ).to_be_visible()


def test_open_admin_module(auth_page):
    auth_page.get_by_role("link", name="Admin").click()

    expect(
        auth_page.get_by_role("heading", name="Admin", exact=True)
    ).to_be_visible()


def test_open_pim_module(auth_page):
    auth_page.get_by_role("link", name="PIM").click()

    expect(
        auth_page.get_by_role("heading", name="PIM", exact=True)
    ).to_be_visible()


def test_open_leave_module(auth_page):
    auth_page.get_by_role("link", name="Leave").click()

    # exact=True avoids matching both "Leave" and "Leave List"
    expect(
        auth_page.get_by_role("heading", name="Leave", exact=True)
    ).to_be_visible()


def test_profile_menu_shows_logout(auth_page):
    auth_page.locator(".oxd-userdropdown-tab").click()

    expect(
        auth_page.get_by_role("menuitem", name="Logout")
    ).to_be_visible()