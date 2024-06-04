import pytest
from playwright.sync_api import sync_playwright
import allure
import os

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()
        yield page
        video_path = page.video.path()
        page.close()
        context.close()
        browser.close()

        # Attach video to Allure report
        if video_path:
            allure.attach.file(video_path, name="test_video", attachment_type=allure.attachment_type.MP4)

@pytest.fixture(scope="function")
def capture_screenshot():
    def _capture_screenshot(page, name):
        screenshot_path = os.path.join("results", f"{name}.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)
    return _capture_screenshot



