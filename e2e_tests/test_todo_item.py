import allure
from playwright.sync_api import Page, expect

def test_todo_items_can_be_added(browser_context):
    page = browser_context
    todo_item = "buy some cheese"
    page.goto("https://demo.playwright.dev/todomvc")
    new_todo = page.get_by_placeholder('What needs to be done?')
    new_todo.fill(todo_item)
    new_todo.press('Enter')

    expect(page.get_by_test_id('todo-title')).to_have_text([todo_item])

    page.screenshot(path="results/Add_todo_item.png")
    page.close()

@allure.feature('Todo Items')
@allure.story('Mark all as completed')
@allure.severity(allure.severity_level.CRITICAL)
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_all_todo_items_are_marked_completed(browser_context, capture_screenshot):
    page = browser_context
    page.goto('https://demo.playwright.dev/todomvc')
    with allure.step("Create todo items"):
        todo_item = "buy some cheese"
        new_todo = page.get_by_placeholder('What needs to be done?')
        new_todo.fill(todo_item)
        new_todo.press('Enter')
        capture_screenshot(page, 'Create_todo_items')

    with allure.step("Mark all todos as complete"):
        page.locator('[for="toggle-all"]').click()

    with allure.step("Verify all todos are marked as completed"):
        expect(page.locator('[data-testid="todo-item"]')).to_have_class(['completed'])

        capture_screenshot(page, 'Mark_all_items_as_completed')
    page.close()
