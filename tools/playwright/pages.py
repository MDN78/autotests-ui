import allure
from playwright.sync_api import Playwright, Page


def initialize_playwright_page(playwright: Playwright, test_name: str, storage_state: str | None = None) -> Page:
    browser = playwright.chromium.launch(headless=False)
    # Add Playwright Trace Viewer options and add video recording
    context = browser.new_context(storage_state=storage_state, record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    # add tracing files to directory with name of test
    context.tracing.stop(path=f'./tracing/{test_name}.zip')
    browser.close()

    # attach file and video to allure report
    allure.attach.file(f'./tracing/{test_name}.zip', name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
