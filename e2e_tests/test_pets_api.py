import allure
import pytest
from playwright.sync_api import APIRequestContext,Playwright
from typing import Generator


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
)-> Generator[APIRequestContext,None,None]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


@allure.feature('Pets Store')
@allure.story('Create a new Pet')
@allure.severity(allure.severity_level.CRITICAL)
@allure.issue("API-333")
@allure.testcase("TMS-4456")
def test_create_pet(api_request_context: APIRequestContext) -> None:

    with allure.step("Create new Pet"):
        data = {
          "id": 0,
          "category": {
            "id": 0,
            "name": "string"
          },
          "name": "doggie",
          "photos": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "available"
        }
        new_pet = api_request_context.post(
            f"https://petstore.swagger.io/v2/pet", data=data
        )
        assert new_pet.ok
        new_pet_response = new_pet.json()
    with allure.step("Verify pet has been created"):
        get_pets = api_request_context.get(f"https://petstore.swagger.io/v2/pet/" + str(new_pet_response["id"]))
        assert get_pets.ok
        get_pets_response = get_pets.json()
        assert get_pets_response["id"] == new_pet_response["id"]
