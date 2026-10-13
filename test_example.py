import re
from playwright.sync_api import expect


# Example 1: Open a website and check its title
def test_check_page_title(page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))


# Example 2: Enter and submit text
def test_add_todo_item(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")

    todo_input = page.get_by_placeholder("What needs to be done?")
    todo_input.fill("Learn Playwright")
    todo_input.press("Enter")

    todo_item = page.get_by_test_id("todo-item").filter(
        has_text="Learn Playwright"
    )
    expect(todo_item).to_be_visible()


# Example 3: Check a checkbox
def test_complete_todo_item(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")

    todo_input = page.get_by_placeholder("What needs to be done?")
    todo_input.fill("Practice Python")
    todo_input.press("Enter")

    todo_item = page.get_by_test_id("todo-item").filter(
        has_text="Practice Python"
    )
    checkbox = todo_item.get_by_role("checkbox", name="Toggle Todo")
    checkbox.check()

    expect(checkbox).to_be_checked()

# Example 4: Choose an option from a dropdown
def test_select_dropdown_option(page):
    page.set_content("""
        <label for="country">Country</label>
        <select id="country">
            <option value="">Choose a country</option>
            <option value="india">India</option>
            <option value="canada">Canada</option>
        </select>
    """)

    country_dropdown = page.get_by_label("Country")
    country_dropdown.select_option("india")

    expect(country_dropdown).to_have_value("india")


# Example 5: Fill a form and click a button
def test_fill_form_and_click_button(page):
    page.set_content("""
        <label for="username">Username</label>
        <input id="username" type="text">
        <button>Submit</button>
        <p id="message"></p>

        <script>
            document.querySelector("button").addEventListener("click", () => {
                document.querySelector("#message").textContent = "Submitted";
            });
        </script>
    """)

    page.get_by_label("Username").fill("Divakar")
    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_text("Submitted")).to_be_visible()


# Example 6: Take a screenshot
def test_take_screenshot(page):
    page.goto("https://playwright.dev/")
    page.screenshot(path="playwright-homepage.png", full_page=True)