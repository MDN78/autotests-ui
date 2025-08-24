from playwright.sync_api import expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_toolbar = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_toolbar).to_be_visible()
    expect(courses_toolbar).to_have_text("Courses")

    courses_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    courses_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_list).to_be_visible()
    expect(courses_list).to_have_text("There is no results")

    description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).to_be_visible()
    expect(description_text).to_have_text("Results from the load test pipeline will be displayed here")
