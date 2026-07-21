from playwright.sync_api import expect

def test_login(page):
    page.goto("https://productstudio.indixpert.com/signin")
    # Email
    page.locator("input[type='email']").fill("amitsingh_99@yopmail.com")

    # Password
    page.locator("input[type='password']").fill("Amit@123")

    # Login button
    page.locator("button[type='submit']").click()

    # Wait for page to load
    page.wait_for_load_state("networkidle")
    page.pause() 
    # Verify login succeeded
    assert "signin" not in page.url.lower()