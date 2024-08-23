# from playwright.sync_api import sync_playwright
# import json
# import time
# import os
# import sys

# def run(playwright):
#     browser = playwright.firefox.launch(headless=True)  # Changed to headless mode for GitHub Actions
#     context = browser.new_context()
#     page = context.new_page()
#     page.set_default_timeout(200000)

#     # Navigate to the page
#     page.goto("https://web.facebook.com/ads/archive/render_ad/?id=863596179026952&access_token=EAAcZB2XVyuJ8BO0MGZBp8uPloUlFcbD2aEus6ZCwrpSGZByBzCjhCI27sCIthxbxXKSpuAsINZBPblnL1f5KZCMACJeZAsgYFlYP9x3ofFMMFlFPM1XAZBW2csD9XdFGW3hkbzFZCt8b921jzdupfnJpZARcIxCnFqwsNaZCbZBaQ3pJgZCu8QCSqzpgIsWhHATYZD&_rdc=1&_rdr")

#     # Wait for user interaction
#     # page.get_by_role("link", name="Contact Number Show Contact Number").click()
#     # print('clicked On Button')
#     # sys.stdout.flush()
#     time.sleep(10)
#     print('Sleeping for 60 Secs.....')
#     sys.stdout.flush()

#     # Capture screenshot
#     os.makedirs('screenshots', exist_ok=True)
#     page.screenshot(path="screenshots/facebook.png")
#     print('Screenshot captured')
#     sys.stdout.flush()

#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)


from playwright.sync_api import sync_playwright
import os
import time
import sys

def run(playwright):
    # Launch Chrome browser
    browser = playwright.chromium.launch(
        headless=True,
        executable_path='/usr/bin/google-chrome'  # Path to Google Chrome executable
    )
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(200000)

    # Navigate to the page
    page.goto("https://web.facebook.com/ads/archive/render_ad/?id=863596179026952&access_token=EAAcZB2XVyuJ8BO0MGZBp8uPloUlFcbD2aEus6ZCwrpSGZByBzCjhCI27sCIthxbxXKSpuAsINZBPblnL1f5KZCMACJeZAsgYFlYP9x3ofFMMFlFPM1XAZBW2csD9XdFGW3hkbzFZCt8b921jzdupfnJpZARcIxCnFqwsNaZCbZBaQ3pJgZCu8QCSqzpgIsWhHATYZD&_rdc=1&_rdr")

    # Wait for the page to load
    time.sleep(10)
    print('Sleeping for 10 Secs.....')
    sys.stdout.flush()

    # Capture screenshot
    os.makedirs('screenshots', exist_ok=True)
    page.screenshot(path="screenshots/facebook.png")
    print('Screenshot captured')
    sys.stdout.flush()

    browser.close()

with sync_playwright() as playwright:
    run(playwright)

