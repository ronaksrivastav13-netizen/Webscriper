
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright

# Create screenshots folder
folder = Path("screenshots")
folder.mkdir(exist_ok=True)

# Website URL
url = "https://www.youtube.com/"

# Create a unique filename
time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = folder / f"screenshot_{time_now}.png"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(
        viewport={"width": 1366, "height": 768}
    )

    page.goto(url, wait_until="domcontentloaded", timeout=60000)

    # Take full-page screenshot
    page.screenshot(path=str(file_path), full_page=True)

    print("Screenshot saved successfully!")
    print(f"Location: {file_path}")
    print(f"Website title: {page.title()}")

    browser.close()
