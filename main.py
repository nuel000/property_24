from playwright.sync_api import sync_playwright
import json
import time
import os
import sys

def run(playwright):
    browser = playwright.chromium.launch(headless=True)  # Changed to headless mode for GitHub Actions
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(200000)

    # Navigate to the page
    page.goto("https://www.property24.com/estate-agents/plus-group-properties/12885")

    # Wait for user interaction
    page.get_by_role("link", name="Contact Number Show Contact Number").click()
    print('clicked On Button')
    sys.stdout.flush()
    time.sleep(60)
    print('Sleeping for 60 Secs.....')
    sys.stdout.flush()

    # Capture screenshot
    os.makedirs('screenshots', exist_ok=True)
    page.screenshot(path="screenshots/capture.png")
    print('Screenshot captured')
    sys.stdout.flush()

    browser.close()

with sync_playwright() as playwright:
    run(playwright)